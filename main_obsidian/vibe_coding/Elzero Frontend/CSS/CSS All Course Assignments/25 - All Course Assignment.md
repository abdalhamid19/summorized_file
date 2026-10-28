---
title: 25 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 25
---

# 25 — CSS Login Card

> [!question] السؤال الرسمي
> اعمل الشكل المطلوب كما في الصورة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-25-reference.jpg]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```html
> <div class="login-card">
>   <h1 class="login-title">Login</h1>
>   <div class="login-content">
>     <form class="login-form">
>       <label for="login-email">Email</label>
>       <input id="login-email" type="email" autocomplete="off">
>       <label for="login-password">Password</label>
>       <input id="login-password" type="password" autocomplete="off">
>       <button class="login-button" type="button">Login</button>
>     </form>
>     <div class="social">
>       <h3>Connect</h3>
>       <button class="facebook" type="button">Facebook</button>
>       <button class="twitter" type="button">Twitter</button>
>       <button class="linkedin" type="button">Linkedin</button>
>     </div>
>     <span class="or">Or</span>
>   </div>
> </div>
> ```
>
> ```css
> .login-card {
>   overflow: hidden;
>   border-radius: 10px;
>   background: #fff;
> }
>
> .login-title {
>   height: 102px;
>   margin: 0;
>   display: grid;
>   place-items: center;
>   color: #fff;
>   background: #1479ed;
>   font-size: 36px;
> }
>
> .login-content {
>   position: relative;
>   padding: 28px 30px 30px;
>   display: grid;
>   grid-template-columns: 1fr 1fr;
>   gap: 80px;
> }
>
> .login-content::before {
>   content: "";
>   position: absolute;
>   top: 35px;
>   bottom: 35px;
>   left: 50%;
>   border-left: 1px solid #eee;
> }
>
> .login-form label {
>   display: block;
>   margin: 0 0 14px;
>   color: #777;
>   font-size: 22px;
> }
>
> .login-form input {
>   width: 100%;
>   height: 55px;
>   margin: 0 0 28px;
>   padding: 10px 14px;
>   border: 1px solid #ddd;
>   border-radius: 10px;
>   background: #fcfcfc;
> }
>
> .login-content button {
>   width: 100%;
>   height: 57px;
>   border: 0;
>   border-radius: 10px;
>   color: #fff;
>   font: 20px Arial, sans-serif;
> }
>
> .login-button { background: #0879ef; }
> .facebook { background: #1877f2; }
> .twitter { background: #25a5e8; }
> .linkedin { background: #087eae; }
>
> .social h3 {
>   margin: 0 0 26px;
>   color: #777;
>   text-align: center;
>   font-size: 22px;
>   font-weight: 400;
> }
>
> .social button { margin-bottom: 17px; }
>
> .or {
>   position: absolute;
>   top: 58%;
>   left: 50%;
>   padding: 6px 9px;
>   color: #777;
>   background: #fff;
>   font-size: 20px;
>   transform: translate(-50%, -50%);
> }
> ```
>
> يقسم `grid-template-columns` المحتوى إلى عمودين: نموذج الدخول يسارًا وأزرار الربط يمينًا. يرسم `::before` الفاصل العمودي، وتغطي كلمة `Or` وسطه بخلفية بيضاء.
>
> الحقول والأزرار عناصر شكلية في هذه المعاينة، ولا يرسل الزر البيانات إلى خدمة خارجية.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-25.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
