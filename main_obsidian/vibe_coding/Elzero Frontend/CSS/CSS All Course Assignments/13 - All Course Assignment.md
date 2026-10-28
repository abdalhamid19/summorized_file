---
title: "All Course Assignment 13 — Active Storage Plan"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 13"
---

# 13 - All Course Assignment

> [!question] المطلوب
> أنشئ الشكل المعروض مع استخدام الألوان نفسها. البطاقة الأولى نشطة، ويظهر الشكل النشط نفسه عند تمرير المؤشر على أي بطاقة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-13-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> نستخدم بنية HTML مناسبة لأن المصدر لم يفرض بنية ثابتة:
> ```html
> <div class="capacity-grid">
>   <article class="capacity-card active">
>     <span class="indicator" aria-hidden="true"></span>
>     <h3>Standard</h3>
>     <p class="capacity"><strong>1</strong> <b>TB</b> <small>(1000gb)</small></p>
>     <p class="rate"><strong>$40</strong>/month</p>
>   </article>
>   <article class="capacity-card">
>     <span class="indicator" aria-hidden="true"></span>
>     <h3>Pro</h3>
>     <p class="capacity"><strong>2</strong> <b>TB</b> <small>(2000gb)</small></p>
>     <p class="rate"><strong>$70</strong>/month</p>
>   </article>
>   <article class="capacity-card">
>     <span class="indicator" aria-hidden="true"></span>
>     <h3>Ultimate</h3>
>     <p class="capacity"><strong>5</strong> <b>TB</b> <small>(5000gb)</small></p>
>     <p class="rate"><strong>$100</strong>/month</p>
>   </article>
> </div>
> ```
> **CSS**
>
> ```css
> * {
>   box-sizing: border-box;
> }
>
> .capacity-grid {
>   display: grid;
>   grid-template-columns: repeat(3, minmax(0, 1fr));
>   gap: 28px;
>   max-width: 860px;
>   margin: 25px auto;
>   font-family: Arial, sans-serif;
> }
>
> .capacity-card {
>   position: relative;
>   min-height: 170px;
>   padding: 20px;
>   border: 2px solid transparent;
>   border-radius: 12px;
>   background-color: #fff;
>   box-shadow: 0 7px 17px #0003;
>   color: #555;
> }
>
> .capacity-card.active,
> .capacity-card:hover {
>   border-color: #3171ff;
> }
>
> .indicator {
>   position: absolute;
>   top: 16px;
>   right: 16px;
>   width: 20px;
>   height: 20px;
>   border-radius: 50%;
>   background-color: #ccc;
> }
>
> .capacity-card.active .indicator,
> .capacity-card:hover .indicator {
>   background-color: #3171ff;
> }
>
> .capacity-card h3 {
>   margin: 0 0 12px;
>   font-size: 18px;
> }
>
> .capacity {
>   margin: 0 0 10px;
> }
>
> .capacity strong {
>   font-size: 48px;
> }
>
> .capacity b {
>   font-size: 28px;
> }
>
> .capacity small {
>   color: #888;
>   font-size: 16px;
> }
>
> .rate {
>   margin: 0;
>   font-size: 16px;
> }
>
> .rate strong {
>   font-size: 18px;
> }
> ```
> **شرح الحل**
> تمثل `active` البطاقة المختارة. تجمع قاعدة `:hover` مع `active` حتى يحصل الخيار الممرر عليه المؤشر على الإطار والدائرة الزرقاوين نفسيهما. تمثل `indicator` الدائرة في HTML.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-13-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
