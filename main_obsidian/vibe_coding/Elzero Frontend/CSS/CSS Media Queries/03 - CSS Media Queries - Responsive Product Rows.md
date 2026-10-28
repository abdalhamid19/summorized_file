---
title: "CSS Media Queries - Responsive Product Rows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - media_queries
  - responsive_design
  - تكليف
aliases:
  - تكليف CSS Media Queries 03
---

# CSS Media Queries - Responsive Product Rows

> [!question] السؤال
> اعمل نفس الشكل والألوان، ووزّع العناصر بالعدد الظاهر في كل مقاس شاشة. استخدم `Media Queries` من دون إطار عمل.
>
> صورة السؤال للشاشات الكبيرة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/reference-task-03-large.png|900]]
>
> صورة السؤال للشاشات المتوسطة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/reference-task-03-medium.png|900]]
>
> صورة السؤال للشاشات الصغيرة والجوالات:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/reference-task-03-small.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .products {
>   display: grid;
>   grid-template-columns: repeat(2, minmax(0, 1fr));
>   grid-template-areas:
>     "one one"
>     "two three"
>     "four four";
>   gap: 30px;
>   width: calc(100% - 60px);
>   max-width: 1050px;
>   margin: 45px auto;
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
> .product-one { grid-area: one; }
> .product-two { grid-area: two; }
> .product-three { grid-area: three; }
> .product-four { grid-area: four; }
>
> @media (max-width: 1099px) and (min-width: 900px) {
>   .products {
>     grid-template-columns: repeat(3, minmax(0, 1fr));
>     grid-template-areas:
>       "one one one"
>       "two three four";
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
>     grid-template-areas:
>       "one"
>       "two"
>       "three"
>       "four";
>   }
>
>   .product h2 {
>     color: #000;
>   }
> }
> ```
>
> في العرض الواسع يشغل العنصر الأول صفًا كاملًا، ويأتي العنصران الثاني والثالث بجانبهما في الصف التالي، ثم يشغل الرابع صفًا كاملًا. في المقاس المتوسط يظهر الأول بعرض كامل ثم تأتي العناصر الثلاثة في صف واحد. على الهاتف يتحول التخطيط إلى عمود واحد. اخترت نقطتي التحول `1099px` و`899px` لأنها غير محددة في نص التكليف.
>
> بنية البطاقات أُعيد بناؤها من الصور المرجعية؛ صور التكليف لا تعرض شيفرة HTML الأصلية. قياسات الحاوية تقريبية بما يطابق توزيع العناصر الظاهر.
>
> **معاينة الحل**
>
> شاشة كبيرة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-03-large.png|900]]
>
> شاشة متوسطة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-03-medium.png|900]]
>
> شاشة صغيرة:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/assets/solution-task-03-small.png|700]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Media Queries/CSS Media Queries Assignments 83-85.html|افتح صفحة معاينة الحلول 83–85]]

## المصدر

[تكليفات CSS للدروس 83–85](https://elzero.org/css-assignments-lesson-from-83-to-85/)
