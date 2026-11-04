---
title: "CSS Selectors - Not First or Last Children"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 08
---

# CSS Selectors - Not First or Last Children

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/reference-task-08.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> div:not(:first-child):not(:last-child), p:not(:first-child):not(:last-child) { color: #f00; font-weight: 700; }
> ```
>
> ### الفكرة الأساسية
>
> يستبعد `:not(:first-child)` أول ابن، ويستبعد `:not(:last-child)` آخر ابن. أدرجت نوعي `div` و`p` في السطر نفسه حتى تتلوّن العناصر الثلاثة التي تحمل كلمة `Elzero` في بنية `HTML` الأصلية.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### خصائص CSS
> >
> > #### `div`
> >
> > تحدد قيمة الخاصية `div`. مثال القيمة: `not(:first-child)``:not`(`:last-child`), `p`:`not(:first-child)``:not`(`:last-child`) { `color`: `#f00`; `font-weight`: 700; }
> >
> > ### الدوال والوحدات
> >
> > #### `not()`
> >
> > تستبعد العناصر التي يطابقها المحدد الموجود بين القوسين.
> >
> > #### `not()`
> >
> > تستبعد العناصر التي يطابقها المحدد الموجود بين القوسين.
> >
> > #### `not()`
> >
> > تستبعد العناصر التي يطابقها المحدد الموجود بين القوسين.
> >
> > #### `not()`
> >
> > تستبعد العناصر التي يطابقها المحدد الموجود بين القوسين.
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
> > div:not(:first-child):not(:last-child), p:not(:first-child):not(:last-child) { color: #f00; font-weight: 700; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `color` وfont-`weight`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/solution-page-task-09.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/09 - CSS Selectors - Not Excluded Items.html|افتح صفحة التكليف 09]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
