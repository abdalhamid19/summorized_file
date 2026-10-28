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
> ```css
> body { min-height: 100vh; margin: 0; display: grid; place-items: center; }
> .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #cbd5e1; border-top-color: #1687e8; border-right-color: #e91e63; border-radius: 50%; }
> .box:hover { animation: spin 1s linear infinite; }
> @keyframes spin { to { transform: rotate(360deg); } }
> ```
>
> يوسّط `body` العنصر في نافذة الصفحة، وتضمن `box-sizing` أن يكون حجمه الخارجي 50×50px. لا تبدأ حركة الحلقة إلا عند `hover`، وتستغرق دورة واحدة ثانية.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Animations/assets/solution-task-02.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Animations/CSS Animation Assignments 74-77.html|افتح صفحة الحل]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/)
