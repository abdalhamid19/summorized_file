---
title: "CSS Animation — Pause on Hover"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - animation
  - تكليف
---

# CSS Animation — Pause on Hover

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها. اجعل العنصر `50×50px` في مركز الصفحة طولًا وعرضًا، واستعمل الألوان المطلوبة ومدة حركة ثانية واحدة، ثم أوقف الحركة عند `hover`.
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-74-to-77/)
>
> [!info] حدود المصدر
> صفحة التكليف تشير إلى بنية سابقة، ولا تعرض صورة GIF في نصها؛ تعذّر تحميل GIF الرسمي من الموقع (403). شكل الحلقة واللون الأزرق في المعاينة تقريبيان.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ### الكود الكامل للحل
>
> ```css
> body { min-height: 100vh; margin: 0; display: grid; place-items: center; }
> .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #cbd5e1; border-top-color: #1687e8; border-radius: 50%; animation: spin 1s linear infinite; }
> .box:hover { animation-play-state: paused; }
> @keyframes spin { to { transform: rotate(360deg); } }
> ```
>
> ### الفكرة الأساسية
>
> يوسّط `body` العنصر في نافذة الصفحة، وتضمن `box-sizing` أن يبقى مقاسه الخارجي 50×`50px` مع الحد. يكمل دورة كل ثانية ويتوقف عند المرور عليه.
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
> > .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #cbd5e1; border-top-color: #1687e8; border-radius: 50%; animation: spin 1s linear infinite; }
> > ```
> >
> > يستهدف العناصر التي تحمل اسم الصنف المحدد. ويجمع السطر خصائص `box-sizing` وwidth وheight وborder وborder-`top-color` وborder-`radius` وanimation.
> >
> > #### السطر 03 — `css`
> >
> > ```css
> > .box:hover { animation-play-state: paused; }
> > ```
> >
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. ويجمع السطر خصائص `animation-play-state`.
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
> ![[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/assets/solution-page-task-01.png|1200]]
>
> **صفحة الشرح المستقلة**
>
> [[vibe_coding/Elzero Frontend/CSS/17 - CSS Animations/01 - CSS Animation — Pause on Hover.html|افتح صفحة التكليف 01]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/)
