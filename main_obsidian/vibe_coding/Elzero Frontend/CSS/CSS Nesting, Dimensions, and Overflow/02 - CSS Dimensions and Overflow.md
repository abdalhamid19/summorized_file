---
title: "CSS Dimensions and Overflow"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - dimensions
  - overflow
  - تكليف
aliases:
  - تكليف أبعاد العناصر وOverflow في CSS
---

# CSS Dimensions and Overflow

> [!question] السؤال
> أنشئ الصناديق بالنصوص والألوان الظاهرة في المثال. اترك `display` على قيمته الأصلية `block`، واجعل عرض العنصر لا يتجاوز `400px`، ثم أخفِ أي جزء من النص يخرج من الصندوق الأخير.
>
> ![الصورة الأصلية للتكليف على موقع الزيرو](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-13-16-1.png)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <div class="box">Title One</div>
> <div class="box">Title Two With More Words</div>
> <div class="box">Title Three With Many Many Many Words</div>
> <div class="box">
>   Title Three With Many Many Many Words Title Three With Many Many Many Words
>   Title Three With Many Many Many Words Title Three With Many Many Many Words
> </div>
> ```
>
> ```css
> .box {
>   box-sizing: border-box;
>   width: fit-content;
>   max-width: 400px;
>   margin: 15px 0;
>   padding: 15px;
>   background-color: brown;
>   color: white;
>   font: 16px / 1.2 "Times New Roman", serif;
> }
>
> .box:last-child {
>   height: 72px;
>   overflow: hidden;
> }
> ```
>
> لم أضف تصريح `display`، لذلك تظل عناصر `div` من نوع `block`. تجعل `width: fit-content` الصندوق ملائمًا لمحتواه، بينما يضع `max-width` سقفًا للعرض. يضمن `box-sizing: border-box` أن يشمل حدّ الـ`400px` المساحة الداخلية والحشو. عند تجاوز النص ارتفاع الصندوق الأخير، تقصّه `overflow: hidden`.
>
> لم يحدد السؤال ارتفاع الصندوق الأخير؛ اخترت `72px` لإظهار القص مع الحفاظ على شكل المثال. يمكنك تغيير هذا الارتفاع إذا أردت إظهار عدد أسطر مختلف.
>
> اللون الأزرق خلف نص الصندوق الأخير في لقطة المصدر هو تظليل تحديد النص داخل الصورة؛ لون الصندوق نفسه بني والنص أبيض.
>
> **معاينة الناتج**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Nesting, Dimensions, and Overflow/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Nesting, Dimensions, and Overflow/CSS Nesting Dimensions Overflow Assignments 13-16.html|افتح صفحة تنفيذ الحلين]]

## المصدر

[تكليفات CSS للدروس 13–16](https://elzero.org/css-assignments-lesson-from-13-to-16/) · [الصورة الأصلية للتكليف الثاني](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-13-16-1.png)
