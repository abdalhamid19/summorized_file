---
title: "CSS Position, List, and Table - Positioning and Layer Order"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف ترتيب الطبقات والتموضع
---

# CSS Position, List, and Table — Positioning and Layer Order

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها. اجعل العناصر مربعة بمقاس `100×100px`، واضبط ترتيب الطبقات. يجب أن يبعد العنصر الأزرق `20px` من أعلى الصفحة ويسارها.
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-30-to-33/)

> [!info] حدود المصدر والمطابقة
> تثبت صفحة التكليف مقاس المربعات `100×100px`، وإزاحة المربع الأزرق `20px` من الأعلى واليسار، وترتيب الطبقات. البنية السابقة وألوان بقية الأشكال غير ظاهرة في النص المتاح؛ لذلك ألوان المربعات الأخرى والمعاينة توضيحية.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-01 .stage {
>   position: static;
>   min-height: 280px;
> }
>
> #task-01 .square {
>   position: absolute;
>   width: 100px;
>   height: 100px;
>   display: grid;
>   place-items: center;
>   color: #fff;
> }
>
> #task-01 .red {
>   top: 80px;
>   left: 80px;
>   background: #e91e63;
>   z-index: 1;
> }
>
> #task-01 .green {
>   top: 50px;
>   left: 50px;
>   background: #4caf50;
>   z-index: 2;
> }
>
> #task-01 .blue {
>   top: 20px;
>   left: 20px;
>   background: #2196f3;
>   z-index: 3;
> }
> ```
>
> تبقى مساحة العرض `static` حتى يُحسب موضع المربع الأزرق من حافة الصفحة نفسها؛ ثم يحدد `top` و`left` المسافة `20px`. وتحدد `z-index` ترتيب تراكب المربعات.
>
> **معاينة الحل**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|صفحة المعاينة للمجموعة]].
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس 30–33](https://elzero.org/css-assignments-lesson-from-30-to-33/)
