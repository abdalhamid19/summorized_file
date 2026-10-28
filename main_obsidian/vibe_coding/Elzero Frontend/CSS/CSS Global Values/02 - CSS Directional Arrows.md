---
title: "CSS Directional Arrows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - pseudo-elements
  - تكليف
aliases:
  - تكليف الأسهم الاتجاهية في CSS
---

# CSS Directional Arrows

> [!question] السؤال
> أنشئ صنفًا أساسيًا اسمه `arrow` وأصناف اتجاه `top` و`right` و`bottom` و`left`. لا يظهر السهم إلا عند الجمع بين `arrow` وصنف الاتجاه، ويظل في منتصف العنصر مهما اختلف عرضه أو ارتفاعه.
>
> ![الصورة المرجعية للتكليف](https://elzero.org/wp-content/uploads/2021/03/css-assignments-lessons-86-88-1.png)
>
> [صفحة التكليف الأصلية](https://elzero.org/css-assignments-lesson-from-86-to-88/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <div class="arrow top"></div>
> <div class="arrow right"></div>
> <div class="arrow bottom"></div>
> <div class="arrow left"></div>
> ```
>
> ```css
> .arrow {
>   --arrow-color: #e91e63;
>   position: relative;
>   width: 160px;
>   height: 110px;
>   border: 1px solid #cbd5e1;
>   background: #f8fafc;
> }
>
> .arrow.top::before,
> .arrow.right::before,
> .arrow.bottom::before,
> .arrow.left::before {
>   position: absolute;
>   top: 50%;
>   left: 50%;
>   width: 0;
>   height: 0;
>   border: 14px solid transparent;
>   content: "";
>   transform: translate(-50%, -50%);
> }
>
> .arrow.top::before {
>   border-bottom-color: var(--arrow-color);
> }
>
> .arrow.right::before {
>   border-left-color: var(--arrow-color);
> }
>
> .arrow.bottom::before {
>   border-top-color: var(--arrow-color);
> }
>
> .arrow.left::before {
>   border-right-color: var(--arrow-color);
> }
> ```
>
> تقصر المحددات على وجود `arrow` مع الاتجاه؛ لذلك لا يعمل `top` وحده. يرسم العنصر الوهمي `::before` مثلثًا بالحدود الشفافة، ثم يلوّن الحد الموافق للاتجاه المطلوب. تحدد نسبتا `top` و`left` المنتصف اعتمادًا على أبعاد الصندوق لا على رقم ثابت.
>
> لم تُذكر درجة لون السهم في النص المستخرج من الصفحة؛ استخدمت لونًا ورديًا للمعاينة، ويمكن استبدال `--arrow-color` بلون الصورة المرجعية.
>
> **معاينة التطبيق**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Global Values/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Global Values/CSS Global Values Assignments 86-88.html|افتح صفحة الحل]]

## المصدر

[تكليفات CSS للدروس 86–88](https://elzero.org/css-assignments-lesson-from-86-to-88/)
