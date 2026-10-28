---
title: "CSS Grid - Three Columns"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 01
---

# CSS Grid - Three Columns

> [!question] السؤال
> استعمل بنية HTML السابقة دون تعديلها، وأنشئ التخطيط الأساسي باستخدام CSS Grid. أظهر كلمات العناصر من CSS، ووسّط النص داخل كل عنصر. أضف تنسيقات الأب لتوضيح أبعاده، ووسّطه أفقيًا، وطابق الألوان المرجعية.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/reference-task-01.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .grid1 {
>   width: min(1220px, calc(100% - 40px));
>   height: 620px;
>   margin-inline: auto;
>   padding: 30px;
>   display: grid;
>   grid-template-columns: repeat(3, 1fr);
>   grid-template-rows: 60px 1fr;
>   gap: 30px;
>   background: #ddd;
>   counter-reset: item;
> }
>
> .grid1 > div {
>   display: grid;
>   place-items: center;
>   color: white;
>   background: #607d8b;
>   counter-increment: item;
> }
>
> .grid1 > div::before {
>   content: "Element " counter(item);
> }
> ```
>
> يقسم `grid-template-columns` المساحة إلى ثلاثة أعمدة متساوية، وتحدد الصفوف شريطًا قصيرًا وثلاثة عناصر كبيرة. يستخدم `counter()` لإظهار تسميات العناصر من CSS دون تغيير عناصر HTML. أُبقيت الأبعاد والألوان على القيم الظاهرة في المرجع المحلي.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Grid/CSS Grid Assignments 57-64.html|افتح صفحة عرض الحلول 57–64]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
