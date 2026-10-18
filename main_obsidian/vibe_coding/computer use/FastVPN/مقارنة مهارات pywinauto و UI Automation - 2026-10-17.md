---
title: مقارنة مهارات pywinauto و UI Automation
date: 2026-10-17
tags:
  - fastvpn
  - windows
  - pywinauto
  - uia
  - skills
---

# مقارنة مهارات pywinauto و UI Automation

> [!summary] القرار
> لسكربت Python الذي يتحكم في FastVPN، استمر باستخدام [[مشروع Windows UIA Automation|السكربت الحالي]]؛ فقد نجح بالفعل في فحص FastVPN والتنقل بين صفحاته بعملية `High` (مستوى صلاحية مرتفع بموافقة UAC، نافذة تأكيد Windows). أفضل مهارة قابلة للإضافة لتوجيه وكيل إلى فحص واجهات Windows والتفاعل معها هي مهارة Microsoft `winapp-ui-automation`، لكنها تستخدم أداة `winapp ui` ولا تكتب سكربت `pywinauto`. أقرب مهارة متخصصة في `pywinauto` هي `windows-desktop-e2e`، لكنها موجهة لاختبارات التطبيقات وليست مشغلًا عامًا. لم أجد مهارة واحدة تجمع بين تحكم عام بـ`pywinauto` وفحص الصلاحيات وحواجز السكربت الحالي.

## ما الذي بحثت عنه؟

استخدمت بحث `skills.sh` و`npx skills find` بكلمتي `pywinauto` و`Windows UI automation`، ثم راجعت ملفات `SKILL.md` في المرشحين الأقرب، ومصادر Microsoft و`pywinauto` الأصلية. استعنت بثلاثة وكلاء فرعيين لمراجعات مستقلة: فهرس المهارات، خيار Microsoft، وملاءمة الخيارات لسكربت FastVPN. تحققت كذلك من سكربت FastVPN وتقارير اختباره محليًا.

كلمة **Skill** هنا تعني ملف تعليمات يعلّم الوكيل أسلوب العمل. أما **pywinauto** فهي مكتبة Python تنفذ الأتمتة، و**winapp** برنامج سطر أوامر منفصل يوفّر أوامر UI Automation (أتمتة واجهة المستخدم) من Microsoft. لذلك وجود مهارة لا يثبّت تلقائيًا المكتبة أو البرنامج الذي تستخدمه.

## الترشيح بحسب الاستخدام

إذا كان المقصود مهارة **للكود واختبارات `pywinauto`**، فاختر `windows-desktop-e2e` من ECC. وإذا كان المقصود أن يتفاعل الوكيل مع تطبيق Windows حيّ ويفحص العناصر بنفسه، فاختر `winapp-ui-automation` من Microsoft. أما FastVPN فيبقى الاختيار العملي الأفضل له هو السكربت الموجود، لأنه جُرّب عليه بالفعل.

| الخيار | أفضل استخدام | الحكم لهذا العمل |
| --- | --- | --- |
| Microsoft `winapp-ui-automation` | توجيه وكيل لفحص تطبيق Windows والبحث في عناصره والتفاعل معها والتحقق من النتيجة | أفضل مهارة خارجية عامة لـUI Automation؛ رسمية من Microsoft. تستخدم `winapp ui`، وليست مهارة كتابة `pywinauto`. عُدّاد الصفحة وقت البحث 46 تثبيتًا وقرابة 1.3K نجمة للمستودع. [صفحة المهارة](https://www.skills.sh/microsoft/winappcli/winapp-ui-automation) · [المصدر الرسمي](https://github.com/microsoft/winappCli/blob/main/plugins/winapp/skills/winapp-ui-automation/SKILL.md) |
| Microsoft `winui-ui-testing` | إنشاء مجموعة اختبارات واجهة آلية على دفعة واحدة عبر `winapp ui` | مهارة اختبار رسمية مساعدة؛ تغطي Win32 وWPF وWinForms وWinUI، وتصلح لاختبارات ذات توقعات ولقطات نتيجة. ليست مهارة `pywinauto` للتحكم العام في تطبيق المستخدم. [ملف المهارة](https://github.com/microsoft/winappCli/blob/main/plugins/winui/agent-plugin/skills/winui-ui-testing/SKILL.md) |
| `affaan-m/ecc@windows-desktop-e2e` | إنشاء اختبارات واجهة آلية لتطبيق Windows باستخدام `pywinauto` و`pytest` | مرشح قوي لاختبارات التطوير المستمرة. نطاقه اختبار E2E (اختبار رحلة المستخدم كاملة) وCI (التكامل المستمر: تشغيل الفحوص تلقائيًا عند تحديث الكود)، وليس سكربت أوامر عام للتحكم اليدوي في برامج المستخدم. تعرض صفحة Skills.sh نحو 4.1K تثبيت وقت البحث؛ عدد التثبيتات مقياس انتشار فقط وليس دليل جودة أو سرعة. [صفحة المهارة](https://www.skills.sh/affaan-m/ecc/windows-desktop-e2e) · [ملف المهارة](https://github.com/affaan-m/ecc/blob/main/skills/windows-desktop-e2e/SKILL.md) |
| `malue-ai/dazee-small@pywinauto` | أمثلة أساسية على اكتشاف النوافذ والعناصر وتشغيل الأفعال عبر `pywinauto` | هو الأكثر مباشرة باسم `pywinauto`، لكن تعليماته تمنع التعامل مع نوافذ المسؤول وUAC، وتطلب تأكيدًا لكل فعل وتضيف انتظارًا قدره نصف ثانية بعد كل خطوة. هذه قيود غير مناسبة لتجربة FastVPN المرتفعة، كما أنها تبطئ التسلسلات. لا أوصي بتثبيته لهذا المشروع. [ملف المهارة](https://github.com/malue-ai/dazee-small/blob/main/instances/xiaodazi/skills/pywinauto/SKILL.md) · [صفحة Skills.sh](https://www.skills.sh/malue-ai/dazee-small/pywinauto) |
| مهارة `computer-use` المضمّنة | التحكم المرئي المباشر في تطبيق Windows من خلال `@oai/sky` | موجودة بالفعل في بيئتك. مناسبة لمهمة تفاعلية مباشرة، لكنها لا تحل محل مكتبة Python ولا تعلّم سكربت `pywinauto` الحالي. |

### خيارات لم تصل إلى الترشيح

- `zrong/skills@os-use` دليل عام طويل يخلط بين `pywinauto` و`pyautogui` (تحكم مرئي بالإحداثيات والصورة)، لذلك لا يطابق الحاجة إلى اختيار عنصر UIA محدد والتحقق منه.
- `youngjunning/windows-app-automation` يقدم مهارة Codex مفصلة ومساعد PowerShell (لغة أوامر Windows) يستخدم .NET (منصة تطوير Microsoft) لـUI Automation، لكنه ليس `pywinauto`، ومستودعه صغير جدًا. في المساعد المنشور تُستدعى `SetForegroundWindow` (طلب تفعيل النافذة) قبل النقر من دون فحص نجاح التفعيل أو إعادة التأكد من النافذة الأمامية قبل إرسال الماوس؛ كما لا يقيس مستوى الصلاحية. لذلك لا أراه بديلًا جاهزًا لسكربت FastVPN الحالي. [ملف المهارة](https://github.com/youngjunning/windows-app-automation/blob/main/SKILL.md) · [المساعد](https://github.com/youngjunning/windows-app-automation/blob/main/scripts/windows-ui.ps1#L252-L258) · [مسار النقر](https://github.com/youngjunning/windows-app-automation/blob/main/scripts/windows-ui.ps1#L391-L405)

## لماذا لا أصف أي خيار بأنه «الأسرع»؟

لم أجد اختبار سرعة مستقلًا يقارن هذه المهارات على **البرنامج نفسه**. المهارة نص تعليمات؛ السرعة الفعلية تعتمد على أداة التنفيذ، وعدد عناصر الواجهة، وطريقة تحديد العنصر، واستجابة التطبيق. لذلك لا يصح استنتاج أن مهارة ما أسرع من عدد تثبيتها.

لتقليل الزمن في سكربت UI Automation:

1. حدّد عنصرًا واحدًا بمعرّف `AutomationId` (معرّف العنصر في شجرة الواجهة) أو باسم ونوع فريدين، بدل طباعة الشجرة كاملة عند كل خطوة.
2. استخدم نمط UIA (واجهة Microsoft لأتمتة الواجهة) مثل `Invoke` (طلب تنفيذ فعل الزر) أو `ValuePattern` (قراءة قيمة حقل أو تغييرها) عندما يدعمه العنصر؛ استخدم نقرة الماوس فقط كخطة بديلة. هذا يتجنب الإحداثيات وشرط تركيز النافذة في الحالات المدعومة.
3. استخدم انتظارًا محددًا للحالة المتوقعة بدل تأخيرات ثابتة. واجهة UI Automation تدعم تخزين خصائص العناصر في cache (ذاكرة مؤقتة) لتقليل استدعاءات النظام المتكررة. [دليل Microsoft لعميل UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-clientsoverview) · [أنماط عناصر التحكم](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-controlpatternsoverview)

وفي مهارة Microsoft تحديدًا، يعرض الخيار `--interactive` العناصر القابلة للفعل فقط، وتوصي المهارة بتجميع الأوامر المتتابعة في استدعاء واحد باستخدام `;` لتقليل جولات الوكيل. هذا يحسّن زمن التنسيق والاستكشاف، ولا يُعد قياسًا لسرعة استجابة FastVPN نفسها. [تعليمات المهارة الرسمية](https://github.com/microsoft/winappCli/blob/main/plugins/winapp/skills/winapp-ui-automation/SKILL.md)

## التوافق وحدود الصلاحية

تدعم `pywinauto` خلفيتين (محركين للوصول إلى الواجهة): `uia` لواجهة Microsoft UI Automation، و`win32` لواجهات Win32 التقليدية. اختيار الخلفية يعتمد على التطبيق؛ السكربت الحالي يثبت `uia` ولا يختبر `win32` تلقائيًا، لذا هو قابل لإعادة الاستخدام مع برامج تكشف عناصر UIA، وليس ضمانًا للتحكم في **كل** برنامج. يوضح Microsoft أن ظهور عنصر للتحكم يعتمد على ما يقدمه التطبيق عبر مزوّد UIA؛ وقد لا توفر العناصر المرسومة خصيصًا شجرة مفيدة. [دليل pywinauto الرسمي](https://github.com/pywinauto/pywinauto/blob/master/docs/getting_started.txt) · [نظرة Microsoft على مزودي UIA](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview)

مهارة `winapp-ui-automation` توصي باستخدام `invoke` و`set-value` والانتظار والتحقق، وتفحص التركيز قبل إدخال لوحة المفاتيح الفعلي. لكنها لا ترفع رمز العملية إلى `High` ولا تمنح `UIAccess` (امتياز خاص لتطبيقات الإتاحة). ويندوز يقيّد تحكم العملية ذات مستوى السلامة الأقل في واجهة عملية أعلى؛ لذلك يجب أن تعمل أداة الأتمتة بصلاحية متوافقة، عبر موافقة UAC (نافذة تأكيد Windows لتشغيل برنامج بصلاحيات أعلى) من المستخدم عند الحاجة. [شرح Windows لأمن UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-securityoverview)

هناك تحذير إضافي: توثيق `winapp ui send-keys --via post-message` يذكر أن `PostMessage` (إرسال رسالة إلى طابور نافذة Windows) يتجاوز UIPI. لكن مرجع Microsoft الرسمي لـ`PostMessage` يقول إن إرسال الرسائل محكوم بـUIPI، ولا يسمح للعملية بالإرسال إلا إلى مستوى سلامة مساوٍ أو أقل. لم أختبر هذا المسار على FastVPN؛ لا أعتبره حلًا لتجاوز حد الصلاحيات، ولا أوصي باستخدامه لهذا الغرض. [توثيق winapp](https://github.com/microsoft/winappCli/blob/main/docs/ui-automation.md#send-keys) · [مرجع PostMessage من Microsoft](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-postmessagew)

أما حالة WinApp CLI الحالية، فتوثيق Microsoft يصفه بأنه **Public Preview** (معاينة عامة) وقد تتغير أوامره. لذلك تصلح المهارة للتجربة الحالية، لكن ينبغي مراجعة التوثيق قبل تثبيت أوامرها في أتمتة طويلة الأمد. [حالة WinApp CLI](https://learn.microsoft.com/en-us/windows/apps/dev-tools/winapp-cli/)

## الدليل المحلي من FastVPN

في اختبار 17 أكتوبر 2026، قرأ [[مشروع Windows UIA Automation|السكربت الحالي]] عدد **961 عنصرًا** من FastVPN بعملية Python بمستوى `High` (صلاحية مرتفعة). رفض السكربت النقرة عندما لم تكن نافذة FastVPN أمامية؛ ثم فعّلها، وتحقق من مقبضها قبل الإرسال، وانتقل إلى `Settings` وعاد إلى `Locations`. بقي VPN على `United States / Boston` دون اتصال أو تغيير للموقع. هذا يثبت هذا المسار المحدد فقط، وليس كل أزرار FastVPN أو كل البرامج. راجع [[اختبار pywinauto على FastVPN - 2026-10-17]].

## النتيجة العملية

- **لـFastVPN وسكربت Python الحالي:** استمر بـ`pywinauto` بعد تشغيل العملية بوساطة UAC وبمستوى متوافق مع FastVPN. استخدم `dry-run` (معاينة الخطوات بلا تنفيذ) و`confirm` (تأكيد الفعل)، وحدد عنصرًا فريدًا، وتحقق من التركيز والنتيجة بعد كل فعل.
- **لوكيل يريد فحص/تشغيل واجهة Windows عبر CLI:** اختَر Microsoft `winapp-ui-automation` إذا رغبت في إضافة مهارة. أمر التثبيت الذي تعرضه صفحة المهارة هو:

  ```powershell
  npx skills add https://github.com/microsoft/winappcli --skill winapp-ui-automation
  ```

  هذا يثبت **المهارة فقط**؛ ولا يضمن رفع صلاحية `winapp` أو نجاحها على FastVPN. لم أثبتها في هذا البحث.
- **لإنشاء اختبارات E2E لتطبيق Windows يملكه المطور:** استخدم `windows-desktop-e2e`، وليس كسكربت تحكم عام للمستخدم.

  ```powershell
  npx skills add https://github.com/affaan-m/ecc --skill windows-desktop-e2e
  ```

إذا أردنا مهارة مخصصة لهذا السكربت، ينبغي أن تضيف اختيارًا موجّهًا بين `uia` و`win32`، مع إبقاء قياس صلاحية القارئ والهدف، رفض المحددات الملتبسة، فحص النافذة الأمامية قبل إدخال الفأرة، والتحقق من الحالة المتوقعة بعد الفعل. لا ينبغي أن ترفع الصلاحية بنفسها أو تتجاوز UAC/UIPI.

## المصادر الأساسية

- [Microsoft: مهارة winapp-ui-automation](https://github.com/microsoft/winappCli/blob/main/plugins/winapp/skills/winapp-ui-automation/SKILL.md)
- [Microsoft: مهارة اختبارات واجهة Windows](https://github.com/microsoft/winappCli/blob/main/plugins/winui/agent-plugin/skills/winui-ui-testing/SKILL.md)
- [ECC: مهارة اختبارات pywinauto](https://github.com/affaan-m/ecc/blob/main/skills/windows-desktop-e2e/SKILL.md)
- [Microsoft: UI Automation في WinApp CLI](https://learn.microsoft.com/en-us/windows/apps/dev-tools/winapp-cli/ui-automation)
- [Microsoft: حالة وتثبيت WinApp CLI](https://learn.microsoft.com/en-us/windows/apps/dev-tools/winapp-cli/)
- [Microsoft: أمان UI Automation ومستويات الصلاحية](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-securityoverview)
- [Microsoft: عميل UI Automation والتخزين المؤقت](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-clientsoverview)
- [Microsoft: مرجع PostMessage وUIPI](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-postmessagew)
- [pywinauto: دليل بدء التشغيل والخلفيات](https://github.com/pywinauto/pywinauto/blob/master/docs/getting_started.txt)
- [pywinauto: المستودع الرسمي](https://github.com/pywinauto/pywinauto)
- [Skills.sh: مهارة Microsoft](https://www.skills.sh/microsoft/winappcli/winapp-ui-automation)
- [[اختيار أفضل أداة لبناء سكربت تحكم عام - 2026-10-17]]
- [[اختبار pywinauto على FastVPN - 2026-10-17]]

[[00 - فهرس التحقيق|العودة إلى فهرس تحقيق FastVPN]]
