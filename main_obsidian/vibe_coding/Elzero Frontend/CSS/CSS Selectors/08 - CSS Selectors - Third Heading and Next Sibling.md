---
title: "CSS Selectors - Third Heading and Adjacent Div"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 07
---

# CSS Selectors - Third Heading and Adjacent Div

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/reference-task-07.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> body > div:first-of-type > h3:nth-of-type(3) + div { color: #f00; font-weight: 700; }
> ```
>
> يختار `:first-of-type` أول `div` بين أبناء `body`، ثم `:nth-of-type(3)` العنوان الثالث من نوع `h3`، ويصل `+` إلى `div` الملاصق له مباشرة.
>
> تتبع صفحة المعاينة بنية HTML المنشورة في المصدر كما هي.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/solution-task-07.png|500]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Selectors/CSS Selectors Assignments 78-82.html|افتح صفحة معاينة الحلول 78–82]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
