---
title: "CSS Pseudo Elements — Number Badge"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Elements — Number Badge
---

# CSS Pseudo Elements — Number Badge

> [!question] السؤال
> أضف الرقم 1 بجانب شريط رمادي يحتوي النص، مع المحافظة على شكل المرجع.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> div {
>   position: relative;
>   width: 90%;
>   min-height: 88px;
>   margin: 40px auto;
>   padding: 20px 40px;
>   background: #d3d3d3;
> }
>
> div::before {
>   content: "1";
>   position: absolute;
>   top: 0;
>   left: -46px;
>   width: 44px;
>   height: 100%;
>   display: grid;
>   place-items: center;
>   background: #f00;
>   color: #fff;
>   font-weight: bold;
> }
> ```
>
> أنشأ `::before` الرقم دون إضافة عنصر HTML. وضعت الشارة خارج الحافة اليسرى باستخدام التموضع النسبي، وأبقيت النص داخل الشريط.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/solution-task-02.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
