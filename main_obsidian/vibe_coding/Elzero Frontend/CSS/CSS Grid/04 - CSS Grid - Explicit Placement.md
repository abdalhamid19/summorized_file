---
title: "CSS Grid - Explicit Placement"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 04
---

# CSS Grid - Explicit Placement

> [!question] السؤال
> رتّب العناصر الثمانية في شبكة Grid لتطابق الصورة، مع إظهار الأب وأبعاده وتوسيطه أفقيًا، واستخدم اللون الأزرق الظاهر في المرجع.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/reference-task-04.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .grid4 {
>   width: min(1220px, calc(100% - 40px));
>   height: 700px;
>   margin-inline: auto;
>   padding: 35px;
>   display: grid;
>   grid-template-columns: repeat(6, 1fr);
>   grid-template-rows: 70px 70px repeat(3, 1fr) 70px;
>   gap: 35px;
>   background: #ddd;
> }
>
> .grid4 > div {
>   display: grid;
>   place-items: center;
>   color: white;
>   background: #2196f3;
> }
>
> .grid4 > :nth-child(1) { grid-column: 1 / 7; grid-row: 6; }
> .grid4 > :nth-child(2) { grid-column: 1 / 5; grid-row: 2; }
> .grid4 > :nth-child(3) { grid-column: 5 / 7; grid-row: 2; }
> .grid4 > :nth-child(4) { grid-column: 1 / 3; grid-row: 3; }
> .grid4 > :nth-child(5) { grid-column: 3 / 7; grid-row: 3 / 6; }
> .grid4 > :nth-child(6) { grid-column: 1 / 3; grid-row: 4; }
> .grid4 > :nth-child(7) { grid-column: 1 / 3; grid-row: 5; }
> .grid4 > :nth-child(8) { grid-column: 1 / 7; grid-row: 1; }
> ```
>
> تحدد `grid-column` و`grid-row` مواقع كل عنصر صراحة. يمتد العنصر 5 على ثلاثة صفوف، والعنصران 1 و8 على عرض الشبكة كاملة في أسفلها وأعلاها.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/solution-task-04.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Grid/CSS Grid Assignments 57-64.html|افتح صفحة عرض الحلول 57–64]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
