---
title: "CSS Pseudo Element — Replace Inline Text"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-transitions-and-variables
  - تكليف
aliases:
  - CSS Pseudo Element — Replace Inline Text
---

# CSS Pseudo Element — Replace Inline Text

> [!question] السؤال
> حافظ على بنية العنصر ذات التنسيق المضمن. أخفِ النص Hello Div وأظهر Elzero بخط 20px داخل عنصر بعرض 400px في وسط الصفحة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> div {
>   width: 400px;
>   margin: 0 auto;
>   text-align: center;
>   font-size: 0 !important;
> }
>
> div::before {
>   content: "Elzero";
>   font-size: 20px;
> }
> ```
>
> يتغلب `!important` على حجم الخط 80px الموجود في `style` المضمن، فيختفي نص Hello Div دون إزالة النص من HTML. ثم يضيف `::before` كلمة Elzero بحجم 20px.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/assets/solution-task-02.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/CSS Transitions and Variables Assignments 42-45.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
