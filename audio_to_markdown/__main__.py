import argparse
import sys
from pathlib import Path

from . import config, pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="تفريغ صوت عربي وتدقيقه وتحويله إلى Markdown عبر Cohere")
    parser.add_argument("--audio", type=Path, default=config.AUDIO_FILE, help="مسار الملف الصوتي")
    parser.add_argument("--output", type=Path, default=config.OUTPUT_MD, help="مسار ملف Markdown الناتج")
    parser.add_argument("--chunk-seconds", type=int, default=None, help="مدة المقطع بالثواني")
    args = parser.parse_args()

    if args.chunk_seconds:
        config.CHUNK_SECONDS = args.chunk_seconds

    pipeline.run(args.audio, args.output)


if __name__ == "__main__":
    sys.exit(main())
