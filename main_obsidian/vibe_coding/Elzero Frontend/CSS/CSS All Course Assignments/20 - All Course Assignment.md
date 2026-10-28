---
title: 20 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 20
---

# 20 — CSS Rounded Badge

> [!question] السؤال الرسمي
> استخدم بنية HTML التالية كما هي دون تعديل، واكتب CSS لعمل الشكل في الصورة.
>
> ```html
> <h1>Elzero</h1>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-20-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```css
> h1 {
>   position: relative;
>   width: 320px;
>   height: 165px;
>   margin: 0;
>   display: grid;
>   place-items: center;
>   border: 5px solid #f44336;
>   border-bottom: 10px solid #111;
>   border-radius: 78px;
>   background: #fff;
>   box-shadow: 0 15px 0 -5px #f44336;
>   color: #111;
>   font: 54px/1 monospace;
> }
>
> h1::before,
> h1::after {
>   content: "";
>   position: absolute;
>   top: 50%;
>   width: 38px;
>   height: 38px;
>   border: 5px solid #f44336;
>   border-radius: 50%;
>   background: #fff;
>   transform: translateY(-50%);
> }
>
> h1::before { left: -55px; }
> h1::after { right: -55px; }
> ```
>
> تعطي `border-radius` الحواف المستديرة، ويضيف `box-shadow` الشريط الأحمر أسفل الشارة. العنصران الزائفان `::before` و`::after` يرسمان الحلقتين الجانبيتين دون إضافة عناصر إلى HTML.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-20.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
