---
title: "04 - CSS Position, List, and Table - Table-only Layout"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف Table-only Layout
---

# 04 - CSS Position, List, and Table - Table-only Layout

> [!question] السؤال
> أنشئ الشكل باستخدام الجدول فقط، من دون إضافة عناصر أخرى. يجب أن يكون عرض الجدول 700px وفي منتصف الصفحة.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-30-to-33/>)
>
> [!info] حدود المصدر والمطابقة
> تحدد صفحة التكليف جدولًا فقط بعرض `700px` وتوسيطه. تعذّر علي قراءة تفاصيل الصورة المرجعية، لذلك الصفوف والألوان في المعاينة أمثلة توضيحية، ولا أؤكد مطابقتها للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-04 table {
>   width: 700px;
>   margin: 24px auto;
>   border-collapse: collapse;
>   font: 16px Arial, sans-serif;
> }
> #task-04 caption { padding: 12px; background: #222; color: #fff; font-weight: 700; }
> #task-04 th, #task-04 td { padding: 12px; border: 2px solid #444; text-align: left; }
> #task-04 th { background: #2196f3; color: #fff; }
> #task-04 td { background: #eee; color: #222; }
> ```
>
> **شرح الحل**
>
> العنصر الوحيد في هذا الجزء هو `table` نفسه مع عناصره الدلالية الداخلية. يثبت `width: 700px` الحجم، و`margin: 24px auto` يوسّطه. استخدمت صفوفًا تجريبية لعرض البنية.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Position List Table/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-30-to-33/)
