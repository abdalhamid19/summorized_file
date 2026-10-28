---
title: "CSS All Course Assignment 04"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 04
---

# CSS All Course Assignment 04

> [!question] المطلوب
> نسّق حقل الهاتف ليطابق الصورة، مع الإبقاء على HTML المعطى حرفيًا دون تعديل.
>
> ```html
> <div class="input-box">
>   <span class="prefix">+20</span>
>   <input type="tel" placeholder="1011001100" />
> </div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-04-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> * {
>   box-sizing: border-box;
> }
>
> body {
>   min-height: 100vh;
>   margin: 0;
>   display: grid;
>   place-items: center;
>   background: #eee;
>   font-family: Arial, sans-serif;
> }
>
> .input-box {
>   display: flex;
>   width: min(900px, calc(100% - 32px));
>   height: 110px;
>   overflow: hidden;
>   border: 3px solid #ddd;
>   border-radius: 12px;
>   background: #fff;
> }
>
> .prefix {
>   flex: 0 0 130px;
>   display: grid;
>   place-items: center;
>   color: #fff;
>   background: #009688;
>   font-size: 42px;
> }
>
> .input-box input {
>   flex: 1;
>   min-width: 0;
>   border: 0;
>   border-left: 1px solid #009688;
>   outline: 0;
>   padding: 0 28px;
>   font-size: 40px;
> }
>
> .input-box input::placeholder {
>   color: #757575;
>   opacity: 1;
> }
> ```
>
> ### `Flexbox`
>
> الحاوية `display: flex` تضع البادئة والحقل جنبًا إلى جنب، ويملأ الحقل المساحة الباقية بفضل `flex: 1`.
>
> ### `box-sizing`
>
> القيمة `border-box` تجعل العرض والارتفاع يشملان الحدود، فتظل أبعاد الحقل متوقعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-04-solution.png]]

المعاينة: [04 - All Course Assignment.html](04%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
