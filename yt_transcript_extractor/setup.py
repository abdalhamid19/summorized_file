from setuptools import setup, find_packages

setup(
    name="yt_transcript_extractor",
    version="1.0.0",
    description="Professional YouTube Transcript Extractor Tool",
    author="AI Coding Assistant",
    packages=find_packages(),
    install_requires=[
        "youtube-transcript-api>=0.6.2",
        "yt-dlp>=2024.3.10",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "yt-transcript=yt_transcript_extractor.cli:main",
        ],
    },
    python_requires=">=3.8",
)
