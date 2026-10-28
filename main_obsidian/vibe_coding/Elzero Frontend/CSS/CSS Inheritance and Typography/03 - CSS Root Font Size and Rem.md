---
title: "CSS Root Font Size and Rem"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - typography
  - rem
  - تكليف
aliases:
  - تكليف أحجام الخط بوحدة rem
---

# CSS Root Font Size and Rem

> [!question] السؤال
> اجعل حجم الخط في `Root Element` يساوي `20px`، ثم استخدم `rem` لتحديد أحجام الخط في العناصر الثلاثة: `50px` و`40px` و`30px`.
>
> [صفحة التكليفات للدروس 22–26](https://elzero.org/css-assignments-lesson-from-22-to-26/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> html {
>   font-size: 20px;
> }
>
> .first {
>   font-size: 2.5rem;
> }
>
> .second {
>   font-size: 2rem;
> }
>
> .third {
>   font-size: 1.5rem;
> }
> ```
>
> تعني `rem` حجم الخط الأساسي في العنصر الجذر `html`. عند جعل الجذر `20px`، نحصل على الأحجام المطلوبة بضرب الجذر في المعامل: `2.5 × 20 = 50px`، و`2 × 20 = 40px`، و`1.5 × 20 = 30px`.
>
> **معاينة الأحجام**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Inheritance and Typography/assets/solution-task-03.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Inheritance and Typography/CSS Inheritance Typography Assignments 22-26.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS للدروس 22–26](https://elzero.org/css-assignments-lesson-from-22-to-26/)
