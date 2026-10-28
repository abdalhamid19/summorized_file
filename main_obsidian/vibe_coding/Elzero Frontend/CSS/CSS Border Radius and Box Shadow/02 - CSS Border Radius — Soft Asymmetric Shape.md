---
title: "CSS Border Radius — Soft Asymmetric Shape"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-border-radius-and-box-shadow
  - تكليف
aliases:
  - CSS Border Radius — Soft Asymmetric Shape
---

# CSS Border Radius — Soft Asymmetric Shape

> [!question] السؤال
> أنشئ عنصرًا 100×100px في منتصف الشاشة، مع زاوية دائرية غير متماثلة وظل داخلي، وأضف بادئات الخواص اللازمة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .shape {
>   width: 100px;
>   height: 100px;
>   margin: auto;
>   background: #eee;
>   -webkit-border-radius: 15% 50% 0 50%;
>   -moz-border-radius: 15% 50% 0 50%;
>   border-radius: 15% 50% 0 50%;
>   -webkit-box-shadow: inset 8px 8px 14px #777, inset -8px -8px 14px #888;
>   -moz-box-shadow: inset 8px 8px 14px #777, inset -8px -8px 14px #888;
>   box-shadow: inset 8px 8px 14px #777, inset -8px -8px 14px #888;
> }
>
> body {
>   min-height: 100vh;
>   display: grid;
>   place-items: center;
> }
> ```
>
> تحدد قيم `border-radius` الأربع انحناء كل زاوية على حدة. جعلت الظلّين الداخليين باتجاهين متعاكسين لإظهار ملمس ناعم قريب من الصورة، ووسّطت العنصر باستخدام Grid.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/assets/solution-task-02.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/CSS Border Radius and Box Shadow Assignments 38-41.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
