---
title: "All Course Assignment 10 — Checkerboard"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 10"
---

# 10 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل رقعة الشطرنج كما في الصورة.
>
> ```html
> <div class="container">
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
> </div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-10-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> * {
>   box-sizing: border-box;
> }
>
> .container {
>   display: grid;
>   grid-template-columns: repeat(8, 1fr);
>   width: min(100%, 810px);
>   aspect-ratio: 1;
>   border: 5px solid #000;
> }
>
> .white {
>   background-color: #fff;
> }
>
> .black {
>   background-color: #000;
> }
> ```
>
> ### الفكرة الأساسية
>
> ينشئ `display: grid` شبكة من ثمانية أعمدة متساوية. يحدد `aspect-ratio: 1` شكلًا مربعًا، وترتيب عناصر `HTML` الثمانية والستين يوزع الأبيض والأسود على الصفوف بالتناوب.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `*`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `.container`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.white`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.black`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > ### خصائص CSS
> >
> > #### `box-sizing`
> >
> > تحدد حساب أبعاد الصندوق. مثال القيمة: `border-box`
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `grid-template-columns`
> >
> > تحدد أعمدة `Grid`. مثال القيمة: `repeat(8, 1fr)`
> >
> > #### `width`
> >
> > تحدد عرض العنصر. مثال القيمة: `min(100%, 810px)`
> >
> > #### `aspect-ratio`
> >
> > تحدد نسبة العرض للارتفاع. مثال القيمة: 1
> >
> > #### `border`
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. مثال القيمة: `5px` `solid` `#000`
> >
> > #### `background-color`
> >
> > تحدد لون الخلفية. مثال القيمة: `#fff`
> >
> > ### الدوال والوحدات
> >
> > #### `repeat()`
> >
> > تكرر مسارًا أو مجموعة مسارات بعدد محدد في تخطيط `Grid`.
> >
> > #### `min()`
> >
> > تختار أصغر قيمة من القيم المعطاة.
> >
> > #### `fr`
> >
> > جزء من مساحة `Grid`.
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
> > * {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   box-sizing: border-box;
> > ```
> >
> > تحدد حساب أبعاد الصندوق. والقيمة هنا `border-box`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > .container {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   grid-template-columns: repeat(8, 1fr);
> > ```
> >
> > تحدد أعمدة `Grid`. والقيمة هنا `repeat(8, 1fr)`.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> >   width: min(100%, 810px);
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `min(100%, 810px)`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> >   aspect-ratio: 1;
> > ```
> >
> > تحدد نسبة العرض للارتفاع. والقيمة هنا 1.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   border: 5px solid #000;
> > ```
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. والقيمة هنا `5px` `solid` `#000`.
> >
> > #### السطر 10 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 11 — `css`
> >
> > ```css
> > .white {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> >   background-color: #fff;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#fff`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 14 — `css`
> >
> > ```css
> > .black {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> >   background-color: #000;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#000`.
> >
> > #### السطر 16 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-10.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/10 - All Course Assignment.html|افتح صفحة التكليف 10]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
