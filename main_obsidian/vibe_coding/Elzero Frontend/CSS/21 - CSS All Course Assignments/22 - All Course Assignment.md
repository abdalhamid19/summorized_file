---
title: 22 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 22
---

# 22 — CSS Grid Photo Gallery

> [!question] السؤال الرسمي
> اعمل الشكل كما في الصورة، ويمكن استخدام أي صور.
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-22-reference.jpg]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```html
> <div class="gallery">
>   <img src="assets/task22-photo-01.jpg" alt="Gaming controller">
>   <img src="assets/task22-photo-02.jpg" alt="Gaming setup">
>   <img src="assets/task22-photo-03.jpg" alt="Sports car">
>   <img src="assets/task22-photo-04.jpg" alt="Video game scene">
>   <img src="assets/task22-photo-05.jpg" alt="Basketball">
>   <img src="assets/task22-photo-06.jpg" alt="Cycling">
>   <img src="assets/task22-photo-07.jpg" alt="Virtual reality">
>   <img src="assets/task22-photo-08.jpg" alt="Earth from space">
> </div>
> ```
>
> ```css
> .gallery {
>   width: 950px;
>   height: 715px;
>   display: grid;
>   grid-template-columns: repeat(4, minmax(0, 1fr));
>   grid-template-rows: repeat(3, minmax(0, 1fr));
>   gap: 20px;
> }
>
> .gallery img {
>   width: 100%;
>   height: 100%;
>   object-fit: cover;
>   border-radius: 10px;
> }
>
> .gallery img:nth-child(1) { grid-column: 1; grid-row: 1 / span 2; }
> .gallery img:nth-child(2) { grid-column: 2; grid-row: 1; }
> .gallery img:nth-child(3) { grid-column: 3 / span 2; grid-row: 1; }
> .gallery img:nth-child(4) { grid-column: 2; grid-row: 2 / span 2; }
> .gallery img:nth-child(5) { grid-column: 3; grid-row: 2; }
> .gallery img:nth-child(6) { grid-column: 4; grid-row: 2; }
> .gallery img:nth-child(7) { grid-column: 1; grid-row: 3; }
> .gallery img:nth-child(8) { grid-column: 3 / span 2; grid-row: 3; }
> ```
>
> ### الفكرة الأساسية
>
> تحدد `grid-template-columns` أربعة أعمدة متساوية. تستخدم `grid-column` و`grid-row` لتكبير الصور الطويلة والعريضة لتطابق توزيع الصورة.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.gallery`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.gallery img`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > ### خصائص CSS
> >
> > #### `width`
> >
> > تحدد عرض العنصر. مثال القيمة: `950px`
> >
> > #### `height`
> >
> > تحدد ارتفاع العنصر. مثال القيمة: `715px`
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `grid-template-columns`
> >
> > تحدد أعمدة `Grid`. مثال القيمة: `repeat(4, minmax(0, 1fr)`)
> >
> > #### `grid-template-rows`
> >
> > تحدد صفوف `Grid`. مثال القيمة: `repeat(3, minmax(0, 1fr)`)
> >
> > #### `gap`
> >
> > تحدد المسافة بين عناصر التخطيط. مثال القيمة: `20px`
> >
> > #### `object-fit`
> >
> > تحدد ملاءمة الصورة لصندوقها. مثال القيمة: `cover`
> >
> > #### `border-radius`
> >
> > تدوّر زوايا العنصر. مثال القيمة: `10px`
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
> > #### `minmax()`
> >
> > تحدد حدًا أدنى وحدًا أقصى لحجم مسار في `Grid`.
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
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > #### `fr`
> >
> > جزء من مساحة `Grid`.
> >
> > ### علامات HTML
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<img>`
> >
> > صورة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
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
> > #### السطر 01 — `html`
> >
> > ```html
> > <div class="gallery">
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 02 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-01.jpg" alt="Gaming controller">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 03 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-02.jpg" alt="Gaming setup">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 04 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-03.jpg" alt="Sports car">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 05 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-04.jpg" alt="Video game scene">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 06 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-05.jpg" alt="Basketball">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 07 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-06.jpg" alt="Cycling">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 08 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-07.jpg" alt="Virtual reality">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 09 — `html`
> >
> > ```html
> >   <img src="assets/task22-photo-08.jpg" alt="Earth from space">
> > ```
> >
> > يفتح وسم `img` المستخدم بوصفه صورة.؛ `src` يحدد مصدر الملف.
> >
> > #### السطر 10 — `html`
> >
> > ```html
> > </div>
> > ```
> >
> > يغلق وسم `div` وينهي العنصر.
> >
> > #### السطر 11 — `css`
> >
> > ```css
> > .gallery {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> >   width: 950px;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `950px`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> >   height: 715px;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `715px`.
> >
> > #### السطر 14 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> >   grid-template-columns: repeat(4, minmax(0, 1fr));
> > ```
> >
> > تحدد أعمدة `Grid`. والقيمة هنا `repeat(4, minmax(0, 1fr)`).
> >
> > #### السطر 16 — `css`
> >
> > ```css
> >   grid-template-rows: repeat(3, minmax(0, 1fr));
> > ```
> >
> > تحدد صفوف `Grid`. والقيمة هنا `repeat(3, minmax(0, 1fr)`).
> >
> > #### السطر 17 — `css`
> >
> > ```css
> >   gap: 20px;
> > ```
> >
> > تحدد المسافة بين عناصر التخطيط. والقيمة هنا `20px`.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> > .gallery img {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> >   width: 100%;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 21 — `css`
> >
> > ```css
> >   height: 100%;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 22 — `css`
> >
> > ```css
> >   object-fit: cover;
> > ```
> >
> > تحدد ملاءمة الصورة لصندوقها. والقيمة هنا `cover`.
> >
> > #### السطر 23 — `css`
> >
> > ```css
> >   border-radius: 10px;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `10px`.
> >
> > #### السطر 24 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 25 — `css`
> >
> > ```css
> > .gallery img:nth-child(1) { grid-column: 1; grid-row: 1 / span 2; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 26 — `css`
> >
> > ```css
> > .gallery img:nth-child(2) { grid-column: 2; grid-row: 1; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 27 — `css`
> >
> > ```css
> > .gallery img:nth-child(3) { grid-column: 3 / span 2; grid-row: 1; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 28 — `css`
> >
> > ```css
> > .gallery img:nth-child(4) { grid-column: 2; grid-row: 2 / span 2; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 29 — `css`
> >
> > ```css
> > .gallery img:nth-child(5) { grid-column: 3; grid-row: 2; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 30 — `css`
> >
> > ```css
> > .gallery img:nth-child(6) { grid-column: 4; grid-row: 2; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 31 — `css`
> >
> > ```css
> > .gallery img:nth-child(7) { grid-column: 1; grid-row: 3; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
> > #### السطر 32 — `css`
> >
> > ```css
> > .gallery img:nth-child(8) { grid-column: 3 / span 2; grid-row: 3; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `grid-column` وgrid-`row`.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-22.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/22 - All Course Assignment.html|افتح صفحة التكليف 22]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
