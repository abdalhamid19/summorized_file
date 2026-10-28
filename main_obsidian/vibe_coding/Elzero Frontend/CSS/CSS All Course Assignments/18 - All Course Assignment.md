---
title: 18 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 18
---

# 18 — CSS Counter and Pseudo-element

> [!question] السؤال الرسمي
> استخدم بنية HTML التالية كما هي دون تعديل، واكتب CSS لعمل الشكل في الصورة. هذا تكليف تحدٍّ، ولا تستخدم `::after`.
>
> ```html
> <ul>
>   <li>Python</li>
>   <li>PHP</li>
>   <li>JavaScript</li>
>   <li>C++</li>
>   <li>C#</li>
>   <li>Java</li>
> </ul>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-18-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```css
> ul {
>   counter-reset: language 10;
>   list-style: none;
>   margin: 0;
>   padding: 0;
>   background: #fff;
>   font: 24px Arial, sans-serif;
> }
>
> li {
>   height: 105px;
>   padding: 0 22px;
>   display: flex;
>   align-items: center;
>   justify-content: space-between;
>   border-bottom: 1px solid #d2d2d2;
>   counter-increment: language 3;
> }
>
> li:last-child {
>   border-bottom: 0;
> }
>
> li::before {
>   order: 2;
>   content: "(" counter(language) ")";
>   width: 75px;
>   height: 75px;
>   display: grid;
>   place-items: center;
>   border-radius: 50%;
>   color: #fff;
>   background: #9c27b0;
>   font: bold 16px Arial, sans-serif;
> }
>
> li:nth-child(even)::before {
>   background: #f44336;
> }
> ```
>
> يبدأ `counter-reset` العداد من 10، ثم تزيده `counter-increment` بمقدار 3 لكل عنصر؛ لذلك تظهر الأرقام 13 و16 و19 و22 و25 و28.
>
> ينشئ `::before` (عنصرًا زائفًا قبل محتوى العنصر) الدائرة والرقم من CSS، فيبقى HTML كما أُعطي. الخاصية `order` تنقل الدائرة إلى يمين النص داخل حاوية `flex`.
>
> يبدّل `:nth-child(even)` لون الدائرة في الصفوف الزوجية. لا يستخدم الحل `::after`.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-18.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
