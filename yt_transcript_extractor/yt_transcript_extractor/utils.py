import os
import re
from typing import Optional

# YouTube Video ID length and character constraints
RAW_VIDEO_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{11}$")

# Recognized YouTube URL formats
YOUTUBE_URL_PATTERNS = [
    re.compile(r"(?:v=|\/)([a-zA-Z0-9_-]{11})(?:[&?\/]|$)"),
    re.compile(r"youtu\.be\/([a-zA-Z0-9_-]{11})"),
    re.compile(r"youtube\.com\/embed\/([a-zA-Z0-9_-]{11})"),
    re.compile(r"youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})"),
]

# Time conversion constants
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
MS_PER_SECOND = 1000


def extract_video_id(url_or_id: str) -> Optional[str]:
    """
    Extracts 11-character YouTube video ID from a URL or raw ID string.
    """
    if not url_or_id:
        return None

    cleaned_input = url_or_id.strip()

    if RAW_VIDEO_ID_PATTERN.match(cleaned_input):
        return cleaned_input

    for pattern in YOUTUBE_URL_PATTERNS:
        match = pattern.search(cleaned_input)
        if match:
            return match.group(1)

    return None


def format_seconds(seconds: float, srt_format: bool = False) -> str:
    """
    Formats seconds into MM:SS, HH:MM:SS, or SRT timestamp format.
    """
    non_negative_seconds = max(0.0, float(seconds))
    hours = int(non_negative_seconds // SECONDS_PER_HOUR)
    minutes = int((non_negative_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE)
    secs = int(non_negative_seconds % SECONDS_PER_MINUTE)
    millis = int(round((non_negative_seconds - int(non_negative_seconds)) * MS_PER_SECOND))

    if srt_format:
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def sanitize_filename(name: str) -> str:
    """
    Sanitizes string for safe filesystem usage.
    """
    sanitized = re.sub(r'[\\/*?:"<>|]', "_", name)
    sanitized = re.sub(r"\s+", "_", sanitized)
    return sanitized.strip("_") or "transcript"


def ensure_dir(path: str) -> None:
    """
    Creates directory if it does not exist.
    """
    if path:
        os.makedirs(path, exist_ok=True)

