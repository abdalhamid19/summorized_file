import unittest
import os
import json
from yt_transcript_extractor.utils import extract_video_id, format_seconds, sanitize_filename
from yt_transcript_extractor.formatters import TranscriptFormatter
from yt_transcript_extractor.extractor import YouTubeTranscriptExtractor

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


class TestExtractorIntegration(unittest.TestCase):

    def test_real_video_extraction(self):
        video_id = "N1H-2WthmsQ"
        extractor = YouTubeTranscriptExtractor(video_id)
        self.assertEqual(extractor.video_id, video_id)

        # Test get_transcript
        transcript = extractor.get_transcript(preferred_languages=["ar", "en-US", "en"])
        self.assertIsInstance(transcript, list)
        self.assertGreater(len(transcript), 0)
        self.assertIn("text", transcript[0])
        self.assertIn("start", transcript[0])


if __name__ == "__main__":
    unittest.main()
