---
title: "CSS Background Repeat"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - background
  - تكليف
aliases:
  - CSS Background Assignment 02
  - تكرار صورة الخلفية
---

# CSS Background Repeat

> [!question] السؤال
> استخدم البنية التالية. اجعل طول وعرض كل `div` هو `400px`، وضع صورة التكليف خلفيةً لها. اجعل خلفية الشكل 1 لا تتكرر، والشكل 2 تتكرر طوليًا فقط، والشكل 3 عرضيًا فقط، والشكل 4 طوليًا وعرضيًا.
>
> ```html
> <div class="assign-2-shape-1">Normal Div</div>
> <div class="assign-2-shape-2">Normal Div</div>
> <div class="assign-2-shape-3">Normal Div</div>
> <div class="assign-2-shape-4">Normal Div</div>
> ```
>
> صورة الخلفية والرسم المرجعي:
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/background-grid.png|200]]
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/reference-task-02.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .assign-2-shape-1,
> .assign-2-shape-2,
> .assign-2-shape-3,
> .assign-2-shape-4 {
>   width: 400px;
>   height: 400px;
>   margin: 20px;
>   color: white;
>   background-image: url("assets/background-grid.png");
> }
>
> .assign-2-shape-1 {
>   background-repeat: no-repeat;
> }
>
> .assign-2-shape-2 {
>   background-repeat: repeat-y;
> }
>
> .assign-2-shape-3 {
>   background-repeat: repeat-x;
> }
>
> .assign-2-shape-4 {
>   background-repeat: repeat;
> }
> ```
>
> تعني `repeat-y` التكرار على المحور الرأسي، وتعني `repeat-x` التكرار على المحور الأفقي. أما `repeat` فيكرر الصورة على المحورين، و`no-repeat` يمنع تكرارها.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/CSS Background Assignments 05-08.html|افتح صفحة التنفيذ]]

## المصدر

[صفحة التكليفات](https://elzero.org/css-assignments-lesson-from-5-to-8/) · [الرسم المرجعي للتكليف 02](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-5-8-2.png) · [صورة الخلفية المطلوبة](https://elzero.org/wp-content/uploads/2021/02/css-assignment-5-8.png)
