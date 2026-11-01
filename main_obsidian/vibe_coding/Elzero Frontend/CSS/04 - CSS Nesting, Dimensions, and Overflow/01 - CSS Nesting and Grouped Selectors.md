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
> .parent {
>   .child .title {
>     color: red;
>   }
>
>   & > .title {
>     color: blue;
>   }
>
>   p,
>   & ~ .title {
>     color: green;
>   }
> }
> ```
>
> **شرح الحل سطرًا بسطر**
>
> 1. السطر `.parent {` يبدأ قاعدة العنصر الأب؛ ووضع المحددات التابعة داخلها هو أسلوب **CSS Nesting** (التداخل داخل قاعدة الأب).
> 2. السطر `.child .title {` يختار عنصر `.title` الموجود داخل `.child`، وكلاهما داخل `.parent`.
> 3. السطر `color: red;` يلوّن كلمة `Title` الداخلية بالأحمر.
> 4. القوس `}` يغلق قاعدة `.child .title`.
> 5. السطر `& > .title {` يستخدم `&` (محدد التداخل الذي يشير إلى `.parent`) مع `>` (رمز الابن المباشر)، فيختار عنصر `.title` الذي يعرض `Child Title`.
> 6. السطر `color: blue;` يلوّن الابن المباشر بالأزرق.
> 7. القوس `}` يغلق قاعدة الابن المباشر.
> 8. السطر `p,` يبدأ **Grouped Selectors** (تجميع المحددات)، ويستهدف الفقرة داخل `.parent`.
> 9. السطر `& ~ .title {` يضيف المحدد الثاني؛ ويستهدف `~` عنوان القسم الذي يأتي شقيقًا بعد `.parent` على المستوى نفسه.
> 10. السطر `color: green;` يلوّن المحددين في المجموعة نفسها بالأخضر.
> 11. القوس `}` يغلق قاعدة اللون الأخضر، والقوس الأخير يغلق قاعدة `.parent`.
>
> لم تتغير أي عقدة في HTML.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/04 - CSS Nesting, Dimensions, and Overflow/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/04 - CSS Nesting, Dimensions, and Overflow/CSS Nesting Dimensions Overflow Assignments 13-16.html|افتح صفحة تنفيذ الحلين]]

## المصدر

[تكليفات CSS للدروس 13–16](https://elzero.org/css-assignments-lesson-from-13-to-16/)
