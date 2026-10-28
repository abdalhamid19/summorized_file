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
> ```css
> body { min-height: 100vh; margin: 0; display: grid; place-items: center; }
> .box { box-sizing: border-box; width: 50px; height: 50px; border: 7px solid #cbd5e1; border-top-color: #1687e8; border-radius: 50%; animation: spin 1s linear infinite; }
> .box:hover { animation-play-state: paused; }
> @keyframes spin { to { transform: rotate(360deg); } }
> ```
>
> يوسّط `body` العنصر في نافذة الصفحة، وتضمن `box-sizing` أن يبقى مقاسه الخارجي 50×50px مع الحد. يكمل دورة كل ثانية ويتوقف عند المرور عليه.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Animations/assets/solution-task-01.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Animations/CSS Animation Assignments 74-77.html|افتح صفحة الحل]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/)
