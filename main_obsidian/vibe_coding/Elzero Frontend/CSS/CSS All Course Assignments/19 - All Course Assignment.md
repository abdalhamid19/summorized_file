---
title: 19 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 19
---

# 19 — CSS Layered Color Frame

> [!question] السؤال الرسمي
> استخدم بنية HTML التالية كما هي دون تعديل، واكتب CSS لعمل الشكل في الصورة. يُمنع استخدام `Pseudo Elements` (العناصر الزائفة) و`Gradients` (التدرجات اللونية)، ويجب تغيير عرض الإطار من مكان واحد فقط.
>
> ```html
> <div>Elzero</div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-19-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```css
> div {
>   --border-size: 16px;
>   width: 683px;
>   height: 130px;
>   display: grid;
>   place-items: center;
>   border: var(--border-size) solid #cddc39;
>   background: #eee;
>   box-shadow:
>     0 0 0 calc(var(--border-size) * 1) #e91e63,
>     0 0 0 calc(var(--border-size) * 2) #9c27b0,
>     0 0 0 calc(var(--border-size) * 3) #4caf50,
>     0 0 0 calc(var(--border-size) * 4) #3f51b5,
>     0 0 0 calc(var(--border-size) * 5) #795548,
>     0 0 0 calc(var(--border-size) * 6) #ffc107,
>     0 0 0 calc(var(--border-size) * 7) #009688;
>   font: bold 24px Arial, sans-serif;
> }
> ```
>
> المتغير `--border-size` هو الموضع الوحيد الذي نغيّر منه سمك الإطار. كل طبقة في `box-shadow` (ظل الصندوق) تستخدم مضاعفًا لهذا المتغير لتكوين مستطيل لوني متتابع حول العنصر.
>
> يبقى العنصر نفسه كما هو؛ لا يستخدم الحل عناصر زائفة أو تدرجات. طبقة `border` الداخلية باللون الأخضر الفاتح، والظلال المتراكبة تكمل بقية الألوان.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-19.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
