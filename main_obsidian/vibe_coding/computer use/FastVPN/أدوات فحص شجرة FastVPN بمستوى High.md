---
title: أدوات فحص شجرة FastVPN بمستوى High
date: 2026-10-15
tags:
  - fastvpn
  - windows
  - accessibility
  - uia
  - computer-use
---

# أدوات فحص شجرة FastVPN بمستوى High

## الغرض وحدود البحث

هذا جرد للأدوات المنشورة التي يمكن أن تساعد في قراءة شجرة عناصر واجهة FastVPN، ثم مقارنة النتيجة عندما يعمل قارئ الشجرة بمستوى الصلاحية نفسه للتطبيق. المقصود بـ«كل الأدوات» هنا الأدوات العملية التي أمكن التحقق من وظائفها في وثائق Microsoft أو المشروع الأصلي؛ لا توجد قائمة مغلقة تشمل كل البرامج التجارية والداخلية.

**نتيجة المقارنة الحالية:** على PID FastVPN `8744` نفسه وبالأمر والعمق نفسيهما، أعاد قارئ `Medium` عنصرًا واحدًا، وأعاد قارئ `High` عدد `961` عنصرًا. التفاصيل والحدود أدناه.

| العملية المقاسة سابقًا | المستوى وقت القياس | الملاحظة |
|---|---|---|
| `node_repl.exe`، PID `3348` | Medium، SID `S-1-16-8192` | مستضيف أداة التحكم. |
| `node.exe`، PID `2652` و`7880` | Medium | عمليتان مرتبطتان بأداة التحكم. |
| `ChatGPT.exe` و`codex.exe` | Medium | لا تُستخدم هذه القياسات لإثبات مستوى قارئ مستقل سيبدأ لاحقًا. |
| `FastVPN.exe`، PID `6052` بحسب المحضر السابق | High، SID `S-1-16-12288` | أعد اكتشاف PID إذا أعيد تشغيل التطبيق؛ الأرقام تتغير. |

## نتيجة تجربة WinApp CLI المحلية

ثُبّت `Windows App Development CLI` بالإصدار `0.7.1`. فُحصت شجرة FastVPN بأمر القراءة فقط `winapp ui inspect` مع `--json` والعمق `8`؛ لم تُستخدم أوامر النقر أو التفعيل.

### المحاولة الأولى: تشغيل Medium

في 15 أكتوبر 2026 قرأ PID `33244` نافذة FastVPN PID `6052` وهو يعمل بمستوى `Medium`:

| العملية | PID | Integrity Level وSID | TokenElevation | TokenElevationType | TokenUIAccess |
|---|---:|---|---|---|---|
| `winapp.exe` | `33244` | Medium، `S-1-16-8192` | `False` | `Limited` | `False` |
| `FastVPN.exe` | `6052` | High، `S-1-16-12288` | `True` | `Full` | `False` |

```powershell
winapp ui inspect -a 6052 --depth 8 --json
```

انتهى الأمر برمز `0`، لكنه أعاد عنصرًا واحدًا فقط (`Window` باسم `FastVPN`) من دون عناصر داخلية. كان PID `33244` متوسطًا لأنني شغّلت CLI من عملية عادية بمستوى `Medium` ولم أطلب تشغيل نسخة جديدة عبر UAC. Windows لا يرفع رمز عملية حية بعد إنشائها.

### إعادة الاختبار على PID نفسه بمستويي Medium وHigh

للتأكد من أثر الصلاحية، قورنت القراءتان على PID FastVPN نفسه `8744`، في جلسة المستخدم نفسها، مع CLI `0.7.1` والأمر والعمق نفسيهما. أُطلقت نسخة PowerShell جديدة عبر `RunAs` بعد موافقة UAC؛ بقيت عملية Codex وأداة `node_repl` على `Medium`.

| العملية وقت الفحص | PID | Integrity Level وSID | TokenElevation | TokenElevationType | TokenUIAccess |
|---|---:|---|---|---|---|
| `powershell.exe`، مشغّل المقارنة Medium | `3924` | Medium، `S-1-16-8192` | `False` | `Limited` | `False` |
| `winapp.exe`، قراءة Medium عند 14:17:33 | `16680` | Medium، `S-1-16-8192` | `False` | `Limited` | `False` |
| `winapp.exe`، قراءة High عند 14:16:52 | `10488` | High، `S-1-16-12288` | `True` | `Full` | `False` |
| `FastVPN.exe`، الهدف في القراءتين | `8744` | High، `S-1-16-12288` | `True` | `Full` | `False` |

```powershell
winapp ui inspect -a 8744 --depth 8 --json
```

| نتيجة القراءة على الهدف نفسه | Medium | High |
|---|---:|---:|
| النوافذ | 1 | 1 |
| `elementCount` والعناصر المعدودة فعليًا | 1 | 961 |
| رمز الخروج | 0 | 0 |
| `stderr` | فارغ | فارغ |

تضمنت شجرة High `4` أزرار، و`474` عنصر نص، و`248` صورة، و`118` عنصرًا مخصصًا، و`112` عنصر قائمة، وعنصر `List` واحد، و`3` فواصل، وعنصر `Window` واحد. من الأمثلة زر `Connect VPN` بمعرّف `Connect`، والموقع `United States` والمدينة `Boston`، وعناصر `Locations` و`Settings` و`Account`. يبيّن JSON أن `102` عنصرًا موسوم بـ`isOffscreen=true`، وأن `859` موسوم بـ`false`؛ كما أن `interactive=false`، أي إن الاختبار قرأ الشجرة ولم ينفّذ تفاعلًا.

الفرق الكبير على PID الهدف نفسه وبالوسيطات نفسها يدعم بقوة أن تشغيل القارئ عند `Medium` كان سبب غياب العناصر الداخلية في هذه المقارنة. لكنه لا يثبت أن كل عنصر مرئي أو قابل للتفاعل، ولا يثبت أن مضيف Codex صار مرتفعًا: العملية المرتفعة كانت `winapp.exe` مستقلة أُنشئت بموافقة UAC. `TokenUIAccess=False` للقارئ المرتفع أيضًا؛ نجاح تعداد الشجرة هنا لا يتطلب أن يكون `UIAccess` مفعّلًا.

> [!important] تحديث قاعدة الأذونات
> أفاد المستخدم أن دعم Namecheap أكد أن `Everyone: Allow FullControl` قاعدة متوقعة وصحيحة في هذا التثبيت ولا تمثل مخالفة. لم نطّلع بأنفسنا على نص التذكرة أو رد الدعم؛ وبناءً على هذه الإفادة نسحب التحذير السابق الذي عامل القاعدة كخلل مؤكد أو شرط يمنع اختبار قارئ UIA مرتفع. لا نوصي بتعديل ACL يدويًا اعتمادًا على التحليل السابق. هذا التوضيح لا يغيّر قياس `High` ولا يثبت سبب نقص الشجرة.

## مصطلحات سريعة

| المصطلح | معناه هنا |
|---|---|
| `UI Automation (UIA)` | واجهة Windows التي تكشف عناصر مثل الأزرار والحقول في صورة شجرة يمكن لقارئ الإتاحة أو أداة الاختبار فحصها. |
| `Integrity Level (IL)` | مستوى سلامة رمز العملية. `Medium` مستوى البرامج العادية غالبًا؛ `High` مستوى العملية التي رُفعت بموافقة UAC. |
| `UAC` | نافذة التحكم بحساب المستخدم التي تطلب موافقة فعلية لبدء عملية مرتفعة. الموافقة تبدأ عملية جديدة؛ لا ترفع `node_repl.exe` العامل أصلًا. |
| `UIAccess` | امتياز خاص لبعض تقنيات المساعدة الموثوقة. ليس اسم أداة، ولا يعني بذاته أن مستوى السلامة صار `High`. |
| `Provider` | جزء من التطبيق أو إطار الواجهة يصف عناصره لـUIA. لا تستطيع أداة الفحص اختراع أزرار دلالية إذا لم يكشفها التطبيق. |

تختلف شجرة `Raw` (كل عناصر UIA المتاحة) عن `Control` (العناصر التي تمثل عناصر تحكم للمستخدم) وعن `Content` (مجموعة أضيق للمحتوى). لذلك قد تختلف مخرجات الأدوات حتى عند فحص النافذة نفسها. كما أن أجزاء الشجرة تُبنى عند الطلب، وتعتمد على دعم الـProvider في التطبيق. [شرح شجرة UI Automation ومناظيرها](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-treeoverview) · [نظرة عامة على UIA Providers](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview)

## ترتيب الخيارات لهذا الفحص

1. **للفحص المرئي الموثق للتطبيق الإداري:** Accessibility Insights for Windows، بوضع `Live Inspect`. توثق الأداة صراحة أن التطبيقات التي تعمل كمسؤول تحتاج إلى تشغيل Accessibility Insights كمسؤول في كل جلسة، أو إلى إعداد UIAccess الخاص بها. [الأسئلة الشائعة: فحص التطبيقات الإدارية](https://accessibilityinsights.io/docs/windows/reference/faq/) · [دليل Live Inspect](https://accessibilityinsights.io/docs/windows/getstarted/inspect/)
2. **أداة مثبتة على هذا الجهاز:** Power Automate for desktop. أظهر فحص الحزم المحلي في 15 أكتوبر 2026 الحزمة `Microsoft.PowerAutomateDesktop` بالإصدار `11.2609.183.0`. وتوثق Microsoft أن أداة `Inspect UI elements` تعرض الشجرة، وأنه إذا كان التطبيق المستهدف مرتفعًا فيُعاد تشغيل Power Automate بصلاحيات مرتفعة. استخدم نافذة الفحص للقراءة فقط، ولا تنشئ تدفقًا ينفّذ أفعالًا. [دليل Inspect UI elements](https://learn.microsoft.com/en-us/power-automate/desktop-flows/inspect-ui-elements)
3. **أفضل لقطة نصية أو JSON للمقارنة:** `winapp ui inspect`. يستهدف PID أو اسم التطبيق ويطبع شجرة UIA؛ يدعم `--json` للحفظ والمقارنة. لكنه في `Public Preview` (معاينة عامة قد تتغير أوامره وبنية JSON)، ويضم أوامر أخرى للنقر والتفعيل؛ لا تستخدم في هذه التجربة إلا `inspect`. **تحديث 15 أكتوبر 2026:** ثُبّت محليًا من WinGet بالمعرف `Microsoft.WinAppCli`، ونجح تشغيل الإصدار `0.7.1`. [توثيق CLI وحالة المعاينة](https://learn.microsoft.com/en-us/windows/apps/dev-tools/winapp-cli/) · [دليل UI automation وJSON والاستهداف بـPID](https://github.com/microsoft/winappCli/blob/main/docs/ui-automation.md)
4. **مفتش رسومي مستقل مفتوح المصدر:** `FlaUInspect`. يعرض شجرة وخصائص UIA، ويتيح الاختيار بين `UIA2` و`UIA3`. هو مشروع مجتمع مبني على FlaUI، وليس منتج Microsoft. يجب تشغيل ملف الفحص نفسه عبر UAC ثم قياس رمز عمليته؛ لا نفترض أن مجرد وجود نافذة الأداة يعني أنها `High`. [المستودع والإصدارات](https://github.com/FlaUI/FlaUInspect)

> [!warning] Power Automate وUIAccess
> وضع `UIAccess` في Power Automate يعطي مكوّن UI Automation مستوى `Medium+` مع امتياز خاص للتعامل مع تطبيقات مرتفعة، ولا يثبت أن القارئ نفسه يعمل بمستوى `High`. ولأن المطلوب هنا مقارنة High مقابل Medium، استخدم تشغيل Power Automate كمسؤول عبر UAC، لا وضع UIAccess. تذكر Microsoft أيضًا أن UIAccess يتطلب تغييرًا في سجل Windows وله اعتبارات أمنية. [توثيق UIAccess في Power Automate](https://learn.microsoft.com/en-us/power-automate/desktop-flows/how-to/enable-ui-access)

## فهرس الأدوات

| الأداة | هل تقرأ شجرة UIA؟ | طريقة التشغيل المرتفع لهذا الاختبار | التقييم والحدود |
|---|---|---|---|
| **Accessibility Insights for Windows** | نعم؛ `Live Inspect` يعرض العنصر ومكانه وخصائصه. | شغّل البرنامج نفسه بـ`Run as administrator` واقبل UAC يدويًا. توثيق الأداة يذكر هذا المسار صراحة للتطبيقات الإدارية. | **الخيار الأول للفحص اليدوي.** يفحص ما يقدمه التطبيق؛ وقد لا يجد بعض إطارات Java/Swing التي تحتاج Java Access Bridge. |
| **Power Automate for desktop** | نعم؛ `Inspect UI elements` يعرض شجرة سطح المكتب وخصائص العناصر. | أعد تشغيل Power Automate كمسؤول إذا كان FastVPN مرتفعًا، ثم افحص من نافذة Inspect. قِس PID الخاص بمكوّن قراءة الواجهة، لا تكتفِ بكون المصمم مفتوحًا. | **متوفر محليًا بحسب فحص الحزم.** هو منتج أتمتة تدفقات أكبر من المطلوب؛ التزم بواجهة Inspect ولا تشغّل إجراءً. |
| **Windows App Development CLI (`winapp ui inspect`)** | نعم؛ نص أو JSON مع استهداف التطبيق بالـPID. | افتح طرفية جديدة عبر UAC وشغّل الأمر منها، ثم تحقق من PID الفعلي لـ`winapp` أو عملية القراءة المساعدة. لا تفترض أن مستوى الطرفية يثبت مستوى كل ابن لها. | **الأفضل للحفظ والمقارنة الآلية.** Public Preview؛ ثبّت إصدار CLI في سجل التجربة لأن الأوامر ومخطط JSON قد يتغيران. |
| **FlaUInspect** | نعم؛ شجرة وخصائص وأنماط التحكم، مع UIA2/UIA3. | شغّل الأداة نفسها عبر UAC، ثم قِس عمليتها أو العملية المساعدة التي تقرأ UIA. | مفتوح المصدر ومفيد للمقارنة المستقلة؛ توثيق المجتمع لا يضمن وحده نتيجة High على FastVPN. |
| **`Inspect.exe` من Windows SDK** | نعم؛ يدعم UIA وMSAA ومناظير Raw/Control/Content. | وثائق Microsoft تقول إنه لا يحتاج عادةً لمسؤول، لكنها لا تثبت سيناريو المقارنة مع تطبيق High. يمكن تشغيله عبر UAC كاختبار مستقل والتحقق من رمزه. | **مقارن احتياطي جيد، لكنه Legacy (قديم).** تجنب قائمة `Action` حتى تظل المحاولة قراءة فقط. [مرجع Inspect](https://learn.microsoft.com/en-us/windows/win32/winauto/inspect-objects) |
| **AccScope من Windows SDK** | نعم؛ يصوّر عناصر UIA بأوضاع مثل `Leaf Control` و`Text Pattern` و`Narrator` ومرشحات تحكم. | يمكن تشغيله مرتفعًا ثم قياس رمز قارئه؛ وثائقه لا تؤكد مباشرة أن الرفع شرط أو ضمان لفحص FastVPN. | أداة تصوّر وتشخيص للمطورين، وLegacy. ليست مستكشف Raw tree عامًّا ولا أفضل وسيلة لحفظ شجرة نصية. [مرجع AccScope](https://learn.microsoft.com/en-us/windows/win32/winauto/accscope) |
| **Visual UI Automation Verify** | واجهة لاختبار UIA فيها لوحة للشجرة والخصائص والنتائج. | إذا استخدمته، شغّل قارئه مرتفعًا وتحقق من PID. لا تعرض وثائق Microsoft وصفًا خاصًا لتجاوز فرق High/Medium. | Legacy وموجّه أساسًا لاختبارات تنفيذ UIA وتسجيل نتائجها، لا إلى استعراض شجرة شامل؛ مرجع مقارنة ثانوي. [مرجع UIA Verify](https://learn.microsoft.com/en-us/windows/win32/winauto/ui-automation-verify) |
| **Python مع `pywinauto`** | نعم؛ حدد الخلفية `uia` لتعداد عناصر النافذة وطباعة معرفات العناصر والأبناء. | شغّل `python.exe` الجديد عبر UAC؛ اتصل بـPID FastVPN نفسه، ثم قِس PID الذي ينفذ الطباعة. | جيد لإنتاج سجل قابل للتكرار، لكنه يتطلب كتابة/تشغيل سكربت. الخلفية الافتراضية `win32` ليست بديلًا عن UIA؛ استخدم `backend="uia"` وطباعة المعرفات فقط. [دليل البدء وواجهة UIA](https://pywinauto.readthedocs.io/en/latest/getting_started.html) |
| **Python مع `uiautomation`** | نعم؛ تتضمن المكتبة `automation.py` لتعداد الشجرة ويمكن توجيه الكود إلى PID. | شغّل Python أو الأمر `automation.py` كعملية جديدة عبر UAC، ثم قِس رمز القارئ. | مكتبة مجتمع مباشرة لـUIA؛ README ينصح بالتشغيل كمسؤول لتفادي فشل تعداد عناصر في بعض الحالات. إذا كان التطبيق Electron فقد يتطلب تمكين دعم renderer عند بدء التطبيق؛ لا تضف وسيطًا غير موثق إلى FastVPN لمجرد التجربة. [المستودع ودليل الأداة](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows) |
| **PowerShell مع `.NET UI Automation`** | نعم؛ يمكن كتابة قارئ يبدأ من `AutomationElement.RootElement` ثم يقرأ `FindAll` أو `TreeWalker`. | افتح PowerShell جديدًا عبر `RunAs` بموافقة UAC ونفّذ سكربت قراءة فقط؛ افحص رمز PowerShell الذي ينفذ استدعاء UIA نفسه. | لا يوجد أمر PowerShell جاهز مخصص للشجرة؛ يحتاج سكربتًا، لكنه يستخدم API Microsoft مباشرة. استهدف نافذة FastVPN وعمقًا محددًا بدل تعداد الشاشة كلها. [مرجع RootElement](https://learn.microsoft.com/en-us/dotnet/api/system.windows.automation.automationelement.rootelement?view=windowsdesktop-9.0) |
| **WinAppDriver مع Appium Inspector** | يمكن أن يعرض مصدر عناصر التطبيق وشجرة XML عبر جلسة اختبار. | يجب تشغيل الخادم/المكوّن الذي يجمع المصدر بمستوى ملائم، والتحقق من رمزه أيضًا. | إطار اختبار أثقل يعتمد خادمًا وجلسة، ومصمم لتشغيل سيناريوهات التفاعل. خادم WinAppDriver لم تُصنه Microsoft منذ 2022؛ لذلك لا نوصي به لفحص قراءة واحدة. [WinAppDriver](https://github.com/microsoft/WinAppDriver) · [Appium Windows Driver وحالة الخادم](https://github.com/appium/appium-windows-driver) · [قائمة Appium الرسمية للسواقات](https://github.com/appium/appium/blob/master/packages/appium/docs/en/ecosystem/drivers.md) · [Appium Inspector](https://github.com/appium/appium-inspector) |

تسرد Microsoft أيضًا `AccChecker` لفحص قواعد الإتاحة و`AccEvent` لمراقبة أحداث الإتاحة؛ يفيدان عند تشخيص دعم التطبيق، لكنهما ليسا البديل المباشر الأبسط لقراءة شجرة FastVPN ومقارنة رمز القارئ. وتقول صفحة أدوات الاختبار إن `Accessible Explorer` و`UI Spy` أداتان متقادمتان لم تعودا متاحتين. [قائمة أدوات اختبار الإتاحة من Microsoft](https://learn.microsoft.com/en-us/windows/win32/winauto/accessibility-testingtools)

## أدوات قياس الرمز وليست قارئات شجرة

- **Sysinternals AccessChk:** أداة سطر أوامر لفحص رمز عملية بعينها. توثيق Microsoft يشرح `-p` لاستهداف عملية أو PID، و`-f` لعرض معلومات الرمز الكاملة، و`-v` لإضافة `Integrity Level`. مثال القراءة:

  `accesschk64.exe -p -f -v <PID>`

  شغّل AccessChk نفسه بصلاحية تسمح له بقراءة العملية المستهدفة، وتأكد أن `<PID>` هو PID القارئ الفعلي. AccessChk يعرض مستوى السلامة، لكنه ليس وحده إثباتًا لحقلي `TokenElevation` و`TokenUIAccess`. [توثيق AccessChk](https://learn.microsoft.com/en-us/sysinternals/downloads/accesschk)
- **Process Explorer:** يعرض العمليات وخصائصها، ويمكنه المساعدة في مراجعة `Integrity Level` وهوية الملف. لا يعرض شجرة UIA، ولا يغني عن قراءة حقول Token المطلوبة عند توثيق المقارنة. [Process Explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer) · [فيديو Microsoft عن Process Explorer ومستويات السلامة](https://learn.microsoft.com/en-us/shows/defrag-tools/2-process-explorer)
- **Windows API `GetTokenInformation`:** الوسيلة الدقيقة لاستعلام `TokenIntegrityLevel` و`TokenElevation` و`TokenElevationType` و`TokenUIAccess` من رمز العملية. `TokenElevationTypeFull` يعني أن الرمز مرتفع. قد تحتاج إلى كود مساعد؛ لا تخلط بين `UIAccess=True` وبين `High`. [GetTokenInformation](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) · [حقول TOKEN_INFORMATION_CLASS](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_information_class) · [أنواع الرفع](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_elevation_type)

## أدوات تعرض معلومات نافذة مختلفة عن شجرة UIA

- **Spy++** يعرض شجرة النوافذ والعمليات والخيوط ورسائل Win32؛ يفيد لمعرفة تقسيم النوافذ، لكنه ليس بديلًا لشجرة UIA الدلالية. [دليل Spy++ من Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/using-spy-increment)
- **AutoIt Window Info (Au3Info)** يعرض عناوين النوافذ والنص والفئة والحجم وعناصر Win32 تحت المؤشر؛ ليس بديلًا لشجرة UIA الدلالية. [توثيق Au3Info](https://www.autoitscript.com/autoit3/docs/intro/au3spy.htm)

## ما المقصود بإثبات أن الفاحص High؟

لا يكفي ظهور نافذة UAC أو كون الطرفية الأم مرتفعة. يجب أن نسجل العملية التي نفذت قراءة UIA نفسها، لأن بعض الأدوات تنشئ عملية مساعدة:

| الحقل | ما يسجل في التجربة |
|---|---|
| اسم الأداة ونسختها | مثال: Accessibility Insights أو `winapp` مع الإصدار. |
| PID القارئ | PID لعملية الفحص التي استعلمت عن UIA، مع PID العملية الأم/المساعدة إن وجدت. |
| موافقة UAC | نعم/لا ووقت بدء العملية؛ لا تُؤتمت شاشة سطح المكتب الآمن. |
| `TokenIntegrityLevel` | يجب أن يظهر `High`؛ والـSID المتوقع `S-1-16-12288`. |
| `TokenElevation` أو `TokenElevationType` | سجّل `True` أو `TokenElevationTypeFull` لإثبات الرفع. سجّل Integrity منفصلًا. |
| `TokenUIAccess` | سجله مستقلًا كـ`True` أو `False`؛ لا تستنتج منه مستوى High. |
| العملية المستهدفة | PID ومسار `FastVPN.exe` ووقت القياس؛ أعد اكتشاف PID بعد إعادة التشغيل ولا تعتمد على PID قديم. |
| نتيجة الشجرة | لقطة Raw/Control/Content أو JSON، وعمق القراءة، والمرشحات، وهل ظهرت عناصر داخلية. |

تؤكد Microsoft أن `GetTokenInformation` يقرأ بيانات الرمز، وأن `UIAccess` امتياز خاص ببرامج تقنيات المساعدة وله شروط توقيع وموقع تثبيت. [معلومات رمز الوصول](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) · [اعتبارات أمان UI Automation وUIAccess](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-securityoverview) · [سياسة UIPI وUIAccess](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-account-control-allow-uiaccess-applications-to-prompt-for-elevation-without-using-the-secure-desktop)

بدء أداة بـ`Run as administrator` عبر UAC ينشئ عملية جديدة؛ لا يرفع العملية الحية تلقائيًا. مثال Microsoft:

`Start-Process -FilePath "powershell" -Verb RunAs`

[مرجع Start-Process وخيار RunAs](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-5.1)

## خطوات مقارنة مقترحة

1. اترك FastVPN مفتوحًا بالحالة نفسها، من دون تغيير الموقع أو ضغط `Connect VPN`. سجّل وقت الفحص واكتشف PID الحالي من جديد.
2. اختر أولًا **Accessibility Insights** إذا أردت رؤية مباشرة. افتحه بـ`Run as administrator` واقبل UAC بنفسك، أو استخدم **Power Automate Inspect** بعد إعادة تشغيله كمسؤول؛ فهما يملكان مسارًا موثقًا لفحص تطبيق مرتفع. لا تغيّر إعدادات UAC ولا تحاول التحكم بسطح المكتب الآمن.
3. قبل قراءة الشجرة، سجّل PID قارئ UIA ومستوى رمزه. يمكن استخدام AccessChk المرتفع للتحقق من Integrity Level. ولتسجيل `TokenElevation` و`TokenUIAccess` بدقة، استخدم قارئ `GetTokenInformation` أو وسيلة موثوقة تعرض هذين الحقلين.
4. اقرأ الشجرة فقط. لا تستخدم أوامر `click` أو `invoke` أو `set-value`، ولا تشغّل تدفق Power Automate. عند الحاجة إلى ملف قابل للمقارنة، استخدم `winapp ui inspect -a <FastVPN-PID> --json` بعد التحقق من إصدار CLI ورمز عملية الفحص.
5. سجّل المنظور والعمق والمرشحات، ثم كرر القراءة بأداة ثانية مستقلة. لا تقارن JSON محدود العمق بشجرة كاملة. عند المقارنة بين `Inspect.exe` أو AccScope والأداة الأولى، دوّن إن كان الفرق بين Raw وControl وContent بدل اعتباره فرق صلاحية.
6. إذا ظهرت عناصر داخلية في قارئ `High` ولم تظهر في Medium، فهذا يدعم أن اختلاف مستوى الصلاحية ساهم في المشكلة. إذا بقيت النافذة وحدها في عدة قراءات High ومناظير UIA، فهذا يرجّح محدودية Provider أو طريقة عرض مخصصة؛ لكنه لا يثبتها دون فحص التطبيق أو دعم Namecheap. [شرح Providers](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview)

يجب أن يعمل القارئ والهدف في جلسة المستخدم نفسها. تحذر وثائق Microsoft من أن UI Automation لا يتيح الاتصال بين عمليتين بدأتا لمستخدمين مختلفين عبر `Run as`؛ لذلك إذا طلب UAC بيانات مسؤول لمستخدم آخر، سجّل ذلك، ولا تعتبر النتيجة مقارنة صالحة قبل التأكد من هوية المستخدم والجلسة. [نظرة Microsoft على UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-uiautomationoverview)

## خلاصة تنفيذية

- **ابدأ بـAccessibility Insights كمسح مرئي موثق، أو Power Automate Inspect لأنه مثبت في هذا الجهاز.**
- **استخدم `winapp ui inspect --json` أو `pywinauto` إذا كان المطلوب حفظ شجرة قابلة للمقارنة.**
- **قِس رمز قارئ الشجرة نفسه قبل المقارنة**؛ المتوقع لـHigh هو `S-1-16-12288` مع `TokenElevation=True` أو `TokenElevationTypeFull`. سجّل `TokenUIAccess` منفصلًا.
- لا يوجد ضمان أن الشجرة ستصبح كاملة بعد الرفع؛ ظهور العناصر يعتمد أيضًا على الـProvider ومنظور القراءة.
- إفادة المستخدم عن Namecheap تنفي اعتبار قاعدة ACL مخالفة أو شرطًا سابقًا لهذا الاختبار؛ لم نتحقق من نص رد الدعم مباشرة ولم نعدّل ACL.

## مواد مرجعية إضافية: كتاب، مقال، وفيديو

- **كتاب:** [Windows Internals, Part 1, 7th Edition — Microsoft Press](https://learn.microsoft.com/en-us/sysinternals/resources/windows-internals). خلفية معمقة عن العمليات ورموز الوصول وأمن Windows؛ يغطي Windows 10 وServer 2016، لذلك لا يستخدم لإثبات تفاصيل إصدار Windows الحالي أو شجرة FastVPN.
- **مقال تقني:** [Why is it so hard to write a program that requires UI Access privilege? — The Old New Thing](https://devblogs.microsoft.com/oldnewthing/20121213-00/?p=5843). شرح Raymond Chen لسبب فرض شروط صارمة على UIAccess؛ مرجع توضيحي قديم، وتبقى وثائق Microsoft الحالية هي المرجع للسياسة.
- **فيديو Microsoft:** [Defrag Tools #2 — Process Explorer](https://learn.microsoft.com/en-us/shows/defrag-tools/2-process-explorer)، وخصوصًا الدقيقة 18:07 لشرح Integrity Levels وUAC. يشرح قياس مستوى العملية ولا يشرح شجرة UIA.

---

[[00 - فهرس التحقيق|العودة إلى فهرس تحقيق FastVPN]]
