---
title: "CSS All Course Assignment 08"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 08
---

# CSS All Course Assignment 08

> [!question] المطلوب
> أنشئ البطاقات الظاهرة في الصورة من روابط فارغة؛ لا تعدّل HTML، واستخرج النص المعروض من الخصائص الموجودة في الرابط.
>
> ```html
> <a class="url" href="https://google.com" title="Google"></a>
> <a class="link" href="https://elzero.org/" title="Elzero Academy"></a>
> <a href="https://www.elzero.courses/" title="Elzero Courses"></a>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-08-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body {
>   margin: 0;
>   padding: 21px 16px 16px;
>   background: #eee;
>   font-family: Arial, sans-serif;
> }
>
> a {
>   display: block;
>   width: max-content;
>   max-width: 100%;
>   margin-bottom: 20px;
>   padding: 19px 20px;
>   box-sizing: border-box;
>   border-radius: 12px;
>   color: #fff;
>   background: #2196f3;
>   font: 700 32px/1.2 Arial, sans-serif;
>   text-decoration: none;
> }
>
> a::before {
>   content: "Name: " attr(title) " | URL: " attr(href);
> }
> ```
>
> ### الفكرة الأساسية
>
> العنصر الوهمي `::before` يضيف نصًا قبل محتوى الرابط. الدالة `attr(title)` تقرأ اسم الموقع من الخاصية `title`، و`attr(href)` تقرأ عنوانه؛ وهكذا تظهر البطاقات رغم أن الروابط لا تحتوي على نص داخل `HTML`.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `body`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `a`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `a::before`
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > ### خصائص CSS
> >
> > #### `margin`
> >
> > تضيف مسافة خارجية. مثال القيمة: 0
> >
> > #### `padding`
> >
> > تضيف مساحة داخلية. مثال القيمة: `21px` `16px` `16px`
> >
> > #### `background`
> >
> > تضبط الخلفية. مثال القيمة: `#eee`
> >
> > #### `font-family`
> >
> > تحدد عائلة الخط. مثال القيمة: `Arial`, `sans-serif`
> >
> > #### `display`
> >
> > تحدد طريقة عرض العنصر. مثال القيمة: `block`
> >
> > #### `width`
> >
> > تحدد عرض العنصر. مثال القيمة: `max-content`
> >
> > #### `max-width`
> >
> > تحدد أقصى عرض. مثال القيمة: `100%`
> >
> > #### `margin-bottom`
> >
> > تحدد قيمة الخاصية `margin-bottom`. مثال القيمة: `20px`
> >
> > #### `box-sizing`
> >
> > تحدد حساب أبعاد الصندوق. مثال القيمة: `border-box`
> >
> > #### `border-radius`
> >
> > تدوّر زوايا العنصر. مثال القيمة: `12px`
> >
> > #### `color`
> >
> > تحدد لون النص. مثال القيمة: `#fff`
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: 700 `32px`/1.2 `Arial`, `sans-serif`
> >
> > #### `text-decoration`
> >
> > تضيف أو تزيل خطًا زخرفيًا. مثال القيمة: `none`
> >
> > #### `a`
> >
> > تحدد قيمة الخاصية `a`. مثال القيمة: `:before` {
> >
> > #### `content`
> >
> > تحدد محتوى العنصر الزائف. مثال القيمة: "`Name`: " `attr(title)` " | `URL`: " `attr(href)`
> >
> > ### الدوال والوحدات
> >
> > #### `attr()`
> >
> > تقرأ قيمة خاصية `HTML` لاستخدامها في محتوى `CSS`.
> >
> > #### `attr()`
> >
> > تقرأ قيمة خاصية `HTML` لاستخدامها في محتوى `CSS`.
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
> > body {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> >   margin: 0;
> > ```
> >
> > تضيف مسافة خارجية. والقيمة هنا 0.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> >   padding: 21px 16px 16px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `21px` `16px` `16px`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> >   background: #eee;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#eee`.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> >   font-family: Arial, sans-serif;
> > ```
> >
> > تحدد عائلة الخط. والقيمة هنا `Arial`, `sans-serif`.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> > a {
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> >   display: block;
> > ```
> >
> > تحدد طريقة عرض العنصر. والقيمة هنا `block`.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   width: max-content;
> > ```
> >
> > تحدد عرض العنصر. والقيمة هنا `max-content`.
> >
> > #### السطر 10 — `css`
> >
> > ```css
> >   max-width: 100%;
> > ```
> >
> > تحدد أقصى عرض. والقيمة هنا `100%`.
> >
> > #### السطر 11 — `css`
> >
> > ```css
> >   margin-bottom: 20px;
> > ```
> >
> > تحدد قيمة الخاصية `margin-bottom`. والقيمة هنا `20px`.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> >   padding: 19px 20px;
> > ```
> >
> > تضيف مساحة داخلية. والقيمة هنا `19px` `20px`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> >   box-sizing: border-box;
> > ```
> >
> > تحدد حساب أبعاد الصندوق. والقيمة هنا `border-box`.
> >
> > #### السطر 14 — `css`
> >
> > ```css
> >   border-radius: 12px;
> > ```
> >
> > تدوّر زوايا العنصر. والقيمة هنا `12px`.
> >
> > #### السطر 15 — `css`
> >
> > ```css
> >   color: #fff;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `#fff`.
> >
> > #### السطر 16 — `css`
> >
> > ```css
> >   background: #2196f3;
> > ```
> >
> > تضبط الخلفية. والقيمة هنا `#2196f3`.
> >
> > #### السطر 17 — `css`
> >
> > ```css
> >   font: 700 32px/1.2 Arial, sans-serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا 700 `32px`/1.2 `Arial`, `sans-serif`.
> >
> > #### السطر 18 — `css`
> >
> > ```css
> >   text-decoration: none;
> > ```
> >
> > تضيف أو تزيل خطًا زخرفيًا. والقيمة هنا `none`.
> >
> > #### السطر 19 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 20 — `css`
> >
> > ```css
> > a::before {
> > ```
> >
> > ينشئ عنصرًا زائفًا لتنسيقه من دون إضافة وسم جديد إلى `HTML`.
> >
> > #### السطر 21 — `css`
> >
> > ```css
> >   content: "Name: " attr(title) " | URL: " attr(href);
> > ```
> >
> > تحدد محتوى العنصر الزائف. والقيمة هنا "`Name`: " `attr(title)` " | `URL`: " `attr(href)`.
> >
> > #### السطر 22 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-08.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/08 - All Course Assignment.html|افتح صفحة التكليف 08]]

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
