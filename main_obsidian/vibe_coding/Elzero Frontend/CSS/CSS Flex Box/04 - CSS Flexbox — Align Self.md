---
title: "CSS Flexbox — Align Self"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Align Self
---

# CSS Flexbox — Align Self

> [!question] السؤال
> أنشئ أبًا 600×300px وثلاثة عناصر. ضع الأول والثالث عند اليمين أعلى وأسفل، والعنصر الثاني عريضًا عند اليسار في الوسط.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/reference-task-04.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .parent {
>   width: 600px;
>   height: 300px;
>   margin: 0 auto;
>   padding: 10px;
>   display: flex;
>   flex-direction: column;
>   justify-content: space-between;
>   align-items: flex-end;
>   background: #eee;
> }
>
> .parent > div {
>   width: 30px;
>   height: 80px;
>   display: grid;
>   place-items: center;
>   color: #fff;
>   background: #009688;
> }
>
> .two {
>   width: 320px;
>   align-self: flex-start;
> }
> ```
>
> ترتب `flex-direction: column` العناصر رأسيًا، وتوزعها `space-between` على ارتفاع الأب. يغيّر `align-self` محاذاة العنصر الثاني وحده إلى اليسار ويزيد عرضه.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/solution-task-04.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
