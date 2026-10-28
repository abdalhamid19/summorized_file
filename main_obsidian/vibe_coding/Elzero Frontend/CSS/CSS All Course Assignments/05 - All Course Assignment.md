---
title: "CSS All Course Assignment 05"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 05
---

# CSS All Course Assignment 05

> [!question] المطلوب — تحدي
> حوّل الخطوط الثلاثة إلى أيقونة قائمة متحركة كما في المرجع، مع عدم تعديل HTML.
>
> ```html
> <div class="menu">
>   <span></span>
>   <span></span>
>   <span></span>
> </div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-05-reference.gif]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> body {
>   min-height: 100vh;
>   margin: 0;
>   display: grid;
>   place-items: center;
>   background: #eee;
> }
>
> .menu {
>   position: relative;
>   width: 180px;
>   height: 138px;
>   cursor: pointer;
> }
>
> .menu span {
>   position: absolute;
>   left: 0;
>   width: 180px;
>   height: 30px;
>   border-radius: 20px;
>   background: #000;
>   transition: top 0.4s ease, transform 0.4s ease, background-color 0.4s ease, opacity 0.3s ease;
> }
>
> .menu span:nth-child(1) {
>   top: 0;
> }
>
> .menu span:nth-child(2) {
>   top: 54px;
> }
>
> .menu span:nth-child(3) {
>   top: 108px;
> }
>
> .menu:hover span:nth-child(1) {
>   top: 54px;
>   transform: rotate(45deg);
>   background: #f00;
> }
>
> .menu:hover span:nth-child(2) {
>   opacity: 0;
>   transform: scaleX(0);
> }
>
> .menu:hover span:nth-child(3) {
>   top: 54px;
>   transform: rotate(-45deg);
>   background: #f00;
> }
> ```
>
> المحدد `:hover` (حالة مرور المؤشر) يغيّر ترتيب الخطين الخارجيين ويديرهما، بينما يخفي الخط الأوسط. وتنعّم `transition` (انتقال الحركة) التبديل بين شكل القائمة وعلامة X الحمراء.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-05-solution.png]]
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-05-menu.png]]

افتح المعاينة ومرّر المؤشر فوق الأيقونة لمشاهدة الحركة: [05 - All Course Assignment.html](05%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
