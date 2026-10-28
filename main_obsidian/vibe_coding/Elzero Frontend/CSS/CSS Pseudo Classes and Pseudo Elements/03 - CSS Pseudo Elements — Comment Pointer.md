---
title: "CSS Pseudo Elements — Comment Pointer"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Elements — Comment Pointer
---

# CSS Pseudo Elements — Comment Pointer

> [!question] السؤال
> نسّق ثلاثة تعليقات، وأضف لسانًا مثلثًا على الحافة اليسرى لكل تعليق باستخدام pseudo-element.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .comment {
>   position: relative;
>   border-left: 5px solid #e91e63;
>   background: #eee;
>   padding: 20px 24px;
> }
>
> .comment::before {
>   content: "";
>   position: absolute;
>   left: -30px;
>   top: 50%;
>   transform: translateY(-50%);
>   border: 15px solid transparent;
>   border-right-color: #e91e63;
> }
> ```
>
> رسمت المثلث بحدود شفافة مع تلوين الحد الأيمن فقط. حرّكته إلى يسار الصندوق، ووسّطته رأسيًا دون إضافة عنصر زخرفي إلى HTML.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/solution-task-03.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
