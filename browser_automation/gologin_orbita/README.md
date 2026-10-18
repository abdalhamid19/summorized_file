# التحكم في متصفح GoLogin عبر CDP

متحكم محلي يعيد تشغيل بروفايل GoLogin (متصفح Orbita، المبني على Chromium) ثم يتصل به عبر `Chrome DevTools Protocol` باستخدام `Playwright`.

**حالة مهمة تم التحقق منها على هذا الجهاز:** متصفح Orbita 152 يتجاهل الوسيط `--remote-debugging-port` تمامًا على خطة `trial`، فلا يفتح المنفذ ولا يظهر ملف `DevToolsActivePort`، ولا يذكر ملف السجل أي شيء عن التصحيح. تم التأكد من ذلك ببروفايل نظيف تمامًا خارج GoLogin أيضًا، فالمشكلة قيد داخل المتصفح نفسه وليست في البروفايل ولا في السكربت. النتيجة العملية: **الأتمتة عبر `CDP` لا تعمل إلا على اشتراك مدفوع.** المنطق هنا صحيح وموثق، لكنه لا يكفي في هذه الحالة.

التحكم في نافذة مفتوحة فعلًا دون اشتراك مدفوع ممكن فقط بطريقة أخرى: أتمتة واجهة ويندوز (`UI Automation` / `SendInput`) وهي تعمل بالإحداثيات وشجرة الوصول، لا بـ `DOM`. راجع [تقرير أتمتة المتصفح](../../docs/research/browser/) للتفاصيل.

## لماذا يُعيد السكربت تشغيل المتصفح

بروتوكول `CDP` لا يعمل إلا إذا شُغّل المتصفح مع `--remote-debugging-port`. البروفايل الذي يفتحه GoLogin من واجهته لا يحمل هذا الوسيط، لذلك لا يمكن لأي أداة خارجية الارتباط بنافذة مفتوحة هكذا. المنطق الذي ينفذه السكربت: يقرأ سطر أوامر العملية الجارية من النظام، ثم يعيد التشغيل بنفس المعالم نفسها (نفس مجلد البيانات، نفس الكوكيز، نفس الجلسات، ونفس معالم البصمة التي وضعها GoLogin) مع إضافة منفذ التصحيح فقط.

## متطلب `orbita.config`

Orbita لا يبدأ إطلاقًا بدون `orbita.config` داخل مجلد البروفايل؛ راجع `chrome_debug.log`:

```
ERROR:gologin\license\license.cc:39] License initialization aborted:
orbita.config not found or not readable in user data dir (exit code 403)
```

يكتب تطبيق GoLogin هذا الملف قبل التشغيل مباشرة ويقرأه Orbita ثم يحذفه، فهو غير متاح إلا في نافذة زمنية قصيرة. لذلك ينتظر السكربت (`--wait-token`) أن تشغّل البروفايل من GoLogin مرة واحدة أثناء عمله، ويلتقط الملف، ثم يغلق نسخة GoLogin ويعيد التشغيل بالملف الملتقط. محتوى الملف معاملات البصمة ورمز تشغيل مؤقت؛ لذلك لا يبقى صالحًا طويلًا، والحل يتكرر عند كل تشغيل جديد.

## الإعداد

يحتاج Python مع `Playwright`، ولا يحتاج تحميل متصفح لأن الاتصال يتم عبر `CDP` على متصفح موجود:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r browser_automation\gologin_orbita\requirements.txt
```

## التشغيل

افتح البروفايل من GoLogin أولًا (حتى يقرأ السكربت مساره ومعاملاته)، ثم شغّل المتحكم. سيُغلق المتصفح ويُفتح مجددًا مع منفذ التصحيح `9222`، وتعود النوافذ السابقة بسبب `--restore-last-session`:

```powershell
.\.venv\Scripts\python.exe browser_automation\gologin_orbita\orbita_cdp_control.py
```

خيارات مفيدة:

```powershell
# عرض أمر إعادة التشغيل دون لمس المتصفح
.\.venv\Scripts\python.exe browser_automation\gologin_orbita\orbita_cdp_control.py --dry-run

# بروفايل محدد عندما يكون مفتوحًا أكثر من ملف
.\.venv\Scripts\python.exe browser_automation\gologin_orbita\orbita_cdp_control.py --profile "$env:LOCALAPPDATA\GoLogin\profiles\YOUR_PROFILE_ID"

# الارتباط فقط دون إغلاق أي متصفح جارٍ
.\.venv\Scripts\python.exe browser_automation\gologin_orbita\orbita_cdp_control.py --no-restart --port 9222
```

المتغيرات: `--port` (المنفذ، الافتراضي `9222`)، `--timeout` (مهلة العناصر بالمللي ثانية، الافتراضي `15000`)، `--no-restart`، `--dry-run`.

## الأوامر

يقرأ المتحكم أمرًا واحدًا في كل سطر بصيغة `JSON Lines`، ويعيد النتيجة بالطريقة نفسها على `stdout`، وأخطاء الأوامر تصل في حقل `message` مع `event: error`:

```json
{"action":"status"}
{"action":"list"}
{"action":"select","index":0}
{"action":"open","url":"https://example.com"}
{"action":"navigate","url":"https://example.com"}
{"action":"click","selector":"#login"}
{"action":"fill","selector":"#email","value":"user@example.com"}
{"action":"press","selector":"#password","key":"Enter"}
{"action":"text","selector":"h1"}
{"action":"wait","selector":".results","state":"visible","timeout":30000}
{"action":"eval","expression":"document.title"}
{"action":"screenshot","path":"shot.png","fullPage":true}
{"action":"cookies","urls":["https://example.com"]}
{"action":"quit"}
```

الأوامر المتاحة:

| الأمر | الوصف |
| --- | --- |
| `status` | إصدار Orbita وحالة الاتصال وعدد النوافذ |
| `list` | قائمة النوافذ مع الرابط والعنوان والنافذة النشطة |
| `select` | اختيار النافذة النشطة بـ `index` |
| `open` | فتح رابط في نافذة جديدة |
| `navigate` | تنقل النافذة النشطة إلى رابط |
| `reload` / `back` / `forward` | إعادة تحميل أو تنقل في السجل |
| `click` | نقر على أول عنصر يطابق `selector` |
| `fill` | كتابة قيمة في أول عنصر يطابق `selector` |
| `press` | ضغط مفتاح على عنصر، مثل `Enter` |
| `text` | نص العنصر بعد إزالة الفراغات |
| `wait` | انتظار حالة عنصر (`visible` أو `hidden` أو `attached`) |
| `eval` | تقييم تعبير `JavaScript` في الصفحة وإرجاع النتيجة |
| `screenshot` | حفظ لقطة للشاشة، `fullPage` لالتقاط الصفحة كاملة |
| `cookies` | أسماء الكوكيز ونطاقاتها فقط، بلا قيم |
| `quit` | فصل الأداة وترك المتصفح يعمل |

`quit` يفصل الاتصال فقط ولا يغلق المتصفح؛ إغلاق المتصفح يتم من واجهة GoLogin كما هو.

## حدود الطريقة

- البروفايل يجب أن يكون مغلقًا ومتاحًا: لا يمكن إمساك ملف البيانات المفتوح، لذلك إعادة التشغيل شرط أساسي وليست تفصيلًا.
- GoLogin يزامن البروفايل مع الخادم عند تشغيله وإيقافه من الواجهة. التشغيل اليدوي يكتب في مجلد البروفايل المحلي فقط، وقد تُستبدل التغييرات المحلية عند مزامنة لاحقة من الواجهة.
- منفذ التصحيح يفتح اتصالًا محليًا بلا كلمة مرور. أبقِ المنفذ على `127.0.0.1` ولا تعرضه على الشبكة، خصوصًا أثناء العمل على حسابات مصرفية، ولا تشغّل أداة طرف ثالث على نفس المنفذ.
- `eval` ينفذ `JavaScript` في سياق الصفحة؛ لا تمرّر نصوصًا أو تعبيرات من مصادر غير موثوقة.
- الأداة لا تكتب كلمات مرور ولا تحل `CAPTCHA`. سجّل الدخول يدويًا في نافذة GoLogin قبل تشغيل الخطوات.
