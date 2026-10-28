---
title: "CSS All Course Assignment 06"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 06
---

# CSS All Course Assignment 06

> [!question] المطلوب
> لوّن الرابط الذي لا يحمل `class`، حتى لو تغيّر ترتيبه بين الروابط. لا تستخدم محددات المواقع مثل `:last-child` ولا تستعمل أسماء `class` في محدد CSS.
>
> ```html
> <a class="url" href="https://google.com">Google</a>
> <a class="link" href="https://elzero.org/">Elzero Academy</a>
> <a href="https://www.elzero.courses/">Elzero Courses</a>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-06-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> body {
>   min-height: 100vh;
>   margin: 0;
>   padding: 0 20px;
>   display: flex;
>   align-items: center;
>   gap: 10px;
>   background: #eee;
>   font: 42px/1.2 "Times New Roman", serif;
> }
>
> a {
>   color: #000;
>   text-decoration: none;
> }
>
> a:not([class]) {
>   color: #ff3b30;
>   font-weight: 700;
> }
> ```
>
> المحدد `:not([class])` يختار رابطًا لا يحمل خاصية `class`، لذلك يبقى الاختيار صحيحًا حتى عند نقل الرابط. لا نعتمد على ترتيبه ولا نكتب أسماء `class` مثل `.url` أو `.link`.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-06-solution.png]]

المعاينة: [06 - All Course Assignment.html](06%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
