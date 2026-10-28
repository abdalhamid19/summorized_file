---
title: "CSS Selectors - Direct Child"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 02
---

# CSS Selectors - Direct Child

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/reference-task-02.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .parent > .child:nth-of-type(2) { color: #f00; font-weight: 700; }
> ```
>
> يشترط `>` أن يكون `child` ابنًا مباشرًا لـ `parent`، ثم يختار `:nth-of-type(2)` ثاني عنصر من نوع `div` بين الأبناء المباشرين.
>
> تتبع صفحة المعاينة بنية HTML المنشورة في المصدر كما هي.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/solution-task-02.png|500]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Selectors/CSS Selectors Assignments 78-82.html|افتح صفحة معاينة الحلول 78–82]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
