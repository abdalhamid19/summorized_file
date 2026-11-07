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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-03-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .font {
>   font: italic bold 30px/30px Arial, sans-serif;
> }
> ```
>
> ### الفكرة الأساسية
>
> اختصار `font` يجمع `font-style` (ميل الخط)، ثم `font-weight` (سماكة الخط)، ثم `font-size` (حجم الخط) و`line-height` (ارتفاع السطر) بعد الشرطة المائلة، ثم `font-family` (عائلة الخط).
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.font`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > ### خصائص CSS
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: `italic` `bold` `30px`/`30px` `Arial`, `sans-serif`
> >
> > ### الدوال والوحدات
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > ### بنية القاعدة
> >
> > #### `{`
> >
> > يفتح مجموعة التصريحات.
> >
> > #### `}`
> >
> > يغلق مجموعة التصريحات.
> >
> > #### `:`
> >
> > يفصل الخاصية عن القيمة.
> >
> > #### `;`
> >
> > ينهي تصريح `CSS`.
> >
> > #### `,`
> >
> > يفصل بين محددات أو قيم.
> >
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `css`
> >
> > ```css
> > .font {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   font: italic bold 30px/30px Arial, sans-serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا `italic` `bold` `30px`/`30px` `Arial`, `sans-serif`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-03.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/03 - All Course Assignment.html|افتح صفحة التكليف 03]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
