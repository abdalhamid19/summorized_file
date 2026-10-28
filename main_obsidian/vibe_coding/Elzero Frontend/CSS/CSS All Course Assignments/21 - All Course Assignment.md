---
title: 21 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 21
---

# 21 — CSS Shorthand Properties

> [!question] السؤال الرسمي
> اختصر خصائص كل `selector` (محدد CSS) في سطر واحد. المثال الأول يوضح طريقة الاختصار.
>
> لا توجد صورة مرجعية لهذا السؤال في الصفحة الرسمية؛ الكود هو مادة السؤال.
>
> ```css
> .example {
>   margin-top: 10px;
>   margin-right: 20px;
>   margin-bottom: 15px;
>   margin-left: 20px;
>   /* Shorten Code in One Line */
> }
>
> .one {
>   background-color: black;
>   background-image: url("../imgs/one.jpg");
>   background-repeat: no-repeat;
>   background-position: left top;
>   background-size: cover;
>   /* Shorten Code in One Line */
> }
>
> .two {
>   border-top-width: 1px;
>   border-top-style: solid;
>   border-top-color: #000;
>   /* Shorten Code in One Line */
> }
>
> .three {
>   top: 10px;
>   right: 20px;
>   bottom: 10px;
>   left: 20px;
>   /* Shorten Code in One Line */
> }
>
> .four {
>   flex-grow: 3;
>   flex-shrink: 3;
>   flex-basis: 10%;
>   /* Shorten Code in One Line */
> }
>
> .five {
>   flex-direction: column;
>   flex-wrap: wrap;
>   /* Shorten Code in One Line */
> }
> ```

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```css
> .example { margin: 10px 20px 15px 20px; }
> .one { background: black url("../imgs/one.jpg") no-repeat left top / cover; }
> .two { border-top: 1px solid #000; }
> .three { inset: 10px 20px; }
> .four { flex: 3 3 10%; }
> .five { flex-flow: column wrap; }
> ```
>
> ترتيب قيم `margin` هو أعلى، يمين، أسفل، يسار؛ لذلك حافظ السطر الأول على القيم الأربع نفسها.
>
> يجمع `background` اللون والصورة والتكرار والموضع والحجم، وتفصل الشرطة المائلة بين الموضع والحجم. يجمع `border-top` العرض والنمط واللون.
>
> يختصر `inset` الجهات الأربع بالترتيب نفسه الذي تستخدمه `top` و`right` و`bottom` و`left`. ويجمع `flex` قيم النمو والضمور والحجم الأساسي، بينما يجمع `flex-flow` الاتجاه والالتفاف.
>
> لا يوجد مظهر مرئي مطلوب في هذا التكليف؛ صفحة المعاينة تعرض أسطر الاختصار فقط.
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
