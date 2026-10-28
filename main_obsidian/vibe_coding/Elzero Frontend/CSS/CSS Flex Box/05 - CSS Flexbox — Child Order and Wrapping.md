---
title: "CSS Flexbox — Child Order and Wrapping"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Child Order and Wrapping
---

# CSS Flexbox — Child Order and Wrapping

> [!question] السؤال
> أنشئ أبًا 600×300px وأربعة عناصر بألوان وأحجام الشكل، ووزّع اثنين في الصف العلوي واثنين في السفلي.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/reference-task-05.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .parent {
>   box-sizing: content-box;
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
> .slot {
>   flex: 0 0 50%;
>   height: 150px;
>   display: flex;
> }
>
> .slot > div {
>   width: 100px;
>   height: 150px;
>   display: grid;
>   place-items: center;
>   color: #fff;
> }
>
> .one { order: 1; }
> .three { order: 2; }
> .four { order: 3; }
> .two { order: 4; }
> .one > div { margin-left: 160px; background: #ff9800; }
> .three > div { margin-left: auto; background: #795548; }
> .four > div { background: #673ab7; }
> .two > div { margin-left: 34px; background: #8bc34a; }
> ```
>
> تقسم حاويات `.slot` الأب إلى عمودين باستخدام Flexbox، ثم يرتب `order` البطاقات بين الصفين وتحدد الهوامش أماكنها داخل كل عمود. أُعيد بناء حاويات التوزيع داخل الديمو لأن صفحة التكليف لا تعرض بنية HTML السابقة.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/solution-task-05.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
