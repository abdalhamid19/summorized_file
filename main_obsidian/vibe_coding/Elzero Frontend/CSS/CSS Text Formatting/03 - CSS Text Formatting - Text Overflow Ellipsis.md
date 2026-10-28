---
title: "03 - CSS Text Formatting - Text Overflow Ellipsis"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Text Overflow Ellipsis
---

# 03 - CSS Text Formatting - Text Overflow Ellipsis

> [!question] السؤال
> استخدم البنية التالية دون تعديلها، واجعل عرض العنصر 400px:
>
> ```html
> <div>
>   Lorem ipsum dolor sit amet consectetur, adipisicing elit.
>   Ea itaque fugit vitae incidunt quis dolores? Id alias
>   eveniet sequi perspiciatis iusto impedit,
>   accusamus maxime reprehenderit blanditiis adipisci sapiente hic velit.
> </div>
> ```
>
> تعرض الصور حالة النص الطبيعي الذي يلتف، وحالة النص الأقصر، وحالة قطع النص عند نهاية العنصر بنقاط يضيفها المتصفح دون كتابتها يدويًا.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-17-to-21/>)
>
> [!info] حدود المصدر والمطابقة
> توضح صفحة التكليف المطلوب وحالات النص، لكن تعذّر علي قراءة تفاصيل الصورة المرجعية أو الحصول على بنية HTML السابقة المشار إليها. لذلك تعرض المعاينة محتوى وصندوقًا توضيحيين، ولا أؤكد مطابقة ألوانهما للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-03 .normal,
> #task-03 .short,
> #task-03 .ellipsis {
>   box-sizing: border-box;
>   width: 400px;
>   margin: 12px auto;
>   padding: 12px;
>   border: 2px solid #009688;
>   color: #222;
> }
> #task-03 .ellipsis {
>   overflow: hidden;
>   white-space: nowrap;
>   text-overflow: ellipsis;
> }
> ```
>
> **شرح الحل**
>
> تحتاج خاصية `text-overflow: ellipsis` إلى مساحة محدودة، مع `overflow: hidden` و`white-space: nowrap`. المتصفح يضيف علامة الحذف بنفسه؛ لا تكتب النقاط داخل النص.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/CSS Text Formatting Assignments 17–21 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-17-to-21/)
