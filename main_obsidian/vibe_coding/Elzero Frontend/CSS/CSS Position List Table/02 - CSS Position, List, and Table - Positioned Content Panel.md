---
title: "02 - CSS Position, List, and Table - Positioned Content Panel"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف Positioned Content Panel
---

# 02 - CSS Position, List, and Table - Positioned Content Panel

> [!question] السؤال
> اجعل الحاوية الرئيسية بعرض 400px، ووسّطها أفقيًا. طابق ألوان الخلفية والحدود مع الصورة.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-30-to-33/>)
>
> [!info] حدود المصدر والمطابقة
> تطلب صفحة التكليف حاوية بعرض `400px` وتوسيطها ومطابقة ألوان الصورة، لكنها تشير إلى بنية HTML سابقة لا تظهر في النص المتاح، وتعذّر علي قراءة ألوان الصورة. لذلك HTML والألوان في المعاينة أمثلة توضيحية، ويجب تطبيق قواعد التموضع على بنية المصدر الأصلية.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-02 .panel {
>   position: relative;
>   box-sizing: border-box;
>   width: 400px;
>   min-height: 180px;
>   margin: 30px auto;
>   padding: 28px;
>   border: 3px solid #e91e63;
>   background: #f5f5f5;
>   color: #222;
> }
> #task-02 .badge { position: absolute; top: -14px; right: 18px; padding: 4px 10px; background: #2196f3; color: white; }
> ```
>
> **شرح الحل**
>
> يثبت `width: 400px` عرض الحاوية، ويجعل `margin-inline: auto` (هنا اختصار `margin: 30px auto`) الهوامش الجانبية متساوية. يوضح المثال تموضع عنصر داخلها.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-30-to-33/)
