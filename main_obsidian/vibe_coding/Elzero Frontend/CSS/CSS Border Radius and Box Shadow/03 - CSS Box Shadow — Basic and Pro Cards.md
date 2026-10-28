---
title: "CSS Box Shadow — Basic and Pro Cards"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-border-radius-and-box-shadow
  - تكليف
aliases:
  - CSS Box Shadow — Basic and Pro Cards
---

# CSS Box Shadow — Basic and Pro Cards

> [!question] السؤال
> أنشئ مقارنة بطاقتين داخل أب بعرض 550px، مع دائرتي السعر والعناوين الزرقاء والفاصل الوسطي، وأضف بادئات الخواص عند الحاجة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .pricing {
>   width: 550px;
>   margin: 0 auto;
>   display: flex;
>   gap: 24px;
>   position: relative;
> }
>
> .plan {
>   flex: 1;
>   padding: 20px;
>   background: #eee;
>   text-align: center;
> }
>
> .plan h2 {
>   padding: 12px;
>   color: #fff;
>   background: #03a9f4;
>   -webkit-border-radius: 8px;
>   -moz-border-radius: 8px;
>   border-radius: 8px;
> }
>
> .plan .price {
>   width: 200px;
>   height: 200px;
>   margin: 35px auto 0;
>   display: grid;
>   place-items: center;
>   -webkit-border-radius: 50%;
>   -moz-border-radius: 50%;
>   border-radius: 50%;
>   background: #ddd;
> }
>
> .pricing::before {
>   content: "Or";
>   position: absolute;
>   left: 50%;
>   top: 50%;
>   transform: translate(-50%, -50%);
>   -webkit-border-radius: 50%;
>   -moz-border-radius: 50%;
>   border-radius: 50%;
>   padding: 12px;
>   color: #fff;
>   background: #03a9f4;
> }
> ```
>
> استخدمت Flex لعرض البطاقتين جنبًا إلى جنب، ونسبة 50% للدائرة. يظهر «Or» في المنتصف عبر `::before` دون عنصر إضافي. بقي عرض الحاوية 550px كما يطلب التكليف.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/assets/solution-task-03.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Border Radius and Box Shadow/CSS Border Radius and Box Shadow Assignments 38-41.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
