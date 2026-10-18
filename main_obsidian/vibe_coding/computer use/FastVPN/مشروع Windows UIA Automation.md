---
title: مشروع Windows UIA Automation
date: 2026-10-17
tags:
  - fastvpn
  - windows
  - pywinauto
  - uia
---

# مشروع Windows UIA Automation

نُقل السكربت وملف الاعتمادات خارج مجلد Obsidian إلى مشروع مستقل في جذر المستودع حتى تبقى الشيفرة وتعليمات تثبيتها منفصلة عن ملاحظات التحقيق.

- مسار المشروع النسبي من جذر المستودع: `windows_uia_automation/`
- مسار المشروع الكامل: `Join-Path $repoRoot 'windows_uia_automation'`
- ملف التشغيل: `Windows UIA Automation.py`
- ملف الاعتمادات المثبتة: `requirements-windows-ui-automation.txt`
- دليل التشغيل: `windows_uia_automation/README.md`

## التثبيت والتشغيل من PowerShell

تعمل الأوامر التالية من جذر المستودع:

```powershell
$repoRoot = (git rev-parse --show-toplevel).Trim()
$uiaProject = Join-Path $repoRoot 'windows_uia_automation'
$uiaVenv = Join-Path $uiaProject '.venv'
$uiaPython = Join-Path $uiaVenv 'Scripts\python.exe'
$uiaScript = Join-Path $uiaProject 'Windows UIA Automation.py'
$uiaRequirements = Join-Path $uiaProject 'requirements-windows-ui-automation.txt'

py -3.13 -m venv $uiaVenv
& $uiaPython -m pip install -r $uiaRequirements
& $uiaPython $uiaScript list-windows
& $uiaPython $uiaScript inspect --pid 12345 --depth 4 --limit 250
```

استبدل `12345` برقم العملية الظاهر حاليًا من `list-windows`. يبدأ `inspect` للقراءة فقط. راجع دليل المشروع قبل استخدام `invoke` أو `click`؛ فهما يرسلان فعلًا واحدًا فقط ويتطلبان `--confirm`.

إذا كان التطبيق يعمل بمستوى `High`، شغّل **PowerShell جديدًا** كمسؤول بعد موافقة `UAC`، ثم أعد فحص النوافذ والعملية. السكربت لا يرفع نفسه تلقائيًا.

## سجل FastVPN

- سجل تجربة `pywinauto` على FastVPN: [[اختبار pywinauto على FastVPN - 2026-10-17]].
- مقارنة الأدوات وحدود السكربت: [[اختيار أفضل أداة لبناء سكربت تحكم عام - 2026-10-17]].
- جرد أدوات قراءة شجرة UIA: [[أدوات فحص شجرة FastVPN بمستوى High]].
