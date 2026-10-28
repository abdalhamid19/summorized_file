---
title: "CSS Transform - Rotate Rings on Hover"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 03
---

# CSS Transform - Rotate Rings on Hover

> [!question] السؤال
> استخدم شكل التكليف السابق. عند تمرير المؤشر فوق الشكل، أدر الأقواس بمدة نصف ثانية كما في الفيديو التوضيحي.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/assets/reference-task-03-frame.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .ring::before,
> .ring::after {
>   transition: transform .5s;
> }
>
> .ring:hover::before { transform: rotate(360deg); }
> .ring:hover::after { transform: rotate(-360deg); }
> ```
>
> تضيف `transition` مدة 0.5 ثانية، وتدير القوسين باتجاهين متعاكسين عند `:hover`. الكود يطبق حركة اللف الظاهرة في GIF المرجعي؛ وتظل طبقة النص ثابتة في المنتصف.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/assets/solution-task-03.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/CSS Transform Scale Rotate Translate Assignments 65-67.html|افتح صفحة معاينة الحلول 65–67]]

## المصدر

[تكليفات CSS للدروس 65–67](https://elzero.org/css-assignments-lesson-from-65-to-67/)
