---
title: "CSS Background Repeat and Position"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - background
  - تكليف
aliases:
  - CSS Background Assignment 03
  - تكرار الخلفية وتحديد موضعها
---

# CSS Background Repeat and Position

> [!question] السؤال
> استخدم البنية التالية. اجعل طول وعرض كل `div` هو `400px`، وضع صورة التكليف خلفيةً لها. اجعل خلفية الشكل 1 لا تتكرر، والشكل 2 تتكرر طوليًا فقط ويكون موضعها ناحية اليمين، والشكل 3 تتكرر عرضيًا فقط ويكون موضعها ناحية الأسفل، والشكل 4 تتكرر طوليًا وعرضيًا.
>
> ```html
> <div class="assign-3-shape-1">Normal Div</div>
> <div class="assign-3-shape-2">Normal Div</div>
> <div class="assign-3-shape-3">Normal Div</div>
> <div class="assign-3-shape-4">Normal Div</div>
> ```
>
> صورة الخلفية والرسم المرجعي:
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/background-grid.png|200]]
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/reference-task-03.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .assign-3-shape-1,
> .assign-3-shape-2,
> .assign-3-shape-3,
> .assign-3-shape-4 {
>   width: 400px;
>   height: 400px;
>   margin: 20px;
>   color: white;
>   background-image: url("assets/background-grid.png");
> }
>
> .assign-3-shape-1 {
>   background-repeat: no-repeat;
> }
>
> .assign-3-shape-2 {
>   background-repeat: repeat-y;
>   background-position: right top;
> }
>
> .assign-3-shape-3 {
>   background-repeat: repeat-x;
>   background-position: left bottom;
> }
>
> .assign-3-shape-4 {
>   background-repeat: repeat;
> }
> ```
>
> يجمع `background-position` بين اتجاهي الموضع. لذلك تبدأ صورة الشكل 2 من اليمين، وتُحاذى صورة الشكل 3 إلى الأسفل، بينما يبقى تكرار الشكلين 1 و4 عند الموضع الافتراضي أعلى اليسار.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/solution-task-03.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/CSS Background Assignments 05-08.html|افتح صفحة التنفيذ]]

## المصدر

[صفحة التكليفات](https://elzero.org/css-assignments-lesson-from-5-to-8/) · [الرسم المرجعي للتكليف 03](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-5-8-3.png) · [صورة الخلفية المطلوبة](https://elzero.org/wp-content/uploads/2021/02/css-assignment-5-8.png)
