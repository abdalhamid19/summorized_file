---
title: "CSS All Course Assignment 02"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 02
---

# CSS All Course Assignment 02

> [!question] المطلوب
> اكتب وسوم HTML التي تستدعي كل ملفات CSS في البنية الآتية، مع اعتبار كل علامتي `--` مستوى واحدًا إلى الداخل.
>
> ```text
> -- Project
> -- helpers.css
> ---- index.html
> ---- css
> ------ main.css
> ------ fonts.css
> ---- libs
> ------ kit.css
> ------ ui.css
> ------ custom
> -------- custom.css
> ```
>
> المثال الذي يبدأ به السؤال:
>
> ```html
> <link rel="stylesheet" href="css/example.css">
> ```

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```html
> <link rel="stylesheet" href="../helpers.css">
> <link rel="stylesheet" href="css/main.css">
> <link rel="stylesheet" href="css/fonts.css">
> <link rel="stylesheet" href="libs/kit.css">
> <link rel="stylesheet" href="libs/ui.css">
> <link rel="stylesheet" href="libs/custom/custom.css">
> ```
>
> المسار `index.html` موجود داخل مجلد `Project`. لذلك يبدأ رابط `helpers.css` بـ `../`، أي ارجع مستوى واحدًا إلى المجلد الأب. بقية الملفات داخل `Project` نفسها، فتبدأ مساراتها مباشرةً بـ `css/` أو `libs/`.
>
> أضف هذه الوسوم داخل `<head>` في صفحة `index.html`. لا توجد صورة مرفقة لهذا السؤال؛ عرض المصدر بنية المجلدات نصيًا.
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
