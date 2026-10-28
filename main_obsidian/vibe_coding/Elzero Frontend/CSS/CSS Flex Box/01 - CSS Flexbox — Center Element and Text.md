---
title: "CSS Flexbox — Center Element and Text"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Center Element and Text
---

# CSS Flexbox — Center Element and Text

> [!question] السؤال
> استخدم بنية عنصر واحد كما هي. اجعل عرضه وارتفاعه 100px، ووسّطه أفقيًا، ثم وسّط كلمة Elzero داخله بالطول والعرض باستخدام Flex، مع الألوان المرجعية.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> div {
>   width: 100px;
>   height: 100px;
>   margin: 0 auto;
>   display: flex;
>   justify-content: center;
>   align-items: center;
>   border-radius: 50%;
>   background: #eee;
>   color: #ff5722;
>   font-weight: bold;
>   box-shadow: -12px 0 #03a9f4, 12px 0 #ff5722;
> }
> ```
>
> يعمل `justify-content` على المحور الرئيسي و`align-items` على المحور المتعامد. هامش `auto` يوسّط العنصر نفسه داخل الصفحة، أما Flex فيوسّط النص داخله.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/solution-task-01.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
