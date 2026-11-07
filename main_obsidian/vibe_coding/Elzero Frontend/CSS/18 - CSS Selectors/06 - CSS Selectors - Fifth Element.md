---
title: "CSS Selectors - Nested Attribute Target"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 05
---

# CSS Selectors - Nested Attribute Target

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/reference-task-05.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body > div:nth-of-type(2) > div[title="Elzero"] { color: #f00; font-weight: 700; }
> ```
>
> ### الفكرة الأساسية
>
> يختار `:nth-of-type(2)` العنصر الأب الثاني من نوع `div` داخل `body`، ثم يصل إلى ابنه `div` الذي يحمل `title="Elzero"`.
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
> > body > div:nth-of-type(2) > div[title="Elzero"] { color: #f00; font-weight: 700; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `color` وfont-`weight`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/solution-page-task-06.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/06 - CSS Selectors - Fifth Element.html|افتح صفحة التكليف 06]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
