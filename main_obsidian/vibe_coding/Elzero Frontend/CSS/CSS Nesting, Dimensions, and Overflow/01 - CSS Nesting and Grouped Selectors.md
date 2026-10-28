---
title: "CSS Nesting and Grouped Selectors"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف محددات CSS المتداخلة وتجميع المحددات
---

# CSS Nesting and Grouped Selectors

> [!question] السؤال
> حافظ على بنية HTML كما هي. لوّن كلمة `Title` بالأحمر، وجملة `Child Title` بالأزرق، وجملتي `Paragraph Content` و`Section Title` بالأخضر، ثم اجمع المحددات التي تستخدم اللون نفسه.
>
> ```html
> <div class="parent">
>   <div class="child">This Is Child <span class="title">Title</span></div>
>   <span class="title">Child Title</span>
>   <p>Paragraph Content</p>
> </div>
> <div class="title">Section Title</div>
> ```
>
> [صفحة التكليف الأصلية](https://elzero.org/css-assignments-lesson-from-13-to-16/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .parent .child .title {
>   color: red;
> }
>
> .parent > .title {
>   color: blue;
> }
>
> p,
> body > .title {
>   color: green;
> }
> ```
>
> يختار المحدد الأول كلمة `Title` داخل العنصر `.child` المتداخل، بينما يختار المحدد الثاني عنصر `.title` الموجود مباشرة داخل `.parent`. جمعت المحددات التي تحتاج اللون الأخضر في قاعدة واحدة؛ فيطابق `p` الفقرة، ويطابق `body > .title` العنوان الموجود مباشرة داخل `body` في البنية الأصلية. لم تتغير أي عقدة في HTML.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Nesting, Dimensions, and Overflow/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Nesting, Dimensions, and Overflow/CSS Nesting Dimensions Overflow Assignments 13-16.html|افتح صفحة تنفيذ الحلين]]

## المصدر

[تكليفات CSS للدروس 13–16](https://elzero.org/css-assignments-lesson-from-13-to-16/)
