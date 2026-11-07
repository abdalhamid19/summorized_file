---
title: "CSS Selectors - Combined Classes"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف CSS Selectors 78-82 01
---

# CSS Selectors - Combined Classes

> [!question] السؤال
> اختر المحدد أو المحددات في سطر واحد لتلوين كلمة Elzero بالأحمر مع إبقاء HTML كما هو.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/reference-task-01.png|500]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> div.main.red { color: #f00; font-weight: 700; }
> ```
>
> ### الفكرة الأساسية
>
> يجمع `div` بين اسم الوسم والصنفين؛ لذلك يطابق العنصرين اللذين يحملان `main` و`red` معًا، ولا يطابق فقرة تحمل الصنفين.
>
> > [!info]- معاني الرموز المستخدمة في الحل
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
> > div.main.red { color: #f00; font-weight: 700; }
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`. ويجمع السطر خصائص `color` وfont-`weight`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/assets/solution-page-task-02.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/18 - CSS Selectors/02 - CSS Selectors - Combined Classes.html|افتح صفحة التكليف 02]]

## المصدر

[تكليفات CSS للدروس 78–82](https://elzero.org/css-assignments-lesson-from-78-to-82/)
