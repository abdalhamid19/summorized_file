---
title: "CSS Selectors - Not First or Last Children"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 08
---

# CSS Selectors - Not First or Last Children

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/reference-task-08.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> div:not(:first-child):not(:last-child), p:not(:first-child):not(:last-child) { color: #f00; font-weight: 700; }
> ```
>
> يستبعد `:not(:first-child)` أول ابن، ويستبعد `:not(:last-child)` آخر ابن. أدرجت نوعي `div` و`p` في السطر نفسه حتى تتلوّن العناصر الثلاثة التي تحمل كلمة Elzero في بنية HTML الأصلية.
>
> تتبع صفحة المعاينة بنية HTML المنشورة في المصدر كما هي.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Selectors/assets/solution-task-08.png|500]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Selectors/CSS Selectors Assignments 78-82.html|افتح صفحة معاينة الحلول 78–82]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
