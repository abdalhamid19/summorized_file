import json
from pathlib import Path

from . import client, config

AUDIO_MIME_FIELDS = {"language": "ar"}


def transcribe_chunk(chunk_path: Path) -> str:
    headers = {"Authorization": f"Bearer {config.COHERE_API_KEY}"}
    fields = {"model": config.TRANSCRIBE_MODEL, **AUDIO_MIME_FIELDS}
    data = client.post_with_retry(
        config.TRANSCRIBE_URL,
        headers=headers,
        upload_path=chunk_path,
        upload_fields=fields,
        description=f"transcribe {chunk_path.name}",
    )
    return data["text"].strip()


def transcribe_all(chunks: list[Path], work_dir: Path = None) -> list[str]:
    work_dir = work_dir or config.WORK_DIR
    transcripts_dir = work_dir / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    return [
        _transcribe_with_cache(chunk, index, len(chunks), transcripts_dir)
        for index, chunk in enumerate(chunks)
    ]


def _transcribe_with_cache(chunk: Path, index: int, total: int, transcripts_dir: Path) -> str:
    out_file = transcripts_dir / f"{chunk.stem}.json"
    if out_file.exists():
        print(f"[{index + 1}/{total}] {chunk.name} (cached)")
        return json.loads(out_file.read_text(encoding="utf-8"))["text"]

    print(f"[{index + 1}/{total}] Transcribing {chunk.name}...")
    text = transcribe_chunk(chunk)
    out_file.write_text(json.dumps({"text": text}, ensure_ascii=False), encoding="utf-8")
    print(f"  -> {len(text)} chars")
    return text
