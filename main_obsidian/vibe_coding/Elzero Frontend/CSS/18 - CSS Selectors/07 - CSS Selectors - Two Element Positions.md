---
title: "CSS Selectors - Fourth Div in Second Root"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 06
---

# CSS Selectors - Fourth Div in Second Root

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/reference-task-06.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body > div:first-of-type > div:nth-child(3),
> body > div:nth-of-type(2) > div:nth-child(4) { color: #f00; font-weight: 700; }
> ```
>
> ### الفكرة الأساسية
>
> يحدد الأول `div` الثالث داخل الأب الأول، ويحدد الثاني `div` الرابع داخل الأب الثاني. هذان الموضعان يحملان كلمة `Elzero` في `HTML` المنشور.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### الدوال والوحدات
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-of-type()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته من نوع `HTML` نفسه.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
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
> > body > div:first-of-type > div:nth-child(3),
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> > body > div:nth-of-type(2) > div:nth-child(4) { color: #f00; font-weight: 700; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `color` وfont-`weight`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/solution-page-task-07.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/07 - CSS Selectors - Two Element Positions.html|افتح صفحة التكليف 07]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
