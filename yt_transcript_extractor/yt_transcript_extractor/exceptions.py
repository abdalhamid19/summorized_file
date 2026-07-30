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
            f"الترجمات معطّلة من قِبَل صاحب القناة للفيديو '{video_id}'.\n"
            "لا يمكن استخراج النص لأن صاحب المحتوى أوقف هذه الميزة.\n"
            "الحل الوحيد الممكن: استخدام Whisper لتحويل الصوت إلى نص مباشرة."
        )


class NoTranscriptAvailable(TranscriptExtractionError):
    """
    Raised when the video exists but has no transcripts in any language.
    Different from SubtitlesDisabledByOwner — here YouTube simply never generated captions.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"لا توجد ترجمات متاحة لأي لغة للفيديو '{video_id}'.\n"
            "يوتيوب لم يولّد ترجمات تلقائية لهذا المحتوى.\n"
            "الحل الممكن: استخدام Whisper لتحويل الصوت إلى نص."
        )


class RequestBlockedByYouTube(TranscriptExtractionError):
    """
    Raised when YouTube is blocking requests from the current IP address.
    Typically happens from cloud/server IPs or after too many rapid requests.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"يوتيوب حظر الطلب للفيديو '{video_id}'.\n"
            "السبب: عنوان IP الخاص بك (أو الخادم) تم التعرف عليه كروبوت.\n"
            "الحلول المقترحة:\n"
            "  1. استخدم Residential Proxy بدلاً من خادم سحابي.\n"
            "  2. مرّر كوكيز المتصفح: yt-dlp --cookies-from-browser chrome\n"
            "  3. انتظر بضع ساعات وأعد المحاولة مع تأخير بين الطلبات."
        )


class VideoNotFound(TranscriptExtractionError):
    """
    Raised when the video ID does not correspond to an existing YouTube video.
    """
    def __init__(self, video_id: str):
        self.video_id = video_id
        super().__init__(
            f"الفيديو '{video_id}' غير موجود أو تم حذفه أو أنه فيديو خاص (private).\n"
            "تحقق من صحة الرابط أو معرّف الفيديو."
        )


class YtDlpNotInstalled(TranscriptExtractionError):
    """
    Raised when yt-dlp is not installed in the current environment.
    """
    def __init__(self):
        super().__init__(
            "yt-dlp غير مثبّت في البيئة الحالية.\n"
            "قم بتثبيته بالأمر: pip install yt-dlp"
        )


class NetworkError(TranscriptExtractionError):
    """
    Raised on general network/connectivity failures unrelated to YouTube policy.
    """
    def __init__(self, video_id: str, original_error: str = ""):
        self.video_id = video_id
        detail = f"\nالخطأ الأصلي: {original_error}" if original_error else ""
        super().__init__(
            f"فشل الاتصال بالشبكة عند محاولة استخراج ترجمات الفيديو '{video_id}'.{detail}\n"
            "تحقق من اتصالك بالإنترنت وأعد المحاولة."
        )
