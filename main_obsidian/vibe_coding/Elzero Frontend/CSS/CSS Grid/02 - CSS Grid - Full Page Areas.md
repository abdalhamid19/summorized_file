---
title: "CSS Grid - Full Page Areas"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 02
---

# CSS Grid - Full Page Areas

> [!question] السؤال
> أنشئ توزيع الصفحة بالشكل والألوان المرجعية، واستخدم CSS Grid فقط. يجب أن يمتد التخطيط إلى كامل مساحة الصفحة، ويحتوي على Header وSection وAside وFooter.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/reference-task-02.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .grid2 {
>   height: 100vh;
>   display: grid;
>   grid-template-columns: minmax(0, 2fr) minmax(220px, 1fr);
>   grid-template-rows: 90px 1fr 90px;
>   grid-template-areas:
>     "header header"
>     "section aside"
>     "footer footer";
> }
>
> .grid2 > :nth-child(1) { grid-area: header; background: #03a9f4; }
> .grid2 > :nth-child(2) { grid-area: section; background: #ff5722; }
> .grid2 > :nth-child(3) { grid-area: aside; background: #607d8b; }
> .grid2 > :nth-child(4) { grid-area: footer; background: #009688; }
>
> .grid2 > * {
>   padding: 28px;
>   color: #fff;
> }
> ```
>
> تملأ `height: 100vh` طول نافذة العرض كاملة. تسمي `grid-template-areas` مناطق الصفحة، وتربطها بالعناصر الأربع بحسب ترتيبها في البنية. هذا المثال يفترض ترتيب العناصر: Header ثم Section ثم Aside ثم Footer.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Grid/CSS Grid Assignments 57-64.html|افتح صفحة عرض الحلول 57–64]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
