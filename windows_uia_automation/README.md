# مشروع أتمتة واجهة Windows باستخدام UIA

هذا مشروع Python مستقل لعرض النوافذ، وفحص شجرة عناصر الواجهة، وإرسال فعل واحد إلى عنصر محدد باستخدام `pywinauto` (مكتبة Python للتحكم بواجهات Windows) و`UIA` (واجهة Windows المخصصة لإتاحة عناصر التطبيقات).

## المتطلبات والتثبيت

يعمل المشروع على Windows ويتطلب Python `3.13` و`pywinauto 0.6.9`، المثبتة من الملف المثبت الإصدارات `requirements-windows-ui-automation.txt`.

افتح PowerShell داخل هذا المجلد، ثم أنشئ بيئة Python مستقلة وثبّت الاعتماد:

```powershell
py -3.13 -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r ".\requirements-windows-ui-automation.txt"
$uiaPython = Join-Path (Get-Location).Path '.venv\Scripts\python.exe'
$uiaScript = Join-Path (Get-Location).Path 'Windows UIA Automation.py'
```

## الاستخدام

اعرض النوافذ الحالية، ثم افحص نافذة التطبيق باستخدام `PID` (رقم تعريف العملية) الذي ظهر للتو:

```powershell
& $uiaPython $uiaScript list-windows
& $uiaPython $uiaScript inspect --pid 12345 --depth 4 --limit 250
```

يعمل `inspect` للقراءة فقط. استخدم `--title` بدل `--pid` عندما يكون عنوان النافذة فريدًا. أعد `list-windows` بعد إعادة تشغيل التطبيق لأن رقم العملية يتغير.

قبل الفعل، نفّذ `--dry-run` لمراجعة العنصر المطابق دون إرساله. يتطلب الفعل الحقيقي `--confirm` وعنصرًا وحيدًا بالاسم الدقيق أو `AutomationId` (معرّف العنصر الذي يعلنه التطبيق):

```powershell
& $uiaPython $uiaScript invoke --pid 12345 --name 'Settings' --dry-run
& $uiaPython $uiaScript invoke --pid 12345 --name 'Settings' --confirm --expect-name 'General'
```

`invoke` يطلب الفعل الافتراضي من عنصر UIA. أما `click` فيرسل نقرة ماوس إلى موضع العنصر؛ وهو أقل ضمانًا لأن فحص النافذة الأمامية وإرسال النقرة عمليتان منفصلتان. لا تستخدمه إلا بعد مراجعة العنصر، ويمكن طلب تفعيل النافذة والتحقق منها عبر `--activate-window`.

`--expect-name` و`--expect-automation-id` يتحققان من وجود العنصر المتوقع بعد الفعل. هذا فحص لحالة الواجهة بعد التنفيذ، ولا يثبت وحده أن الفعل هو سبب الحالة.

## الصلاحيات وحدود الاستخدام

لا يرفع السكربت صلاحياته تلقائيًا ولا يتجاوز `UAC` (نافذة موافقة Windows). إذا كان التطبيق يعمل بمستوى `High`، افتح PowerShell جديدًا واختر `Run as administrator`، ثم وافق على طلب UAC وشغّل السكربت في جلسة Windows نفسها. يقيس السكربت صلاحية العملية الحالية والهدف قبل الفعل، ويرفض الهدف الأعلى صلاحية.

تعتمد النتائج على العناصر التي يعلنها التطبيق إلى `UIA`. لذلك لا يضمن المشروع قراءة أو التحكم بكل برنامج أو بكل عنصر فيه. لا يقرأ قيم الحقول المدخلة، ولا يكتب نصًا، ولا يرسل اختصارات لوحة المفاتيح أو سلسلة أفعال.

التفاصيل التاريخية لاختبار FastVPN محفوظة في مجلد FastVPN داخل Obsidian؛ هذا المشروع يحتوي على السكربت ومتطلباته وتعليمات تشغيله.
