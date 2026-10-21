---
title: "CSS Background Size and Position"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - background
  - تكليف
aliases:
  - CSS Background Assignment 04
  - حجم الخلفية وموضعها
---

# CSS Background Size and Position

> [!question] السؤال
> استخدم البنية التالية. اجعل طول وعرض كل `div` هو `400px`، وضع صورة التكليف خلفيةً لها. اجعل خلفية الشكل 1 تملأ `80%` من طول العنصر وعرضه. اجعل الشكلين 2 و3 كما في الصورة، واجعل خلفية الشكل 4 تملأ `50%` من طول العنصر وعرضه مع تغيير موضعها.
>
> ```html
> <div class="assign-4-shape-1">Normal Div</div>
> <div class="assign-4-shape-2">Normal Div</div>
> <div class="assign-4-shape-3">Normal Div</div>
> <div class="assign-4-shape-4">Normal Div</div>
> ```
>
> صورة الخلفية والرسم المرجعي:
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/background-grid.png|200]]
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/reference-task-04.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .assign-4-shape-1,
> .assign-4-shape-2,
> .assign-4-shape-3,
> .assign-4-shape-4 {
>   width: 400px;
>   height: 400px;
>   margin: 20px;
>   color: white;
>   background-image: url("assets/background-grid.png");
>   background-repeat: no-repeat;
> }
>
> .assign-4-shape-1 {
>   background-size: 80% 80%;
> }
>
> .assign-4-shape-2 {
>   background-size: 80% 100%;
>   background-position: right top;
> }
>
> .assign-4-shape-3 {
>   background-size: 100% 80%;
>   background-position: left bottom;
> }
>
> .assign-4-shape-4 {
>   background-size: 50% 50%;
>   background-position: right bottom;
> }
> ```
>
> يحدد `background-size` العرض والارتفاع النسبيين للصورة، ويمنع `no-repeat` ظهور نسخ إضافية منها في المساحة المتبقية. في الشكلين 2 و3 يُستنتج من الرسم أن الصورة تملأ أحد البعدين بالكامل و`80%` من البعد الآخر. وفي الشكل 4 تظهر الصورة بحجم نصف العنصر ومحاذاة إلى الركن السفلي الأيمن.
>
> يذكر تعليق أسفل صفحة التكليف `background-position: 50%` كسطر ناقص. هذه القيمة توسيط الصورة؛ أما الرسم فيعرضها عند الركن السفلي الأيمن، لذا استُخدم `right bottom` لمطابقة الشكل.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/solution-task-04.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/CSS Background Assignments 05-08.html|افتح صفحة التنفيذ]]

## المصدر

[صفحة التكليفات](https://elzero.org/css-assignments-lesson-from-5-to-8/) · [الرسم المرجعي للتكليف 04](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-5-8-4.png) · [صورة الخلفية المطلوبة](https://elzero.org/wp-content/uploads/2021/02/css-assignment-5-8.png)
