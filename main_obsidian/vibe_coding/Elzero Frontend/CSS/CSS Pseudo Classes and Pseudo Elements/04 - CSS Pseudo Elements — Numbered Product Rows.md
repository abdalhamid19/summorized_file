---
title: "CSS Pseudo Elements — Numbered Product Rows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Elements — Numbered Product Rows
---

# CSS Pseudo Elements — Numbered Product Rows

> [!question] السؤال
> أنشئ ستة صفوف للعناوين مع أرقام متتابعة يسارها وشريط أحمر رفيع عند اليمين، باستخدام pseudo-elements.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/reference-task-04.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .products {
>   counter-reset: product;
> }
>
> .product {
>   counter-increment: product;
>   display: flex;
>   align-items: center;
>   min-height: 60px;
>   border-right: 5px solid #f44336;
>   background: #eee;
> }
>
> .product::before {
>   content: counter(product);
>   width: 60px;
>   min-height: 60px;
>   margin-right: 20px;
>   display: grid;
>   place-items: center;
>   color: #fff;
>   background: #f44336;
>   font-weight: bold;
> }
> ```
>
> يبدأ العداد من الصفر ثم يزيد مرةً لكل صف. يعرض `::before` الرقم، فيبقى الترقيم تلقائيًا ولا نكتب الأرقام يدويًا داخل النصوص.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/solution-task-04.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
