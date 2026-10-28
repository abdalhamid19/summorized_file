---
title: "CSS Inheritance of Padding and Border"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - inheritance
  - تكليف
aliases:
  - تكليف وراثة الحشو والحدود في CSS
---

# CSS Inheritance of Padding and Border

> [!question] السؤال
> استخدم بنية HTML الموجودة في التكليف دون تعديلها. اجعل العنصر `p` الابن يرث `padding` و`border` من عنصر `div` الأب؛ أي تغيير في قيم الأب يجب أن ينعكس على الابن دون إضافة تنسيق مباشر له من جديد.
>
> [صفحة التكليفات للدروس 22–26](https://elzero.org/css-assignments-lesson-from-22-to-26/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> بافتراض أن البنية الأصلية تحتوي `p` داخل `div` ذي الصنف `parent`، يكون CSS:
>
> ```css
> .parent {
>   padding: 20px;
>   border: 3px solid #147d73;
> }
>
> .parent > p {
>   padding: inherit;
>   border: inherit;
> }
> ```
>
> الكلمة `inherit` تنقل القيمة المحسوبة من الأب إلى الابن للخاصية المحددة. لذلك إذا غيّرت `padding` أو `border` في `.parent` يتبعها `p` تلقائيًا. أُبقيت قيم المثال والألوان واضحة، ويجب مطابقتها للصورة المرجعية عند عرضها.
>
> **معاينة توضيحية للسلوك**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Inheritance and Typography/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Inheritance and Typography/CSS Inheritance Typography Assignments 22-26.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS للدروس 22–26](https://elzero.org/css-assignments-lesson-from-22-to-26/)
