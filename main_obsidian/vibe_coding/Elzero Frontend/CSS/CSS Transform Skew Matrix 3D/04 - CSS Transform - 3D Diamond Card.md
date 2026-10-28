---
title: "CSS Transform - 3D Diamond Card"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 04
---

# CSS Transform - 3D Diamond Card

> [!question] السؤال
> اجعل العنصر 200×200px، ووسّطه رأسيًا وأفقيًا، ثم كوّن الشكل والألوان في الصورة المرجعية.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/reference-task-04.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .card {
>   position: relative;
>   width: 200px;
>   height: 200px;
>   margin: auto;
>   display: flex;
>   align-items: flex-end;
>   padding: 8px;
>   color: white;
>   background: #607d8b;
>   perspective: 600px;
> }
>
> .card::before {
>   content: "";
>   position: absolute;
>   width: 200px;
>   height: 200px;
>   left: 0;
>   top: -100px;
>   z-index: 1;
>   background: #000;
>   border: 2px solid white;
>   transform: rotate(45deg);
> }
> ```
>
> يحوّل `rotate(45deg)` المربع الأسود إلى شكل ماسي. يتموضع فوق البطاقة الزرقاء الرمادية مع حد أبيض، ويظل النص أسفل البطاقة. استخدم حاوية `display: grid; place-items: center; min-height: 100vh` لتوسيط العنصرين في الشاشة.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/solution-task-04.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/CSS Transform Skew Matrix 3D Assignments 68-73.html|افتح صفحة معاينة الحلول 68–73]]

## المصدر

[تكليفات CSS للدروس 68–73](https://elzero.org/css-assignments-lesson-from-68-to-73/)
