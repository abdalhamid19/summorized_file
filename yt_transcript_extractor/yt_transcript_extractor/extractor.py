import glob
import json
import os
import subprocess
import sys
from typing import Any, Dict, List, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from .utils import extract_video_id

DEFAULT_PREFERRED_LANGUAGES = ["ar", "en-US", "en"]
YTDLP_METADATA_TIMEOUT_SECONDS = 15
YTDLP_SUBTITLE_TIMEOUT_SECONDS = 30
WATCH_URL_TEMPLATE = "https://www.youtube.com/watch?v={video_id}"


class YouTubeTranscriptExtractor:
    """
    Extracts transcripts from YouTube videos using youtube-transcript-api
    with a yt-dlp fallback mechanism.
    """

    def __init__(self, video_url_or_id: str):
        self.raw_input = video_url_or_id
        extracted_id = extract_video_id(video_url_or_id)
        if not extracted_id:
            raise ValueError(f"Invalid YouTube URL or Video ID: {video_url_or_id}")

        self.video_id = extracted_id
        self.metadata: Dict[str, Any] = {}

    def fetch_metadata(self) -> Dict[str, Any]:
        """
        Fetches video metadata (title, uploader, duration) via yt-dlp.
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
        """
        available_languages = []
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(self.video_id)
            for transcript in transcript_list:
                available_languages.append({
                    "language": transcript.language,
                    "language_code": transcript.language_code,
                    "is_generated": transcript.is_generated,
                    "is_translatable": transcript.is_translatable,
                })
        except Exception:
            pass
        return available_languages

    def get_transcript(self, preferred_languages: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """
        Retrieves transcript entries for preferred languages.
        Tries youtube-transcript-api first, then falls back to yt-dlp.
        """
        target_languages = preferred_languages or DEFAULT_PREFERRED_LANGUAGES

        # Attempt 1: youtube-transcript-api
        primary_transcript = self._get_transcript_via_api(target_languages)
        if primary_transcript:
            return primary_transcript

        # Attempt 2: yt-dlp fallback
        ytdlp_transcript = self._fetch_via_ytdlp(target_languages)
        if ytdlp_transcript:
            return ytdlp_transcript

        raise RuntimeError(
            f"Could not retrieve transcript for video {self.video_id}. "
            "Subtitles may be disabled or unavailable."
        )

    # --- Private Helper Methods ---

    def _fetch_metadata_via_ytdlp(self) -> Optional[Dict[str, Any]]:
        """Executes yt-dlp process to extract metadata json."""
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
        except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
            pass
        return None

    def _get_transcript_via_api(self, preferred_languages: List[str]) -> Optional[List[Dict[str, Any]]]:
        """Fetches transcript using youtube-transcript-api library."""
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(self.video_id)
            target_transcript = self._select_best_matching_transcript(transcript_list, preferred_languages)
            if target_transcript:
                fetched_data = target_transcript.fetch()
                return self._normalize_transcript_entries(fetched_data)
        except Exception:
            pass
        return None

    def _select_best_matching_transcript(self, transcript_list: Any, preferred_languages: List[str]) -> Any:
        """Selects the transcript matching language preferences or returns the first available."""
        for lang in preferred_languages:
            lang_lower = lang.lower()
            for transcript in transcript_list:
                code_lower = transcript.language_code.lower()
                if code_lower == lang_lower or code_lower.startswith(lang_lower):
                    return transcript

        # Fallback to first transcript if no match found
        for transcript in transcript_list:
            return transcript
        return None

    def _normalize_transcript_entries(self, fetched_data: Any) -> List[Dict[str, Any]]:
        """Normalizes transcript objects/dicts into a standard dictionary format."""
        normalized = []
        for item in fetched_data:
            if hasattr(item, "text"):
                text = item.text
                start = item.start
                duration = item.duration
            else:
                text = item.get("text", "")
                start = item.get("start", 0.0)
                duration = item.get("duration", 0.0)

            normalized.append({"text": text, "start": start, "duration": duration})
        return normalized

    def _fetch_via_ytdlp(self, preferred_languages: List[str]) -> Optional[List[Dict[str, Any]]]:
        """Fallback method using yt-dlp to extract auto-captions or subtitles."""
        temp_prefix = f"temp_sub_{self.video_id}"
        lang_arg = ",".join(preferred_languages)
        watch_url = WATCH_URL_TEMPLATE.format(video_id=self.video_id)

        cmd = [
            sys.executable,
            "-m",
            "yt_dlp",
            "--skip-download",
            "--write-sub",
            "--write-auto-sub",
            "--sub-lang",
            lang_arg,
            "--sub-format",
            "json3",
            "-o",
            temp_prefix,
            watch_url,
        ]

        try:
            subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=YTDLP_SUBTITLE_TIMEOUT_SECONDS,
            )

            matching_files = glob.glob(f"{temp_prefix}*.json3")
            if not matching_files:
                return None

            sub_file_path = matching_files[0]
            with open(sub_file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            self._cleanup_temp_files(matching_files)
            return self._parse_json3_events(data.get("events", []))
        except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
            return None

    def _parse_json3_events(self, events: List[Dict[str, Any]]) -> Optional[List[Dict[str, Any]]]:
        """Parses json3 subtitle events into standard transcript dictionaries."""
        transcript = []
        for event in events:
            t_start_ms = event.get("tStartMs", 0)
            d_duration_ms = event.get("dDurationMs", 0)
            segments = event.get("segs", [])
            text = "".join(s.get("utf8", "") for s in segments).strip()

            if text and text != "\n":
                transcript.append({
                    "text": text,
                    "start": t_start_ms / 1000.0,
                    "duration": d_duration_ms / 1000.0,
                })

        return transcript if transcript else None

    def _cleanup_temp_files(self, file_paths: List[str]) -> None:
        """Safely removes temporary files."""
        for path in file_paths:
            try:
                if os.path.exists(path):
                    os.remove(path)
            except OSError:
                pass

