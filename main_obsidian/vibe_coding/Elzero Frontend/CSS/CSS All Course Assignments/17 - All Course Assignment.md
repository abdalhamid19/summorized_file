---
title: 17 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 17
---

# 17 — CSS Multi-column Text

> [!question] السؤال الرسمي
> استخدم بنية HTML التالية كما هي دون تعديل، واكتب CSS لعمل الشكل في الصورة.
>
> ```html
> <div>
>   Hello, Iam Osama Elzero From Elzero Web School. Iam In Love With Programming Specially C++, Python, JS, And Many
>   More Languages Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis, maxime recusandae! Eveniet, quas
>   eius amet nostrum enim sint quis, ab perferendis voluptatibus culpa doloremque nulla harum aliquid illum?
>   Perspiciatis, veniam.
> </div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-17-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```css
> div {
>   columns: 3;
>   column-gap: 30px;
>   column-rule: 2px dashed #222;
>   padding: 15px 20px;
>   background: #fff;
>   font: 18px/1.9 Arial, sans-serif;
> }
> ```
>
> خاصية `columns` (تقسيم النص إلى أعمدة) تجعل النص ينساب في ثلاثة أعمدة متوازنة.
>
> خاصية `column-gap` (المسافة بين الأعمدة) تترك فراغًا مقداره 26px، و`column-rule` ترسم الخط المتقطع الفاصل.
>
> الخاصية المختصرة `font` تضبط حجم الخط وارتفاع السطر ونوع الخط في سطر واحد.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-17.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
