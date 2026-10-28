---
title: "CSS Selectors - Fourth Div in Second Root"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 06
---

# CSS Selectors - Fourth Div in Second Root

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/reference-task-06.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> body > div:first-of-type > div:nth-child(3),
> body > div:nth-of-type(2) > div:nth-child(4) { color: #f00; font-weight: 700; }
> ```
>
> يحدد الأول `div` الثالث داخل الأب الأول، ويحدد الثاني `div` الرابع داخل الأب الثاني. هذان الموضعان يحملان كلمة Elzero في HTML المنشور.
>
> تتبع صفحة المعاينة بنية HTML المنشورة في المصدر كما هي.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/solution-task-06.png|500]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Selectors/CSS Selectors Assignments 78-82.html|افتح صفحة معاينة الحلول 78–82]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
