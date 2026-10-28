---
title: "04 - CSS Stylesheet Path - ../source/css/main.css"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - stylesheets
  - تكليف
aliases:
  - تكليف مسار source/css/main.css
---

# 04 - CSS Stylesheet Path - ../source/css/main.css

> [!question] السؤال
> استدعِ `main.css` من مجلد `source/css` الموجود خارج مجلد `website` الذي يحتوي على `index.html`.
>
> ```text
> Project/
> ├── website/
> │   └── index.html
> └── source/
>     └── css/
>         └── main.css
> ```
>
> ```html
> <link rel="stylesheet" href="{ Write Path Here }" />
> ```
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-1-to-4/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <link rel="stylesheet" href="../source/css/main.css" />
> ```
>
> **سبب المسار**
>
> يبدأ المسار من `website/index.html`. تصعد `..` إلى مجلد `Project`، ثم تدخل `source/css` للوصول إلى `main.css`.
>
> **هيكل المشروع**
>
> ```text
> task-04-sibling-source-demo/
> ├── website/
> │   └── index.html
> └── source/
>     └── css/
>         └── main.css
> ```
>
> **عرض يعمل**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Basics/Demo 04 - sibling source css main/website/index.html|معاينة صفحة HTML]] أو [[vibe_coding/Elzero Frontend/CSS/CSS Basics/Demo 04 - sibling source css main/source/css/main.css|ملف main.css]].

## المصدر

[تكليفات CSS للدروس 01–04](https://elzero.org/css-assignments-lesson-from-1-to-4/)
