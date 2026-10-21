---
title: "CSS Visibility and Preserved Layout Space"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - display
  - visibility
  - تكليف
aliases:
  - CSS Border Assignment 02
  - إخفاء العنصر مع الاحتفاظ بمساحته
---

# CSS Visibility and Preserved Layout Space

> [!question] السؤال
> استخدم بنية HTML التالية من دون تعديلها. اجعل عرض العناصر `400px`، ثم أخفِ العنصر الثاني مع الاحتفاظ بمكانه في مساحة العمل، ونسّق العنصرين الظاهرين كما في الصورة.
>
> ```html
> <div class="element element-1">This Is Important Note</div>
> <div class="element element-2">This Is Important Note</div>
> <div class="element element-3">This Is Important Note</div>
> ```
>
> الصورة المرجعية:
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border, Outline, and Display/assets/reference-task-02.png|900]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .element {
>   box-sizing: border-box;
>   width: 400px;
>   max-width: 100%;
>   padding: 10px;
>   margin: 20px 0;
>   background-color: #eee;
> }
>
> .element-1 {
>   border-left: 5px solid #e91e63;
> }
>
> .element-2 {
>   visibility: hidden;
> }
>
> .element-3 {
>   border-left: 5px solid #009688;
> }
> ```
>
> يحدد `box-sizing: border-box` العرض الإجمالي للعنصر بـ`400px` بما فيه الحشو والحد. تُخفي `visibility: hidden` العنصر الثاني ومحتواه بصريًا، لكنها تترك صندوقه في التخطيط؛ لهذا تبقى المساحة الفارغة بين العنصرين الظاهرين. تحتفظ البنية المعطاة كما هي، ويضيف `border-left` الشريط الوردي للأول والتركوازي للثالث.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border, Outline, and Display/assets/solution-task-02.png|800]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Border, Outline, and Display/CSS Border Outline Display Assignments 09-12.html|افتح صفحة تنفيذ الحلين]]

## المصدر

[صفحة تكليفات CSS للدروس 09–12](https://elzero.org/css-assignments-lesson-from-9-to-12/) · [الصورة المرجعية للتكليف الثاني](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-9-12-2.png)
