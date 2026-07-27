import json
from typing import List, Dict, Any
from .utils import format_seconds

class TranscriptFormatter:
    """
    Formats transcript items into various output formats: TXT, JSON, SRT, Markdown.
    """

    @staticmethod
    def to_txt(transcript: List[Dict[str, Any]], title: str = "", video_id: str = "") -> str:
        lines = []
        if title:
            lines.append(f"Title: {title}")
        if video_id:
            lines.append(f"Video ID: {video_id}")
            lines.append(f"URL: https://www.youtube.com/watch?v={video_id}")
        if title or video_id:
            lines.append("-" * 50)

        for item in transcript:
            start_str = format_seconds(item['start'])
            text = item['text'].strip()
            lines.append(f"[{start_str}] {text}")

        return "\n".join(lines)

    @staticmethod
    def to_json(transcript: List[Dict[str, Any]], title: str = "", video_id: str = "", language: str = "") -> str:
        data = {
            "metadata": {
                "title": title,
                "video_id": video_id,
                "url": f"https://www.youtube.com/watch?v={video_id}" if video_id else "",
                "language": language,
                "count": len(transcript)
            },
            "transcript": transcript
        }
        return json.dumps(data, ensure_ascii=False, indent=2)

    @staticmethod
    def to_srt(transcript: List[Dict[str, Any]]) -> str:
        blocks = []
        for i, item in enumerate(transcript, start=1):
            start = item['start']
            duration = item.get('duration', 2.0)
            end = start + duration

            start_srt = format_seconds(start, srt_format=True)
            end_srt = format_seconds(end, srt_format=True)
            text = item['text'].strip()

            block = f"{i}\n{start_srt} --> {end_srt}\n{text}\n"
            blocks.append(block)

        return "\n".join(blocks)

    @staticmethod
    def to_markdown(transcript: List[Dict[str, Any]], title: str = "", video_id: str = "", language: str = "") -> str:
        md = []
        md.append(f"# {title or 'YouTube Video Transcript'}\n")
        if video_id:
            md.append(f"- **رابط الفيديو (URL):** [https://www.youtube.com/watch?v={video_id}](https://www.youtube.com/watch?v={video_id})")
            md.append(f"- **معرف الفيديو (Video ID):** `{video_id}`")
        if language:
            md.append(f"- **اللغة (Language):** `{language}`")
        md.append(f"- **عدد الجمل/المقاطع:** `{len(transcript)}`\n")
        md.append("---\n")
        md.append("## 📜 التفريغ النصي الكامل مع التوقيتات\n")

        for item in transcript:
            time_str = format_seconds(item['start'])
            text = item['text'].strip()
            md.append(f"- **`[{time_str}]`** {text}")

        return "\n".join(md)
