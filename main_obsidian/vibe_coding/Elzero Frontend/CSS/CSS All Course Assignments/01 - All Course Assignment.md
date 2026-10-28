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
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-01-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
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
> ### `CSS custom property`
>
> المتغير `--line-size` يحفظ سُمك الخط. غيّر قيمة واحدة لتعديل كل الحدود والخطوط معًا.
>
> ### `pseudo-element`
>
> العنصر الوهمي `::before` يرسم الخطين الأزرق والأخضر حول العنصر من دون إضافة أو تعديل أي HTML.
>
> ### `outline`
>
> الخاصية `outline` ترسم الخط الأسود خارج الحد، لذلك لا نحتاج إلى `box-shadow` الممنوع في السؤال.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-01-solution.png]]

المعاينة: [01 - All Course Assignment.html](01%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
