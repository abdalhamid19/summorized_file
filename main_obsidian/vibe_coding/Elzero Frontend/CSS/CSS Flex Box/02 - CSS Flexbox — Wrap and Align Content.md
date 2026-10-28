---
title: "CSS Flexbox — Wrap and Align Content"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Wrap and Align Content
---

# CSS Flexbox — Wrap and Align Content

> [!question] السؤال
> أنشئ أبًا 600×300px مع ستة عناصر. وزّعها ثلاثة أعلى وثلاثة أسفل كما في الصورة، مع توسيط الأب أفقيًا.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/reference-task-02.png]]
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
>   flex-wrap: wrap;
>   justify-content: space-between;
>   align-content: space-between;
>   background: #eee;
> }
>
> .parent > div {
>   flex: 0 0 32%;
>   height: 40px;
>   display: flex;
>   justify-content: center;
>   align-items: center;
>   color: #fff;
>   background: #f44336;
> }
> ```
>
> تسمح `flex-wrap` بتقسيم العناصر على صفين. توزع `justify-content: space-between` كل صف أفقيًا، بينما تدفع `align-content` الصفين إلى أعلى وأسفل مساحة الأب.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/solution-task-02.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
