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
> **1. نطاق المعاينة**
>
> ```css
> #task-01-preview {
> ```
>
> يحدد هذا السطر لوحة المعاينة فقط، حتى يظل تأثير الألوان داخل التكليف.
>
> **2. قاعدة العنصر الأب**
>
> ```css
> .parent {
> ```
>
> يبدأ قاعدة العنصر الأب؛ وكتابة المحددات التابعة داخلها هي أسلوب **CSS Nesting** (التداخل داخل قاعدة الأب).
>
> **3. محدد العنوان الداخلي**
>
> ```css
> .child .title {
> ```
>
> يختار عنصر العنوان الموجود داخل العنصر الابن.
>
> **4. لون العنوان الداخلي**
>
> ```css
> color: red;
> ```
>
> يلوّن كلمة `Title` الداخلية بالأحمر.
>
> **5. إغلاق قاعدة العنوان الداخلي**
>
> ```css
> }
> ```
>
> يغلق القاعدة التي اختارت العنوان الداخلي.
>
> **6. محدد الابن المباشر**
>
> ```css
> & > .title {
> ```
>
> يستخدم هذا السطر **nesting selector** (محدد التداخل) للإشارة إلى العنصر الأب، ثم يشترط أن يكون العنوان ابنًا مباشرًا له؛ لذلك يطابق جملة Child Title.
>
> **7. لون الابن المباشر**
>
> ```css
> color: blue;
> ```
>
> يلوّن الابن المباشر بالأزرق.
>
> **8. إغلاق قاعدة الابن المباشر**
>
> ```css
> }
> ```
>
> يغلق قاعدة الابن المباشر.
>
> **9. بداية مجموعة المحددات**
>
> ```css
> p,
> ```
>
> يبدأ هذا السطر مجموعة المحددات، ويختار الفقرة داخل العنصر الأب.
>
> **10. محدد عنوان القسم**
>
> ```css
> & ~ .title {
> ```
>
> يختار عنوان القسم باستخدام **general sibling combinator** (محدد الشقيق العام)، الذي يستهدف عنصرًا يشارك العنصر الأب الحاوية نفسها ويأتي بعده.
>
> **11. اللون المشترك**
>
> ```css
> color: green;
> ```
>
> يلوّن الفقرة وعنوان القسم بالأخضر لأنهما ضمن مجموعة المحددات نفسها.
>
> **12. إغلاق القواعد**
>
> ```css
> }
> }
> }
> ```
>
> يغلق القوس الأول قاعدة اللون الأخضر، والثاني قاعدة العنصر الأب، والثالث نطاق المعاينة.
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
