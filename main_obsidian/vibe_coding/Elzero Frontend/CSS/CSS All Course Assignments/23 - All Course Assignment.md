---
title: 23 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 23
---

# 23 — CSS Grid Item Placement

> [!question] السؤال الرسمي
> استخدم بنية HTML التالية كما هي دون تعديل، واكتب CSS لعمل الشكل في الصورة.
>
> ```html
> <div class="the-grid"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-23-reference.jpg]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```css
> .the-grid {
>   display: grid;
>   grid-template-columns: repeat(5, minmax(0, 1fr));
>   grid-template-rows: repeat(4, 100px) repeat(6, 46.5px);
>   gap: 12px;
>   counter-reset: grid-item;
> }
>
> .the-grid > div {
>   display: grid;
>   place-items: center;
>   background: #fff;
>   counter-increment: grid-item;
>   font: bold 40px Arial, sans-serif;
> }
>
> .the-grid > div::before { content: counter(grid-item); }
> .the-grid > div:nth-child(1) { grid-column: 1 / span 2; grid-row: 1 / span 2; }
> .the-grid > div:nth-child(2) { grid-column: 3; grid-row: 1; }
> .the-grid > div:nth-child(3) { grid-column: 4 / span 2; grid-row: 1; }
> .the-grid > div:nth-child(4) { grid-column: 3 / span 3; grid-row: 2 / span 2; }
> .the-grid > div:nth-child(5) { grid-column: 1 / span 2; grid-row: 3; }
> .the-grid > div:nth-child(6) { grid-column: 1 / span 4; grid-row: 4; }
> .the-grid > div:nth-child(7) { grid-column: 5; grid-row: 4; }
> .the-grid > div:nth-child(8) { grid-column: 1; grid-row: 5 / span 3; }
> .the-grid > div:nth-child(9) { grid-column: 2 / span 3; grid-row: 5 / span 3; }
> .the-grid > div:nth-child(10) { grid-column: 5; grid-row: 5; }
> .the-grid > div:nth-child(11) { grid-column: 5; grid-row: 6; }
> .the-grid > div:nth-child(12) { grid-column: 5; grid-row: 7; }
> .the-grid > div:nth-child(13) { grid-column: 1 / span 5; grid-row: 8; }
> .the-grid > div:nth-child(14) { grid-column: 1 / span 2; grid-row: 9; }
> .the-grid > div:nth-child(15) { grid-column: 3 / span 3; grid-row: 9; }
> .the-grid > div:nth-child(16) { grid-column: 1; grid-row: 10; }
> .the-grid > div:nth-child(17) { grid-column: 2; grid-row: 10; }
> .the-grid > div:nth-child(18) { grid-column: 3; grid-row: 10; }
> .the-grid > div:nth-child(19) { grid-column: 4; grid-row: 10; }
> .the-grid > div:nth-child(20) { grid-column: 5; grid-row: 10; }
> ```
>
> يعرّف `grid-template-columns` خمسة أعمدة، وتحدد `grid-template-rows` صفوفًا أطول للأجزاء العلوية وصفوفًا قصيرة للجزء السفلي.
>
> تضبط `grid-column` و`grid-row` موضع كل خانة وعدد الأعمدة والصفوف التي تشغلها. الرقم الظاهر يأتي من `counter` (عداد CSS) بدل إضافة نص أو عنصر إلى HTML؛ لذلك تبقى البنية المعطاة كما هي.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-23.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
