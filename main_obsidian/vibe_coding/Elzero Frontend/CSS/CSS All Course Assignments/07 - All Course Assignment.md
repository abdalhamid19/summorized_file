---
title: "CSS All Course Assignment 07"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 07
---

# CSS All Course Assignment 07

> [!question] المطلوب — تحدي
> نسّق القائمة المرقّمة وعناصرها الفرعية لتطابق الصورة، مع الحفاظ على HTML كما هو.
>
> ```html
> <ul>
>   <li>List item</li>
>   <li>List item</li>
>   <li>List item</li>
>   <li>
>     List item
>     <ul>
>       <li>Sub List item</li>
>       <li>Sub List item</li>
>       <li>Sub List item</li>
>     </ul>
>   </li>
> </ul>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-07-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> * {
>   box-sizing: border-box;
> }
>
> body {
>   margin: 0;
>   padding: 13px 18px 18px;
>   background: #eee;
>   color: #000;
>   font: 28px/1.2 Arial, sans-serif;
> }
>
> body > ul {
>   margin: 0;
>   padding: 0;
>   list-style: none;
>   counter-reset: main-item;
> }
>
> body > ul > li {
>   min-height: 80px;
>   margin-bottom: 10px;
>   padding: 10px;
>   background: #fff;
>   line-height: 60px;
>   counter-increment: main-item;
> }
>
> body > ul > li::before {
>   content: counter(main-item);
>   display: inline-flex;
>   align-items: center;
>   justify-content: center;
>   width: 60px;
>   height: 60px;
>   margin-right: 20px;
>   background: #ddd;
>   font-weight: 700;
>   vertical-align: top;
>   line-height: 1;
> }
>
> body > ul > li:nth-child(4) {
>   padding-bottom: 40px;
>   background: #ddd;
> }
>
> body > ul > li:nth-child(4)::before {
>   background: #fff;
> }
>
> body > ul > li > ul {
>   margin: 30px 0 0 30px;
>   padding: 0;
>   list-style: none;
>   counter-reset: sub-item;
> }
>
> body > ul > li > ul > li {
>   height: 80px;
>   margin: 10px 0;
>   padding: 10px;
>   background: #fff;
>   line-height: 60px;
>   counter-increment: sub-item;
> }
>
> body > ul > li > ul > li::before {
>   content: counter(main-item) "." counter(sub-item);
>   display: inline-flex;
>   align-items: center;
>   justify-content: center;
>   width: 60px;
>   height: 60px;
>   margin-right: 20px;
>   color: #fff;
>   background: #009688;
>   font-weight: 700;
>   vertical-align: top;
>   line-height: 1;
> }
> ```
>
> خاصية `counter-reset` تبدأ العدّاد، و`counter-increment` تزيده لكل عنصر. وتضيف `::before` (عنصرًا وهميًا) رقمًا قبل النص من دون إدخال أرقام أو تغيير بنية HTML. العدّاد `main-item` يعطي رقم العنصر الأب، و`sub-item` يكوّن الأرقام مثل `4.1` و`4.2` و`4.3`.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-07-solution.png]]

المعاينة: [07 - All Course Assignment.html](07%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
