---
title: "CSS Box Shadow — Layered Circles"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-border-radius-and-box-shadow
  - تكليف
aliases:
  - CSS Box Shadow — Layered Circles
---

# CSS Box Shadow — Layered Circles

> [!question] السؤال
> أنشئ ثلاثة عناصر دائرية قطرها 100px، مع إطار أسود وظلين متداخلين بالوردي والأزرق، وأضف بادئات المتصفح عند الحاجة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .circles {
>   counter-reset: item;
>   display: flex;
>   justify-content: space-around;
>   gap: 24px;
> }
>
> .circle {
>   counter-increment: item;
>   position: relative;
>   width: 100px;
>   height: 100px;
>   display: grid;
>   place-items: center;
>   border: 3px solid #000;
>   background: #eee;
>   -webkit-border-radius: 50%;
>   -moz-border-radius: 50%;
>   border-radius: 50%;
>   -webkit-box-shadow: -8px -6px 0 #e91e63, 8px 6px 0 #2196f3;
>   -moz-box-shadow: -8px -6px 0 #e91e63, 8px 6px 0 #2196f3;
>   box-shadow: -8px -6px 0 #e91e63, 8px 6px 0 #2196f3;
> }
>
> .circle::before {
>   content: counter(item);
>   position: absolute;
>   top: -12px;
>   left: 50%;
>   transform: translateX(-50%);
>   width: 24px;
>   height: 24px;
>   border-radius: 50%;
>   background: #000;
>   color: #fff;
>   text-align: center;
> }
> ```
>
> تنتج `border-radius: 50%` دائرة عندما يتساوى العرض والارتفاع. أضفت ظلين في خاصية واحدة، أحدهما مزاح للأعلى واليسار والآخر للأسفل واليمين. هذه البادئات مطلوبة في تمرين الدرس، رغم أن المتصفحات الحديثة لا تحتاجها عادةً.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/assets/solution-task-01.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/CSS Border Radius and Box Shadow Assignments 38-41.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
