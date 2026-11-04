---
title: "CSS Transform - Rotate Rings on Hover"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 03
---

# CSS Transform - Rotate Rings on Hover

> [!question] السؤال
> استخدم شكل التكليف السابق. عند تمرير المؤشر فوق الشكل، أدر الأقواس بمدة نصف ثانية كما في الفيديو التوضيحي.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/15 - CSS Transform Scale Rotate Translate/assets/reference-task-03-frame.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .ring::before,
> .ring::after {
>   transition: transform .5s;
> }
>
> .ring:hover::before { transform: rotate(360deg); }
> .ring:hover::after { transform: rotate(-360deg); }
> ```
>
> ### الفكرة الأساسية
>
> تضيف `transition` مدة 0.5 ثانية، وتدير القوسين باتجاهين متعاكسين عند `:hover`. الكود يطبق حركة اللف الظاهرة في `GIF` المرجعي؛ وتظل طبقة النص ثابتة في المنتصف.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.ring::after`
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > ### خصائص CSS
> >
> > #### `transition`
> >
> > تجعل تغير الخاصية تدريجيًا. مثال القيمة: `transform` .`5s`
> >
> > ### الدوال والوحدات
> >
> > #### `rotate()`
> >
> > تدير العنصر بالزاوية المحددة.
> >
> > #### `rotate()`
> >
> > تدير العنصر بالزاوية المحددة.
> >
> > #### `s`
> >
> > ثانية.
> >
> > #### `deg`
> >
> > درجة زاوية.
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
> > .ring::before,
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> > .ring::after {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   transition: transform .5s;
> > ```
> >
> > تجعل تغير الخاصية تدريجيًا. والقيمة هنا `transform` .`5s`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> > .ring:hover::before { transform: rotate(360deg); }
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`. ويجمع السطر خصائص `transform`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> > .ring:hover::after { transform: rotate(-360deg); }
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`. ويجمع السطر خصائص `transform`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/15 - CSS Transform Scale Rotate Translate/assets/solution-page-task-03.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/15 - CSS Transform Scale Rotate Translate/03 - CSS Transform - Rotate Rings on Hover.html|افتح صفحة التكليف 03]]

## المصدر

[تكليفات CSS للدروس 65–67](https://elzero.org/css-assignments-lesson-from-65-to-67/)
