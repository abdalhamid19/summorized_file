---
title: "CSS Transform - Two Colored Ring Arcs"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 02
---

# CSS Transform - Two Colored Ring Arcs

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها، واجعل الشكل دائريًا بحلقتين ملونتين متقطعتين حول كلمة Elzero، مع مطابقة الألوان.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/assets/reference-task-02.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .ring {
>   position: relative;
>   width: 200px;
>   height: 200px;
>   margin-inline: auto;
>   display: grid;
>   place-items: center;
>   border-radius: 50%;
>   background: #eee;
> }
>
> .ring::before,
> .ring::after {
>   content: "";
>   position: absolute;
>   border-radius: 50%;
>   mask: radial-gradient(farthest-side, transparent calc(100% - 7px), #000 calc(100% - 6px));
> }
>
> .ring::before {
>   inset: -5px;
>   background: conic-gradient(from 10deg, #2196f3 0 300deg, transparent 300deg 360deg);
> }
>
> .ring::after {
>   inset: 3px;
>   background: conic-gradient(from 110deg, #e91e63 0 300deg, transparent 300deg 360deg);
> }
> ```
>
> تُنشئ `conic-gradient` أقواس اللون والفجوة، وتحوّل `mask` الطبقة إلى حلقة مجوفة. قد تختلف نقطة بداية الفجوات بدرجات قليلة عن الرسم، لكن الألوان والقطاعات الدائرية مطابقة للمشهد.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/CSS Transform Scale Rotate Translate Assignments 65-67.html|افتح صفحة معاينة الحلول 65–67]]

## المصدر

[تكليفات CSS للدروس 65–67](https://elzero.org/css-assignments-lesson-from-65-to-67/)
