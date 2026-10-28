---
title: 24 - All Course Assignment
date: 2026-10-28
tags:
  - Elzero
  - CSS
  - assignments
aliases:
  - CSS All Course 24
---

# 24 — CSS Progress Bars

> [!question] السؤال الرسمي
> اعمل الشكل المطلوب كما في الصورة.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-24-reference.jpg]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```html
> <div class="progress-panel">
>   <div class="metric">
>     <div class="label">Money</div>
>     <div class="value">$20.000</div>
>     <div class="track" style="--value: 80%; --color: #1877dc"><div class="fill"></div><span class="badge">80%</span></div>
>   </div>
>   <div class="metric">
>     <div class="label">Projects</div>
>     <div class="value">24</div>
>     <div class="track" style="--value: 55%; --color: #f5a623"><div class="fill"></div><span class="badge">55%</span></div>
>   </div>
>   <div class="metric">
>     <div class="label">Team</div>
>     <div class="value">12</div>
>     <div class="track" style="--value: 75%; --color: #2eaf61"><div class="fill"></div><span class="badge">75%</span></div>
>   </div>
> </div>
> ```
>
> ```css
> .progress-panel {
>   padding: 24px;
>   border-radius: 16px;
>   background: #fff;
> }
>
> .metric { height: 111px; }
> .label { margin-bottom: 4px; color: #858585; font-size: 16px; }
> .value { margin-bottom: 12px; color: #111; font-size: 18px; font-weight: bold; }
>
> .track {
>   position: relative;
>   width: 100%;
>   height: 5px;
>   background: #eee;
> }
>
> .fill {
>   width: var(--value);
>   height: 100%;
>   background: var(--color);
> }
>
> .badge {
>   position: absolute;
>   top: -37px;
>   left: var(--value);
>   padding: 4px 6px;
>   border-radius: 8px;
>   color: #fff;
>   background: var(--color);
>   font-size: 14px;
>   font-weight: bold;
>   transform: translateX(-50%);
> }
>
> .badge::after {
>   content: "";
>   position: absolute;
>   left: 50%;
>   bottom: -5px;
>   border-width: 5px 5px 0;
>   border-style: solid;
>   border-color: var(--color) transparent transparent;
>   transform: translateX(-50%);
> }
> ```
>
> تمثل `--value` نسبة التقدم، وتملأ `.fill` هذا الجزء من المسار الرمادي. يضع `badge` (شارة النسبة) القيمة فوق نهاية الامتلاء، ويصنع `::after` طرفها السفلي الصغير.
>
> كل صف يحدد لونه ونسبته بقيم المتغيرات نفسها، بينما يبقى شكل المؤشر مشتركًا بين الصفوف.
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/solution-task-24.png]]
>
> [افتح صفحة معاينة الأسئلة 17–25](CSS All Course Assignments 17-25.html)

## المصدر

[تكليفات CSS على جميع الدروس — أكاديمية الزيرو](https://elzero.org/css-assignments-lesson-from-1-to-88/)
