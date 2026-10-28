---
title: "CSS Transform - Variable Color Skew Shape"
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

# CSS Transform - Variable Color Skew Shape

> [!question] السؤال
> استخدم البنية السابقة، واجعل عرض العنصر 150px، ووسّطه أفقيًا، وعرّف اللون الأساسي بمتغير CSS. طابق الشكل والألوان المرجعية.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/reference-task-01.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .shape {
>   --main-color: #ff5722;
>   width: 150px;
>   height: 140px;
>   margin-inline: auto;
>   display: grid;
>   place-items: center;
>   color: white;
>   background: var(--main-color);
>   clip-path: polygon(0 0, 50% 13%, 100% 0, 91% 50%, 100% 100%, 50% 87%, 0 100%, 9% 50%);
> }
> ```
>
> يقص `clip-path` الزوايا للداخل والخارج لتكوين شكل الساعة الرملية الظاهر. المتغير `--main-color` يحقق شرط تحديد اللون الأساسي من قيمة واحدة. العرض في الصورة المرجعية يقارب 210px؛ صفحة التكليف النصية تذكر 150px، لذا اعتمدت 150px في ملاحظة السؤال وأبقيت قيمة المثال توضيحية.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/CSS Transform Skew Matrix 3D Assignments 68-73.html|افتح صفحة معاينة الحلول 68–73]]

## المصدر

[تكليفات CSS للدروس 68–73](https://elzero.org/css-assignments-lesson-from-68-to-73/)
