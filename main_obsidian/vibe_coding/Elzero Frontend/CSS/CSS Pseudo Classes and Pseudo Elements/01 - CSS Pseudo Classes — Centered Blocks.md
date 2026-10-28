---
title: "CSS Pseudo Classes — Centered Blocks"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Classes — Centered Blocks
---

# CSS Pseudo Classes — Centered Blocks

> [!question] السؤال
> نفّذ الشكل بثلاثة عناصر بعرض 300px وارتفاع 60px، وسطها أفقيًا، واجعل العنصر الأوسط أحمر والأول والثالث رماديين.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> div {
>   width: 300px;
>   height: 60px;
>   margin: 0 auto 25px;
>   background: #eee;
> }
>
> div:nth-child(2) {
>   background: #f00;
> }
> ```
>
> استخدمت `:nth-child(2)` لاختيار العنصر الثاني بحسب ترتيبه بين الإخوة. بقيت الأبعاد 300×60px، والهامش الأفقي التلقائي يوسّط العناصر.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/assets/solution-task-01.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
