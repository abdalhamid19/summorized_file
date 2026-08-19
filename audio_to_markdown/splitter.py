import subprocess
from pathlib import Path

from . import config

FFMPEG_TIMEOUT_SECONDS = 1800
FFMPEG_ERROR_TAIL_CHARS = 500
BYTES_PER_MB = 1024 * 1024


def split_audio(audio_file: Path = None, work_dir: Path = None) -> list[Path]:
    audio_file = audio_file or config.AUDIO_FILE
    work_dir = work_dir or config.WORK_DIR
    chunks_dir = work_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)

    existing = sorted(chunks_dir.glob("chunk_*.mp3"))
    if existing:
        print(f"Found {len(existing)} existing chunks, skipping split")
        return existing

    _run_ffmpeg_split(audio_file, chunks_dir)
    chunks = sorted(chunks_dir.glob("chunk_*.mp3"))
    _validate_chunk_sizes(chunks)
    print(f"Created {len(chunks)} chunks")
    return chunks


def _run_ffmpeg_split(audio_file: Path, chunks_dir: Path) -> None:
    command = [
        "ffmpeg", "-y", "-i", str(audio_file),
        "-vn", "-ac", "1", "-b:a", config.AUDIO_BITRATE,
        "-f", "segment", "-segment_time", str(config.CHUNK_SECONDS),
        "-reset_timestamps", "1",
        str(chunks_dir / "chunk_%03d.mp3"),
    ]
    print(f"Splitting {audio_file.name} into {config.CHUNK_SECONDS}s chunks @ {config.AUDIO_BITRATE}...")
    result = subprocess.run(command, capture_output=True, text=True, timeout=FFMPEG_TIMEOUT_SECONDS)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {result.stderr[-FFMPEG_ERROR_TAIL_CHARS:]}")


def _validate_chunk_sizes(chunks: list[Path]) -> None:
    for chunk in chunks:
        size_mb = chunk.stat().st_size / BYTES_PER_MB
        if size_mb > config.MAX_FILE_MB:
            raise RuntimeError(f"Chunk {chunk.name} is {size_mb:.1f}MB, over {config.MAX_FILE_MB}MB limit")
