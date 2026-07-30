"""
Custom exceptions for YouTube Transcript Extractor.
Each exception maps to a specific, actionable failure reason.
"""


class TranscriptExtractionError(Exception):
    """Base class for all transcript extraction errors."""
    pass


class SubtitlesDisabledByOwner(TranscriptExtractionError):
    """
    Raised when the video owner has explicitly disabled subtitles/transcripts.
    This is not a network or tool issue — the content simply has no captions available.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"Subtitles are disabled by the channel owner for video '{video_id}'.\n"
            "The video owner has explicitly disabled this feature.\n"
            "The only possible solution: Use Whisper to convert audio to text directly."
        )


class NoTranscriptAvailable(TranscriptExtractionError):
    """
    Raised when the video exists but has no transcripts in any language.
    Different from SubtitlesDisabledByOwner — here YouTube simply never generated captions.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"No transcripts are available in any language for video '{video_id}'.\n"
            "YouTube did not generate automatic captions for this content.\n"
            "Possible solution: Use Whisper to convert audio to text."
        )


class RequestBlockedByYouTube(TranscriptExtractionError):
    """
    Raised when YouTube is blocking requests from the current IP address.
    Typically happens from cloud/server IPs or after too many rapid requests.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"YouTube blocked the request for video '{video_id}'.\n"
            "Reason: Your IP address (or server) was detected as a bot.\n"
            "Suggested solutions:\n"
            "  1. Use a Residential Proxy instead of a cloud server.\n"
            "  2. Pass browser cookies: yt-dlp --cookies-from-browser chrome\n"
            "  3. Wait a few hours and retry with delays between requests."
        )


class VideoNotFound(TranscriptExtractionError):
    """
    Raised when the video ID does not correspond to an existing YouTube video.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"Video '{video_id}' was not found, has been deleted, or is private.\n"
            "Please verify the link or video ID is correct."
        )


class YtDlpNotInstalled(TranscriptExtractionError):
    """
    Raised when yt-dlp is not installed in the current environment.
    """
    def __init__(self):
        super().__init__(
            "yt-dlp is not installed in the current environment.\n"
            "Install it with: pip install yt-dlp"
        )


class NetworkError(TranscriptExtractionError):
    """
    Raised on general network/connectivity failures unrelated to YouTube policy.
    """
    def __init__(self, video_id: str, original_error: str = ""):
        self.video_id = video_id
        detail = f"\nOriginal error: {original_error}" if original_error else ""
        super().__init__(
            f"Network connection failed when attempting to extract transcripts for video '{video_id}'.{detail}\n"
            "Please check your internet connection and try again."
        )
