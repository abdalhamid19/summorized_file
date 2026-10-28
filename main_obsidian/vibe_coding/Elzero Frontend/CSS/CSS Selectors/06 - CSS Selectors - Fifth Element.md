---
title: "CSS Selectors - Nested Attribute Target"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 05
---

# CSS Selectors - Nested Attribute Target

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/reference-task-05.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> body > div:nth-of-type(2) > div[title="Elzero"] { color: #f00; font-weight: 700; }
> ```
>
> يختار `:nth-of-type(2)` العنصر الأب الثاني من نوع `div` داخل `body`، ثم يصل إلى ابنه `div` الذي يحمل `title="Elzero"`.
>
> تتبع صفحة المعاينة بنية HTML المنشورة في المصدر كما هي.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/solution-task-05.png|500]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Selectors/CSS Selectors Assignments 78-82.html|افتح صفحة معاينة الحلول 78–82]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
