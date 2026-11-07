---
title: "CSS Transform - Two Colored Ring Arcs"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 02
---

# CSS Transform - Two Colored Ring Arcs

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها، واجعل الشكل دائريًا بحلقتين ملونتين متقطعتين حول كلمة Elzero، مع مطابقة الألوان.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/15 - CSS Transform Scale Rotate Translate/assets/reference-task-02.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .ring {
>   position: relative;
>   width: 200px;
>   height: 200px;
>   margin-inline: auto;
>   display: grid;
>   place-items: center;
>   border-radius: 50%;
>   background: #eee;
> }
>
> .ring::before,
> .ring::after {
>   content: "";
>   position: absolute;
>   border-radius: 50%;
>   mask: radial-gradient(farthest-side, transparent calc(100% - 7px), #000 calc(100% - 6px));
> }
>
> .ring::before {
>   inset: -5px;
>   background: conic-gradient(from 10deg, #2196f3 0 300deg, transparent 300deg 360deg);
> }
>
> .ring::after {
>   inset: 3px;
>   background: conic-gradient(from 110deg, #e91e63 0 300deg, transparent 300deg 360deg);
> }
> ```
>
> ### الفكرة الأساسية
>
> تُنشئ `conic-gradient` أقواس اللون والفجوة، وتحوّل `mask` الطبقة إلى حلقة مجوفة. قد تختلف نقطة بداية الفجوات بدرجات قليلة عن الرسم، لكن الألوان والقطاعات الدائرية مطابقة للمشهد.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.ring`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.ring::after`
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### `.ring::before`
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > ### خصائص CSS
> >
> > #### `position`
> >
> > تحدد طريقة التموضع. مثال القيمة: `relative`
> >
> > #### `width`
> >
> > تحدد عرض العنصر. مثال القيمة: `200px`
> >
> > #### `height`
> >
> > تحدد ارتفاع العنصر. مثال القيمة: `200px`
> >
> > #### `margin-inline`
> >
> > تضيف مسافة على جانبي العنصر. مثال القيمة: `auto`
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `place-items`
> >
> > تختصر محاذاة `Grid`. مثال القيمة: `center`
> >
> > #### `border-radius`
> >
> > تدوّر زوايا العنصر. مثال القيمة: `50%`
> >
> > #### `background`
> >
> > تضبط الخلفية. مثال القيمة: `#eee`
> >
> > #### `content`
> >
> > تحدد محتوى العنصر الزائف. مثال القيمة: ""
> >
> > #### `mask`
> >
> > تحدد قيمة الخاصية `mask`. مثال القيمة: `radial-gradient(farthest-side, transparent calc(100% - 7px)`, `#000` `calc(100% - 6px)`)
> >
> > #### `inset`
> >
> > تحدد المسافات من الحواف. مثال القيمة: -`5px`
> >
> > ### الدوال والوحدات
> >
> > #### `radial-gradient()`
> >
> > تنشئ تدرجًا لونيًا ينتشر من نقطة مركزية.
> >
> > #### `calc()`
> >
> > تحسب قيمة من تعبير رياضي، ويمكنها الجمع بين وحدات `CSS` المختلفة.
> >
> > #### `calc()`
> >
> > تحسب قيمة من تعبير رياضي، ويمكنها الجمع بين وحدات `CSS` المختلفة.
> >
> > #### `conic-gradient()`
> >
> > تنشئ تدرجًا لونيًا يلتف حول نقطة مركزية.
> >
> > #### `conic-gradient()`
> >
> > تنشئ تدرجًا لونيًا يلتف حول نقطة مركزية.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
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
> > .ring {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   position: relative;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `relative`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   width: 200px;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `200px`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> >   height: 200px;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `200px`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   margin-inline: auto;
> > ```
> >
> > تضيف مسافة على جانبي العنصر. والقيمة هنا `auto`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> >   place-items: center;
> > ```
> >
> > تختصر محاذاة `Grid`. والقيمة هنا `center`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> >   border-radius: 50%;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `50%`.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   background: #eee;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#eee`.
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
> > .ring::before,
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> > .ring::after {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> >   content: "";
> > ```
> >
> > تحدد محتوى العنصر الزائف. والقيمة هنا "".
> >
> > #### السطر 14 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> >   border-radius: 50%;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `50%`.
> >
> > #### السطر 16 — `css`
> >
> > ```css
> >   mask: radial-gradient(farthest-side, transparent calc(100% - 7px), #000 calc(100% - 6px));
> > ```
> >
> > تحدد قيمة الخاصية `mask`. والقيمة هنا `radial-gradient(farthest-side, transparent calc(100% - 7px)`, `#000` `calc(100% - 6px)`).
> >
> > #### السطر 17 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> > .ring::before {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> >   inset: -5px;
> > ```
> >
> > تحدد المسافات من الحواف. والقيمة هنا -`5px`.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> >   background: conic-gradient(from 10deg, #2196f3 0 300deg, transparent 300deg 360deg);
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `conic-gradient(from 10deg, #2196f3 0 300deg, transparent 300deg 360deg)`.
> >
> > #### السطر 21 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 22 — `css`
> >
> > ```css
> > .ring::after {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 23 — `css`
> >
> > ```css
> >   inset: 3px;
> > ```
> >
> > تحدد المسافات من الحواف. والقيمة هنا `3px`.
> >
> > #### السطر 24 — `css`
> >
> > ```css
> >   background: conic-gradient(from 110deg, #e91e63 0 300deg, transparent 300deg 360deg);
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `conic-gradient(from 110deg, #e91e63 0 300deg, transparent 300deg 360deg)`.
> >
> > #### السطر 25 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/15 - CSS Transform Scale Rotate Translate/assets/solution-page-task-02.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/15 - CSS Transform Scale Rotate Translate/02 - CSS Transform - Two Colored Ring Arcs.html|افتح صفحة التكليف 02]]

## المصدر

[تكليفات CSS للدروس 65–67](https://elzero.org/css-assignments-lesson-from-65-to-67/)
