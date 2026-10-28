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
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-12-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> نستخدم بنية HTML مناسبة لأن المصدر لم يفرض بنية ثابتة:
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
> **شرح الحل**
> توزع `CSS Grid` البطاقات على ثلاثة أعمدة. تضع `flex-direction: column` عناصر كل بطاقة عموديًا، وتدفع `margin-top: auto` الزر إلى أسفلها. يرسم `::before` طرف الشريط الأزرق المائل من دون عنصر HTML إضافي.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-12-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
