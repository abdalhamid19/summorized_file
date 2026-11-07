---
title: "All Course Assignment 09 — Gradient Text"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 09"
---

# 09 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل الشكل كما في الصورة. يمكنك اختيار لونين مختلفين.
>
> ```html
> <div class="text">elzero web school</div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/assignment-09-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body {
>   margin: 0;
>   background-color: #eee;
> }
>
> .text {
>   color: transparent;
>   font: 700 clamp(24px, 4.1vw, 68px) / 1 Arial, sans-serif;
>   white-space: nowrap;
>   text-align: center;
>   text-transform: capitalize;
>   background-image: linear-gradient(to bottom, #f0440a, #bd8c0e);
>   -webkit-background-clip: text;
>   background-clip: text;
> }
> ```
>
> ### الفكرة الأساسية
>
> تجعل الخاصية `text-transform: capitalize` بداية كل كلمة حرفًا كبيرًا. تنشئ `linear-gradient` تدرجًا بين اللونين. تجعل `background-clip: text` التدرج ظاهرًا داخل شكل الحروف، لذلك نجعل لون النص شفافًا.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### محددات CSS
> >
> > #### `body`
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`.
> >
> > #### `.text`
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > ### خصائص CSS
> >
> > #### `margin`
> >
> > تضيف مسافة خارجية. مثال القيمة: 0
> >
> > #### `background-color`
> >
> > تحدد لون الخلفية. مثال القيمة: `#eee`
> >
> > #### `color`
> >
> > تحدد لون النص. مثال القيمة: `transparent`
> >
> > #### `font`
> >
> > تجمع إعدادات الخط. مثال القيمة: 700 `clamp(24px, 4.1vw, 68px)` / 1 `Arial`, `sans-serif`
> >
> > #### `white-space`
> >
> > تحدد التفاف النص والمسافات. مثال القيمة: `nowrap`
> >
> > #### `text-align`
> >
> > تحاذي النص. مثال القيمة: `center`
> >
> > #### `text-transform`
> >
> > تغيّر شكل الحروف الظاهر. مثال القيمة: `capitalize`
> >
> > #### `background-image`
> >
> > تحدد صورة أو تدرج الخلفية. مثال القيمة: `linear-gradient(to bottom, #f0440a, #bd8c0e)`
> >
> > #### `-webkit-background-clip`
> >
> > تحدد قيمة الخاصية -`webkit-background-clip`. مثال القيمة: `text`
> >
> > #### `background-clip`
> >
> > تحدد قيمة الخاصية `background-clip`. مثال القيمة: `text`
> >
> > ### الدوال والوحدات
> >
> > #### `clamp()`
> >
> > تحصر القيمة بين حد أدنى وقيمة مفضلة وحد أقصى.
> >
> > #### `linear-gradient()`
> >
> > تنشئ تدرجًا لونيًا يسير في اتجاه خطي.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > #### `vw`
> >
> > نسبة من عرض نافذة العرض.
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
> >   background-color: #eee;
> > ```
> >
> > تحدد لون الخلفية. والقيمة هنا `#eee`.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > }
> > ```
> >
> > يغلق نطاق القاعدة التي بدأها المحدد.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> > .text {
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> >   color: transparent;
> > ```
> >
> > تحدد لون النص. والقيمة هنا `transparent`.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> >   font: 700 clamp(24px, 4.1vw, 68px) / 1 Arial, sans-serif;
> > ```
> >
> > تجمع إعدادات الخط. والقيمة هنا 700 `clamp(24px, 4.1vw, 68px)` / 1 `Arial`, `sans-serif`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> >   white-space: nowrap;
> > ```
> >
> > تحدد التفاف النص والمسافات. والقيمة هنا `nowrap`.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> >   text-align: center;
> > ```
> >
> > تحاذي النص. والقيمة هنا `center`.
> >
> > #### السطر 10 — `css`
> >
> > ```css
> >   text-transform: capitalize;
> > ```
> >
> > تغيّر شكل الحروف الظاهر. والقيمة هنا `capitalize`.
> >
> > #### السطر 11 — `css`
> >
> > ```css
> >   background-image: linear-gradient(to bottom, #f0440a, #bd8c0e);
> > ```
> >
> > تحدد صورة أو تدرج الخلفية. والقيمة هنا `linear-gradient(to bottom, #f0440a, #bd8c0e)`.
> >
> > #### السطر 12 — `css`
> >
> > ```css
> >   -webkit-background-clip: text;
> > ```
> >
> > تحدد قيمة الخاصية -`webkit-background-clip`. والقيمة هنا `text`.
> >
> > #### السطر 13 — `css`
> >
> > ```css
> >   background-clip: text;
> > ```
> >
> > تحدد قيمة الخاصية `background-clip`. والقيمة هنا `text`.
> >
> > #### السطر 14 — `css`
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
> ![[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/assets/solution-page-task-09.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/21 - CSS All Course Assignments/09 - All Course Assignment.html|افتح صفحة التكليف 09]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
