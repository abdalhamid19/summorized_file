---
title: "All Course Assignment 16 — Company Data Table"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 16"
---

# 16 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل الجدول كما في الصورة.
>
> ```html
> <table>
>   <caption>
>     Company Data
>   </caption>
>   <tfoot>
>     <tr>
>       <td colspan="3">Total</td>
>       <td>600</td>
>       <td>600</td>
>       <td>600</td>
>     </tr>
>   </tfoot>
>   <thead>
>     <tr>
>       <th>Company</th>
>       <th>Contact</th>
>       <th>Country</th>
>       <th>Revenue</th>
>       <th>Cost</th>
>       <th>Profit</th>
>     </tr>
>   </thead>
>   <tbody>
>     <tr>
>       <td>Alfreds Futterkiste</td>
>       <td>Maria Anders</td>
>       <td>Germany</td>
>       <td>100</td>
>       <td>100</td>
>       <td>100</td>
>     </tr>
>     <tr>
>       <td>Centro comercial Moctezuma</td>
>       <td>Francisco Chang</td>
>       <td>Mexico</td>
>       <td>100</td>
>       <td>100</td>
>       <td>100</td>
>     </tr>
>     <tr>
>       <td>Ernst Handel</td>
>       <td>Roland Mendel</td>
>       <td>Austria</td>
>       <td>100</td>
>       <td>100</td>
>       <td>100</td>
>     </tr>
>     <tr>
>       <td>Island Trading</td>
>       <td>Helen Bennett</td>
>       <td>UK</td>
>       <td>100</td>
>       <td>100</td>
>       <td>100</td>
>     </tr>
>     <tr>
>       <td>Laughing Bacchus Winecellars</td>
>       <td>Yoshi Tannamuri</td>
>       <td>Canada</td>
>       <td>100</td>
>       <td>100</td>
>       <td>100</td>
>     </tr>
>     <tr>
>       <td>Magazzini Alimentari Riuniti</td>
>       <td>Giovanni Rovelli</td>
>       <td>Italy</td>
>       <td>100</td>
>       <td>100</td>
>       <td>100</td>
>     </tr>
>   </tbody>
> </table>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-16-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> **CSS**
>
> ```css
> table {
>   width: 100%;
>   max-width: 1000px;
>   margin: 0 auto;
>   border-collapse: collapse;
>   table-layout: fixed;
>   background-color: #fff;
>   font: 16px Arial, sans-serif;
> }
>
> th:first-child,
> td:first-child {
>   width: 34%;
> }
>
> th:nth-child(2),
> td:nth-child(2) {
>   width: 21%;
> }
>
> th:nth-child(3),
> td:nth-child(3) {
>   width: 14%;
> }
>
> th:nth-child(n + 4),
> td:nth-child(n + 4) {
>   width: 10.33%;
> }
>
> th,
> td {
>   padding: 14px 8px;
>   border: 2px solid #eee;
>   text-align: center;
> }
>
> th {
>   background-color: #ddd;
> }
>
> tfoot td {
>   font-weight: 700;
> }
>
> tfoot td:first-child {
>   background-color: #ffe400;
> }
>
> tfoot td:not(:first-child) {
>   background-color: #009aff;
>   color: #fff;
> }
>
> caption {
>   caption-side: bottom;
>   padding: 14px;
>   background-color: #ccc;
>   font-size: 22px;
>   font-weight: 700;
> }
> ```
> **شرح الحل**
> تضع `caption-side: bottom` عنوان الجدول أسفله. يلون المحدد `tfoot td:first-child` خانة Total بالأصفر، وتلون `tfoot td:not(:first-child)` قيم الإجمالي بالأزرق. يحافظ `table-layout: fixed` على توزيع الأعمدة.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-16-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
