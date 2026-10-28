---
title: "CSS Media Queries - Four Responsive Products"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - media_queries
  - responsive_design
  - تكليف
aliases:
  - تكليف CSS Media Queries 02
---

# CSS Media Queries - Four Responsive Products

> [!question] السؤال
> اعمل نفس الشكل والألوان، ووزّع العناصر الأربعة بالعدد الظاهر في كل مقاس شاشة. استخدم `Media Queries` من دون إطار عمل.
>
> صورة السؤال للشاشات الكبيرة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/reference-task-02-large.png|900]]
>
> صورة السؤال للشاشات المتوسطة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/reference-task-02-medium.png|900]]
>
> صورة السؤال للشاشات الصغيرة والجوالات:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/reference-task-02-small.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .products {
>   display: grid;
>   grid-template-columns: repeat(4, minmax(0, 1fr));
>   gap: 30px;
>   width: 93%;
>   max-width: 1200px;
>   margin: 50px auto;
> }
>
> .product {
>   min-height: 92px;
>   display: grid;
>   align-content: center;
>   gap: 8px;
>   border: 1px solid #ddd;
>   background: #eee;
>   text-align: center;
> }
>
> .product h2 {
>   margin: 0;
>   color: #009688;
>   font-size: 20px;
> }
>
> .product p {
>   margin: 0;
>   color: #333;
>   font-size: 16px;
> }
>
> @media (max-width: 1099px) {
>   .products {
>     grid-template-columns: repeat(2, minmax(0, 1fr));
>   }
>
>   .product h2 {
>     color: #f00;
>   }
> }
>
> @media (max-width: 899px) {
>   .products {
>     grid-template-columns: 1fr;
>   }
>
>   .product h2 {
>     color: #000;
>   }
> }
> ```
>
> تعرض الشبكة أربعة أعمدة في العرض الواسع، وعمودين في العرض المتوسط، وعمودًا واحدًا في الهاتف. يتبدل لون العنوان من الأخضر المزرق إلى الأحمر ثم الأسود كما في الصور. اخترت نقطتي التحول `1099px` و`899px` لتقسيم المقاسات؛ التكليف يعرض حالات مرئية ولا يحدد أرقامًا إلزامية لنقاط التحول.
>
> بنية بطاقات هذه المعاينة أُعيد بناؤها لتطابق التوزيع والألوان الظاهرة في المراجع؛ صور التكليف لا تعرض شيفرة HTML الأصلية.
>
> **معاينة الحل**
>
> شاشة كبيرة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-02-large.png|900]]
>
> شاشة متوسطة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-02-medium.png|900]]
>
> شاشة صغيرة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-02-small.png|700]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/CSS Media Queries Assignments 83-85.html|افتح صفحة معاينة الحلول 83–85]]

## المصدر

[تكليفات CSS للدروس 83–85](https://elzero.org/css-assignments-lesson-from-83-to-85/)
