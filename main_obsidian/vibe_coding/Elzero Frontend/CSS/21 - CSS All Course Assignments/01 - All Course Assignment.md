---
title: "CSS All Course Assignment 01"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 01
---

# CSS All Course Assignment 01

> [!question] المطلوب
> طابق الصورة مع إبقاء HTML كما هو. اجعل سُمك الخطوط الملونة `5px`، ولا تستخدم `box-shadow`. كتحدٍ إضافي، تحكّم بالسُمك من متغير CSS واحد.
>
> ```html
> <div class="elzero-lines">Lines</div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-01-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> :root {
>   --line-size: 5px;
> }
>
> body {
>   min-height: 100vh;
>   margin: 0;
>   display: grid;
>   place-items: center;
>   background: #fff;
> }
>
> .elzero-lines {
>   position: relative;
>   display: grid;
>   place-items: center;
>   width: min(400px, calc(100% - 40px));
>   min-height: 68px;
>   box-sizing: border-box;
>   border: var(--line-size) solid red;
>   outline: var(--line-size) solid #000;
>   outline-offset: calc(var(--line-size) + var(--line-size));
>   font: 700 14px/1 Georgia, serif;
> }
>
> .elzero-lines::before {
>   content: "";
>   position: absolute;
>   inset: calc(0px - var(--line-size) - var(--line-size));
>   border: var(--line-size) solid blue;
>   outline: var(--line-size) solid green;
>   pointer-events: none;
> }
> ```
>
> ### الفكرة الأساسية
>
> المتغير `--line-size` يحفظ سُمك الخط. غيّر قيمة واحدة لتعديل كل الحدود والخطوط معًا.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `:root`
> >
> > يستهدف جذر الصفحة، موضع المتغيرات العامة عادةً.
> >
> > #### `body`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `.elzero-lines`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.elzero-lines::before`
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > ### خصائص CSS
> >
> > #### `--line-size`
> >
> > تحدد قيمة الخاصية `--line-size`. مثال القيمة: `5px`
> >
> > #### `min-height`
> >
> > تحدد أقل ارتفاع. مثال القيمة: `100vh`
> >
> > #### `margin`
> >
> > تضيف مسافة خارجية. مثال القيمة: 0
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `place-items`
> >
> > تختصر محاذاة `Grid`. مثال القيمة: `center`
> >
> > #### `background`
> >
> > تضبط الخلفية. مثال القيمة: `#fff`
> >
> > #### `position`
> >
> > تحدد طريقة التموضع. مثال القيمة: `relative`
> >
> > #### `width`
> >
> > تحدد عرض العنصر. مثال القيمة: `min(400px, calc(100% - 40px)`)
> >
> > #### `box-sizing`
> >
> > تحدد حساب أبعاد الصندوق. مثال القيمة: `border-box`
> >
> > #### `border`
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. مثال القيمة: `var(--line-size)` `solid` `red`
> >
> > #### `outline`
> >
> > ترسم خطًا خارج الحد. مثال القيمة: `var(--line-size)` `solid` `#000`
> >
> > #### `outline-offset`
> >
> > تحدد المسافة بين العنصر وخط `outline`. مثال القيمة: `calc(var(--line-size)` + `var(--line-size)`)
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: 700 `14px`/1 `Georgia`, `serif`
> >
> > #### `content`
> >
> > تحدد محتوى العنصر الزائف. مثال القيمة: ""
> >
> > #### `inset`
> >
> > تحدد المسافات من الحواف. مثال القيمة: `calc(0px - var(--line-size)` - `var(--line-size)`)
> >
> > #### `pointer-events`
> >
> > تحدد استقبال أحداث المؤشر. مثال القيمة: `none`
> >
> > ### الدوال والوحدات
> >
> > #### `min()`
> >
> > تختار أصغر قيمة من القيم المعطاة.
> >
> > #### `calc()`
> >
> > تحسب قيمة من تعبير رياضي، ويمكنها الجمع بين وحدات `CSS` المختلفة.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `calc()`
> >
> > تحسب قيمة من تعبير رياضي، ويمكنها الجمع بين وحدات `CSS` المختلفة.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `calc()`
> >
> > تحسب قيمة من تعبير رياضي، ويمكنها الجمع بين وحدات `CSS` المختلفة.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > #### `vh`
> >
> > نسبة من ارتفاع نافذة العرض.
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
> > :root {
> > ```
> >
> > يستهدف جذر الصفحة، موضع المتغيرات العامة عادةً.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   --line-size: 5px;
> > ```
> >
> > تحدد قيمة الخاصية `--line-size`. والقيمة هنا `5px`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > body {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   min-height: 100vh;
> > ```
> >
> > تحدد أقل ارتفاع. والقيمة هنا `100vh`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   margin: 0;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> >   place-items: center;
> > ```
> >
> > تختصر محاذاة `Grid`. والقيمة هنا `center`.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   background: #fff;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#fff`.
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
> > .elzero-lines {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> >   position: relative;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `relative`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 14 — `css`
> >
> > ```css
> >   place-items: center;
> > ```
> >
> > تختصر محاذاة `Grid`. والقيمة هنا `center`.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> >   width: min(400px, calc(100% - 40px));
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `min(400px, calc(100% - 40px)`).
> >
> > #### السطر 16 — `css`
> >
> > ```css
> >   min-height: 68px;
> > ```
> >
> > تحدد أقل ارتفاع. والقيمة هنا `68px`.
> >
> > #### السطر 17 — `css`
> >
> > ```css
> >   box-sizing: border-box;
> > ```
> >
> > تحدد حساب أبعاد الصندوق. والقيمة هنا `border-box`.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> >   border: var(--line-size) solid red;
> > ```
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. والقيمة هنا `var(--line-size)` `solid` `red`.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> >   outline: var(--line-size) solid #000;
> > ```
> >
> > ترسم خطًا خارج الحد. والقيمة هنا `var(--line-size)` `solid` `#000`.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> >   outline-offset: calc(var(--line-size) + var(--line-size));
> > ```
> >
> > تحدد المسافة بين العنصر وخط `outline`. والقيمة هنا `calc(var(--line-size)` + `var(--line-size)`).
> >
> > #### السطر 21 — `css`
> >
> > ```css
> >   font: 700 14px/1 Georgia, serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا 700 `14px`/1 `Georgia`, `serif`.
> >
> > #### السطر 22 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 23 — `css`
> >
> > ```css
> > .elzero-lines::before {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 24 — `css`
> >
> > ```css
> >   content: "";
> > ```
> >
> > تحدد محتوى العنصر الزائف. والقيمة هنا "".
> >
> > #### السطر 25 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 26 — `css`
> >
> > ```css
> >   inset: calc(0px - var(--line-size) - var(--line-size));
> > ```
> >
> > تحدد المسافات من الحواف. والقيمة هنا `calc(0px - var(--line-size)` - `var(--line-size)`).
> >
> > #### السطر 27 — `css`
> >
> > ```css
> >   border: var(--line-size) solid blue;
> > ```
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. والقيمة هنا `var(--line-size)` `solid` `blue`.
> >
> > #### السطر 28 — `css`
> >
> > ```css
> >   outline: var(--line-size) solid green;
> > ```
> >
> > ترسم خطًا خارج الحد. والقيمة هنا `var(--line-size)` `solid` `green`.
> >
> > #### السطر 29 — `css`
> >
> > ```css
> >   pointer-events: none;
> > ```
> >
> > تحدد استقبال أحداث المؤشر. والقيمة هنا `none`.
> >
> > #### السطر 30 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-01.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/01 - All Course Assignment.html|افتح صفحة التكليف 01]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
