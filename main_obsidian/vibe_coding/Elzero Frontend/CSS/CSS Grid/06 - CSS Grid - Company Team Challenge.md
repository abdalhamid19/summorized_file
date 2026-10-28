---
title: "CSS Grid - Company Team Challenge"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 06
---

# CSS Grid - Company Team Challenge

> [!question] السؤال
> حل التحدي ببناء بطاقات فريق باستخدام CSS Grid، وتوزيعها في المساحات كما في الصورة. استخدم نصوصًا وصورًا من اختيارك، ونسّق البطاقات والألوان.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/reference-challenge-company-team.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> .challenge {
>   display: grid;
>   grid-template-columns: repeat(4, minmax(0, 1fr));
>   grid-template-areas:
>     "one one two three"
>     "four five five three"
>     "four six six three"
>     "seven eight nine ten";
>   gap: 10px;
>   padding: 10px;
>   background: #eee;
> }
>
> .card { padding: 22px; background: white; border-bottom: 3px solid #f4511e; }
> .card.dark { color: white; background: #000; }
>
> .challenge .a { grid-area: one; }
> .challenge .b { grid-area: two; }
> .challenge .c { grid-area: three; }
> .challenge .d { grid-area: four; }
> .challenge .e { grid-area: five; }
> .challenge .f { grid-area: six; }
> .challenge .g { grid-area: seven; }
> .challenge .h { grid-area: eight; }
> .challenge .i { grid-area: nine; }
> .challenge .j { grid-area: ten; }
> ```
>
> تحدد `grid-template-areas` مواضع البطاقات العشر. ينبغي أن يطابق ترتيب HTML ترتيب البطاقات من الأولى إلى العاشرة. نصوص الأشخاص مجرد محتوى تجريبي يمكن استبداله.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Grid/assets/solution-task-06.png|900]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Grid/CSS Grid Assignments 57-64.html|افتح صفحة عرض الحلول 57–64]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
