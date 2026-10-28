---
title: "CSS Reusable Utility Classes"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - global-values
  - تكليف
aliases:
  - تكليف أصناف CSS المساعدة القابلة لإعادة الاستخدام
---

# CSS Reusable Utility Classes

> [!question] السؤال
> أنشئ مجموعة أصناف قابلة لإعادة الاستخدام:
>
> - `center-flex` لتوسيط محتويات العنصر بالطول والعرض باستخدام `Flex`.
> - `center-position` لتوسيط العنصر نفسه داخل العنصر الأب بالطول والعرض.
> - `circle-100` و`circle-200` لجعل العنصر دائريًا بقياسي `100×100px` و`200×200px`.
>
> [صفحة التكليف الأصلية](https://elzero.org/css-assignments-lesson-from-86-to-88/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .center-flex {
>   display: flex;
>   justify-content: center;
>   align-items: center;
> }
>
> .center-position {
>   position: absolute;
>   top: 50%;
>   left: 50%;
>   transform: translate(-50%, -50%);
> }
>
> .circle-100 {
>   width: 100px;
>   height: 100px;
>   border-radius: 50%;
> }
>
> .circle-200 {
>   width: 200px;
>   height: 200px;
>   border-radius: 50%;
> }
> ```
>
> أضف `position: relative` إلى الأب الذي يحتوي العنصر ذي `center-position`؛ عندها تكون نقطة المنتصف محسوبة داخل هذا الأب. يوسّط `center-flex` العناصر الداخلية، بينما يوسّط `center-position` العنصر الذي أُضيف إليه الصنف. تجعل النسبة `50%` الحافتين دائريتين تمامًا بعد مساواة العرض والارتفاع.
>
> **معاينة التطبيق**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Global Values/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Global Values/CSS Global Values Assignments 86-88.html|افتح صفحة الحل]]

## المصدر

[تكليفات CSS للدروس 86–88](https://elzero.org/css-assignments-lesson-from-86-to-88/)
