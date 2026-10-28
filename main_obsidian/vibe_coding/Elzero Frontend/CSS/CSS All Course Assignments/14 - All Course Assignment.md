---
title: "All Course Assignment 14 — CSS Camera"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 14"
---

# 14 - All Course Assignment

> [!question] المطلوب
> تحدي: ارسم الشكل المعروض بنفسك مع استخدام الألوان نفسها. الفكرة مستوحاة من CodePen مع تعديلات.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-14-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> نستخدم بنية HTML مناسبة لأن المصدر لم يفرض بنية ثابتة:
> ```html
> <div class="camera" aria-label="CSS illustration of a camera">
>   <div class="camera__viewfinder">
>     <span class="camera__window"><span class="camera__screen"></span></span>
>   </div>
>   <span class="camera__shutter"></span>
>   <span class="camera__button"></span>
>   <div class="camera__body">
>     <div class="camera__lens">
>       <div class="camera__ring">
>         <div class="camera__glass"><span class="camera__glare"></span></div>
>       </div>
>     </div>
>   </div>
> </div>
> ```
> **CSS**
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
> .camera {
>   position: relative;
>   width: min(100%, 600px);
>   height: 460px;
>   margin: 60px auto 0;
> }
>
> .camera__body {
>   position: absolute;
>   inset: 60px 0 0;
>   border-radius: 20px;
>   background: linear-gradient(to bottom, #ccc 0 25%, #607d8b 25% 75%, #ccc 75% 100%);
> }
>
> .camera__viewfinder {
>   position: absolute;
>   z-index: 2;
>   top: 0;
>   left: calc(50% - 97px);
>   width: 194px;
>   height: 60px;
>   border-radius: 24px 24px 0 0;
>   background-color: #607d8b;
>   clip-path: polygon(14% 0, 86% 0, 100% 100%, 0 100%);
> }
>
> .camera__window {
>   position: absolute;
>   top: 14px;
>   left: 37px;
>   display: grid;
>   width: 120px;
>   height: 30px;
>   place-items: center;
>   border-radius: 10px;
>   background-color: #ccc;
> }
>
> .camera__screen {
>   width: 40px;
>   height: 15px;
>   border-radius: 3px;
>   background-color: #607d8b;
> }
>
> .camera__shutter {
>   position: absolute;
>   z-index: 3;
>   top: 38px;
>   left: 30px;
>   width: 80px;
>   height: 22px;
>   border-radius: 18px 18px 0 0;
>   background-color: #607d8b;
> }
>
> .camera__button {
>   position: absolute;
>   z-index: 4;
>   top: 37px;
>   left: 42px;
>   width: 57px;
>   height: 22px;
>   border-radius: 4px 4px 0 0;
>   background-color: #e91e63;
> }
>
> .camera__lens {
>   position: absolute;
>   z-index: 5;
>   top: 42px;
>   left: 50%;
>   display: grid;
>   width: 315px;
>   height: 315px;
>   transform: translateX(-50%);
>   place-items: center;
>   border: 20px solid #eee;
>   border-radius: 50%;
>   background-color: #ccc;
>   box-shadow: 0 4px 16px #0006;
> }
>
> .camera__ring {
>   display: grid;
>   width: 100%;
>   height: 100%;
>   place-items: center;
>   border-radius: 50%;
>   background-color: #3e3e3e;
> }
>
> .camera__glass {
>   position: relative;
>   width: 150px;
>   height: 150px;
>   border-radius: 50%;
>   background-color: #358fb6;
> }
>
> .camera__glare {
>   position: absolute;
>   top: 20px;
>   left: 20px;
>   width: 40px;
>   height: 40px;
>   border-radius: 50%;
>   background-color: #75c2df;
> }
> ```
> **شرح الحل**
> ترسم العناصر المتداخلة جسم الكاميرا والعدسة بطبقات دائرية. تصنع `border-radius` الدوائر، ويقص `clip-path` جوانب محدد المنظر إلى شكل شبه منحرف. يضع `linear-gradient` الشريط الأفقي على جسم الكاميرا.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-14-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
