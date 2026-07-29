import subprocess
import json
import os
import sys
import time

AUDIO_FILE = "/mnt/sdcard/pyreview/summorized_file/video_audio.mp3"
CHUNKS_DIR = "/tmp/audio_chunks"
OUTPUT_TRANSCRIPT = "/tmp/transcript_raw.json"
CHUNK_DURATION = 480  # 8 minutes per chunk (well under 25MB limit)
API_KEY = os.environ.get("OPENAI_API_KEY", "")

os.makedirs(CHUNKS_DIR, exist_ok=True)

def split_audio():
    print("Splitting audio into chunks...")
    cmd = [
        "ffmpeg", "-y", "-i", AUDIO_FILE,
        "-f", "segment", "-segment_time", str(CHUNK_DURATION),
        "-c", "copy",
        "-vn",
        os.path.join(CHUNKS_DIR, "chunk_%03d.mp3")
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    chunks = sorted([f for f in os.listdir(CHUNKS_DIR) if f.startswith("chunk_")])
    print(f"Created {len(chunks)} chunks")
    return chunks

def transcribe_chunk(chunk_path):
    import requests
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    with open(chunk_path, "rb") as f:
        files = {"file": (os.path.basename(chunk_path), f, "audio/mpeg")}
        data = {"model": "whisper-1", "response_format": "verbose_json", "language": "ar"}
        resp = requests.post(url, headers=headers, files=files, data=data, timeout=300)
    
    if resp.status_code != 200:
        raise RuntimeError(f"API error {resp.status_code}: {resp.text}")
    
    result = resp.json()
    segments = []
    for seg in result.get("segments", []):
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })
    return segments, result.get("text", "")

def main():
    chunks = split_audio()
    
    all_segments = []
    offset = 0
    
    for i, chunk_name in enumerate(chunks):
        chunk_path = os.path.join(CHUNKS_DIR, chunk_name)
        chunk_size_mb = os.path.getsize(chunk_path) / (1024 * 1024)
        print(f"Transcribing chunk {i+1}/{len(chunks)} ({chunk_size_mb:.1f}MB)...")
        
        segments, full_text = transcribe_chunk(chunk_path)
        
        for seg in segments:
            seg["start"] += offset
            seg["end"] += offset
            all_segments.append(seg)
            print(f"  [{seg['start']:.1f}s - {seg['end']:.1f}s] {seg['text'][:80]}...")
        
        offset += CHUNK_DURATION
    
    with open(OUTPUT_TRANSCRIPT, "w", encoding="utf-8") as f:
        json.dump({"segments": all_segments, "text": " ".join(s["text"] for s in all_segments)}, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone! Transcript saved to {OUTPUT_TRANSCRIPT}")
    print(f"Total segments: {len(all_segments)}")
    print(f"Total duration: ~{all_segments[-1]['end'] if all_segments else 0:.0f}s")

if __name__ == "__main__":
    main()
