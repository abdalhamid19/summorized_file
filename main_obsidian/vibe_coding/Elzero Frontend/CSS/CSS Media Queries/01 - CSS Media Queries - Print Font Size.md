---
title: "CSS Media Queries - Print Font Size"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - media_queries
  - تكليف
aliases:
  - تكليف CSS Media Queries 01
---

# CSS Media Queries - Print Font Size

> [!question] السؤال
> اجعل حجم الخط `40px` عند الطباعة فقط.
>
> صورة السؤال:
>
> التكليف لا يرفق صورة مرجعية؛ المطلوب محدد نصيًا.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> @media print {
>   h1 {
>     font-size: 40px;
>   }
> }
> ```
>
> يطبّق `@media print` القاعدة عند تجهيز الصفحة للطباعة فقط؛ في العرض العادي يظل عنوان الصفحة على حجمه الأصلي.
>
> **معاينة عند محاكاة الطباعة**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-01-print.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/CSS Media Queries Assignments 83-85.html|افتح صفحة معاينة الحلول 83–85]]

## المصدر

[تكليفات CSS للدروس 83–85](https://elzero.org/css-assignments-lesson-from-83-to-85/)
