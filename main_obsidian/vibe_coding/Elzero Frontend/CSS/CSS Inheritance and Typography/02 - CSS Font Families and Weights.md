---
title: "CSS Font Families and Weights"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - typography
  - تكليف
aliases:
  - تكليف أنواع الخطوط وأوزانها
---

# CSS Font Families and Weights

> [!question] السؤال
> حافظ على بنية المثال الأصلية، وأنشئ ثلاثة أسطر بالنص `elzero Web school`: الأول بخط `Open Sans` بوزن `300` ومائل، والثاني بخط `Cairo` بوزن `700`، والثالث بخط `Jomhuria` بوزن `400`.
>
> [صفحة التكليفات للدروس 22–26](https://elzero.org/css-assignments-lesson-from-22-to-26/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <p class="open-sans">elzero Web school</p>
> <p class="cairo">elzero Web school</p>
> <p class="jomhuria">elzero Web school</p>
> ```
>
> ```css
> .open-sans {
>   font-family: "Open Sans", sans-serif;
>   font-size: 24px;
>   font-weight: 300;
>   font-style: italic;
> }
>
> .cairo {
>   font-family: "Cairo", sans-serif;
>   font-size: 24px;
>   font-weight: 700;
> }
>
> .jomhuria {
>   font-family: "Jomhuria", cursive;
>   font-size: 32px;
>   font-weight: 400;
> }
> ```
>
> يجب أن تكون الخطوط متاحة للمتصفح. حمّلت صفحة المعاينة عائلات الخطوط من Google Fonts؛ ويمكن تنزيلها محليًا إذا أردت تشغيل العرض دون اتصال. أحجام الخطوط في المعاينة اختيارية لأن نص التكليف لا يفرض قياسات محددة.
>
> **معاينة الخطوط**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Inheritance and Typography/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Inheritance and Typography/CSS Inheritance Typography Assignments 22-26.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS للدروس 22–26](https://elzero.org/css-assignments-lesson-from-22-to-26/)
