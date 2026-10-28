---
title: "03 - CSS Position, List, and Table - Styled List with Attributes"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف Styled List with Attributes
---

# 03 - CSS Position, List, and Table - Styled List with Attributes

> [!question] السؤال
> أنشئ قائمة بعرض 400px ووسّطها أفقيًا. يمكنك إضافة `class` أو `attribute` لتحقيق الشكل، مع الحفاظ على الألوان كما في الصورة.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-30-to-33/>)
>
> [!info] حدود المصدر والمطابقة
> تحدد صفحة التكليف قائمة بعرض `400px` وتوسيطها، وتسمح باستخدام `class` أو `attribute`. تعذّر علي قراءة تفاصيل الصورة المرجعية؛ لذلك القائمة والألوان في المعاينة مثال توضيحي، ولا أؤكد مطابقتها للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-03 .menu {
>   box-sizing: border-box;
>   width: 400px;
>   margin: 24px auto;
>   padding: 0;
>   list-style: none;
>   border: 2px solid #2196f3;
> }
> #task-03 .menu li {
>   position: relative;
>   padding: 14px 18px 14px 64px;
>   border-bottom: 1px solid #bbb;
>   background: #f5f5f5;
> }
> #task-03 .menu li:last-child { border-bottom: 0; }
> #task-03 .menu li::before {
>   content: attr(data-number);
>   position: absolute;
>   left: 14px;
>   font-weight: 700;
>   color: #e91e63;
> }
> ```
>
> **شرح الحل**
>
> تضمن `width` و`margin` عرض القائمة المطلوب وتوسيطها. يسمح `data-number` بإظهار رقم العنصر بواسطة `attr()` داخل `::before`. اخترت شكل قائمة مرقمة للتوضيح.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-30-to-33/)
