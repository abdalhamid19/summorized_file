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

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
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
> ### الفكرة الأساسية
>
> المسار `index.html` موجود داخل مجلد `Project`. لذلك يبدأ رابط `helpers.css` بـ `../`، أي ارجع مستوى واحدًا إلى المجلد الأب. بقية الملفات داخل `Project` نفسها، فتبدأ مساراتها مباشرةً بـ `css/` أو `libs/`.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### علامات HTML
> >
> > #### `<link>`
> >
> > يربط ملف `CSS`.
> >
> > #### `<link>`
> >
> > يربط ملف `CSS`.
> >
> > #### `<link>`
> >
> > يربط ملف `CSS`.
> >
> > #### `<link>`
> >
> > يربط ملف `CSS`.
> >
> > #### `<link>`
> >
> > يربط ملف `CSS`.
> >
> > #### `<link>`
> >
> > يربط ملف `CSS`.
> >
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `html`
> >
> > ```html
> > <link rel="stylesheet" href="../helpers.css">
> > ```
> >
> > يفتح وسم `link` المستخدم بوصفه يربط ملف `CSS`.؛ `href` يحدد الوجهة.
> >
> > #### السطر 02 — `html`
> >
> > ```html
> > <link rel="stylesheet" href="css/main.css">
> > ```
> >
> > يفتح وسم `link` المستخدم بوصفه يربط ملف `CSS`.؛ `href` يحدد الوجهة.
> >
> > #### السطر 03 — `html`
> >
> > ```html
> > <link rel="stylesheet" href="css/fonts.css">
> > ```
> >
> > يفتح وسم `link` المستخدم بوصفه يربط ملف `CSS`.؛ `href` يحدد الوجهة.
> >
> > #### السطر 04 — `html`
> >
> > ```html
> > <link rel="stylesheet" href="libs/kit.css">
> > ```
> >
> > يفتح وسم `link` المستخدم بوصفه يربط ملف `CSS`.؛ `href` يحدد الوجهة.
> >
> > #### السطر 05 — `html`
> >
> > ```html
> > <link rel="stylesheet" href="libs/ui.css">
> > ```
> >
> > يفتح وسم `link` المستخدم بوصفه يربط ملف `CSS`.؛ `href` يحدد الوجهة.
> >
> > #### السطر 06 — `html`
> >
> > ```html
> > <link rel="stylesheet" href="libs/custom/custom.css">
> > ```
> >
> > يفتح وسم `link` المستخدم بوصفه يربط ملف `CSS`.؛ `href` يحدد الوجهة.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-02.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/02 - All Course Assignment.html|افتح صفحة التكليف 02]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
