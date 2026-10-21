---
title: "CSS Background Colors and Alpha"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - background
  - تكليف
aliases:
  - CSS Background Assignment 01
  - ألوان الخلفية وقناة ألفا
---

# CSS Background Colors and Alpha

> [!question] السؤال
> استخدم البنية التالية لعمل المطلوب:
>
> ```html
> <div class="assign-1-shape-1">Normal Div</div>
> <div class="assign-1-shape-2">Normal Div</div>
> <div class="assign-1-shape-3">Normal Div</div>
> ```
>
> اجعل عرض كل `div` هو `500px`، ووسّطه أفقيًا، وأضف `padding` بقيمة `20px` وخلفية `blueviolet`. اكتب قيمة اللون بصيغ `RGB` و`HSL` و`Hex`. أنشئ العنصرين التاليين بالخلفية نفسها، لكن اجعل الشفافية `0.5` للثاني و`0.1` للثالث.
>
> الرسم المرجعي:
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/reference-task-01.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .assign-1-shape-1,
> .assign-1-shape-2,
> .assign-1-shape-3 {
>   width: 500px;
>   padding: 20px;
>   margin: 20px auto;
> }
>
> .assign-1-shape-1 {
>   background-color: blueviolet;
>   background-color: rgb(138, 43, 226);
>   background-color: hsl(271.17, 75.93%, 52.75%);
>   background-color: #8a2be2;
> }
>
> .assign-1-shape-2 {
>   background-color: rgba(138, 43, 226, 0.5);
> }
>
> .assign-1-shape-3 {
>   background-color: rgba(138, 43, 226, 0.1);
> }
> ```
>
> تضبط `margin: 20px auto` الهامشين الجانبيين على `auto`، فيتوسط العنصر أفقيًا. قيم اللون الأربع في العنصر الأول متكافئة؛ يطبق المتصفح آخر تصريح صالح، ويمكن استبدال الصيغ الثلاث الأخيرة ببعضها عند اختيار صيغة واحدة. تستخدم `rgba` قناة ألفا لتحديد شفافية الخلفية من دون جعل النص شفافًا.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Background, Margin, and Padding/CSS Background Assignments 05-08.html|افتح صفحة التنفيذ]]

## المصدر

[صفحة تكليفات CSS للدروس 05–08](https://elzero.org/css-assignments-lesson-from-5-to-8/) · [الرسم المرجعي](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-5-8-1.png)
