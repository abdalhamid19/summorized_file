---
title: "01 - CSS Float and Opacity - Dynamic Float Grid with Calc"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
  - تكليف
aliases:
  - تكليف Dynamic Float Grid with Calc
---

# 01 - CSS Float and Opacity - Dynamic Float Grid with Calc

> [!question] السؤال
> العنصر الأب عرضه 800px بلا `padding`. اجعل الفواصل الأفقية والرأسية 15px، واجعل عرض العناصر ديناميكيًا بحيث يبقى التخطيط صالحًا عند تغيير عرض الأب إلى 1000px.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-27-to-29/>)
>
> [!info] حدود المصدر والمطابقة
> تحدد صفحة التكليف عرض الأب والفواصل وضرورة بقاء العرض ديناميكيًا، لكن تعذّر علي قراءة الصورة المرجعية أو رؤية البنية السابقة. افترضت أربعة أعمدة وثمانية عناصر في المعاينة فقط؛ غيّر عدد الأعمدة إذا أظهرت الصورة غير ذلك.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> #task-01 .parent {
>   width: 800px;
>   margin: 0 auto;
>   --gap: 15px;
> }
> #task-01 .parent::after {
>   content: "";
>   display: block;
>   clear: both;
> }
> #task-01 .item {
>   float: left;
>   box-sizing: border-box;
>   width: calc((100% - 3 * var(--gap)) / 4);
>   min-height: 100px;
>   margin: 0 var(--gap) var(--gap) 0;
> }
> #task-01 .item:nth-child(4n) { margin-right: 0; }
> @media (min-width: 900px) {
>   #task-01 .parent { width: 1000px; }
> }
> ```
>
> **شرح الحل**
>
> تحسب `calc()` عرض أربعة أعمدة بعد طرح ثلاثة فواصل من عرض الأب، لذا لا نثبت عرض العنصر بالبكسل. يزيل محدد كل عنصر رابع الفاصل الخارجي الزائد. يحرر `clear` الأب من أثر العناصر العائمة.
>
> **معاينة الكود**
>
> افتح [[vibe_coding/Elzero Frontend/CSS/CSS Float and Opacity/CSS Float and Opacity Assignments 27–29 Demo.html|صفحة المعاينة للمجموعة]]؛ هناك تستطيع مشاهدة هذا الجزء مع بقية التكليفات في هذه المجموعة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Float and Opacity/assets/solution-overview.png|900]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-27-to-29/)
