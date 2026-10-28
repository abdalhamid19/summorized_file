---
title: "All Course Assignment 11 — Table Hover Row and Column"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 11"
---

# 11 - All Course Assignment

> [!question] المطلوب
> المطلوب إنشاء الجدول المعروض. عند تمرير المؤشر على أي خلية يتغير لون خلفية الصف والعمود كاملين ما عدا رأس الجدول، ويتغير أيضًا إطار الخلية التي عليها المؤشر. استخدم بنية الجدول المعطاة.
>
> ```html
> <table>
>   <tr>
>     <th>Language</th>
>     <th>Created By</th>
>     <th>Created Year</th>
>   </tr>
>   <tr>
>     <td>Python</td>
>     <td>Guido van Rossum</td>
>     <td>1991</td>
>   </tr>
>   <tr>
>     <td>Java</td>
>     <td>James Gosling</td>
>     <td>1995</td>
>   </tr>
>   <tr>
>     <td>JavaScript</td>
>     <td>Brendan Eich</td>
>     <td>1995</td>
>   </tr>
>   <tr>
>     <td>PHP</td>
>     <td>Rasmus Lerdorf</td>
>     <td>1995</td>
>   </tr>
>   <tr>
>     <td>Swift</td>
>     <td>Chris Lattner</td>
>     <td>2014</td>
>   </tr>
> </table>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-11-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> **CSS**
>
> ```css
> table {
>   width: min(100%, 600px);
>   margin: 24px auto;
>   border-spacing: 2px;
>   table-layout: fixed;
>   color: #111;
>   font: 16px Arial, sans-serif;
> }
>
> th,
> td {
>   padding: 18px 10px;
>   border: 1px solid #ccc;
>   text-align: center;
> }
>
> tr:not(:first-child):has(td:hover) > td {
>   background-color: #f4f4f4;
> }
>
> table:has(tr:not(:first-child) > td:nth-child(1):hover) tr:not(:first-child) > td:nth-child(1),
> table:has(tr:not(:first-child) > td:nth-child(2):hover) tr:not(:first-child) > td:nth-child(2),
> table:has(tr:not(:first-child) > td:nth-child(3):hover) tr:not(:first-child) > td:nth-child(3) {
>   background-color: #f4f4f4;
> }
>
> td:hover {
>   border-color: #2196f3;
>   color: #2196f3;
> }
> ```
> **شرح الحل**
> تغير `:hover` الخلية التي عليها المؤشر. تختار `:has()` الصف أو الجدول الذي يحتوي على خلية تمرير، وتختار `nth-child()` العمود المطلوب. يستبعد `:not(:first-child)` صف العناوين من التلوين. هذه الطريقة تستخدم محدد `:has()` المدعوم في المتصفحات الحديثة.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-11-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
