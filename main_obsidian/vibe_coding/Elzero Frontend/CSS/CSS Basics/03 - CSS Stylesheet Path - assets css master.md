---
title: "03 - CSS Stylesheet Path - assets/css/master.css"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - stylesheets
  - تكليف
aliases:
  - تكليف مسار assets/css/master.css
---

# 03 - CSS Stylesheet Path - assets/css/master.css

> [!question] السؤال
> استدعِ ملف التنسيق الخارجي `master.css` الموجود في `assets/css` بجانب ملف `index.html`.
>
> ```html
> <link rel="stylesheet" href="{ Write Path Here }" />
> ```
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-1-to-4/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <link rel="stylesheet" href="assets/css/master.css" />
> ```
>
> **سبب المسار**
>
> يبدأ المسار من مجلد `index.html`. مجلد `assets` بجانبه مباشرة، ثم داخله `css/master.css`؛ لذلك لا نحتاج إلى `../`.
>
> **هيكل المشروع**
>
> ```text
> task-03-assets-css-demo/
> ├── index.html
> └── assets/
>     └── css/
>         └── master.css
> ```
>
> **عرض يعمل**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Basics/Demo 03 - assets css master/index.html|معاينة صفحة HTML]] أو [[vibe_coding/Elzero Frontend/CSS/CSS Basics/Demo 03 - assets css master/assets/css/master.css|ملف master.css]].

## المصدر

[تكليفات CSS للدروس 01–04](https://elzero.org/css-assignments-lesson-from-1-to-4/)
