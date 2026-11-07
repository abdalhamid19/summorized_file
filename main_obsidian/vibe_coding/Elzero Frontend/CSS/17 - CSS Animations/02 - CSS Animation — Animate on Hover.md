---
title: "CSS Animation — Animate on Hover"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - animation
  - تكليف
---

# CSS Animation — Animate on Hover

> [!question] السؤال
> أنشئ الشكل المطلوب من بنية التكليف. اجعل العنصر `50×50px` في مركز الصفحة، وابدأ الحركة عند `hover` فقط. مدة حركة العنصر الأزرق الأول ثانية واحدة.
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-74-to-77/)
>
> [!info] حدود المصدر
> تعذّر تحميل GIF التكليف الرسمي من الموقع (403)؛ لذلك ألوان الحلقة ومواضع القطاعات تقريبية. يذكر النص «العنصر الأزرق الأول» دون شرح عدد عناصر الشكل أو توزيعها، لذا تمثل الحلقة الواحدة في المعاينة سلوك الحركة فقط.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body { min-height: 100vh; margin: 0; display: grid; place-items: center; }
> .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #cbd5e1; border-top-color: #1687e8; border-right-color: #e91e63; border-radius: 50%; }
> .box:hover { animation: spin 1s linear infinite; }
> @keyframes spin { to { transform: rotate(360deg); } }
> ```
>
> ### الفكرة الأساسية
>
> يوسّط `body` العنصر في نافذة الصفحة، وتضمن `box-sizing` أن يكون حجمه الخارجي 50×`50px`. لا تبدأ حركة الحلقة إلا عند `hover`، وتستغرق دورة واحدة ثانية.
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
> > [!info]- شرح الحل سطرًا بسطر
> >
> > يبقى الكود الكامل أعلى الإجابة، ويأتي كل سطر مستقلًا مع شرحه العربي تحته.
> >
> > #### السطر 01 — `css`
> >
> > ```css
> > body { min-height: 100vh; margin: 0; display: grid; place-items: center; }
> > ```
> >
> > يحدد العنصر الذي ستطبق عليه قواعد `CSS`. ويجمع السطر خصائص `min-height` وmargin وdisplay وplace-`items`.
> >
> > #### السطر 02 — `css`
> >
> > ```css
> > .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #cbd5e1; border-top-color: #1687e8; border-right-color: #e91e63; border-radius: 50%; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `box-sizing` وwidth وheight وborder وborder-`top-color` وborder-`right-color` وborder-`radius`.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > .box:hover { animation: spin 1s linear infinite; }
> > ```
> >
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. ويجمع السطر خصائص `animation`.
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
> ![[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/assets/solution-page-task-02.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/02 - CSS Animation — Animate on Hover.html|افتح صفحة التكليف 02]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/)
