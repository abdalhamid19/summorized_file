import sys
import os
sys.path.insert(0, os.path.abspath('yt_transcript_extractor'))
from yt_transcript_extractor.extractor import YouTubeTranscriptExtractor

try:
    url = "https://www.youtube.com/watch?v=rMORt-RUisY"
    extractor = YouTubeTranscriptExtractor(url)
    print("Fetching metadata...")
    metadata = extractor.fetch_metadata()
    print("Metadata:", metadata)
    print("Fetching languages...")
    langs = extractor.list_languages()
    print("Languages:", langs)
    print("Fetching transcript...")
    transcript = extractor.get_transcript(["ar"])
    print("Transcript retrieved! First 5 entries:")
    print(transcript[:5])
except Exception as e:
    print("Error:", e)
