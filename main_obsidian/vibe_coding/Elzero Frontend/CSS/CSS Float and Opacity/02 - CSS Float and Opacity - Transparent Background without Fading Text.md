---
title: "02 - CSS Float and Opacity - Transparent Background without Fading Text"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
  - تكليف
aliases:
  - تكليف Transparent Background without Fading Text
---

# 02 - CSS Float and Opacity - Transparent Background without Fading Text

> [!question] السؤال
> استخدم البنية التالية:
>
> ```html
> <div class="normal">Normal</div>
> <div class="one">One</div>
> <div class="two">Two</div>
> ```
>
> لكل العناصر خلفية واحدة، وخلفية العنصرين الأخيرين بشفافية 0.1. حافظ على ظهور النص واضحًا.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-27-to-29/>)
>
> [!info] حدود المصدر والمطابقة
> المطلوب هو خلفية مشتركة، وشفافية 0.1 للعنصرين الأخيرين مع بقاء النص واضحًا. تعذّر علي قراءة اللون في الصورة المرجعية، لذلك استخدمت لونًا نموذجيًا؛ أما HTML في صفحة المعاينة فيشرح الفكرة بعناصر بديلة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-02 .stage > div {
>   box-sizing: border-box;
>   width: 300px;
>   margin: 20px auto;
>   padding: 20px;
>   color: black;
>   font-weight: bold;
>   font-size: 1rem;
>   background-color: #009688;
> }
> #task-02 .stage > .one,
> #task-02 .stage > .two {
>   background-color: rgba(0, 150, 136, 0.1);
> }
> ```
>
> **شرح الحل**
>
> استخدمت `rgba()` على لون الخلفية بدل `opacity` على العنصر كله. بهذه الطريقة تصبح الخلفية شفافة بنسبة 0.1 وتظل الكتابة سوداء واضحة.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Float and Opacity/CSS Float and Opacity Assignments 27–29 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Float and Opacity/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-27-to-29/)
