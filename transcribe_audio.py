import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import requests

AUDIO_FILE = Path(os.environ.get("AUDIO_FILE", "video_audio.mp3"))
CHUNKS_DIR = Path(tempfile.gettempdir()) / "audio_chunks"
OUTPUT_TRANSCRIPT = Path(tempfile.gettempdir()) / "transcript_raw.json"
CHUNK_DURATION_SECONDS = 480
WHISPER_API_URL = "https://api.openai.com/v1/audio/transcriptions"
WHISPER_MODEL = "whisper-1"
TRANSCRIPT_LANGUAGE = "ar"
REQUEST_TIMEOUT_SECONDS = 300
API_KEY = os.environ.get("OPENAI_API_KEY", "")


def split_audio() -> list[str]:
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    print("Splitting audio into chunks...")
    command = [
        "ffmpeg", "-y", "-i", str(AUDIO_FILE),
        "-f", "segment", "-segment_time", str(CHUNK_DURATION_SECONDS),
        "-c", "copy", "-vn",
        str(CHUNKS_DIR / "chunk_%03d.mp3"),
    ]
    subprocess.run(command, capture_output=True, text=True, timeout=REQUEST_TIMEOUT_SECONDS)
    chunks = sorted(file for file in os.listdir(CHUNKS_DIR) if file.startswith("chunk_"))
    print(f"Created {len(chunks)} chunks")
    return chunks


def transcribe_chunk(chunk_path: Path):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    with open(chunk_path, "rb") as audio:
        files = {"file": (chunk_path.name, audio, "audio/mpeg")}
        data = {"model": WHISPER_MODEL, "response_format": "verbose_json", "language": TRANSCRIPT_LANGUAGE}
        response = requests.post(WHISPER_API_URL, headers=headers, files=files, data=data, timeout=REQUEST_TIMEOUT_SECONDS)

    if response.status_code != 200:
        raise RuntimeError(f"API error {response.status_code}: {response.text}")

    result = response.json()
    segments = [
        {"start": segment["start"], "end": segment["end"], "text": segment["text"].strip()}
        for segment in result.get("segments", [])
    ]
    return segments, result.get("text", "")


def size_in_mb(path: Path) -> float:
    return path.stat().st_size / (1024 * 1024)


def main() -> None:
    chunks = split_audio()
    all_segments = []
    offset = 0

    for index, chunk_name in enumerate(chunks):
        chunk_path = CHUNKS_DIR / chunk_name
        print(f"Transcribing chunk {index + 1}/{len(chunks)} ({size_in_mb(chunk_path):.1f}MB)...")

        segments, _ = transcribe_chunk(chunk_path)
        for segment in segments:
            segment["start"] += offset
            segment["end"] += offset
            all_segments.append(segment)
            print(f"  [{segment['start']:.1f}s - {segment['end']:.1f}s] {segment['text'][:80]}...")

        offset += CHUNK_DURATION_SECONDS

    full_text = " ".join(segment["text"] for segment in all_segments)
    OUTPUT_TRANSCRIPT.write_text(
        json.dumps({"segments": all_segments, "text": full_text}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\nDone! Transcript saved to {OUTPUT_TRANSCRIPT}")
    print(f"Total segments: {len(all_segments)}")
    print(f"Total duration: ~{all_segments[-1]['end'] if all_segments else 0:.0f}s")


if __name__ == "__main__":
    sys.exit(main())
