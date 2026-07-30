import glob
import json
import os
import subprocess
import sys
from typing import Any, Dict, List, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
    RequestBlocked,
)
from .utils import extract_video_id
from .exceptions import (
    SubtitlesDisabledByOwner,
    NoTranscriptAvailable,
    RequestBlockedByYouTube,
    VideoNotFound,
    NetworkError,
    YtDlpNotInstalled,
)

DEFAULT_PREFERRED_LANGUAGES = ["ar", "en-US", "en"]
YTDLP_METADATA_TIMEOUT_SECONDS = 15
YTDLP_SUBTITLE_TIMEOUT_SECONDS = 30
WATCH_URL_TEMPLATE = "https://www.youtube.com/watch?v={video_id}"


class YouTubeTranscriptExtractor:
    """
    Extracts transcripts from YouTube videos using youtube-transcript-api
    with a yt-dlp fallback mechanism.

    Raises specific exceptions instead of returning None so callers
    can distinguish between disabled subtitles, blocked requests,
    missing videos, and network failures.
    """

    def __init__(self, video_url_or_id: str):
        self.raw_input = video_url_or_id
        extracted_id = extract_video_id(video_url_or_id)
        if not extracted_id:
            raise ValueError(f"معرّف الفيديو أو الرابط غير صحيح: {video_url_or_id}\nيرجى التأكد من صحة الرابط أو معرّف الفيديو.")

        self.video_id = extracted_id
        self.metadata: Dict[str, Any] = {}

    def fetch_metadata(self) -> Dict[str, Any]:
        """
        Fetches video metadata (title, uploader, duration) via yt-dlp.
        Returns a fallback dict if yt-dlp is unavailable or the request fails.
        """
        metadata = self._fetch_metadata_via_ytdlp()
        if metadata:
            self.metadata = metadata
            return self.metadata

        self.metadata = {
            "title": f"Video_{self.video_id}",
            "uploader": "Unknown",
            "duration": 0,
            "view_count": 0,
            "description": "",
        }
        return self.metadata

    def list_languages(self) -> List[Dict[str, Any]]:
        """
        Lists available transcript languages for the video.

        Raises:
            SubtitlesDisabledByOwner: Owner explicitly disabled subtitles.
            VideoNotFound: Video does not exist or is private.
            RequestBlockedByYouTube: IP is blocked by YouTube.
            NetworkError: General connectivity failure.
        """
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(self.video_id)
            return [
                {
                    "language": t.language,
                    "language_code": t.language_code,
                    "is_generated": t.is_generated,
                    "is_translatable": t.is_translatable,
                }
                for t in transcript_list
            ]
        except TranscriptsDisabled:
            raise SubtitlesDisabledByOwner(self.video_id)
        except VideoUnavailable:
            raise VideoNotFound(self.video_id)
        except RequestBlocked:
            raise RequestBlockedByYouTube(self.video_id)
        except Exception as exc:
            raise NetworkError(self.video_id, str(exc)) from exc

    def get_transcript(self, preferred_languages: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """
        Retrieves transcript entries for the preferred languages.
        Tries youtube-transcript-api first, then falls back to yt-dlp.

        Raises:
            SubtitlesDisabledByOwner: Owner disabled subtitles — no workaround via API.
            VideoNotFound: Video does not exist or is private.
            RequestBlockedByYouTube: IP blocked by YouTube (raised only if both methods fail with block).
            NoTranscriptAvailable: Video exists but has no captions in any language.
            NetworkError: General connectivity failure.
        """
        target_languages = preferred_languages or DEFAULT_PREFERRED_LANGUAGES

        # Attempt 1: youtube-transcript-api
        # This raises typed exceptions on hard failures (disabled, blocked, not found).
        primary_result = self._get_transcript_via_api(target_languages)
        if primary_result is not None:
            return primary_result

        # Attempt 2: yt-dlp fallback (handles cases where the API is rate-limited
        # but yt-dlp with cookies/proxy might still succeed).
        ytdlp_result = self._fetch_via_ytdlp(target_languages)
        if ytdlp_result is not None:
            return ytdlp_result

        raise NoTranscriptAvailable(self.video_id)

    # --- Private Helper Methods ---

    def _fetch_metadata_via_ytdlp(self) -> Optional[Dict[str, Any]]:
        """Executes yt-dlp to extract metadata JSON. Returns None on any failure."""
        watch_url = WATCH_URL_TEMPLATE.format(video_id=self.video_id)
        cmd = [sys.executable, "-m", "yt_dlp", "-j", watch_url]
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=YTDLP_METADATA_TIMEOUT_SECONDS,
            )
            if result.returncode == 0 and result.stdout.strip():
                info = json.loads(result.stdout)
                return {
                    "title": info.get("title", ""),
                    "uploader": info.get("uploader", ""),
                    "duration": info.get("duration", 0),
                    "view_count": info.get("view_count", 0),
                    "description": info.get("description", ""),
                }
        except FileNotFoundError:
            # yt-dlp not installed — metadata is optional, so silently return None
            pass
        except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
            pass
        return None

    def _get_transcript_via_api(self, preferred_languages: List[str]) -> Optional[List[Dict[str, Any]]]:
        """
        Fetches transcript via youtube-transcript-api.

        Re-raises hard failures (disabled, blocked, video not found) so they
        propagate up immediately without trying yt-dlp.
        Returns None only when no matching language is found (soft failure).
        """
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(self.video_id)
            target = self._select_best_matching_transcript(transcript_list, preferred_languages)
            if target is None:
                return None
            fetched = target.fetch()
            return self._normalize_transcript_entries(fetched)

        except TranscriptsDisabled:
            # Hard failure: owner disabled subtitles. yt-dlp cannot help here.
            raise SubtitlesDisabledByOwner(self.video_id)

        except VideoUnavailable:
            # Hard failure: video is private, deleted, or region-locked.
            raise VideoNotFound(self.video_id)

        except RequestBlocked:
            # Soft failure: IP blocked. Let yt-dlp try with its own method.
            return None

        except NoTranscriptFound:
            # Soft failure: no transcript for requested languages; yt-dlp may find more.
            return None

        except Exception:
            # Unknown soft failure — let yt-dlp attempt as fallback.
            return None

    def _select_best_matching_transcript(self, transcript_list: Any, preferred_languages: List[str]) -> Any:
        """Selects the transcript matching language preferences, or returns the first available."""
        for lang in preferred_languages:
            lang_lower = lang.lower()
            for transcript in transcript_list:
                code_lower = transcript.language_code.lower()
                if code_lower == lang_lower or code_lower.startswith(lang_lower):
                    return transcript

        # Fallback: return the first available transcript regardless of language
        for transcript in transcript_list:
            return transcript
        return None

    def _normalize_transcript_entries(self, fetched_data: Any) -> List[Dict[str, Any]]:
        """Normalizes transcript objects or dicts into a standard dictionary format."""
        normalized = []
        for item in fetched_data:
            if hasattr(item, "text"):
                text, start, duration = item.text, item.start, item.duration
            else:
                text = item.get("text", "")
                start = item.get("start", 0.0)
                duration = item.get("duration", 0.0)
            normalized.append({"text": text, "start": start, "duration": duration})
        return normalized

    def _fetch_via_ytdlp(self, preferred_languages: List[str]) -> Optional[List[Dict[str, Any]]]:
        """
        Fallback: extracts auto-captions or subtitles via yt-dlp subprocess.
        Returns None if yt-dlp is unavailable or no subtitles are found.
        Does NOT raise — it is always a soft fallback.
        """
        temp_prefix = f"temp_sub_{self.video_id}"
        lang_arg = ",".join(preferred_languages)
        watch_url = WATCH_URL_TEMPLATE.format(video_id=self.video_id)

        cmd = [
            sys.executable, "-m", "yt_dlp",
            "--skip-download",
            "--write-sub",
            "--write-auto-sub",
            "--sub-lang", lang_arg,
            "--sub-format", "json3",
            "-o", temp_prefix,
            watch_url,
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=YTDLP_SUBTITLE_TIMEOUT_SECONDS,
            )

            # Detect owner-disabled subtitles from yt-dlp stderr output
            stderr_lower = (result.stderr or "").lower()
            if "subtitles are disabled" in stderr_lower or "has no subtitles" in stderr_lower:
                raise SubtitlesDisabledByOwner(self.video_id)

            matching_files = glob.glob(f"{temp_prefix}*.json3")
            if not matching_files:
                return None

            sub_file_path = matching_files[0]
            with open(sub_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            self._cleanup_temp_files(matching_files)
            return self._parse_json3_events(data.get("events", []))

        except SubtitlesDisabledByOwner:
            # Re-raise — this is a hard failure even inside the fallback
            raise
        except FileNotFoundError:
            raise YtDlpNotInstalled()
        except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
            return None

    def _parse_json3_events(self, events: List[Dict[str, Any]]) -> Optional[List[Dict[str, Any]]]:
        """Parses json3 subtitle events into standard transcript dictionaries."""
        transcript = []
        for event in events:
            t_start_ms = event.get("tStartMs", 0)
            d_duration_ms = event.get("dDurationMs", 0)
            text = "".join(s.get("utf8", "") for s in event.get("segs", [])).strip()
            if text and text != "\n":
                transcript.append({
                    "text": text,
                    "start": t_start_ms / 1000.0,
                    "duration": d_duration_ms / 1000.0,
                })
        return transcript if transcript else None

    def _cleanup_temp_files(self, file_paths: List[str]) -> None:
        """Safely removes temporary subtitle files."""
        for path in file_paths:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                pass
