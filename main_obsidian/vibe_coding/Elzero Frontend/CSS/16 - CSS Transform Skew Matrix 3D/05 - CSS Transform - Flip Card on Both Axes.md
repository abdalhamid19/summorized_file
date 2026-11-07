---
title: "CSS Transform - Flip Card on Both Axes"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 05
---

# CSS Transform - Flip Card on Both Axes

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها، واجعل البطاقة 200×200px ومتمركزة رأسيًا وأفقيًا. أنشئ انقلابًا حول المحور الأفقي وآخر حول المحور الرأسي.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/16 - CSS Transform Skew Matrix 3D/assets/reference-task-05-frame.png|650]]
> ![[vibe_coding/Elzero Frontend/CSS/16 - CSS Transform Skew Matrix 3D/assets/reference-task-05-2-frame.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .flip-card {
>   width: 200px;
>   height: 200px;
>   perspective: 700px;
> }
>
> .flip-card__inner {
>   position: relative;
>   width: 100%;
>   height: 100%;
>   transform-style: preserve-3d;
>   transition: transform .8s;
> }
>
> .flip-card:hover .flip-card__inner { transform: rotateY(180deg); }
> .flip-card--vertical:hover .flip-card__inner { transform: rotateX(180deg); }
>
> .flip-card__face {
>   position: absolute;
>   inset: 0;
>   display: grid;
>   place-items: center;
>   color: white;
>   background: #e91e63;
>   backface-visibility: hidden;
> }
>
> .flip-card__back { transform: rotateY(180deg); background: #009688; }
> .flip-card--vertical .flip-card__back { transform: rotateX(180deg); }
> ```
>
> ### الفكرة الأساسية
>
> تحدد `perspective` عمق المشهد، وتحافظ `preserve-3d` على وجهي البطاقة في فضاء ثلاثي الأبعاد. الحل الأول يدور حول محور `Y`، والثاني حول `X`، فينتجان الانقلاب الأفقي والرأسي.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.flip-card`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.flip-card__inner`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.flip-card__face`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > ### خصائص CSS
> >
> > #### `width`
> >
> > تحدد عرض العنصر. مثال القيمة: `200px`
> >
> > #### `height`
> >
> > تحدد ارتفاع العنصر. مثال القيمة: `200px`
> >
> > #### `perspective`
> >
> > تحدد قيمة الخاصية `perspective`. مثال القيمة: `700px`
> >
> > #### `position`
> >
> > تحدد طريقة التموضع. مثال القيمة: `relative`
> >
> > #### `transform-style`
> >
> > تحدد قيمة الخاصية `transform-style`. مثال القيمة: `preserve-3d`
> >
> > #### `transition`
> >
> > تجعل تغير الخاصية تدريجيًا. مثال القيمة: `transform` .`8s`
> >
> > #### `inset`
> >
> > تحدد المسافات من الحواف. مثال القيمة: 0
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `place-items`
> >
> > تختصر محاذاة `Grid`. مثال القيمة: `center`
> >
> > #### `color`
> >
> > تحدد لون النص. مثال القيمة: `white`
> >
> > #### `background`
> >
> > تضبط الخلفية. مثال القيمة: `#e91e63`
> >
> > #### `backface-visibility`
> >
> > تحدد قيمة الخاصية `backface-visibility`. مثال القيمة: `hidden`
> >
> > ### الدوال والوحدات
> >
> > #### `rotateY()`
> >
> > تدير العنصر ثلاثي الأبعاد حول محور `Y`.
> >
> > #### `rotateX()`
> >
> > تدير العنصر ثلاثي الأبعاد حول محور `X`.
> >
> > #### `rotateY()`
> >
> > تدير العنصر ثلاثي الأبعاد حول محور `Y`.
> >
> > #### `rotateX()`
> >
> > تدير العنصر ثلاثي الأبعاد حول محور `X`.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
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
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `css`
> >
> > ```css
> > .flip-card {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   width: 200px;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `200px`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   height: 200px;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `200px`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> >   perspective: 700px;
> > ```
> >
> > تحدد قيمة الخاصية `perspective`. والقيمة هنا `700px`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> > .flip-card__inner {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> >   position: relative;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `relative`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> >   width: 100%;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   height: 100%;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 10 — `css`
> >
> > ```css
> >   transform-style: preserve-3d;
> > ```
> >
> > تحدد قيمة الخاصية `transform-style`. والقيمة هنا `preserve-3d`.
> >
> > #### السطر 11 — `css`
> >
> > ```css
> >   transition: transform .8s;
> > ```
> >
> > تجعل تغير الخاصية تدريجيًا. والقيمة هنا `transform` .`8s`.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> > .flip-card:hover .flip-card__inner { transform: rotateY(180deg); }
> > ```
> >
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. ويجمع السطر خصائص `transform`.
> >
> > #### السطر 14 — `css`
> >
> > ```css
> > .flip-card--vertical:hover .flip-card__inner { transform: rotateX(180deg); }
> > ```
> >
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. ويجمع السطر خصائص `transform`.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> > .flip-card__face {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 16 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 17 — `css`
> >
> > ```css
> >   inset: 0;
> > ```
> >
> > تحدد المسافات من الحواف. والقيمة هنا 0.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> >   place-items: center;
> > ```
> >
> > تختصر محاذاة `Grid`. والقيمة هنا `center`.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> >   color: white;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `white`.
> >
> > #### السطر 21 — `css`
> >
> > ```css
> >   background: #e91e63;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#e91e63`.
> >
> > #### السطر 22 — `css`
> >
> > ```css
> >   backface-visibility: hidden;
> > ```
> >
> > تحدد قيمة الخاصية `backface-visibility`. والقيمة هنا `hidden`.
> >
> > #### السطر 23 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 24 — `css`
> >
> > ```css
> > .flip-card__back { transform: rotateY(180deg); background: #009688; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `transform` وbackground.
> >
> > #### السطر 25 — `css`
> >
> > ```css
> > .flip-card--vertical .flip-card__back { transform: rotateX(180deg); }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `transform`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/16 - CSS Transform Skew Matrix 3D/assets/solution-page-task-05.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/16 - CSS Transform Skew Matrix 3D/05 - CSS Transform - Flip Card on Both Axes.html|افتح صفحة التكليف 05]]

## المصدر

[تكليفات CSS للدروس 68–73](https://elzero.org/css-assignments-lesson-from-68-to-73/)
