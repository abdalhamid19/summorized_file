---
title: "04 - CSS Text Formatting - Centered Styled Link"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Centered Styled Link
---

# 04 - CSS Text Formatting - Centered Styled Link

> [!question] السؤال
> استخدم الرابط دون تعديل HTML:
>
> ```html
> <a href="https://elzero.org">elzero</a>
> ```
>
> اجعله في منتصف الصفحة تمامًا ونسّق مظهره كما في الصورة المرجعية.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-17-to-21/>)
>
> [!info] حدود المصدر والمطابقة
> تطلب صفحة التكليف توسيط الرابط وتنسيقه وفق صورة مرجعية، لكن تعذّر علي قراءة تفاصيل الصورة أو العثور على بنية HTML السابقة المشار إليها. لذلك الخلفية والتباعد في المعاينة أمثلة توضيحية، ولا أؤكد مطابقة اللون للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-04 {
>   min-height: 260px;
>   display: grid;
>   place-items: center;
> }
> #task-04 a {
>   padding: 18px 30px;
>   border-radius: 8px;
>   background: #009688;
>   color: #fff;
>   font: 700 24px Arial, sans-serif;
>   text-decoration: none;
> }
> ```
>
> **شرح الحل**
>
> يضع `display: grid` و`place-items: center` الرابط في منتصف المساحة المتاحة.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/CSS Text Formatting Assignments 17–21 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-17-to-21/)
