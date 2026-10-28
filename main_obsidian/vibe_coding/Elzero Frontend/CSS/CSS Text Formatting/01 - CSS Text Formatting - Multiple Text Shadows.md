---
title: "01 - CSS Text Formatting - Multiple Text Shadows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Multiple Text Shadows
---

# 01 - CSS Text Formatting - Multiple Text Shadows

> [!question] السؤال
> أنشئ تأثير الظلال المتعددة للنص مع مراعاة الألوان الظاهرة في الصورة المرجعية.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-17-to-21/>)
>
> [!info] حدود المصدر والمطابقة
> صفحة التكليف الرسمية تربط بصورة مرجعية، لكن تعذّر علي قراءة الصورة في هذه الجلسة، كما أن بنية HTML السابقة المشار إليها غير ظاهرة في النص المتاح. لذلك تستخدم المعاينة عناصر بديلة، وألوان الظلال أمثلة توضيحية لا أؤكد مطابقتها للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-01 .text-shadow {
>   color: #222;
>   text-shadow:
>     2px 2px 0 #e91e63,
>     -2px -2px 0 #2196f3,
>     4px 4px 0 #ff9800;
> }
> ```
>
> **شرح الحل**
>
> تقبل خاصية `text-shadow` عدة ظلال مفصولة بفواصل. كل ظل يحدد الإزاحة الأفقية والرأسية والانتشار واللون؛ ترتيبها يسمح بتركيب أكثر من حد لوني حول النص.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/CSS Text Formatting Assignments 17–21 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-17-to-21/)
