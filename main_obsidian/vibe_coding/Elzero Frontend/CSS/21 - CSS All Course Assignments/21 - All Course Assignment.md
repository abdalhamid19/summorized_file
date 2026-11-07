---
title: 21 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 21
---

# 21 — CSS Shorthand Properties

> [!question] السؤال الرسمي
> اختصر خصائص كل `selector` (محدد CSS) في سطر واحد. المثال الأول يوضح طريقة الاختصار.
>
> لا توجد صورة مرجعية لهذا السؤال في الصفحة الرسمية؛ الكود هو مادة السؤال.
>
> ```css
> .example {
>   margin-top: 10px;
>   margin-right: 20px;
>   margin-bottom: 15px;
>   margin-left: 20px;
>   /* Shorten Code in One Line */
> }
>
> .one {
>   background-color: black;
>   background-image: url("../imgs/one.jpg");
>   background-repeat: no-repeat;
>   background-position: left top;
>   background-size: cover;
>   /* Shorten Code in One Line */
> }
>
> .two {
>   border-top-width: 1px;
>   border-top-style: solid;
>   border-top-color: #000;
>   /* Shorten Code in One Line */
> }
>
> .three {
>   top: 10px;
>   right: 20px;
>   bottom: 10px;
>   left: 20px;
>   /* Shorten Code in One Line */
> }
>
> .four {
>   flex-grow: 3;
>   flex-shrink: 3;
>   flex-basis: 10%;
>   /* Shorten Code in One Line */
> }
>
> .five {
>   flex-direction: column;
>   flex-wrap: wrap;
>   /* Shorten Code in One Line */
> }
> ```

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .example { margin: 10px 20px 15px 20px; }
> .one { background: black url("../imgs/one.jpg") no-repeat left top / cover; }
> .two { border-top: 1px solid #000; }
> .three { inset: 10px 20px; }
> .four { flex: 3 3 10%; }
> .five { flex-flow: column wrap; }
> ```
>
> ### الفكرة الأساسية
>
> ترتيب قيم `margin` هو أعلى، يمين، أسفل، يسار؛ لذلك حافظ السطر الأول على القيم الأربع نفسها.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### الدوال والوحدات
> >
> > #### `url()`
> >
> > تطبق وظيفة `CSS` خاصة داخل قيمة الخاصية.
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
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `css`
> >
> > ```css
> > .example { margin: 10px 20px 15px 20px; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `margin`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> > .one { background: black url("../imgs/one.jpg") no-repeat left top / cover; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `background`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > .two { border-top: 1px solid #000; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `border-top`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > .three { inset: 10px 20px; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `inset`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> > .four { flex: 3 3 10%; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `flex`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> > .five { flex-flow: column wrap; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `flex-flow`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-21.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/21 - All Course Assignment.html|افتح صفحة التكليف 21]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
