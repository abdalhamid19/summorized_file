---
title: "CSS Gradients — Multicolor Frame"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-filters-and-gradients
  - تكليف
aliases:
  - CSS Gradients — Multicolor Frame
---

# CSS Gradients — Multicolor Frame

> [!question] السؤال
> أنشئ عنصرًا عرضه 600px في وسط الصفحة، بإطار متدرج متعدد الألوان وخلفية داخلية رمادية ونص Elzero. لا تستخدم Box Shadow.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Filters and Gradients/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .frame {
>   width: 600px;
>   margin: 0 auto;
>   padding: 8px;
>   background: linear-gradient(
>     90deg,
>     #f44336 0 20%,
>     #2196f3 20% 40%,
>     #4caf50 40% 60%,
>     #e91e63 60% 80%,
>     #673ab7 80% 100%
>   );
> }
>
> .inner {
>   min-height: 86px;
>   display: grid;
>   place-items: center;
>   background: #eee;
>   font: bold 56px Georgia, serif;
>   letter-spacing: 16px;
> }
>
> .inner::first-letter { color: #f44336; }
> ```
>
> حققت الإطار باستخدام `linear-gradient` على الحاوية مع حشو داخلي، بدل `box-shadow`. تقسم نقاط التوقف التدرج إلى خمسة ألوان واضحة، وتلون `::first-letter` الحرف الأول.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Filters and Gradients/assets/solution-task-01.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Filters and Gradients/CSS Filters Gradients Assignments 54-56.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
