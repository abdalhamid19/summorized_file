---
title: "All Course Assignment 10 — Checkerboard"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 10"
---

# 10 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل رقعة الشطرنج كما في الصورة.
>
> ```html
> <div class="container">
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
>   <div class="black"></div>
>   <div class="white"></div>
> </div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-10-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> **CSS**
>
> ```css
> * {
>   box-sizing: border-box;
> }
>
> .container {
>   display: grid;
>   grid-template-columns: repeat(8, 1fr);
>   width: min(100%, 810px);
>   aspect-ratio: 1;
>   border: 5px solid #000;
> }
>
> .white {
>   background-color: #fff;
> }
>
> .black {
>   background-color: #000;
> }
> ```
> **شرح الحل**
> ينشئ `display: grid` شبكة من ثمانية أعمدة متساوية. يحدد `aspect-ratio: 1` شكلًا مربعًا، وترتيب عناصر HTML الثمانية والستين يوزع الأبيض والأسود على الصفوف بالتناوب.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-10-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
