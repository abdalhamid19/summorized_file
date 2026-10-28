---
title: "02 - CSS Text Formatting - Text Transform"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Text Transform
---

# 02 - CSS Text Formatting - Text Transform

> [!question] السؤال
> استخدم البنية التالية دون تعديلها:
>
> ```html
> <p class="one">elzero Web school</p>
> <p class="two">elzero Web school</p>
> <p class="three">elzero Web school</p>
> ```
>
> رتّب النتائج كما في المرجع: `uppercase` بحجم كبير، ثم `Title Case` بحجم متوسط، ثم `lowercase` بحجم صغير.
>
> قيم `48px` و`36px` و`24px` في الحل تقريبية؛ المطلوب هو التدرج البصري لا قياس بكسل موثق.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-17-to-21/>)
>
> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-02 .one { text-transform: uppercase; font-size: 48px; }
> #task-02 .two { text-transform: capitalize; font-size: 36px; }
> #task-02 .three { text-transform: lowercase; font-size: 24px; }
> ```
>
> **شرح الحل**
>
> تحوّل `uppercase` النص إلى أحرف كبيرة، ويجعل `capitalize` بدايات الكلمات كبيرة، ويحوّل `lowercase` النص إلى أحرف صغيرة. تضع الأحجام القيم بالترتيب الكبير ثم المتوسط ثم الصغير.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/CSS Text Formatting Assignments 17–21 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Text Formatting/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-17-to-21/)
