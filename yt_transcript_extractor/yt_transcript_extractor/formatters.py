import json
from typing import List, Dict, Any, Callable
from .utils import format_seconds

YOUTUBE_WATCH_URL = "https://www.youtube.com/watch?v={video_id}"


class TranscriptFormatter:
    """
    Formats transcript items into various output formats: TXT, JSON, SRT, Markdown.
    """

    @classmethod
    def format(
        cls,
        fmt: str,
        transcript: List[Dict[str, Any]],
        title: str = "",
        video_id: str = "",
        language: str = ""
    ) -> str:
        """
        Formats transcript using the specified format identifier (txt, json, srt, md).
        """
        fmt_key = fmt.lower().strip()

        if fmt_key == "json":
            return cls.to_json(transcript, title=title, video_id=video_id, language=language)
        elif fmt_key == "srt":
            return cls.to_srt(transcript)
        elif fmt_key in ("md", "markdown"):
            return cls.to_markdown(transcript, title=title, video_id=video_id, language=language)
        elif fmt_key == "txt":
            return cls.to_txt(transcript, title=title, video_id=video_id, language=language)
        else:
            raise ValueError(f"Unsupported format: '{fmt}'. Supported formats: txt, json, srt, md.")

    @staticmethod
    def to_txt(
        transcript: List[Dict[str, Any]],
        title: str = "",
        video_id: str = "",
        language: str = ""
    ) -> str:
        lines = []
        if title:
            lines.append(f"Title: {title}")
        if video_id:
            lines.append(f"Video ID: {video_id}")
            lines.append(f"URL: {YOUTUBE_WATCH_URL.format(video_id=video_id)}")
        if title or video_id:
            lines.append("-" * 50)

        for item in transcript:
            start_str = format_seconds(item["start"])
            text = item["text"].strip()
            lines.append(f"[{start_str}] {text}")

        return "\n".join(lines)

    @staticmethod
    def to_json(
        transcript: List[Dict[str, Any]],
        title: str = "",
        video_id: str = "",
        language: str = ""
    ) -> str:
        data = {
            "metadata": {
                "title": title,
                "video_id": video_id,
                "url": YOUTUBE_WATCH_URL.format(video_id=video_id) if video_id else "",
                "language": language,
                "count": len(transcript),
            },
            "transcript": transcript,
        }
        return json.dumps(data, ensure_ascii=False, indent=2)

    @staticmethod
    def to_srt(transcript: List[Dict[str, Any]]) -> str:
        blocks = []
        for index, item in enumerate(transcript, start=1):
            start = item["start"]
            duration = item.get("duration", 2.0)
            end = start + duration

            start_srt = format_seconds(start, srt_format=True)
            end_srt = format_seconds(end, srt_format=True)
            text = item["text"].strip()

            block = f"{index}\n{start_srt} --> {end_srt}\n{text}\n"
            blocks.append(block)

        return "\n".join(blocks)

    @staticmethod
    def to_markdown(
        transcript: List[Dict[str, Any]],
        title: str = "",
        video_id: str = "",
        language: str = ""
    ) -> str:
        md = [f"# {title or 'YouTube Video Transcript'}\n"]
        if video_id:
            url = YOUTUBE_WATCH_URL.format(video_id=video_id)
            md.append(f"- **Video URL:** [{url}]({url})")
            md.append(f"- **Video ID:** `{video_id}`")
        if language:
            md.append(f"- **Language:** `{language}`")
        md.append(f"- **Total Entries:** `{len(transcript)}`\n")
        md.append("---\n")
        md.append("## 📜 Complete Transcript with Timestamps\n")

        for item in transcript:
            time_str = format_seconds(item["start"])
            text = item["text"].strip()
            md.append(f"- **`[{time_str}]`** {text}")

        return "\n".join(md)

