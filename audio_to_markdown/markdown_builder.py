from datetime import date
from pathlib import Path

from . import config


def build_markdown(sections: list[str], title: str = None, source: str = None) -> str:
    title = title or config.AUDIO_FILE.stem
    source = source or config.AUDIO_FILE.name
    header = (
        f"# {title}\n\n"
        f"> [!info] معلومات\n"
        f"> - **المصدر الصوتي:** `{source}`\n"
        f"> - **التفريغ:** {config.TRANSCRIBE_MODEL} (Cohere)\n"
        f"> - **التدقيق:** {config.AUDIT_MODEL} (Cohere)\n"
        f"> - **التاريخ:** {date.today().isoformat()}\n\n---\n"
    )
    body = "\n\n".join(section.strip() for section in sections if section.strip())
    return header + "\n" + body + "\n"
