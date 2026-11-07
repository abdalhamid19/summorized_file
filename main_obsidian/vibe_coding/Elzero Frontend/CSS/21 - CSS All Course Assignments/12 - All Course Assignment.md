---
title: "All Course Assignment 12 — Pricing Plans"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 12"
---

# 12 - All Course Assignment

> [!question] المطلوب
> أنشئ الشكل المعروض مع استخدام الألوان نفسها.
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-12-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```html
> <div class="plans">
>   <article class="plan-card">
>     <h3>Personal</h3>
>     <p class="price"><span>$</span><strong>10</strong><small>/ Mo</small></p>
>     <ul>
>       <li><strong>Free</strong> Weekly Meeting</li>
>       <li><strong>1x</strong> Monthly Call</li>
>       <li><strong>Unlimited</strong> Messenger Chats</li>
>       <li><strong>Free</strong> Control Panel Access</li>
>       <li><strong>1x</strong> Face to Face Meeting</li>
>     </ul>
>     <button>Buy Now</button>
>   </article>
>   <article class="plan-card featured">
>     <div class="ribbon">Most Popular</div>
>     <h3>Business</h3>
>     <p class="price"><span>$</span><strong>15</strong><small>/ Mo</small></p>
>     <ul>
>       <li><strong>Free</strong> Weekly Meeting</li>
>       <li><strong>2x</strong> Monthly Call</li>
>       <li><strong>Unlimited</strong> Messenger Chats</li>
>       <li><strong>Free</strong> Control Panel Access</li>
>       <li><strong>2x</strong> Face to Face Meeting</li>
>     </ul>
>     <button>Buy Now</button>
>   </article>
>   <article class="plan-card">
>     <h3>Enterprise</h3>
>     <p class="price"><span>$</span><strong>20</strong><small>/ Mo</small></p>
>     <ul>
>       <li><strong>Free</strong> Daily Meeting</li>
>       <li><strong>3x</strong> Monthly Call</li>
>       <li><strong>Unlimited</strong> Messenger Chats</li>
>       <li><strong>Free</strong> Control Panel Access</li>
>       <li><strong>3x</strong> Face to Face Meeting</li>
>     </ul>
>     <button>Buy Now</button>
>   </article>
> </div>
> ```
>
> ```css
> * {
>   box-sizing: border-box;
> }
>
> body {
>   margin: 0;
>   background-color: #eee;
>   font-family: Arial, sans-serif;
> }
>
> .plans {
>   display: grid;
>   grid-template-columns: repeat(3, minmax(0, 1fr));
>   gap: 20px;
>   max-width: 1200px;
>   margin: 50px auto;
>   padding: 0 16px;
> }
>
> .plan-card {
>   position: relative;
>   display: flex;
>   flex-direction: column;
>   align-items: center;
>   min-height: 548px;
>   padding: 55px 18px 38px;
>   border: 1px solid #ccc;
>   background-color: #fff;
>   text-align: center;
> }
>
> .plan-card h3 {
>   margin: 0 0 30px;
>   font-size: 30px;
> }
>
> .price {
>   display: flex;
>   align-items: baseline;
>   gap: 2px;
>   margin: 0 0 30px;
>   color: #197beb;
> }
>
> .price span {
>   font-size: 30px;
> }
>
> .price strong {
>   font-size: 50px;
> }
>
> .price small {
>   color: #888;
>   font-size: 16px;
> }
>
> .plan-card ul {
>   display: grid;
>   gap: 22px;
>   width: 100%;
>   margin: 0;
>   padding: 0;
>   color: #888;
>   list-style: none;
>   font-size: 16px;
> }
>
> .plan-card button {
>   width: 140px;
>   margin-top: auto;
>   padding: 18px 12px;
>   border: 0;
>   border-radius: 32px;
>   background-color: #197beb;
>   color: #fff;
>   font-weight: 700;
> }
>
> .ribbon {
>   position: absolute;
>   top: -21px;
>   left: 10%;
>   width: 80%;
>   padding: 15px 8px;
>   background-color: #197beb;
>   color: #fff;
>   font-weight: 700;
> }
>
> .ribbon::before {
>   position: absolute;
>   top: 0;
>   left: -18px;
>   border-top: 21px solid #0e67cd;
>   border-left: 18px solid transparent;
>   content: "";
> }
> ```
>
> ### الفكرة الأساسية
>
> توزع `CSS Grid` البطاقات على ثلاثة أعمدة. تضع `flex-direction: column` عناصر كل بطاقة عموديًا، وتدفع `margin-top: auto` الزر إلى أسفلها. يرسم `::before` طرف الشريط الأزرق المائل من دون عنصر `HTML` إضافي.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `*`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `body`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `.plans`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.plan-card`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.plan-card h3`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.price`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.price span`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### `.price strong`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > ### خصائص CSS
> >
> > #### `box-sizing`
> >
> > تحدد حساب أبعاد الصندوق. مثال القيمة: `border-box`
> >
> > #### `margin`
> >
> > تضيف مسافة خارجية. مثال القيمة: 0
> >
> > #### `background-color`
> >
> > تحدد لون الخلفية. مثال القيمة: `#eee`
> >
> > #### `font-family`
> >
> > تحدد عائلة الخط. مثال القيمة: `Arial`, `sans-serif`
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `grid`
> >
> > #### `grid-template-columns`
> >
> > تحدد أعمدة `Grid`. مثال القيمة: `repeat(3, minmax(0, 1fr)`)
> >
> > #### `gap`
> >
> > تحدد المسافة بين عناصر التخطيط. مثال القيمة: `20px`
> >
> > #### `max-width`
> >
> > تحدد أقصى عرض. مثال القيمة: `1200px`
> >
> > #### `padding`
> >
> > تضيف مساحة داخلية. مثال القيمة: 0 `16px`
> >
> > #### `position`
> >
> > تحدد طريقة التموضع. مثال القيمة: `relative`
> >
> > #### `flex-direction`
> >
> > تحدد اتجاه عناصر `Flex`. مثال القيمة: `column`
> >
> > #### `align-items`
> >
> > تحاذي العناصر عرضيًا. مثال القيمة: `center`
> >
> > #### `min-height`
> >
> > تحدد أقل ارتفاع. مثال القيمة: `548px`
> >
> > #### `border`
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. مثال القيمة: `1px` `solid` `#ccc`
> >
> > #### `text-align`
> >
> > تحاذي النص. مثال القيمة: `center`
> >
> > #### `font-size`
> >
> > تحدد حجم النص. مثال القيمة: `30px`
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
> > #### `fr`
> >
> > جزء من مساحة `Grid`.
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
> > #### `<h3>`
> >
> > عنوان فرعي.
> >
> > #### `<h3>`
> >
> > عنوان فرعي.
> >
> > #### `<p>`
> >
> > فقرة.
> >
> > #### `<span>`
> >
> > عنصر داخل السطر.
> >
> > #### `<span>`
> >
> > عنصر داخل السطر.
> >
> > #### `<p>`
> >
> > فقرة.
> >
> > #### `<ul>`
> >
> > قائمة غير مرتبة.
> >
> > #### `<li>`
> >
> > عنصر قائمة.
> >
> > #### `<li>`
> >
> > عنصر قائمة.
> >
> > #### `<li>`
> >
> > عنصر قائمة.
> >
> > #### `<li>`
> >
> > عنصر قائمة.
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
> > <div class="plans">
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 02 — `html`
> >
> > ```html
> >   <article class="plan-card">
> > ```
> >
> > يفتح وسم `article` المستخدم بوصفه عنصر `HTML`.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 03 — `html`
> >
> > ```html
> >     <h3>Personal</h3>
> > ```
> >
> > يفتح وسم `h3` المستخدم بوصفه عنوان فرعي.
> >
> > #### السطر 04 — `html`
> >
> > ```html
> >     <p class="price"><span>$</span><strong>10</strong><small>/ Mo</small></p>
> > ```
> >
> > يفتح وسم `p` المستخدم بوصفه فقرة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 05 — `html`
> >
> > ```html
> >     <ul>
> > ```
> >
> > يفتح وسم `ul` المستخدم بوصفه قائمة غير مرتبة.
> >
> > #### السطر 06 — `html`
> >
> > ```html
> >       <li><strong>Free</strong> Weekly Meeting</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 07 — `html`
> >
> > ```html
> >       <li><strong>1x</strong> Monthly Call</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 08 — `html`
> >
> > ```html
> >       <li><strong>Unlimited</strong> Messenger Chats</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 09 — `html`
> >
> > ```html
> >       <li><strong>Free</strong> Control Panel Access</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 10 — `html`
> >
> > ```html
> >       <li><strong>1x</strong> Face to Face Meeting</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 11 — `html`
> >
> > ```html
> >     </ul>
> > ```
> >
> > يغلق وسم `ul` وينهي العنصر.
> >
> > #### السطر 12 — `html`
> >
> > ```html
> >     <button>Buy Now</button>
> > ```
> >
> > يفتح وسم `button` المستخدم بوصفه زر.
> >
> > #### السطر 13 — `html`
> >
> > ```html
> >   </article>
> > ```
> >
> > يغلق وسم `article` وينهي العنصر.
> >
> > #### السطر 14 — `html`
> >
> > ```html
> >   <article class="plan-card featured">
> > ```
> >
> > يفتح وسم `article` المستخدم بوصفه عنصر `HTML`.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 15 — `html`
> >
> > ```html
> >     <div class="ribbon">Most Popular</div>
> > ```
> >
> > يفتح وسم `div` المستخدم بوصفه حاوية عامة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 16 — `html`
> >
> > ```html
> >     <h3>Business</h3>
> > ```
> >
> > يفتح وسم `h3` المستخدم بوصفه عنوان فرعي.
> >
> > #### السطر 17 — `html`
> >
> > ```html
> >     <p class="price"><span>$</span><strong>15</strong><small>/ Mo</small></p>
> > ```
> >
> > يفتح وسم `p` المستخدم بوصفه فقرة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 18 — `html`
> >
> > ```html
> >     <ul>
> > ```
> >
> > يفتح وسم `ul` المستخدم بوصفه قائمة غير مرتبة.
> >
> > #### السطر 19 — `html`
> >
> > ```html
> >       <li><strong>Free</strong> Weekly Meeting</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 20 — `html`
> >
> > ```html
> >       <li><strong>2x</strong> Monthly Call</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 21 — `html`
> >
> > ```html
> >       <li><strong>Unlimited</strong> Messenger Chats</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 22 — `html`
> >
> > ```html
> >       <li><strong>Free</strong> Control Panel Access</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 23 — `html`
> >
> > ```html
> >       <li><strong>2x</strong> Face to Face Meeting</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 24 — `html`
> >
> > ```html
> >     </ul>
> > ```
> >
> > يغلق وسم `ul` وينهي العنصر.
> >
> > #### السطر 25 — `html`
> >
> > ```html
> >     <button>Buy Now</button>
> > ```
> >
> > يفتح وسم `button` المستخدم بوصفه زر.
> >
> > #### السطر 26 — `html`
> >
> > ```html
> >   </article>
> > ```
> >
> > يغلق وسم `article` وينهي العنصر.
> >
> > #### السطر 27 — `html`
> >
> > ```html
> >   <article class="plan-card">
> > ```
> >
> > يفتح وسم `article` المستخدم بوصفه عنصر `HTML`.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 28 — `html`
> >
> > ```html
> >     <h3>Enterprise</h3>
> > ```
> >
> > يفتح وسم `h3` المستخدم بوصفه عنوان فرعي.
> >
> > #### السطر 29 — `html`
> >
> > ```html
> >     <p class="price"><span>$</span><strong>20</strong><small>/ Mo</small></p>
> > ```
> >
> > يفتح وسم `p` المستخدم بوصفه فقرة.؛ `class` يربطه بصنف `CSS`.
> >
> > #### السطر 30 — `html`
> >
> > ```html
> >     <ul>
> > ```
> >
> > يفتح وسم `ul` المستخدم بوصفه قائمة غير مرتبة.
> >
> > #### السطر 31 — `html`
> >
> > ```html
> >       <li><strong>Free</strong> Daily Meeting</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 32 — `html`
> >
> > ```html
> >       <li><strong>3x</strong> Monthly Call</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 33 — `html`
> >
> > ```html
> >       <li><strong>Unlimited</strong> Messenger Chats</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 34 — `html`
> >
> > ```html
> >       <li><strong>Free</strong> Control Panel Access</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 35 — `html`
> >
> > ```html
> >       <li><strong>3x</strong> Face to Face Meeting</li>
> > ```
> >
> > يفتح وسم `li` المستخدم بوصفه عنصر قائمة.
> >
> > #### السطر 36 — `html`
> >
> > ```html
> >     </ul>
> > ```
> >
> > يغلق وسم `ul` وينهي العنصر.
> >
> > #### السطر 37 — `html`
> >
> > ```html
> >     <button>Buy Now</button>
> > ```
> >
> > يفتح وسم `button` المستخدم بوصفه زر.
> >
> > #### السطر 38 — `html`
> >
> > ```html
> >   </article>
> > ```
> >
> > يغلق وسم `article` وينهي العنصر.
> >
> > #### السطر 39 — `html`
> >
> > ```html
> > </div>
> > ```
> >
> > يغلق وسم `div` وينهي العنصر.
> >
> > #### السطر 40 — `css`
> >
> > ```css
> > * {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 41 — `css`
> >
> > ```css
> >   box-sizing: border-box;
> > ```
> >
> > تحدد حساب أبعاد الصندوق. والقيمة هنا `border-box`.
> >
> > #### السطر 42 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 43 — `css`
> >
> > ```css
> > body {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 44 — `css`
> >
> > ```css
> >   margin: 0;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0.
> >
> > #### السطر 45 — `css`
> >
> > ```css
> >   background-color: #eee;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#eee`.
> >
> > #### السطر 46 — `css`
> >
> > ```css
> >   font-family: Arial, sans-serif;
> > ```
> >
> > تحدد عائلة الخط. والقيمة هنا `Arial`, `sans-serif`.
> >
> > #### السطر 47 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 48 — `css`
> >
> > ```css
> > .plans {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 49 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 50 — `css`
> >
> > ```css
> >   grid-template-columns: repeat(3, minmax(0, 1fr));
> > ```
> >
> > تحدد أعمدة `Grid`. والقيمة هنا `repeat(3, minmax(0, 1fr)`).
> >
> > #### السطر 51 — `css`
> >
> > ```css
> >   gap: 20px;
> > ```
> >
> > تحدد المسافة بين عناصر التخطيط. والقيمة هنا `20px`.
> >
> > #### السطر 52 — `css`
> >
> > ```css
> >   max-width: 1200px;
> > ```
> >
> > تحدد أقصى عرض. والقيمة هنا `1200px`.
> >
> > #### السطر 53 — `css`
> >
> > ```css
> >   margin: 50px auto;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا `50px` `auto`.
> >
> > #### السطر 54 — `css`
> >
> > ```css
> >   padding: 0 16px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا 0 `16px`.
> >
> > #### السطر 55 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 56 — `css`
> >
> > ```css
> > .plan-card {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 57 — `css`
> >
> > ```css
> >   position: relative;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `relative`.
> >
> > #### السطر 58 — `css`
> >
> > ```css
> >   display: flex;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `flex`.
> >
> > #### السطر 59 — `css`
> >
> > ```css
> >   flex-direction: column;
> > ```
> >
> > تحدد اتجاه عناصر `Flex`. والقيمة هنا `column`.
> >
> > #### السطر 60 — `css`
> >
> > ```css
> >   align-items: center;
> > ```
> >
> > تحاذي العناصر عرضيًا. والقيمة هنا `center`.
> >
> > #### السطر 61 — `css`
> >
> > ```css
> >   min-height: 548px;
> > ```
> >
> > تحدد أقل ارتفاع. والقيمة هنا `548px`.
> >
> > #### السطر 62 — `css`
> >
> > ```css
> >   padding: 55px 18px 38px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `55px` `18px` `38px`.
> >
> > #### السطر 63 — `css`
> >
> > ```css
> >   border: 1px solid #ccc;
> > ```
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. والقيمة هنا `1px` `solid` `#ccc`.
> >
> > #### السطر 64 — `css`
> >
> > ```css
> >   background-color: #fff;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#fff`.
> >
> > #### السطر 65 — `css`
> >
> > ```css
> >   text-align: center;
> > ```
> >
> > تحاذي النص. والقيمة هنا `center`.
> >
> > #### السطر 66 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 67 — `css`
> >
> > ```css
> > .plan-card h3 {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 68 — `css`
> >
> > ```css
> >   margin: 0 0 30px;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0 0 `30px`.
> >
> > #### السطر 69 — `css`
> >
> > ```css
> >   font-size: 30px;
> > ```
> >
> > تحدد حجم النص. والقيمة هنا `30px`.
> >
> > #### السطر 70 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 71 — `css`
> >
> > ```css
> > .price {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 72 — `css`
> >
> > ```css
> >   display: flex;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `flex`.
> >
> > #### السطر 73 — `css`
> >
> > ```css
> >   align-items: baseline;
> > ```
> >
> > تحاذي العناصر عرضيًا. والقيمة هنا `baseline`.
> >
> > #### السطر 74 — `css`
> >
> > ```css
> >   gap: 2px;
> > ```
> >
> > تحدد المسافة بين عناصر التخطيط. والقيمة هنا `2px`.
> >
> > #### السطر 75 — `css`
> >
> > ```css
> >   margin: 0 0 30px;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0 0 `30px`.
> >
> > #### السطر 76 — `css`
> >
> > ```css
> >   color: #197beb;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#197beb`.
> >
> > #### السطر 77 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 78 — `css`
> >
> > ```css
> > .price span {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 79 — `css`
> >
> > ```css
> >   font-size: 30px;
> > ```
> >
> > تحدد حجم النص. والقيمة هنا `30px`.
> >
> > #### السطر 80 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 81 — `css`
> >
> > ```css
> > .price strong {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 82 — `css`
> >
> > ```css
> >   font-size: 50px;
> > ```
> >
> > تحدد حجم النص. والقيمة هنا `50px`.
> >
> > #### السطر 83 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 84 — `css`
> >
> > ```css
> > .price small {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 85 — `css`
> >
> > ```css
> >   color: #888;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#888`.
> >
> > #### السطر 86 — `css`
> >
> > ```css
> >   font-size: 16px;
> > ```
> >
> > تحدد حجم النص. والقيمة هنا `16px`.
> >
> > #### السطر 87 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 88 — `css`
> >
> > ```css
> > .plan-card ul {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 89 — `css`
> >
> > ```css
> >   display: grid;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `grid`.
> >
> > #### السطر 90 — `css`
> >
> > ```css
> >   gap: 22px;
> > ```
> >
> > تحدد المسافة بين عناصر التخطيط. والقيمة هنا `22px`.
> >
> > #### السطر 91 — `css`
> >
> > ```css
> >   width: 100%;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `100%`.
> >
> > #### السطر 92 — `css`
> >
> > ```css
> >   margin: 0;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0.
> >
> > #### السطر 93 — `css`
> >
> > ```css
> >   padding: 0;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا 0.
> >
> > #### السطر 94 — `css`
> >
> > ```css
> >   color: #888;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#888`.
> >
> > #### السطر 95 — `css`
> >
> > ```css
> >   list-style: none;
> > ```
> >
> > تحدد علامة القائمة. والقيمة هنا `none`.
> >
> > #### السطر 96 — `css`
> >
> > ```css
> >   font-size: 16px;
> > ```
> >
> > تحدد حجم النص. والقيمة هنا `16px`.
> >
> > #### السطر 97 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 98 — `css`
> >
> > ```css
> > .plan-card button {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 99 — `css`
> >
> > ```css
> >   width: 140px;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `140px`.
> >
> > #### السطر 100 — `css`
> >
> > ```css
> >   margin-top: auto;
> > ```
> >
> > تحدد قيمة الخاصية `margin-top`. والقيمة هنا `auto`.
> >
> > #### السطر 101 — `css`
> >
> > ```css
> >   padding: 18px 12px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `18px` `12px`.
> >
> > #### السطر 102 — `css`
> >
> > ```css
> >   border: 0;
> > ```
> >
> > ترسم الحد وتحدد سمكه ونمطه ولونه. والقيمة هنا 0.
> >
> > #### السطر 103 — `css`
> >
> > ```css
> >   border-radius: 32px;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `32px`.
> >
> > #### السطر 104 — `css`
> >
> > ```css
> >   background-color: #197beb;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#197beb`.
> >
> > #### السطر 105 — `css`
> >
> > ```css
> >   color: #fff;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#fff`.
> >
> > #### السطر 106 — `css`
> >
> > ```css
> >   font-weight: 700;
> > ```
> >
> > تحدد سُمك الخط. والقيمة هنا 700.
> >
> > #### السطر 107 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 108 — `css`
> >
> > ```css
> > .ribbon {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 109 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 110 — `css`
> >
> > ```css
> >   top: -21px;
> > ```
> >
> > تحدد المسافة من أعلى مرجع التموضع. والقيمة هنا -`21px`.
> >
> > #### السطر 111 — `css`
> >
> > ```css
> >   left: 10%;
> > ```
> >
> > تحدد المسافة من اليسار. والقيمة هنا `10%`.
> >
> > #### السطر 112 — `css`
> >
> > ```css
> >   width: 80%;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `80%`.
> >
> > #### السطر 113 — `css`
> >
> > ```css
> >   padding: 15px 8px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `15px` `8px`.
> >
> > #### السطر 114 — `css`
> >
> > ```css
> >   background-color: #197beb;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#197beb`.
> >
> > #### السطر 115 — `css`
> >
> > ```css
> >   color: #fff;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#fff`.
> >
> > #### السطر 116 — `css`
> >
> > ```css
> >   font-weight: 700;
> > ```
> >
> > تحدد سُمك الخط. والقيمة هنا 700.
> >
> > #### السطر 117 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 118 — `css`
> >
> > ```css
> > .ribbon::before {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 119 — `css`
> >
> > ```css
> >   position: absolute;
> > ```
> >
> > تحدد طريقة التموضع. والقيمة هنا `absolute`.
> >
> > #### السطر 120 — `css`
> >
> > ```css
> >   top: 0;
> > ```
> >
> > تحدد المسافة من أعلى مرجع التموضع. والقيمة هنا 0.
> >
> > #### السطر 121 — `css`
> >
> > ```css
> >   left: -18px;
> > ```
> >
> > تحدد المسافة من اليسار. والقيمة هنا -`18px`.
> >
> > #### السطر 122 — `css`
> >
> > ```css
> >   border-top: 21px solid #0e67cd;
> > ```
> >
> > تحدد قيمة الخاصية `border-top`. والقيمة هنا `21px` `solid` `#0e67cd`.
> >
> > #### السطر 123 — `css`
> >
> > ```css
> >   border-left: 18px solid transparent;
> > ```
> >
> > تحدد قيمة الخاصية `border-left`. والقيمة هنا `18px` `solid` `transparent`.
> >
> > #### السطر 124 — `css`
> >
> > ```css
> >   content: "";
> > ```
> >
> > تحدد محتوى العنصر الزائف. والقيمة هنا "".
> >
> > #### السطر 125 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-12.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/12 - All Course Assignment.html|افتح صفحة التكليف 12]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
