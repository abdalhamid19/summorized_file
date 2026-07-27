import json
import subprocess
from typing import List, Dict, Any, Optional
from youtube_transcript_api import YouTubeTranscriptApi
from .utils import extract_video_id

class YouTubeTranscriptExtractor:
    """
    Extracts transcripts from YouTube videos using youtube-transcript-api
    with a yt-dlp fallback mechanism.
    """

    def __init__(self, video_url_or_id: str):
        self.raw_input = video_url_or_id
        self.video_id = extract_video_id(video_url_or_id)
        if not self.video_id:
            raise ValueError(f"Invalid YouTube URL or Video ID: {video_url_or_id}")
        self.metadata = {}

    def fetch_metadata(self) -> Dict[str, Any]:
        """
        Fetches video metadata (title, uploader, duration) via yt-dlp.
        """
        try:
            cmd = ['python', '-m', 'yt_dlp', '-j', f'https://www.youtube.com/watch?v={self.video_id}']
            res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=15)
            if res.returncode == 0 and res.stdout:
                info = json.loads(res.stdout)
                self.metadata = {
                    "title": info.get("title", ""),
                    "uploader": info.get("uploader", ""),
                    "duration": info.get("duration", 0),
                    "view_count": info.get("view_count", 0),
                    "description": info.get("description", "")
                }
                return self.metadata
        except Exception:
            pass

        self.metadata = {
            "title": f"Video_{self.video_id}",
            "uploader": "Unknown",
            "duration": 0
        }
        return self.metadata

    def list_languages(self) -> List[Dict[str, Any]]:
        """
        Lists available transcript languages for the video.
        """
        available = []
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(self.video_id)
            for t in transcript_list:
                available.append({
                    "language": t.language,
                    "language_code": t.language_code,
                    "is_generated": t.is_generated,
                    "is_translatable": t.is_translatable
                })
        except Exception as e:
            # Fallback or empty if IP blocked / no transcript
            pass
        return available

    def get_transcript(self, preferred_languages: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """
        Retrieves transcript entries for preferred languages or defaults (ar, en).
        Tries primary API first, then yt-dlp fallback.
        """
        if preferred_languages is None:
            preferred_languages = ['ar', 'en-US', 'en']

        # Method 1: youtube-transcript-api via list/fetch
        try:
            ytt = YouTubeTranscriptApi()
            transcript_list = ytt.list(self.video_id)
            
            # Match preferred language codes
            target_t = None
            for lang in preferred_languages:
                for t in transcript_list:
                    if t.language_code.lower() == lang.lower() or t.language_code.lower().startswith(lang.lower()):
                        target_t = t
                        break
                if target_t:
                    break

            if not target_t:
                # pick first available
                for t in transcript_list:
                    target_t = t
                    break

            if target_t:
                fetched = target_t.fetch()
                result = []
                for item in fetched:
                    # handles both dict and object attributes
                    if hasattr(item, 'text'):
                        text = item.text
                        start = item.start
                        duration = item.duration
                    else:
                        text = item.get('text', '')
                        start = item.get('start', 0.0)
                        duration = item.get('duration', 0.0)
                    result.append({'text': text, 'start': start, 'duration': duration})
                return result
        except Exception as e1:
            pass

        # Method 2: yt-dlp fallback subtitles download
        yt_dlp_sub_data = self._fetch_via_ytdlp(preferred_languages)
        if yt_dlp_sub_data:
            return yt_dlp_sub_data

        raise RuntimeError(f"Could not retrieve transcript for video {self.video_id}. Subtitles may be disabled or unavailable.")

    def _fetch_via_ytdlp(self, preferred_languages: List[str]) -> Optional[List[Dict[str, Any]]]:
        """
        Fallback method using yt-dlp to extract auto-captions/subtitles.
        """
        try:
            lang_str = ",".join(preferred_languages)
            cmd = [
                'python', '-m', 'yt_dlp',
                '--skip-download',
                '--write-sub', '--write-auto-sub',
                '--sub-lang', lang_str,
                '--sub-format', 'json3',
                '-o', f'temp_sub_{self.video_id}',
                f'https://www.youtube.com/watch?v={self.video_id}'
            ]
            subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            # Check generated files
            import os, glob
            files = glob.glob(f'temp_sub_{self.video_id}*.json3')
            if not files:
                return None

            sub_file = files[0]
            with open(sub_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # clean up temp file
            for file in files:
                try:
                    os.remove(file)
                except Exception:
                    pass

            events = data.get('events', [])
            transcript = []
            for ev in events:
                tStartMs = ev.get('tStartMs', 0)
                dDurationMs = ev.get('dDurationMs', 0)
                segs = ev.get('segs', [])
                text = "".join([s.get('utf8', '') for s in segs]).strip()
                if text and text != '\n':
                    transcript.append({
                        'text': text,
                        'start': tStartMs / 1000.0,
                        'duration': dDurationMs / 1000.0
                    })
            return transcript if transcript else None
        except Exception:
            return None
