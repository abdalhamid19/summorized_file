---
title: "CSS Border Colors and Outline"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - border
  - outline
  - تكليف
aliases:
  - CSS Border Assignment 01
  - الحدود الملونة وOutline
---

# CSS Border Colors and Outline

> [!question] السؤال
> أنشئ ثلاثة عناصر `div` من دون تحديد عرض، واجعلها بجانب بعضها كما في المثال وبالألوان نفسها. اجعل سمك كل حافة `5px`.
>
> الصورة المرجعية:
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border, Outline, and Display/assets/reference-task-01.png|900]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <div class="shape shape-one">Shape 1</div>
> <div class="shape shape-two">Shape 2</div>
> <div class="shape shape-three">Shape 3</div>
> ```
>
> ```css
> .shape {
>   display: inline-block;
>   padding: 20px;
>   margin: 20px;
>   background-color: #d3d3d3;
> }
>
> .shape-one {
>   border: 5px solid red;
>   outline: 5px solid black;
> }
>
> .shape-two {
>   border: 5px solid;
>   border-color: blue green;
> }
>
> .shape-three {
>   border: 5px dashed;
>   border-color: red green blue yellow;
> }
> ```
>
> تعرض `inline-block` العناصر جنبًا إلى جنب مع احتفاظ كل عنصر بعرضه الطبيعي؛ لم نحدد `width`. يضيف العنصر الأول `outline` أسود خارج الحد الأحمر. في العنصر الثاني يوزّع التصريح ذو اللونين الأزرق على الأعلى والأسفل والأخضر على الجانبين. أما ترتيب الألوان الأربعة في العنصر الثالث فهو أعلى، ثم يمين، ثم أسفل، ثم يسار.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border, Outline, and Display/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Border, Outline, and Display/CSS Border Outline Display Assignments 09-12.html|افتح صفحة تنفيذ الحلين]]

## المصدر

[صفحة تكليفات CSS للدروس 09–12](https://elzero.org/css-assignments-lesson-from-9-to-12/) · [الصورة المرجعية للتكليف الأول](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-9-12-1.png)
