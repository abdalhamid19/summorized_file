---
title: "CSS Transform - Layered Rotated Cards"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 01
---

# CSS Transform - Layered Rotated Cards

> [!question] السؤال
> استخدم بنية HTML كما هي. اجعل العنصر 300×200px، ووسّطه أفقيًا، ونسّق الشكل والألوان كما في الصورة.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/assets/reference-task-01.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .card {
>   position: relative;
>   width: 300px;
>   height: 200px;
>   margin-inline: auto;
>   display: grid;
>   place-items: center;
>   color: #03a9f4;
>   background: #eee;
>   font: bold 34px Georgia, serif;
> }
>
> .card::before,
> .card::after {
>   content: "";
>   position: absolute;
>   inset: 0;
>   z-index: -1;
> }
>
> .card::before { background: #e91e63; transform: rotate(6deg); }
> .card::after { background: #03a9f4; transform: rotate(-6deg); }
> ```
>
> تُدير `::before` و`::after` الشكلين الملونين خلف البطاقة الأصلية باتجاهين متعاكسين. تبقى الخلفية الرمادية والنص في المقدمة كما في معاينة الصفحة.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Scale Rotate Translate/CSS Transform Scale Rotate Translate Assignments 65-67.html|افتح صفحة معاينة الحلول 65–67]]

## المصدر

[تكليفات CSS للدروس 65–67](https://elzero.org/css-assignments-lesson-from-65-to-67/)
