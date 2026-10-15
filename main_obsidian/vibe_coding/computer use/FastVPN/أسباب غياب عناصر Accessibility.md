---
title: لماذا قد تظهر نافذة FastVPN وحدها في شجرة Accessibility؟
date: 2026-10-15
tags:
  - fastvpn
  - accessibility
  - ui-automation
  - windows
aliases:
  - محدودية مزود إمكانية الوصول في FastVPN
  - رسم واجهة FastVPN وعناصر الأتمتة
---

# لماذا قد تظهر نافذة FastVPN وحدها في شجرة Accessibility؟

## الخلاصة

في إعادة القياس المسجلة في [[إعادة قياس الصلاحية وشجرة الواجهة]]، أظهرت قراءة `sky` بعد تنشيط نافذة FastVPN عنصر النافذة الجذر فقط؛ لم تظهر أزرار أو عناصر فرعية. في القياس نفسه كان `FastVPN.exe` بمستوى **High**، وكان `node_repl.exe` ذو PID `3348` وعمليتا `node.exe` ذوا PID `2652` و`7880` بمستوى **Medium**.

هذا يثبت ما أعادته أداة التحكم في تلك اللقطة. لا يثبت أن FastVPN لا يوفّر عناصر إمكانية وصول مطلقًا، ولا يحدد وحده هل السبب فرق الصلاحيات، أو مزوّد الواجهة، أو طريقة بناء الشجرة لدى أداة القراءة.

> [!important] حدود الاختبار
> لم تُرفع أداة التحكم إلى High، ولذلك لم تُقارن شجرة Medium بشجرة قارئ يعمل بمستوى High. كما لم تُحدّد تقنية واجهة FastVPN أو طريقة رسمها من هذه اللقطة.

## ما هو مزوّد Accessibility؟

**UI Automation (UIA)** هو إطار Windows الذي يسمح لقارئات الشاشة وأدوات الفحص والاختبار بقراءة معلومات الواجهة والتعامل معها. يعمل **Provider** (مزوّد الواجهة) داخل التطبيق أو عبر وسيط، ويعرّف للعميل العناصر وخصائصها وعلاقاتها والوظائف التي تدعمها. العميل لا يحوّل كل ما يراه في الصورة إلى أزرار تلقائيًا؛ بل يقرأ العناصر التي يستطيع مزوّد الواجهة كشفها. تشرح Microsoft بنية العميل والمزوّد في [نظرة UI Automation العامة](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-uiautomationoverview) و[نظرة مزوّدات UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview).

تأتي عناصر Windows القياسية في أطر مثل Win32 وWindows Forms وWPF عادةً مع دعم UIA. أمّا **Custom Control** (عنصر تحكم مخصص) أو عنصر من مكتبة خارجية فقد يحتاج إلى مزوّد خاص. من دون مزوّد مناسب قد تكون معلومات الأداة محدودة إلى خصائص النافذة المضيفة، مثل موضعها، فلا ترى زرًا أو قائمة كعنصر مستقل. وتشرح Microsoft الفرق بين [المزوّدات المضمّنة والمخصصة](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview) و[المزوّد الوسيط للعناصر التي لا تكشف مزوّدًا كاملًا](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-clientsideprovider).

قد يكون المزوّد موجودًا لكنه **ناقص**: مثلًا يكشف النافذة أو اللوحة الرئيسية ولا يعرّف أبناءها، أو لا يربط العناصر بأسمائها وأنواعها وعلاقاتها. في العناصر المركبة، يشرح توثيق Microsoft أن المزوّد يعرّف التنقل بين أجزاء العنصر وحدوده وعلاقته بالعنصر الأب. راجع [تنفيذ مزوّد UI Automation لعناصر مخصصة](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-serversideprovider).

## اختلاف مناظير الشجرة ونطاق القراءة

شجرة UIA ليست قائمة ثابتة واحدة. يستطيع العميل اختيار نطاق البحث وتصفية العناصر ضمن مناظير مختلفة:

- **Raw View** (العرض الخام): أوسع تمثيل لعناصر الأتمتة التي يقدّمها التطبيق.
- **Control View** (عرض عناصر التحكم): يستبعد عادةً العناصر المستخدمة للزينة أو التخطيط فقط.
- **Content View** (عرض المحتوى): أضيق، ويركّز على العناصر التي تنقل معلومات للمستخدم.

لذلك قد يغيب عنصر من عرض التحكم أو المحتوى مع وجوده في عرض آخر. كما قد يقرأ العميل النافذة ونطاقًا محدودًا من أبنائها فقط. توثيق Microsoft يشرح هذه المناظير والترشيح في [نظرة شجرة UI Automation](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-treeoverview). ونتيجة `sky` المسجلة لا تكفي وحدها لمعرفة أي منظور أو نطاق استُخدم داخليًا؛ لذلك يلزم فحص مستقل قبل نسبة الغياب إلى التطبيق.

## كيف تؤثر طريقة رسم الواجهة؟

**Rendering** (الرسم) هو تحويل حالة الواجهة إلى صورة على الشاشة، بينما **Accessibility tree** (شجرة إمكانية الوصول) هي وصف دلالي للأجزاء التي يمكن لبرنامج قراءتها. هذان مساران مختلفان: ظهور شكل زر في الصورة لا يضمن وجود عنصر `Button` مقابل له في الشجرة.

إذا رسم التطبيق نافذته داخل لوحة واحدة أو سطح رسومي مخصص، فقد يرى المستخدم عدة أزرار ومناطق قابلة للنقر بينما لا يرى برنامج الأتمتة إلا النافذة أو اللوحة التي ترسمها. يحدث ذلك عندما لا يعلن التطبيق عن أجزاء الرسم بوصفها عناصر فرعية ذات أسماء وأنواع وحدود ووظائف. وهذا احتمال عام، وليس دليلًا على أن FastVPN يستخدم رسمًا مخصصًا.

الرسم المخصص لا يمنع Accessibility حتمًا. يستطيع مطوّر التطبيق توفير مزوّد يعلن العناصر الفرعية حتى عندما تُرسم يدويًا؛ وتعرض Microsoft [مثال UI Automation لتطبيق يستخدم Direct2D](https://learn.microsoft.com/en-us/windows/win32/winauto/samples-entry) لإيضاح ذلك. لا نعرف من القياس الحالي هل FastVPN مبني بعناصر أصلية أو لوحة مخصصة أو إطار واجهة آخر؛ لا ينبغي تخمين Electron أو Qt أو غيرهما من مظهر النافذة.

## وجود العنصر يختلف عن القدرة على تشغيله

قد تظهر العقدة في الشجرة من دون أن تدعم الوظيفة التي نحتاجها. **Control Pattern** (نمط تحكم) هو مجموعة خصائص وأوامر تعرّف ما يستطيع العنصر فعله؛ مثل `Invoke` (تشغيل أمر زر) أو `Value` (قراءة/تغيير قيمة). لذلك:

- غياب العقدة يعني أن قارئ الشجرة لم يعرض عنصرًا في ذلك النطاق والمنظور.
- وجود العقدة مع غياب `Invoke` يعني أن العنصر عُرض، لكن نمط الضغط البرمجي غير مكشوف.
- ظهور `Invoke` لا يضمن نجاح العملية؛ يجب قراءة حالة التطبيق بعد التنفيذ.

تشرح Microsoft هذا الفصل في [نظرة أنماط التحكم](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-controlpatternsoverview).

## علاقة UIPI بنتيجة FastVPN

**UIPI — User Interface Privilege Isolation** (عزل واجهة المستخدم بحسب مستوى الصلاحية) قد يقيّد التفاعل من عملية منخفضة الصلاحية مع واجهة عملية مرتفعة. لذا فإن فرق المستوى المقاس يجعل UIPI عاملًا محتملًا في المشكلة. لكنه لا يفسر تلقائيًا مزوّدًا مفقودًا أو شجرة ناقصة؛ رفع مستوى القارئ قد يغيّر ما يمكنه التفاعل معه، لكنه لا يُنشئ عناصر دلالية لم ينشرها التطبيق.

القراءة الفعلية حتى الآن هي: أداة `sky` بمستوى Medium أعادت نافذة الجذر فقط. لم يُختبر قارئ بمستوى مماثل لـFastVPN. أفاد المستخدم أن دعم Namecheap أكد أن قاعدة `Everyone: Allow FullControl` متوقعة ولا تمثل مخالفة؛ لذلك لا نعدها شرطًا يمنع اختبار قارئ UIA مستقلًا بموافقة UAC، ولا نوصي بتغيير ACL استنادًا إلى التحذير السابق. راجع [[توضيح أذونات تثبيت FastVPN]] و[[أدوات فحص شجرة FastVPN بمستوى High]].

## أثر تعطيل Secure Desktop

إيقاف خيار **Switch to the secure desktop when prompting for elevation** (عرض مطالبة الرفع على سطح المكتب الآمن) لا يرفع صلاحية `node_repl.exe` ولا يضيف عناصر إلى شجرة FastVPN. يغيّر موضع مطالبة UAC فقط: تظهر على سطح المكتب التفاعلي العادي بدل السطح المعزول، مع بقاء طلب الموافقة/بيانات المسؤول قائمًا ما لم تتغير إعدادات UAC الأخرى.

النتيجة الأمنية هي ضعف حماية شاشة الموافقة من تقليد نافذة UAC أو خداع المستخدم بواجهة أو مؤشر مزيف. توصي Microsoft بإبقاء الخيار مفعّلًا للحماية من تزوير الإدخال والعرض؛ راجع [سياسة Secure Desktop](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/user-account-control-switch-to-the-secure-desktop-when-prompting-for-elevation) و[شرح عمل UAC](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works). تعطيل هذا الخيار ليس اختبارًا مناسبًا لمعرفة سبب شجرة FastVPN المحدودة.

## كيف نميّز بين الأسباب؟

1. أبقِ FastVPN في الحالة الظاهرة نفسها، وسجّل لقطة النافذة وPID والوقت، من دون الضغط على **Connect VPN**.
2. افحص النافذة بأداة Microsoft `Inspect.exe` من Windows SDK (حزمة أدوات التطوير)، واختر وضع UI Automation ثم افحص **Raw View** و**Control View** و**Content View**. سجّل الاسم ونوع التحكم والرقم التعريفي وأنماط التحكم لكل عنصر. يوضح [دليل Inspect](https://learn.microsoft.com/en-us/windows/win32/winauto/inspect-objects) أن الأداة تعرض خصائص UIA وMSAA ومناظير الشجرة المختلفة.
3. قارن النتيجة مع قراءة `sky` للنافذة نفسها. إذا ظهرت العناصر في Inspect ولم تظهر في `sky`، فالأرجح أن الاختلاف في منظور/نطاق القراءة أو طبقة الأداة. هذه قرينة تحتاج إلى مراجعة إعداداتها.
4. إذا غابت العناصر في Raw View لدى قارئ مناسب، افحص MSAA/`IAccessible` (واجهة إمكانية الوصول الأقدم) وتحقق من دعم التطبيق أو اسأل المورد عن مشكلة Accessibility. إذا ظهرت عناصر لكن بلا نمط `Invoke` أو `Value`، فسجّل ذلك كقصور في الأنماط، لا كغياب للعقد.
5. إذا بقي اختبار فرق الصلاحيات ضروريًا، استخدم فاحص UIA مستقلًا ضيق المهمة وبموافقة UAC، وسجّل PID الفاحص وIntegrity Level وTokenElevation قبل قراءة الشجرة. لا تشغّل مستضيف JavaScript عامًا بصلاحيات إدارية لمجرد قراءة الشجرة. قائمة الأدوات والخطوات في [[أدوات فحص شجرة FastVPN بمستوى High]].

## ما نعرفه وما لا نعرفه عن FastVPN

| البند | الحالة |
|---|---|
| نتيجة قراءة `sky` بعد تنشيط النافذة | نافذة الجذر فقط؛ لا عناصر تحكم فرعية ظاهرة في القراءة |
| مستوى FastVPN عند القياس | High، PID `6052` |
| مستوى `node_repl.exe` المحدد | Medium، PID `3348`؛ لم يُرفع |
| تفسير UIPI | متوافق مع فرق الصلاحيات، لكنه غير مثبت كسبب وحيد |
| اكتمال مزوّد Accessibility في FastVPN | غير معلوم |
| تقنية رسم FastVPN | غير معلومة؛ لا نستنتجها من شكل النافذة |
| شجرة FastVPN عند قارئ High | لم تُختبر |

## مراجع Microsoft

- [UI Automation Overview](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-uiautomationoverview) — علاقة العميل بالمزوّد.
- [UI Automation Providers Overview](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-providersoverview) — العناصر القياسية والمخصصة والمزوّدات.
- [UI Automation Tree Overview](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-treeoverview) — Raw/Control/Content View والنطاق والترشيح.
- [Implement a Server-Side UI Automation Provider](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-serversideprovider) — كشف عناصر التحكم المخصصة والتنقل بينها.
- [UI Automation Control Patterns Overview](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-controlpatternsoverview) — وظائف التحكم مثل Invoke وScroll.
- [Samples (UI Automation)](https://learn.microsoft.com/en-us/windows/win32/winauto/samples-entry) — مثال لإتاحة تطبيق Direct2D.
- [Inspect Objects](https://learn.microsoft.com/en-us/windows/win32/winauto/inspect-objects) — فحص خصائص MSAA وUIA ومناظير الشجرة.
- [Security Considerations for Assistive Technologies](https://learn.microsoft.com/en-us/windows/win32/winauto/uiauto-securityoverview) — حدود UIAccess وتفاوت مستويات السلامة.

## روابط داخل مجلد التحقيق

- [[إعادة قياس الصلاحية وشجرة الواجهة|القياس الفعلي لشجرة FastVPN ومستويات العمليات]]
- [[مشكلة الصلاحية|التقرير الكامل عن FastVPN والصلاحيات والحلول]]
- [[توضيح أذونات تثبيت FastVPN|توضيح أذونات التثبيت بعد رد Namecheap]]
- [[00 - فهرس التحقيق|فهرس التحقيق]]
