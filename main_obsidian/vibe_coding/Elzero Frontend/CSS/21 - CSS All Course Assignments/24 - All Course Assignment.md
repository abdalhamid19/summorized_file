---
title: 24 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 24
---

# 24 — CSS Progress Bars

> [!question] السؤال الرسمي
> اعمل الشكل المطلوب كما في الصورة.
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-24-reference.jpg]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```html
> <div class="progress-panel">
>   <div class="metric">
>     <div class="label">Money</div>
>     <div class="value">$20.000</div>
>     <div class="track" style="--value: 80%; --color: #1877dc"><div class="fill"></div><span class="badge">80%</span></div>
>   </div>
>   <div class="metric">
>     <div class="label">Projects</div>
>     <div class="value">24</div>
>     <div class="track" style="--value: 55%; --color: #f5a623"><div class="fill"></div><span class="badge">55%</span></div>
>   </div>
>   <div class="metric">
>     <div class="label">Team</div>
>     <div class="value">12</div>
>     <div class="track" style="--value: 75%; --color: #2eaf61"><div class="fill"></div><span class="badge">75%</span></div>
>   </div>
> </div>
> ```
>
> ```css
> .progress-panel {
>   padding: 24px;
>   border-radius: 16px;
>   background: #fff;
> }
>
> .metric { height: 111px; }
> .label { margin-bottom: 4px; color: #858585; font-size: 16px; }
> .value { margin-bottom: 12px; color: #111; font-size: 18px; font-weight: bold; }
>
> .track {
>   position: relative;
>   width: 100%;
>   height: 5px;
>   background: #eee;
> }
>
> .fill {
>   width: var(--value);
>   height: 100%;
>   background: var(--color);
> }
>
> .badge {
>   position: absolute;
>   top: -37px;
>   left: var(--value);
>   padding: 4px 6px;
>   border-radius: 8px;
>   color: #fff;
>   background: var(--color);
>   font-size: 14px;
>   font-weight: bold;
>   transform: translateX(-50%);
> }
>
> .badge::after {
>   content: "";
>   position: absolute;
>   left: 50%;
>   bottom: -5px;
>   border-width: 5px 5px 0;
>   border-style: solid;
>   border-color: var(--color) transparent transparent;
>   transform: translateX(-50%);
> }
> ```
>
> ### الفكرة الأساسية
>
> تمثل `--value` نسبة التقدم، وتملأ `.fill` هذا الجزء من المسار الرمادي. يضع `badge` (شارة النسبة) القيمة فوق نهاية الامتلاء، ويصنع `::after` طرفها السفلي الصغير.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `.progress-panel`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.track`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.fill`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.badge`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.badge::after`
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > ### خصائص CSS
> >
> > #### `padding`
> >
> > تضيف مساحة داخلية. مثال القيمة: `24px`
> >
> > #### `border-radius`
> >
> > تدوّر زوايا العنصر. مثال القيمة: `16px`
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
> > تحدد عرض العنصر. مثال القيمة: `100%`
> >
> > #### `height`
> >
> > تحدد ارتفاع العنصر. مثال القيمة: `5px`
> >
> > #### `top`
> >
> > تحدد المسافة من أعلى مرجع التموضع. مثال القيمة: -`37px`
> >
> > #### `left`
> >
> > تحدد المسافة من اليسار. مثال القيمة: `var(--value)`
> >
> > #### `color`
> >
> > تحدد لون النص. مثال القيمة: `#fff`
> >
> > #### `font-size`
> >
> > تحدد حجم النص. مثال القيمة: `14px`
> >
> > #### `font-weight`
> >
> > تحدد سُمك الخط. مثال القيمة: `bold`
> >
> > #### `transform`
> >
> > تطبق دورانًا أو تحريكًا أو تحجيمًا. مثال القيمة: `translateX(-50%)`
> >
> > #### `content`
> >
> > تحدد محتوى العنصر الزائف. مثال القيمة: ""
> >
> > #### `bottom`
> >
> > تحدد المسافة من الأسفل. مثال القيمة: -`5px`
> >
> > #### `border-width`
> >
> > تحدد قيمة الخاصية `border-width`. مثال القيمة: `5px` `5px` 0
> >
> > #### `border-style`
> >
> > تحدد قيمة الخاصية `border-style`. مثال القيمة: `solid`
> >
> > ### الدوال والوحدات
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
> > #### `translateX()`
> >
> > تحرك العنصر أفقيًا على محور `X`.
> >
> > #### `var()`
> >
> > تستدعي قيمة متغير `CSS` مثل `--main-color`.
> >
> > #### `translateX()`
> >
> > تحرك العنصر أفقيًا على محور `X`.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > ### علامات HTML
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<div>`
> >
> > حاوية عامة.
> >
> > #### `<span>`
> >
> > عنصر داخل السطر.
> >
> > #### `<span>`
> >
> > عنصر داخل السطر.
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
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `html`
> >
> > ```html
> > <div class="progress-panel">
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 02 — `html`
> >
> > ```html
> >   <div class="metric">
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 03 — `html`
> >
> > ```html
> >     <div class="label">Money</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 04 — `html`
> >
> > ```html
> >     <div class="value">$20.000</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 05 — `html`
> >
> > ```html
> >     <div class="track" style="--value: 80%; --color: #1877dc"><div class="fill"></div><span class="badge">80%</span></div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 06 — `html`
> >
> > ```html
> >   </div>
> > ```
> >
> > يغلق وسم `div` وينهي العنصر.
> >
> > #### السطر 07 — `html`
> >
> > ```html
> >   <div class="metric">
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 08 — `html`
> >
> > ```html
> >     <div class="label">Projects</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 09 — `html`
> >
> > ```html
> >     <div class="value">24</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 10 — `html`
> >
> > ```html
> >     <div class="track" style="--value: 55%; --color: #f5a623"><div class="fill"></div><span class="badge">55%</span></div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 11 — `html`
> >
> > ```html
> >   </div>
> > ```
> >
> > يغلق وسم `div` وينهي العنصر.
> >
> > #### السطر 12 — `html`
> >
> > ```html
> >   <div class="metric">
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 13 — `html`
> >
> > ```html
> >     <div class="label">Team</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 14 — `html`
> >
> > ```html
> >     <div class="value">12</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 15 — `html`
> >
> > ```html
> >     <div class="track" style="--value: 75%; --color: #2eaf61"><div class="fill"></div><span class="badge">75%</span></div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 16 — `html`
> >
> > ```html
> >   </div>
> > ```
> >
> > يغلق وسم `div` وينهي العنصر.
> >
> > #### السطر 17 — `html`
> >
> > ```html
> > </div>
> > ```
> >
> > يغلق وسم `div` وينهي العنصر.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> > .progress-panel {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> >   padding: 24px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `24px`.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> >   border-radius: 16px;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `16px`.
> >
> > #### السطر 21 — `css`
> >
> > ```css
> >   background: #fff;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#fff`.
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
> > .metric { height: 111px; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `height`.
> >
> > #### السطر 24 — `css`
> >
> > ```css
> > .label { margin-bottom: 4px; color: #858585; font-size: 16px; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `margin-bottom` وcolor وfont-`size`.
> >
> > #### السطر 25 — `css`
> >
> > ```css
> > .value { margin-bottom: 12px; color: #111; font-size: 18px; font-weight: bold; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `margin-bottom` وcolor وfont-`size` وfont-`weight`.
> >
> > #### السطر 26 — `css`
> >
> > ```css
> > .track {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 27 — `css`
> >
> > ```css
> >   position: relative;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `relative`.
> >
> > #### السطر 28 — `css`
> >
> > ```css
> >   width: 100%;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 29 — `css`
> >
> > ```css
> >   height: 5px;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `5px`.
> >
> > #### السطر 30 — `css`
> >
> > ```css
> >   background: #eee;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#eee`.
> >
> > #### السطر 31 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 32 — `css`
> >
> > ```css
> > .fill {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 33 — `css`
> >
> > ```css
> >   width: var(--value);
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `var(--value)`.
> >
> > #### السطر 34 — `css`
> >
> > ```css
> >   height: 100%;
> > ```
> >
> > تحدد ارتفاع العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 35 — `css`
> >
> > ```css
> >   background: var(--color);
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `var(--color)`.
> >
> > #### السطر 36 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 37 — `css`
> >
> > ```css
> > .badge {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 38 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 39 — `css`
> >
> > ```css
> >   top: -37px;
> > ```
> >
> > تحدد المسافة من أعلى مرجع التموضع. والقيمة هنا -`37px`.
> >
> > #### السطر 40 — `css`
> >
> > ```css
> >   left: var(--value);
> > ```
> >
> > تحدد المسافة من اليسار. والقيمة هنا `var(--value)`.
> >
> > #### السطر 41 — `css`
> >
> > ```css
> >   padding: 4px 6px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `4px` `6px`.
> >
> > #### السطر 42 — `css`
> >
> > ```css
> >   border-radius: 8px;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `8px`.
> >
> > #### السطر 43 — `css`
> >
> > ```css
> >   color: #fff;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#fff`.
> >
> > #### السطر 44 — `css`
> >
> > ```css
> >   background: var(--color);
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `var(--color)`.
> >
> > #### السطر 45 — `css`
> >
> > ```css
> >   font-size: 14px;
> > ```
> >
> > تحدد حجم النص. والقيمة هنا `14px`.
> >
> > #### السطر 46 — `css`
> >
> > ```css
> >   font-weight: bold;
> > ```
> >
> > تحدد سُمك الخط. والقيمة هنا `bold`.
> >
> > #### السطر 47 — `css`
> >
> > ```css
> >   transform: translateX(-50%);
> > ```
> >
> > تطبق دورانًا أو تحريكًا أو تحجيمًا. والقيمة هنا `translateX(-50%)`.
> >
> > #### السطر 48 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 49 — `css`
> >
> > ```css
> > .badge::after {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 50 — `css`
> >
> > ```css
> >   content: "";
> > ```
> >
> > تحدد محتوى العنصر الزائف. والقيمة هنا "".
> >
> > #### السطر 51 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 52 — `css`
> >
> > ```css
> >   left: 50%;
> > ```
> >
> > تحدد المسافة من اليسار. والقيمة هنا `50%`.
> >
> > #### السطر 53 — `css`
> >
> > ```css
> >   bottom: -5px;
> > ```
> >
> > تحدد المسافة من الأسفل. والقيمة هنا -`5px`.
> >
> > #### السطر 54 — `css`
> >
> > ```css
> >   border-width: 5px 5px 0;
> > ```
> >
> > تحدد قيمة الخاصية `border-width`. والقيمة هنا `5px` `5px` 0.
> >
> > #### السطر 55 — `css`
> >
> > ```css
> >   border-style: solid;
> > ```
> >
> > تحدد قيمة الخاصية `border-style`. والقيمة هنا `solid`.
> >
> > #### السطر 56 — `css`
> >
> > ```css
> >   border-color: var(--color) transparent transparent;
> > ```
> >
> > تحدد قيمة الخاصية `border-color`. والقيمة هنا `var(--color)` `transparent` `transparent`.
> >
> > #### السطر 57 — `css`
> >
> > ```css
> >   transform: translateX(-50%);
> > ```
> >
> > تطبق دورانًا أو تحريكًا أو تحجيمًا. والقيمة هنا `translateX(-50%)`.
> >
> > #### السطر 58 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-24.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/24 - All Course Assignment.html|افتح صفحة التكليف 24]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
