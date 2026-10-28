---
title: "CSS Grid - Top and Bottom Rows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 05
---

# CSS Grid - Top and Bottom Rows

> [!question] السؤال
> رتّب أربعة عناصر Grid في صف علوي وصف سفلي، مع ترك مساحة وسطى فارغة، ووسّط الأب أفقيًا وطابق اللون الوردي في المرجع.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/reference-task-05.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .grid5 {
>   width: min(1220px, calc(100% - 40px));
>   height: 620px;
>   margin-inline: auto;
>   padding: 35px;
>   display: grid;
>   grid-template-columns: 1fr 1fr;
>   grid-template-rows: 70px 1fr 1fr 70px;
>   gap: 35px;
>   background: #ddd;
> }
>
> .grid5 > div {
>   display: grid;
>   place-items: center;
>   color: white;
>   background: #e91e63;
> }
>
> .grid5 > :nth-child(1) { grid-column: 1; grid-row: 1; }
> .grid5 > :nth-child(2) { grid-column: 2; grid-row: 1; }
> .grid5 > :nth-child(3) { grid-column: 1; grid-row: 4; }
> .grid5 > :nth-child(4) { grid-column: 2; grid-row: 4; }
> ```
>
> يترك صفا الوسط دون عناصر، فيظهر الفراغ الكبير كما في الصورة. يضع `grid-row` العنصرين الأول والثاني في الأعلى، والثالث والرابع في الأسفل.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/solution-task-05.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Grid/CSS Grid Assignments 57-64.html|افتح صفحة عرض الحلول 57–64]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
