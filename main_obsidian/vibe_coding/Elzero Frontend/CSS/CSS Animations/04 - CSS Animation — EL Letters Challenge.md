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
> ترسم شبكة من 3 أعمدة و5 صفوف الحرفين، وتوسّط `body` مجموعة الحروف داخل نافذة العرض. مدة حركة E هي 0.75 ثانية وتأخير L يساوي 0.75 ثانية، فتبدأ L بعد انتهاء E. اخترت حركة ظهور تدريجية كمثال؛ مدة الحركة اختيارية في المصدر.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Animations/assets/solution-task-04.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Animations/CSS Animation Assignments 74-77.html|افتح صفحة الحل]]

## المصدر

[تكليفات CSS للدروس 74–77](https://elzero.org/css-assignments-lesson-from-74-to-77/) · [تحدي EL Letters Animations](https://elzero.org/frontend-el-letters-animations/)
