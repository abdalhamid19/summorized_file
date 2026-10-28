---
title: "CSS All Course Assignment 03"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 03
---

# CSS All Course Assignment 03

> [!question] المطلوب
> اختصر خصائص الخط الآتية في تصريح CSS واحد.
>
> ```css
> .font {
>   font-style: italic;
>   font-weight: bold;
>   font-size: 30px;
>   line-height: 30px;
>   font-family: Arial, sans-serif;
> }
> ```
>
> الصورة في المصدر تعرض شكل كلمة `Elzero` المتوقع.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-03-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> .font {
>   font: italic bold 30px/30px Arial, sans-serif;
> }
> ```
>
> اختصار `font` يجمع `font-style` (ميل الخط)، ثم `font-weight` (سماكة الخط)، ثم `font-size` (حجم الخط) و`line-height` (ارتفاع السطر) بعد الشرطة المائلة، ثم `font-family` (عائلة الخط).
>
> أضافت صفحة المعاينة عنصرًا بسيطًا يحمل كلمة `Elzero` لأن نص المصدر يعرض خصائص CSS والصورة فقط، ولا يقدّم HTML. هذا افتراض للمعاينة، ولا يغيّر إجابة الاختصار.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-03-solution.png]]

المعاينة: [03 - All Course Assignment.html](03%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
