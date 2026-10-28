---
title: "All Course Assignment 09 — Gradient Text"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 09"
---

# 09 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل الشكل كما في الصورة. يمكنك اختيار لونين مختلفين.
>
> ```html
> <div class="text">elzero web school</div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-09-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> **CSS**
>
> ```css
> body {
>   margin: 0;
>   background-color: #eee;
> }
>
> .text {
>   color: transparent;
>   font: 700 clamp(24px, 4.1vw, 68px) / 1 Arial, sans-serif;
>   white-space: nowrap;
>   text-align: center;
>   text-transform: capitalize;
>   background-image: linear-gradient(to bottom, #f0440a, #bd8c0e);
>   -webkit-background-clip: text;
>   background-clip: text;
> }
> ```
> **شرح الحل**
> تجعل الخاصية `text-transform: capitalize` بداية كل كلمة حرفًا كبيرًا. تنشئ `linear-gradient` تدرجًا بين اللونين. تجعل `background-clip: text` التدرج ظاهرًا داخل شكل الحروف، لذلك نجعل لون النص شفافًا.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-09-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
