---
title: "CSS Transform - Flip Card on Both Axes"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 05
---

# CSS Transform - Flip Card on Both Axes

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها، واجعل البطاقة 200×200px ومتمركزة رأسيًا وأفقيًا. أنشئ انقلابًا حول المحور الأفقي وآخر حول المحور الرأسي.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/reference-task-05-frame.png|650]]
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/reference-task-05-2-frame.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .flip-card {
>   width: 200px;
>   height: 200px;
>   perspective: 700px;
> }
>
> .flip-card__inner {
>   position: relative;
>   width: 100%;
>   height: 100%;
>   transform-style: preserve-3d;
>   transition: transform .8s;
> }
>
> .flip-card:hover .flip-card__inner { transform: rotateY(180deg); }
> .flip-card--vertical:hover .flip-card__inner { transform: rotateX(180deg); }
>
> .flip-card__face {
>   position: absolute;
>   inset: 0;
>   display: grid;
>   place-items: center;
>   color: white;
>   background: #e91e63;
>   backface-visibility: hidden;
> }
>
> .flip-card__back { transform: rotateY(180deg); background: #009688; }
> .flip-card--vertical .flip-card__back { transform: rotateX(180deg); }
> ```
>
> تحدد `perspective` عمق المشهد، وتحافظ `preserve-3d` على وجهي البطاقة في فضاء ثلاثي الأبعاد. الحل الأول يدور حول محور Y، والثاني حول X، فينتجان الانقلاب الأفقي والرأسي.
>
> **معاينة الحل**
>
> **الانقلاب حول المحور الرأسي**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/solution-task-05.png|900]]
>
> **الانقلاب حول المحور الأفقي**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/solution-task-05-vertical.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/CSS Transform Skew Matrix 3D Assignments 68-73.html|افتح صفحة معاينة الحلول 68–73]]

## المصدر

[تكليفات CSS للدروس 68–73](https://elzero.org/css-assignments-lesson-from-68-to-73/)
