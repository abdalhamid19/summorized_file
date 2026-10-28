---
title: "CSS Transform - Skewed Green Banner"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - transforms
  - تكليف
aliases:
  - تكليف CSS Transform 02
---

# CSS Transform - Skewed Green Banner

> [!question] السؤال
> استخدم البنية السابقة، ووسّط العنصر أفقيًا، واستخدم متغيرًا للون الأساسي. أنشئ لافتة متوازية الأضلاع وشريطًا أبيض مائلًا كما في الصورة.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/reference-task-02.png|650]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .banner {
>   --main-color: #009688;
>   position: relative;
>   width: 300px;
>   height: 140px;
>   margin-inline: auto;
>   display: grid;
>   place-items: center;
>   color: white;
>   background: var(--main-color);
>   transform: skewX(20deg);
> }
>
> .banner::before {
>   content: "";
>   position: absolute;
>   inset-block: 0;
>   left: 22px;
>   width: 12px;
>   background: white;
> }
>
> .banner span { display: block; margin-left: 50px; transform: skewX(-20deg); }
> ```
>
> يميل `skewX` جسم اللافتة. تعكس الكلمة الميل حتى تظهر مستقيمة، بينما يبقى الشريط الأبيض في زاويته المائلة. اللون الأساسي متغير ليكون تغييره من مكان واحد.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transform Skew Matrix 3D/CSS Transform Skew Matrix 3D Assignments 68-73.html|افتح صفحة معاينة الحلول 68–73]]

## المصدر

[تكليفات CSS للدروس 68–73](https://elzero.org/css-assignments-lesson-from-68-to-73/)
