---
title: "CSS All Course Assignment 08"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - Elzero
  - تكليف
aliases:
  - All Course CSS Assignment 08
---

# CSS All Course Assignment 08

> [!question] المطلوب
> أنشئ البطاقات الظاهرة في الصورة من روابط فارغة؛ لا تعدّل HTML، واستخرج النص المعروض من الخصائص الموجودة في الرابط.
>
> ```html
> <a class="url" href="https://google.com" title="Google"></a>
> <a class="link" href="https://elzero.org/" title="Elzero Academy"></a>
> <a href="https://www.elzero.courses/" title="Elzero Courses"></a>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-08-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> body {
>   margin: 0;
>   padding: 21px 16px 16px;
>   background: #eee;
>   font-family: Arial, sans-serif;
> }
>
> a {
>   display: block;
>   width: max-content;
>   max-width: 100%;
>   margin-bottom: 20px;
>   padding: 19px 20px;
>   box-sizing: border-box;
>   border-radius: 12px;
>   color: #fff;
>   background: #2196f3;
>   font: 700 32px/1.2 Arial, sans-serif;
>   text-decoration: none;
> }
>
> a::before {
>   content: "Name: " attr(title) " | URL: " attr(href);
> }
> ```
>
> العنصر الوهمي `::before` يضيف نصًا قبل محتوى الرابط. الدالة `attr(title)` تقرأ اسم الموقع من الخاصية `title`، و`attr(href)` تقرأ عنوانه؛ وهكذا تظهر البطاقات رغم أن الروابط لا تحتوي على نص داخل HTML.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-08-solution.png]]

المعاينة: [08 - All Course Assignment.html](08%20-%20All%20Course%20Assignment.html).
## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
