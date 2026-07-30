"""
YouTube Transcript Extractor Package
Author: AI Coding Assistant
"""

from .extractor import YouTubeTranscriptExtractor
from .formatters import TranscriptFormatter
from .exceptions import (
    TranscriptExtractionError,
    SubtitlesDisabledByOwner,
    NoTranscriptAvailable,
    RequestBlockedByYouTube,
    VideoNotFound,
    NetworkError,
    YtDlpNotInstalled,
)

__version__ = "1.1.0"
__all__ = [
    "YouTubeTranscriptExtractor",
    "TranscriptFormatter",
    # Exceptions
    "TranscriptExtractionError",
    "SubtitlesDisabledByOwner",
    "NoTranscriptAvailable",
    "RequestBlockedByYouTube",
    "VideoNotFound",
    "NetworkError",
    "YtDlpNotInstalled",
]
