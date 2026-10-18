# التحكم في نافذة GoLogin المفتوحة عبر أتمتة واجهة ويندوز

متحكم محلي يتعامل مع نافذة GoLogin (Orbita) المفتوحة **دون** إيقافها، ودون مفتاح API، ودون اشتراك مدفوع. يعتمد على `UI Automation` من ويندوز: يقرأ شجرة الوصول للعناصر، ويكتب داخلها، ويرسل نقرات وإدخالات حقيقية. لا يحتاج `CDP` ولا `Playwright`.

هذا هو الطريق الوحيد المتاح على خطة `trial`: انظر [مجلد gologin_orbita](../gologin_orbita/README.md) للتفاصيل عن حجب GoLogin لـ `--remote-debugging-port` على الخطط غير المدفوعة.

## ما تم التحقق منه فعليًا

| العملية | النتيجة |
| --- | --- |
| قراءة نوافذ Orbita وعنوانها وموضعها | تعمل |
| قراءة التبويبات والعنوان الحالي | تعمل |
| قراءة رابط الصفحة من شريط العناوين | تعمل |
| قراءة نص الصفحة | تعمل (عبر عقد `Text` داخل المستند) |
| فتح رابط / بحث | يعمل |
| كتابة عربية داخل أي حقل | تعمل |
| نقر على عنصر باسمه (أزرار المتصفح) | تعمل |
| نقر على رابط داخل الصفحة باسمه | **غير موثوقة**، انظر الحدود |
| لقطة شاشة للنافذة | تعمل |

## الإعداد

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r browser_automation\windows_uia_control\requirements.txt
```

يحتاج الأداة أن تكون النافذة **مرئية وغير مصغرة** على شاشة سطح المكتب نفسها. لا تعمل على جلسة عن بُعد أو مع نافذة في سطح مكتب افتراضي آخر.

## التشغيل

```powershell
.\.venv\Scripts\python.exe browser_automation\windows_uia_control\win_uia_control.py
```

عند وجود أكثر من بروفايل مفتوح، حدّد النافذة بعنوان جزئي:

```powershell
.\.venv\Scripts\python.exe browser_automation\windows_uia_control\win_uia_control.py --window "profile 2"
```

خيارات أخرى: `--delay <مللي>` لتسريع الاستجابة، و`--commands <ملف>` لقراءة الأوامر من ملف `UTF-8` بدل الإدخال القياسي.

## قراءة الأوامر من ملف

الأفضل عمليًا للخطوات الطويلة وللكتابة العربية: احفظ الأوامر في ملف `UTF-8` (بمسارات `/` لا `\`، لأن `\` في `JSON` محرف هروب):

```json
{"action":"navigate","url":"https://example.com"}
{"action":"page-text","limit":800}
{"action":"screenshot","path":"C:/Users/user/shots/page.png"}
{"action":"quit"}
```

```powershell
.\.venv\Scripts\python.exe browser_automation\windows_uia_control\win_uia_control.py --commands steps.jsonl
```

عند القراءة من الإدخال القياسي في PowerShell استخدم الترميز التالي كذلك حتى لا تتلف العربية:

```powershell
$OutputEncoding = [System.Text.Encoding]::UTF8
Get-Content steps.jsonl -Encoding UTF8 | .\.venv\Scripts\python.exe browser_automation\windows_uia_control\win_uia_control.py
```

## الأوامر

المخرجات على `stdout` بصيغة `JSON Lines`، وأخطاء الأوامر تصل في حقل `message` مع `event: error`.

| الأمر | الوصف |
| --- | --- |
| `windows` | كل نوافذ Orbita: العنوان، المعرّف، حدود النافذة |
| `focus` | إحضار النافذة إلى المقدمة |
| `tabs` | التبويبات مع التبويب المحدد |
| `select-tab` | بـ `index` أو `name` |
| `url` | قراءة رابط الصفحة الحالية |
| `navigate` | فتح رابط (يكتب في شريط العناوين ويلغي محتواه أولًا) |
| `search` | كتابة استعلام في شريط العناوين كبحث |
| `click` | `x` و`y` مع `relative` و`button` (`left`/`right`/`middle`) |
| `click-name` | نقر عنصر باسمه، مع `controlType` و`partial` |
| `type` | كتابة في عنصر (`name`) أو في شريط العناوين، مع `clear` |
| `keys` | إرسال مفاتيح (`{ENTER}`، `^l`) لعنصر محدد أو للنافذة |
| `scroll` | تمرير بعجلة الفأرة، `amount` سالب للأسفل |
| `page-text` | نص الصفحة، `limit` للحد الأقصى للأحرف |
| `screenshot` | لقطة للنافذة في `path` |
| `quit` | إنهاء المتحكم فقط، والمتصفح يبقى مفتوحًا |

أمثلة:

```json
{"action":"click","x":600,"y":420}
{"action":"click-name","name":"إعادة التحميل","controlType":"Button"}
{"action":"click-name","name":"اشترِ الآن","partial":true}
{"action":"type","name":"بحث","text":"ساعة ذكية","clear":true}
{"action":"keys","name":"بحث","keys":"{ENTER}"}
{"action":"select-tab","name":"Example Domain"}
{"action":"screenshot","path":"C:/Users/user/shots/step-3.png"}
```

## حدود الطريقة

- **ليست تحكمًا في `DOM`**: الأداة ترى ما تراه واجهة ويندوز. لا `JavaScript`، ولا مراقبة شبكة، ولا قراءة كوكيز، ولا انتظار ثابت لكل `selector`.
- **نقر الروابط داخل الصفحة بالاسم غير موثوق**: Orbita لا تحدّث عقد الروابط في شجرة الوصول بعد كل تنقل، وقد تبقى أسماء من الصفحة السابقة. استخدم `page-text` ثم `click` بالإحداثيات.
- **الإحداثيات تتغير** بحسب حجم النافذة والتمرير. استخدم `relative` مع حدود النافذة من `windows`، وأعد الحساب بعد كل تغيير تخطيط.
- **قبل كل كتابة نقر على العنصر**: Chromium لا يستقبل الحروف المحقونة إلا بعد أن يكون له عنصر مركّز داخليًا. الأداة تفعل ذلك تلقائيًا في `type` و`navigate`، أما `keys` بلا `name` فقد لا تصل للصفحة.
- **أي نافذة في المقدمة تتلقّى الإدخال**: لا تركّز على عناوين بنكية أو حساسية أثناء عمل السكربت.
- الأداة لا تكتب كلمات مرور ولا تحل `CAPTCHA`. ضع المستخدم في حلقة إن لزم.

## صيانة

الحزم المستخدمة: `pywinauto` (شجرة الوصول)، `Pillow` (لقطات الشاشة). لا حاجة إلى `Playwright` ولا `Selenium` ولا أي متصفح إضافي.
