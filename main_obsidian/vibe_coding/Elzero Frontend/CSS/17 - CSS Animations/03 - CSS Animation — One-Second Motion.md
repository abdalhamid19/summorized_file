---
title: "CSS Animation — One-Second Motion"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - animation
  - تكليف
---

# CSS Animation — One-Second Motion

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها. اجعل العنصر `50×50px` في مركز الصفحة، وطبّق الشكل والألوان والحركة المطلوبة بمدة ثانية واحدة.
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-74-to-77/)
>
> [!info] حدود المصدر
> صفحة التكليف تشير إلى بنية سابقة، ولا تعرض صورة GIF في نصها؛ تعذّر تحميل GIF الرسمي من الموقع (403). الحلقة الرمادية هنا شكل توضيحي، وألوانها ليست مطابقة متحققًا منها.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> html, body { min-height: 100%; margin: 0; }
> body { min-height: 100vh; display: grid; place-items: center; }
> .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #222; border-top-color: #aaa; border-radius: 50%; animation: spin 1s linear infinite; }
> @keyframes spin { to { transform: rotate(360deg); } }
> ```
>
> ### الفكرة الأساسية
>
> يجعل `body` نافذة العرض كاملة ويضع العنصر في منتصفها. تضمن `box-sizing` أن يكون القياس الخارجي للحلقة 50×`50px` رغم الحد. تدور الحلقة باستمرار دورة كل ثانية.
>
> > [!info]- معاني الرموز المستخدمة في الحل
> >
> > ### الدوال والوحدات
> >
> > #### `rotate()`
> >
> > تدير العنصر بالزاوية المحددة.
> >
> > #### `vh`
> >
> > نسبة من ارتفاع نافذة العرض.
> >
> > #### `px`
> >
> > وحدة بكسل `CSS`.
> >
> > #### `s`
> >
> > ثانية.
> >
> > #### `deg`
> >
> > درجة زاوية.
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
> > .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #222; border-top-color: #aaa; border-radius: 50%; animation: spin 1s linear infinite; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `box-sizing` وwidth وheight وborder وborder-`top-color` وborder-`radius` وanimation.
> >
> > #### السطر 04 — `css`
> >
> > ```css
> > @keyframes spin { to { transform: rotate(360deg); } }
> > ```
> >
> > يعرّف مراحل الحركة التي يمكن تشغيلها.
> >
>
> **لقطة صفحة الشرح**
>
> ![[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/assets/solution-page-task-03.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/03 - CSS Animation — One-Second Motion.html|افتح صفحة التكليف 03]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/)
