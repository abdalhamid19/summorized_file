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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-17-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
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
> ### الفكرة الأساسية
>
> خاصية `columns` (تقسيم النص إلى أعمدة) تجعل النص ينساب في ثلاثة أعمدة متوازنة.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `div`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > ### خصائص CSS
> >
> > #### `columns`
> >
> > تحدد قيمة الخاصية `columns`. مثال القيمة: 3
> >
> > #### `column-gap`
> >
> > تحدد قيمة الخاصية `column-gap`. مثال القيمة: `30px`
> >
> > #### `column-rule`
> >
> > تحدد قيمة الخاصية `column-rule`. مثال القيمة: `2px` `dashed` `#222`
> >
> > #### `padding`
> >
> > تضيف مساحة داخلية. مثال القيمة: `15px` `20px`
> >
> > #### `background`
> >
> > تضبط الخلفية. مثال القيمة: `#fff`
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: `18px`/1.9 `Arial`, `sans-serif`
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
> > div {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   columns: 3;
> > ```
> >
> > تحدد قيمة الخاصية `columns`. والقيمة هنا 3.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   column-gap: 30px;
> > ```
> >
> > تحدد قيمة الخاصية `column-gap`. والقيمة هنا `30px`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> >   column-rule: 2px dashed #222;
> > ```
> >
> > تحدد قيمة الخاصية `column-rule`. والقيمة هنا `2px` `dashed` `#222`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   padding: 15px 20px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `15px` `20px`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   background: #fff;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#fff`.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> >   font: 18px/1.9 Arial, sans-serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا `18px`/1.9 `Arial`, `sans-serif`.
> >
> > #### السطر 08 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-17.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/17 - All Course Assignment.html|افتح صفحة التكليف 17]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
