---
title: "CSS Selectors - Attribute Value"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 04
---

# CSS Selectors - Attribute Value

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/reference-task-04.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body > div[title]:not(.no-need) { color: #f00; font-weight: 700; }
> ```
>
> ### الفكرة الأساسية
>
> يختار `[title]` عناصر `div` المباشرة داخل `body` التي تحمل سمة `title`، ثم يستبعد `:not(.no-need)` عنصر الاختبار الإضافي؛ وهكذا تبقى الكلمات الثلاث المطلوبة.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### الدوال والوحدات
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
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `css`
> >
> > ```css
> > body > div[title]:not(.no-need) { color: #f00; font-weight: 700; }
> > ```
> >
> > يختار العناصر بحسب خاصية `HTML` أو قيمتها. ويجمع السطر خصائص `color` وfont-`weight`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/solution-page-task-05.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/05 - CSS Selectors - Attribute Value.html|افتح صفحة التكليف 05]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
