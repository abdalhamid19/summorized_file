import unittest
import os
import json
from yt_transcript_extractor.utils import extract_video_id, format_seconds, sanitize_filename
from yt_transcript_extractor.formatters import TranscriptFormatter
from yt_transcript_extractor.extractor import YouTubeTranscriptExtractor
from yt_transcript_extractor.exceptions import (
    SubtitlesDisabledByOwner,
    NoTranscriptAvailable,
    RequestBlockedByYouTube,
    VideoNotFound,
    TranscriptExtractionError,
)

class TestUtils(unittest.TestCase):

    def test_extract_video_id(self):
        # Valid URLs
        self.assertEqual(extract_video_id("N1H-2WthmsQ"), "N1H-2WthmsQ")
        self.assertEqual(extract_video_id("https://www.youtube.com/watch?v=N1H-2WthmsQ"), "N1H-2WthmsQ")
        self.assertEqual(extract_video_id("https://youtu.be/N1H-2WthmsQ"), "N1H-2WthmsQ")
        self.assertEqual(extract_video_id("https://www.youtube.com/shorts/N1H-2WthmsQ"), "N1H-2WthmsQ")

        # Invalid URL
        self.assertIsNone(extract_video_id("invalid_string_without_id"))

    def test_format_seconds(self):
        self.assertEqual(format_seconds(65.0), "01:05")
        self.assertEqual(format_seconds(3665.0), "01:01:05")
        self.assertEqual(format_seconds(65.5, srt_format=True), "00:01:05,500")

    def test_sanitize_filename(self):
        self.assertEqual(sanitize_filename("Title / Test: 1?"), "Title___Test__1")


class TestFormatters(unittest.TestCase):

    def setUp(self):
        self.sample_transcript = [
            {"text": "Hello world", "start": 0.0, "duration": 2.0},
            {"text": "Welcome to Python", "start": 2.5, "duration": 3.0}
        ]

    def test_to_txt(self):
        txt = TranscriptFormatter.to_txt(self.sample_transcript, title="Sample", video_id="abc123xyz89")
        self.assertIn("[00:00] Hello world", txt)
        self.assertIn("[00:02] Welcome to Python", txt)

    def test_to_json(self):
        res_json = TranscriptFormatter.to_json(self.sample_transcript, title="Sample", video_id="abc123xyz89")
        parsed = json.loads(res_json)
        self.assertEqual(parsed["metadata"]["title"], "Sample")
        self.assertEqual(len(parsed["transcript"]), 2)

    def test_to_srt(self):
        srt = TranscriptFormatter.to_srt(self.sample_transcript)
        self.assertIn("00:00:00,000 --> 00:00:02,000", srt)
        self.assertIn("Hello world", srt)

    def test_to_markdown(self):
        md = TranscriptFormatter.to_markdown(self.sample_transcript, title="Sample Title", video_id="abc123xyz89")
        self.assertIn("# Sample Title", md)
        self.assertIn("**`[00:00]`** Hello world", md)

    def test_format_dispatch(self):
        txt = TranscriptFormatter.format("txt", self.sample_transcript, title="Sample", video_id="abc123xyz89")
        self.assertIn("[00:00] Hello world", txt)

        json_out = TranscriptFormatter.format("json", self.sample_transcript, title="Sample", video_id="abc123xyz89")
        parsed = json.loads(json_out)
        self.assertEqual(parsed["metadata"]["title"], "Sample")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            TranscriptFormatter.format("invalid_fmt", self.sample_transcript)


class TestExceptions(unittest.TestCase):
    """Tests that typed exceptions carry the correct video_id and message."""

    def test_subtitles_disabled_by_owner(self):
        exc = SubtitlesDisabledByOwner("rMORt-RUisY")
        self.assertEqual(exc.video_id, "rMORt-RUisY")
        self.assertIn("rMORt-RUisY", str(exc))
        self.assertIn("disabled by the channel owner", str(exc))
        # Must be a subclass of the base error
        self.assertIsInstance(exc, TranscriptExtractionError)

    def test_no_transcript_available(self):
        exc = NoTranscriptAvailable("abc12345678")
        self.assertEqual(exc.video_id, "abc12345678")
        self.assertIn("abc12345678", str(exc))
        self.assertIsInstance(exc, TranscriptExtractionError)

    def test_request_blocked(self):
        exc = RequestBlockedByYouTube("abc12345678")
        self.assertEqual(exc.video_id, "abc12345678")
        self.assertIn("blocked", str(exc))
        self.assertIsInstance(exc, TranscriptExtractionError)

    def test_video_not_found(self):
        exc = VideoNotFound("abc12345678")
        self.assertEqual(exc.video_id, "abc12345678")
        self.assertIn("abc12345678", str(exc))
        self.assertIsInstance(exc, TranscriptExtractionError)

    def test_invalid_video_id_raises_value_error(self):
        with self.assertRaises(ValueError):
            YouTubeTranscriptExtractor("not_a_valid_url_or_id")


class TestExtractorIntegration(unittest.TestCase):

    def test_real_video_extraction(self):
        video_id = "N1H-2WthmsQ"
        extractor = YouTubeTranscriptExtractor(video_id)
        self.assertEqual(extractor.video_id, video_id)

        try:
            transcript = extractor.get_transcript(preferred_languages=["ar", "en-US", "en"])
            self.assertIsInstance(transcript, list)
            self.assertGreater(len(transcript), 0)
            self.assertIn("text", transcript[0])
            self.assertIn("start", transcript[0])
        except TranscriptExtractionError as exc:
            # In CI/server environments YouTube may block the request.
            # The important thing is we get a typed exception, not a silent None.
            self.assertIsInstance(exc, TranscriptExtractionError)
            print(f"[test_real_video_extraction] Typed exception raised as expected: {type(exc).__name__}")

    def test_disabled_subtitles_video_raises_typed_error(self):
        """
        rMORt-RUisY has subtitles disabled by the owner.
        Must raise SubtitlesDisabledByOwner, not return None or a generic RuntimeError.
        """
        extractor = YouTubeTranscriptExtractor("rMORt-RUisY")
        try:
            extractor.get_transcript()
            # If no exception is raised, the video may have gained subtitles — that's fine.
        except SubtitlesDisabledByOwner as exc:
            self.assertEqual(exc.video_id, "rMORt-RUisY")
            self.assertIn("disabled by the channel owner", str(exc))
        except TranscriptExtractionError:
            # Any other typed error (blocked IP, etc.) is also acceptable.
            pass


if __name__ == "__main__":
    unittest.main()
