---
title: "CSS Transition — Parent and Child Timing"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-transitions-and-variables
  - تكليف
aliases:
  - CSS Transition — Parent and Child Timing
---

# CSS Transition — Parent and Child Timing

> [!question] السؤال
> عند مرور المؤشر فوق الأب، تحركه للأعلى خلال نصف ثانية، ثم تحرك الابن للأسفل بعد تأخير نصف ثانية، مع ألوان المرجع.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .parent {
>   transition: transform 0.5s ease;
>   -webkit-transition: transform 0.5s ease;
> }
>
> .parent:hover {
>   transform: translateY(-40px);
>   -webkit-transform: translateY(-40px);
> }
>
> .child {
>   transition: transform 0.5s ease 0.5s;
>   -webkit-transition: transform 0.5s ease 0.5s;
> }
>
> .parent:hover .child {
>   transform: translateY(40px);
>   -webkit-transform: translateY(40px);
> }
> ```
>
> انتقال الأب يستغرق 0.5 ثانية. أما الابن فله مدة مماثلة وتأخير 0.5 ثانية، لذلك يبدأ نزوله بعد حركة الأب المطلوبة.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/assets/solution-task-01.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/CSS Transitions and Variables Assignments 42-45.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
