---
title: "All Course Assignment 15 — Outlined Text"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 15"
---

# 15 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل الشكل كما في الصورة.
>
> ```html
> <h2>Elzero Web School</h2>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-15-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> h2 {
>   margin: 0;
>   color: #9c27b0;
>   font: 700 clamp(38px, 7vw, 88px) / 1 Arial, sans-serif;
>   -webkit-text-fill-color: transparent;
>   -webkit-text-stroke: 2px #9c27b0;
> }
> ```
>
> ### الفكرة الأساسية
>
> تجعل `-webkit-text-fill-color: transparent` داخل الحروف شفافًا، وترسم `-webkit-text-stroke` حدًا بنفسجيًا بسماكة بكسلين. تبقى بنية `h2` كما وردت في السؤال.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `h2`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > ### خصائص CSS
> >
> > #### `margin`
> >
> > تضيف مسافة خارجية. مثال القيمة: 0
> >
> > #### `color`
> >
> > تحدد لون النص. مثال القيمة: `#9c27b0`
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: 700 `clamp(38px, 7vw, 88px)` / 1 `Arial`, `sans-serif`
> >
> > #### `-webkit-text-fill-color`
> >
> > تحدد قيمة الخاصية -`webkit-text-fill-color`. مثال القيمة: `transparent`
> >
> > #### `-webkit-text-stroke`
> >
> > تحدد قيمة الخاصية -`webkit-text-stroke`. مثال القيمة: `2px` `#9c27b0`
> >
> > ### الدوال والوحدات
> >
> > #### `clamp()`
> >
> > تحصر القيمة بين حد أدنى وقيمة مفضلة وحد أقصى.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > #### `vw`
> >
> > نسبة من عرض نافذة العرض.
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
> > h2 {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   margin: 0;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   color: #9c27b0;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#9c27b0`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> >   font: 700 clamp(38px, 7vw, 88px) / 1 Arial, sans-serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا 700 `clamp(38px, 7vw, 88px)` / 1 `Arial`, `sans-serif`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   -webkit-text-fill-color: transparent;
> > ```
> >
> > تحدد قيمة الخاصية -`webkit-text-fill-color`. والقيمة هنا `transparent`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   -webkit-text-stroke: 2px #9c27b0;
> > ```
> >
> > تحدد قيمة الخاصية -`webkit-text-stroke`. والقيمة هنا `2px` `#9c27b0`.
> >
> > #### السطر 07 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-15.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/15 - All Course Assignment.html|افتح صفحة التكليف 15]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
