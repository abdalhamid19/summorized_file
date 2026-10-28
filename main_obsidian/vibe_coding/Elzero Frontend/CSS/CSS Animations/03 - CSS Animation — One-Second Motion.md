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
> ```css
> html, body { min-height: 100%; margin: 0; }
> body { min-height: 100vh; display: grid; place-items: center; }
> .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #222; border-top-color: #aaa; border-radius: 50%; animation: spin 1s linear infinite; }
> @keyframes spin { to { transform: rotate(360deg); } }
> ```
>
> يجعل `body` نافذة العرض كاملة ويضع العنصر في منتصفها. تضمن `box-sizing` أن يكون القياس الخارجي للحلقة 50×50px رغم الحد. تدور الحلقة باستمرار دورة كل ثانية.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Animations/assets/solution-task-03.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Animations/CSS Animation Assignments 74-77.html|افتح صفحة الحل]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/)
