---
title: "CSS Selectors - Direct Child"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 02
---

# CSS Selectors - Direct Child

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/reference-task-02.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .parent > .child:nth-of-type(2) { color: #f00; font-weight: 700; }
> ```
>
> ### الفكرة الأساسية
>
> يشترط `>` أن يكون `child` ابنًا مباشرًا لـ `parent`، ثم يختار `:nth-of-type(2)` ثاني عنصر من نوع `div` بين الأبناء المباشرين.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### الدوال والوحدات
> >
> > #### `nth-of-type()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته من نوع `HTML` نفسه.
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
> > .parent > .child:nth-of-type(2) { color: #f00; font-weight: 700; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `color` وfont-`weight`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/solution-page-task-03.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/03 - CSS Selectors - Direct Child.html|افتح صفحة التكليف 03]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
