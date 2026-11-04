---
title: "CSS Animation — EL Letters Challenge"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - animation
  - تكليف
---

# CSS Animation — EL Letters Challenge

> [!question] السؤال
> ارسم الحرفين E وL بالحركة والألوان نفسها. يجب أن تبدأ الحركة الثانية بعد انتهاء الأولى. استخدم `Flexbox` أو `Grid` لتكوين الحروف.
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-74-to-77/)
>
> [!info] حدود المصدر
> تنص صفحة التحدي على رسم E وL بالألوان نفسها، وعلى أن تبدأ الحركة الثانية بعد اكتمال الأولى، من دون مدة إلزامية. تعذّر تحميل صورة GIF الرسمية (استجاب الموقع برفض 403)؛ لذلك رسم الحروف واللون الأزرق وحركة الظهور في المعاينة أمثلة تقريبية وليست مطابقة مرئية مؤكدة.
> صفحة التحدي الأصلية: [EL Letters Animations](https://elzero.org/frontend-el-letters-animations/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> html, body { min-height: 100%; margin: 0; }
> body { min-height: 100vh; display: grid; place-items: center; }
> .letters { width: max-content; display: flex; align-items: center; justify-content: center; gap: 18px; }
> .letter { width: 110px; height: 166px; display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(5, 1fr); gap: 5px; }
> .letter span { border-radius: 4px; background: transparent; }
> .letter-e span:nth-child(-n+3), .letter-e span:nth-child(4), .letter-e span:nth-child(n+7):nth-child(-n+9), .letter-e span:nth-child(10), .letter-e span:nth-child(n+13) { background: #1477d4; }
> .letter-l span:nth-child(1), .letter-l span:nth-child(4), .letter-l span:nth-child(7), .letter-l span:nth-child(10), .letter-l span:nth-child(n+13) { background: #1477d4; }
> .letter-e { animation: letter-reveal .75s ease-out both; }
> .letter-l { animation: letter-reveal .75s ease-out .75s both; }
> @keyframes letter-reveal { from { opacity: 0; transform: translateY(24px) scale(.7); } to { opacity: 1; transform: translateY(0) scale(1); } }
> ```
>
> ### الفكرة الأساسية
>
> ترسم شبكة من 3 أعمدة و5 صفوف الحرفين، وتوسّط `body` مجموعة الحروف داخل نافذة العرض. مدة حركة `E` هي 0.75 ثانية وتأخير `L` يساوي 0.75 ثانية، فتبدأ `L` بعد انتهاء `E`. اخترت حركة ظهور تدريجية كمثال؛ مدة الحركة اختيارية في المصدر.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### الدوال والوحدات
> >
> > #### `repeat()`
> >
> > تكرر مسارًا أو مجموعة مسارات بعدد محدد في تخطيط `Grid`.
> >
> > #### `repeat()`
> >
> > تكرر مسارًا أو مجموعة مسارات بعدد محدد في تخطيط `Grid`.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `nth-child()`
> >
> > تختار عنصرًا بحسب ترتيبه بين إخوته، ويمكن استخدام صيغة مثل `n` + 4 لاختيار ما بعد العنصر الثالث.
> >
> > #### `translateY()`
> >
> > تحرك العنصر رأسيًا على محور `Y`.
> >
> > #### `scale()`
> >
> > تكبر العنصر أو تصغره على المحورين.
> >
> > #### `translateY()`
> >
> > تحرك العنصر رأسيًا على محور `Y`.
> >
> > #### `scale()`
> >
> > تكبر العنصر أو تصغره على المحورين.
> >
> > #### `vh`
> >
> > نسبة من ارتفاع نافذة العرض.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > #### `fr`
> >
> > جزء من مساحة `Grid`.
> >
> > #### `s`
> >
> > ثانية.
> >
> > ### بنية القاعدة
> >
> > #### `{`
> >
> > يفتح مجموعة التصريحات.
> >
> > #### `}`
> >
> > يغلق مجموعة التصريحات.
> >
> > #### `:`
> >
> > يفصل الخاصية عن القيمة.
> >
> > #### `;`
> >
> > ينهي تصريح `CSS`.
> >
> > #### `,`
> >
> > يفصل بين محددات أو قيم.
> >
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `css`
> >
> > ```css
> > html, body { min-height: 100%; margin: 0; }
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`. ويجمع السطر خصائص `min-height` وmargin.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> > body { min-height: 100vh; display: grid; place-items: center; }
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`. ويجمع السطر خصائص `min-height` وdisplay وplace-`items`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > .letters { width: max-content; display: flex; align-items: center; justify-content: center; gap: 18px; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `width` وdisplay وalign-`items` وjustify-`content` وgap.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > .letter { width: 110px; height: 166px; display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(5, 1fr); gap: 5px; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `width` وheight وdisplay وgrid-`template-columns` وgrid-`template-rows` وgap.
> >
> > #### السطر 05 — `css`
> >
> > ```css
> > .letter span { border-radius: 4px; background: transparent; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `border-radius` وbackground.
> >
> > #### السطر 06 — `css`
> >
> > ```css
> > .letter-e span:nth-child(-n+3), .letter-e span:nth-child(4), .letter-e span:nth-child(n+7):nth-child(-n+9), .letter-e span:nth-child(10), .letter-e span:nth-child(n+13) { background: #1477d4; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `background`.
> >
> > #### السطر 07 — `css`
> >
> > ```css
> > .letter-l span:nth-child(1), .letter-l span:nth-child(4), .letter-l span:nth-child(7), .letter-l span:nth-child(10), .letter-l span:nth-child(n+13) { background: #1477d4; }
> > ```
> >
> > يختار عنصرًا بحسب ترتيبه أو علاقته بإخوته. ويجمع السطر خصائص `background`.
> >
> > #### السطر 08 — `css`
> >
> > ```css
> > .letter-e { animation: letter-reveal .75s ease-out both; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `animation`.
> >
> > #### السطر 09 — `css`
> >
> > ```css
> > .letter-l { animation: letter-reveal .75s ease-out .75s both; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `animation`.
> >
> > #### السطر 10 — `css`
> >
> > ```css
> > @keyframes letter-reveal { from { opacity: 0; transform: translateY(24px) scale(.7); } to { opacity: 1; transform: translateY(0) scale(1); } }
> > ```
> >
> > يعرّف مراحل الحركة التي يمكن تشغيلها.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/assets/solution-page-task-04.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/04 - CSS Animation — EL Letters Challenge.html|افتح صفحة التكليف 04]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/) · [تحدي EL Letters Animations](https://elzero.org/frontend-el-letters-animations/)
