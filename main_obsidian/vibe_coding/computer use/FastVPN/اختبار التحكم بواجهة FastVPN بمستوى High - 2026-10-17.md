---
title: اختبار التحكم بواجهة FastVPN بمستوى High - 2026-10-17
date: 2026-10-17
tags:
  - fastvpn
  - windows
  - desktop-automation
  - uia
---

# اختبار التحكم بواجهة FastVPN بمستوى High - 2026-10-17

## النتيجة

نجح أمر تحكم جديد من عملية مرتفعة مستقلة. كانت الواجهة قبل الأمر على صفحة **Locations**؛ وبعد `winapp ui click Settings` أصبحت على **Settings > General**. يثبت هذا انتقالًا مرئيًا داخل FastVPN، ولا يرفع مضيف Codex أو `node_repl.exe`.

لم يتغير اتصال VPN: ظل زر **Connect VPN** ظاهرًا، وظل الموقع **United States / Boston**. لم يُضغط زر الاتصال، ولم يُغيّر الموقع أو إعدادات FastVPN.

## القياس والتنفيذ

- وقت التنفيذ: 17 أكتوبر 2026، 11:27 صباحًا بتوقيت القاهرة.
- عملية FastVPN المستهدفة: PID `17440`.
- عملية PowerShell الجديدة: PID `34120`، وظهر في `whoami /groups` مستوى **High**، الرمز `S-1-16-12288`.
- أمر الفحص التفاعلي قبل النقرة: `winapp ui inspect -a 17440 --interactive`، رمز الخروج `0`.
- أمر التحكم: `winapp ui click Settings -a 17440 --quiet`، رمز الخروج `0`.
- الفحص التفاعلي ولقطة الشاشة بعد النقرة: رمز الخروج `0` لكل منهما.
- لم يُقَس PID رمز عملية `winapp.exe` نفسها في هذه المحاولة؛ قيس مستوى PowerShell المرتفع الذي شغّلها. وفي تجربة 15 أكتوبر سُجّل `winapp.exe` نفسه بمستوى High؛ راجع [[اختبار التحكم بواجهة FastVPN بمستوى High - 2026-10-15]].

## صور ما قبل الأمر وبعده

تظهر الصورة الأولى قائمة المواقع، وتظهر الثانية صفحة **Settings > General** بعد الأمر.

![[FastVPN-high-control-before-20261017.png]]

![[FastVPN-high-control-after-20261017.png]]

## اختبار السكربت بعد إضافته

- اجتاز الملف فحص صياغة PowerShell. شُغّل وضع `Inspect` بصلاحية High من PID `21892`؛ قرأ شجرة الواجهة ورمز الخروج `0`.
- شُغّل وضع `OpenLocations` من PowerShell PID `10184` بمستوى High على FastVPN PID `17440`. انتقلت الصفحة من **Settings** إلى **Locations**، ونجح الفحص ولقطة الشاشة بعد النقرة. كان رمز خروج أمر التحكم `0`.
- رفضت النسخة المثبتة من `winapp ui click` الاسم العام `Locations` لأنه يطابق عنصرين. كما أن هذا الإصدار لا يدعم `--type` مع `click`. أظهر فحص الشجرة أن `LocationsTitle` هو معرّف العنصر النصي المقصود، فاستُخدم المحدد الفريد بدل تخمين موضع أو اختيار عنصر ملتبس.
- بقي زر **Connect VPN** والموقع **United States / Boston** كما هما؛ لم يتغير اتصال VPN.

![[FastVPN-HighControl-OpenLocations-before-20261017.png]]

![[FastVPN-HighControl-OpenLocations-after-20261017.png]]

## سكربت إعادة الاختبار

أُضيف [[FastVPN-High-Control.ps1|سكربت التحكم المحدود]] بثلاثة أوضاع مسموحة: `Inspect` لفحص العناصر التفاعلية، و`OpenSettings` لفتح الإعدادات، و`OpenLocations` لفتح قائمة المواقع. يستخدم `OpenLocations` المحدد الفريد `LocationsTitle`؛ فالاسم العام `Locations` يطابق صورة وعنوانًا معًا في نسخة CLI المثبتة. يرفض السكربت العمل إذا لم يجد رمز **High**، ويستهدف عملية FastVPN الوحيدة الموجودة. لا يتضمن إيقاف عمليات Codex أو `node_repl`، ولا أمر الاتصال أو تغيير الموقع.

شغّل هذا الأمر من PowerShell عادي؛ سيظهر طلب **UAC** (نافذة موافقة Windows على تشغيل العملية بصلاحيات مسؤول). وافق عليه لتشغيل اختبار فتح الإعدادات:

```powershell
Start-Process -FilePath "$env:WINDIR\System32\WindowsPowerShell\v1.0\powershell.exe" -Verb RunAs -ArgumentList '-NoProfile -File "C:\pc\py\pyreview\summorized_file\main_obsidian\vibe_coding\computer use\FastVPN\FastVPN-High-Control.ps1" -Action OpenSettings -Pause' -Wait
```

للفحص دون نقرة، غيّر `OpenSettings` إلى `Inspect`. يكتب السكربت سجلًا وصورًا قبل النقرة وبعدها في `%TEMP%`، ويُظهر مساراتها في نافذة PowerShell المرتفعة. لا تستخدم `-ExecutionPolicy Bypass`؛ الأمر أعلاه لا يتجاوز سياسة التنفيذ.

يشرح توثيق Microsoft أن `Start-Process -Verb RunAs` يشغّل عملية جديدة عبر طلب الرفع. وتوضح وثائق `winapp ui` أن `click` يحاكي نقرة فأرة ويحتاج سطح مكتب تفاعليًا مفتوحًا؛ لذلك نفذ الاختبار والمستخدم مسجل الدخول والشاشة غير مقفلة. [[أدوات فحص شجرة FastVPN بمستوى High]] تعرض مسارات فحص أخرى.

## ما الذي يثبته هذا الاختبار

يمكن التحكم بتنقل FastVPN عبر عملية `winapp` جديدة تعمل تحت PowerShell مرتفع. هذا مسار عملي لأوامر محدودة تُشغّل بهذه الطريقة؛ لكنه لا يغيّر مستوى صلاحية جلسة Codex أو مضيف أداة التحكم. لذلك لا حاجة إلى إنهاء `ChatGPT.exe` أو `codex.exe` أو `node_repl.exe`، ولا ضمان أن إعادة تشغيلها مرتفعة ستعيد ربط مضيف التحكم أو تمنحه واجهة FastVPN.

راجع [[00 - فهرس التحقيق]] لبقية الأدلة والقيود.

## المراجع الرسمية

- [توثيق Windows App CLI لأتمتة الواجهة](https://github.com/microsoft/winappCli/blob/main/docs/ui-automation.md).
- [توثيق Microsoft للأمر `Start-Process`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process?view=powershell-5.1).
