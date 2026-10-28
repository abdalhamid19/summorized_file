---
title: "CSS Gradients — Input Underlines"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-filters-and-gradients
  - تكليف
aliases:
  - CSS Gradients — Input Underlines
---

# CSS Gradients — Input Underlines

> [!question] السؤال
> نسّق ثلاثة حقول إدخال بعرض 600px ووسطها أفقيًا، بألوان المرجع ومؤشر كتابة أحمر، دون استخدام Box Shadow. اجعل قيمة الحقل الأول Elzero.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Filters and Gradients/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .fields input {
>   display: block;
>   width: 600px;
>   height: 60px;
>   margin: 0 auto 16px;
>   padding: 16px 24px;
>   border: 0;
>   border-bottom: 3px solid transparent;
>   border-image: linear-gradient(90deg, #f44336 0 50%, #009688 50% 100%) 1;
>   background: #f4f4f4;
>   font-size: 26px;
>   caret-color: red;
> }
>
> .fields input::placeholder { color: #777; opacity: 1; }
> ```
>
> يقسم `border-image` الخط السفلي إلى نصفين باللونين الأحمر والأخضر المزرق. خاصية `caret-color` تغيّر لون مؤشر الكتابة فقط، ولا تؤثر على نص الحقل أو حدوده.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Filters and Gradients/assets/solution-task-02.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Filters and Gradients/CSS Filters Gradients Assignments 54-56.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
