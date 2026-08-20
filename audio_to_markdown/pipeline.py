from pathlib import Path

from . import auditor, config, markdown_builder, splitter, transcriber


def run(audio_file: Path = None, output_md: Path = None) -> Path:
    audio_file = audio_file or config.AUDIO_FILE
    output_md = output_md or config.OUTPUT_MD
    _validate_inputs(audio_file)

    chunks = splitter.split_audio(audio_file)
    texts = transcriber.transcribe_all(chunks)
    full_text = "\n\n".join(texts)

    cleaned_text = _save_transcripts(full_text)
    sections = auditor.audit_all(cleaned_text)
    markdown = markdown_builder.build_markdown(sections, title=audio_file.stem, source=audio_file.name)

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text(markdown, encoding="utf-8")
    print(f"\nDone! Markdown saved to {output_md} ({len(markdown)} chars)")
    return output_md


def _validate_inputs(audio_file: Path) -> None:
    if not config.COHERE_API_KEY:
        raise RuntimeError("COHERE_API_KEY is not set (env or .env)")
    if not audio_file.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_file}")


def _save_transcripts(full_text: str) -> str:
    raw_path = config.WORK_DIR / "transcript_full.txt"
    raw_path.write_text(full_text, encoding="utf-8")
    print(f"Raw transcript: {len(full_text)} chars -> {raw_path}")

    cleaned_text = auditor.collapse_repetitions(full_text, max_repeat=1)
    md_path = config.WORK_DIR / "transcript_full.md"
    md_path.write_text(cleaned_text, encoding="utf-8")
    print(f"Cleaned transcript: {len(cleaned_text)} chars -> {md_path}")
    return cleaned_text
