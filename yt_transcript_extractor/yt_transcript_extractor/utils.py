import os
import re
from typing import Optional

def extract_video_id(url_or_id: str) -> Optional[str]:
    """
    Extracts 11-character YouTube video ID from a URL or raw ID string.
    """
    if not url_or_id:
        return None
    
    url_or_id = url_or_id.strip()
    
    # If it's already an 11-character ID
    if len(url_or_id) == 11 and re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
        return url_or_id

    # Patterns for youtube URLs
    patterns = [
        r'(?:v=|\/)([a-zA-Z0-9_-]{11})(?:[&?\/]|$)',
        r'youtu\.be\/([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/embed\/([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/shorts\/([a-zA-Z0-9_-]{11})'
    ]

    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)

    return None


def format_seconds(seconds: float, srt_format: bool = False) -> str:
    """
    Formats seconds into MM:SS, HH:MM:SS, or SRT timestamp format.
    """
    seconds = max(0.0, float(seconds))
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))

    if srt_format:
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def sanitize_filename(name: str) -> str:
    """
    Sanitizes string for safe filesystem usage.
    """
    sanitized = re.sub(r'[\\/*?:"<>|]', '_', name)
    sanitized = re.sub(r'\s+', '_', sanitized)
    return sanitized.strip('_') or 'transcript'


def ensure_dir(path: str) -> None:
    """
    Creates directory if it does not exist.
    """
    if path and not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
