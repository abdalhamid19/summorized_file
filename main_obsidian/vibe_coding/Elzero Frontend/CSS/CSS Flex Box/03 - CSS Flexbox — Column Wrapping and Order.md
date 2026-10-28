---
title: "CSS Flexbox — Column Wrapping and Order"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Column Wrapping and Order
---

# CSS Flexbox — Column Wrapping and Order

> [!question] السؤال
> نسّق العناصر الستة داخل أب 600×300px بحسب الشكل: ثلاث أعمدة بعناصر متفاوتة الارتفاع والترتيب، مع توسيط الأب أفقيًا.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/reference-task-03.png]]
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
>   flex-flow: column wrap;
>   justify-content: space-between;
>   align-content: space-between;
>   background: #eee;
> }
>
> .parent > div {
>   width: 31%;
>   height: 50%;
>   display: flex;
>   justify-content: center;
>   align-items: center;
>   color: #fff;
>   background: #607d8b;
> }
>
> .one { order: 6; height: 25%; }
> .two { order: 4; }
> .three { order: 3; height: 25%; }
> .four { order: 5; }
> .five { order: 2; }
> .six { order: 1; }
> ```
>
> ينشئ `flex-flow: column wrap` أعمدةً جديدة عند امتلاء ارتفاع الأب. يتحكم `order` في تسلسل الامتلاء، وتسمح الارتفاعات المختلفة ببناء النمط المتفاوت في المرجع.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/solution-task-03.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
