---
title: 23 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 23
---

# 23 — CSS Grid Item Placement

> [!question] السؤال الرسمي
> استخدم بنية HTML التالية كما هي دون تعديل، واكتب CSS لعمل الشكل في الصورة.
>
> ```html
> <div class="the-grid"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-23-reference.jpg]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> .the-grid {
>   display: grid;
>   grid-template-columns: repeat(5, minmax(0, 1fr));
>   grid-template-rows: repeat(4, 100px) repeat(6, 46.5px);
>   gap: 12px;
>   counter-reset: grid-item;
> }
>
> .the-grid > div {
>   display: grid;
>   place-items: center;
>   background: #fff;
>   counter-increment: grid-item;
>   font: bold 40px Arial, sans-serif;
> }
>
> .the-grid > div::before { content: counter(grid-item); }
> .the-grid > div:nth-child(1) { grid-column: 1 / span 2; grid-row: 1 / span 2; }
> .the-grid > div:nth-child(2) { grid-column: 3; grid-row: 1; }
> .the-grid > div:nth-child(3) { grid-column: 4 / span 2; grid-row: 1; }
> .the-grid > div:nth-child(4) { grid-column: 3 / span 3; grid-row: 2 / span 2; }
> .the-grid > div:nth-child(5) { grid-column: 1 / span 2; grid-row: 3; }
> .the-grid > div:nth-child(6) { grid-column: 1 / span 4; grid-row: 4; }
> .the-grid > div:nth-child(7) { grid-column: 5; grid-row: 4; }
> .the-grid > div:nth-child(8) { grid-column: 1; grid-row: 5 / span 3; }
> .the-grid > div:nth-child(9) { grid-column: 2 / span 3; grid-row: 5 / span 3; }
> .the-grid > div:nth-child(10) { grid-column: 5; grid-row: 5; }
> .the-grid > div:nth-child(11) { grid-column: 5; grid-row: 6; }
> .the-grid > div:nth-child(12) { grid-column: 5; grid-row: 7; }
> .the-grid > div:nth-child(13) { grid-column: 1 / span 5; grid-row: 8; }
> .the-grid > div:nth-child(14) { grid-column: 1 / span 2; grid-row: 9; }
> .the-grid > div:nth-child(15) { grid-column: 3 / span 3; grid-row: 9; }
> .the-grid > div:nth-child(16) { grid-column: 1; grid-row: 10; }
> .the-grid > div:nth-child(17) { grid-column: 2; grid-row: 10; }
> .the-grid > div:nth-child(18) { grid-column: 3; grid-row: 10; }
> .the-grid > div:nth-child(19) { grid-column: 4; grid-row: 10; }
> .the-grid > div:nth-child(20) { grid-column: 5; grid-row: 10; }
> ```
>
> ### الفكرة الأساسية
>
> يعرّف `grid-template-columns` خمسة أعمدة، وتحدد `grid-template-rows` صفوفًا أطول للأجزاء العلوية وصفوفًا قصيرة للجزء السفلي.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.the-grid`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.the-grid > div`
> >
> > يختار الابن المباشر للعنصر السابق.
> >
> > ### خصائص CSS
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `grid-template-columns`
> >
> > تحدد أعمدة `Grid`. مثال القيمة: `repeat(5, minmax(0, 1fr)`)
> >
> > #### `grid-template-rows`
> >
> > تحدد صفوف `Grid`. مثال القيمة: `repeat(4, 100px)` `repeat(6, 46.5px)`
> >
> > #### `gap`
> >
> > تحدد المسافة بين عناصر التخطيط. مثال القيمة: `12px`
> >
> > #### `counter-reset`
> >
> > تبدأ عداد `CSS`. مثال القيمة: `grid-item`
> >
> > #### `place-items`
> >
> > تختصر محاذاة `Grid`. مثال القيمة: `center`
> >
> > #### `background`
> >
> > تضبط الخلفية. مثال القيمة: `#fff`
> >
> > #### `counter-increment`
> >
> > تزيد عداد `CSS`. مثال القيمة: `grid-item`
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: `bold` `40px` `Arial`, `sans-serif`
> >
> > ### الدوال والوحدات
> >
> > #### `repeat()`
> >
> > تكرر مسارًا أو مجموعة مسارات بعدد محدد في تخطيط `Grid`.
> >
> > #### `minmax()`
> >
> > تحدد حدًا أدنى وحدًا أقصى لحجم مسار في `Grid`.
> >
> > #### `repeat()`
> >
> > تكرر مسارًا أو مجموعة مسارات بعدد محدد في تخطيط `Grid`.
> >
> > #### `repeat()`
> >
> > تكرر مسارًا أو مجموعة مسارات بعدد محدد في تخطيط `Grid`.
> >
> > #### `counter()`
> >
> > تعرض القيمة الحالية لعداد `CSS`.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `fr`
> >
> > جزء من مساحة `Grid`.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
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
> > .the-grid {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   grid-template-columns: repeat(5, minmax(0, 1fr));
> > ```
> >
> > تحدد أعمدة `Grid`. والقيمة هنا `repeat(5, minmax(0, 1fr)`).
> >
> > #### السطر 04 — `css`
> >
> > ```css
> >   grid-template-rows: repeat(4, 100px) repeat(6, 46.5px);
> > ```
> >
> > تحدد صفوف `Grid`. والقيمة هنا `repeat(4, 100px)` `repeat(6, 46.5px)`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   gap: 12px;
> > ```
> >
> > تحدد المسافة بين عناصر التخطيط. والقيمة هنا `12px`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   counter-reset: grid-item;
> > ```
> >
> > تبدأ عداد `CSS`. والقيمة هنا `grid-item`.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> > .the-grid > div {
> > ```
> >
> > يختار الابن المباشر للعنصر السابق.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 10 — `css`
> >
> > ```css
> >   place-items: center;
> > ```
> >
> > تختصر محاذاة `Grid`. والقيمة هنا `center`.
> >
> > #### السطر 11 — `css`
> >
> > ```css
> >   background: #fff;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#fff`.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> >   counter-increment: grid-item;
> > ```
> >
> > تزيد عداد `CSS`. والقيمة هنا `grid-item`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> >   font: bold 40px Arial, sans-serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا `bold` `40px` `Arial`, `sans-serif`.
> >
> > #### السطر 14 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> > .the-grid > div::before { content: counter(grid-item); }
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`. ويجمع السطر خصائص `content`.
> >
> > #### السطر 16 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(1) { grid-column: 1 / span 2; grid-row: 1 / span 2; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 17 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(2) { grid-column: 3; grid-row: 1; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(3) { grid-column: 4 / span 2; grid-row: 1; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(4) { grid-column: 3 / span 3; grid-row: 2 / span 2; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(5) { grid-column: 1 / span 2; grid-row: 3; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 21 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(6) { grid-column: 1 / span 4; grid-row: 4; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 22 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(7) { grid-column: 5; grid-row: 4; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 23 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(8) { grid-column: 1; grid-row: 5 / span 3; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 24 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(9) { grid-column: 2 / span 3; grid-row: 5 / span 3; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 25 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(10) { grid-column: 5; grid-row: 5; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 26 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(11) { grid-column: 5; grid-row: 6; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 27 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(12) { grid-column: 5; grid-row: 7; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 28 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(13) { grid-column: 1 / span 5; grid-row: 8; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 29 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(14) { grid-column: 1 / span 2; grid-row: 9; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 30 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(15) { grid-column: 3 / span 3; grid-row: 9; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 31 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(16) { grid-column: 1; grid-row: 10; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 32 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(17) { grid-column: 2; grid-row: 10; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 33 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(18) { grid-column: 3; grid-row: 10; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 34 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(19) { grid-column: 4; grid-row: 10; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 35 — `css`
> >
> > ```css
> > .the-grid > div:nth-child(20) { grid-column: 5; grid-row: 10; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-23.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/23 - All Course Assignment.html|افتح صفحة التكليف 23]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
