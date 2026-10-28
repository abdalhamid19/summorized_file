---
title: "CSS Variables — Fallback Values"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-transitions-and-variables
  - تكليف
aliases:
  - CSS Variables — Fallback Values
---

# CSS Variables — Fallback Values

> [!question] السؤال
> نسّق العناصر الثلاثة باستخدام المتغيرين الموجودين في :root. لا تعدّل :root؛ وعند تعطيلها أظهر اللون الأخضر المزرق والحشو في الحالة الأولى، ثم fallback بالأحمر والأسود في الحالة الثانية.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية HTML السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> div {
>   color: var(--mainColor, red);
>   border: 5px solid var(--mainColor, #000);
>   padding: var(--mainPadding, 10px);
>   margin: 20px 0;
>   font-size: 30px;
> }
> ```
>
> تقرأ `var()` القيم من `:root` دون تعديلها. عند حذف المتغيرات، تعمل القيم الاحتياطية: نص أحمر، حد أسود، وحشو 10px. عُدّل الفراغ الطباعي `10 px` الوارد في استخراج الصفحة إلى صيغة CSS الصحيحة `10px`؛ فالفراغ يفصل الرقم عن الوحدة ويجعل القيمة غير صالحة.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/assets/solution-task-03.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Transitions and Variables/CSS Transitions and Variables Assignments 42-45.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
