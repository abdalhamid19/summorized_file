---
title: "CSS Grid - Narrow Side Columns"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 03
---

# CSS Grid - Narrow Side Columns

> [!question] السؤال
> استخدم Grid لبناء الشكل المرجعي ذي ثمانية عناصر، واجعل الأب ذا أبعاد واضحة ومتمركزًا أفقيًا، واحتفظ بالألوان المرجعية.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/reference-task-03.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .grid3 {
>   width: min(1220px, calc(100% - 40px));
>   height: 540px;
>   margin-inline: auto;
>   padding: 30px;
>   display: grid;
>   grid-template-columns: 18px 1fr 1fr 18px;
>   grid-template-rows: 1fr 70px;
>   gap: 30px;
>   background: #ddd;
> }
>
> .grid3 > div {
>   display: grid;
>   place-items: center;
>   color: white;
>   background: #444;
> }
> ```
>
> تنشئ الأعمدة الطرفية الضيقة بعرض 18px، ويشغل العنصران الأوسطان بقية المساحة بالتساوي. توضح الصورتان المرجعيتان أن التخطيط يتكون من أربعة أعمدة وصفين؛ اترك ترتيب العناصر كما هو في HTML.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/solution-task-03.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Grid/CSS Grid Assignments 57-64.html|افتح صفحة عرض الحلول 57–64]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
