---
title: "All Course Assignment 15 — Outlined Text"
date: 2026-10-28
tags:
  - elzero
  - css
  - assignment
aliases:
  - "CSS All Course 15"
---

# 15 - All Course Assignment

> [!question] المطلوب
> لديك بنية HTML التالية ممنوع التعديل عليها. اكتب CSS لعمل الشكل كما في الصورة.
>
> ```html
> <h2>Elzero Web School</h2>
> ```
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-15-reference.png]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> **CSS**
>
> ```css
> h2 {
>   margin: 0;
>   color: #9c27b0;
>   font: 700 clamp(38px, 7vw, 88px) / 1 Arial, sans-serif;
>   -webkit-text-fill-color: transparent;
>   -webkit-text-stroke: 2px #9c27b0;
> }
> ```
> **شرح الحل**
> تجعل `-webkit-text-fill-color: transparent` داخل الحروف شفافًا، وترسم `-webkit-text-stroke` حدًا بنفسجيًا بسماكة بكسلين. تبقى بنية `h2` كما وردت في السؤال.
> لمراجعة الصورة بجوار المرجع: [[CSS All Course Assignments.html|صفحة المعاينات]].
> ![[vibe_coding/Elzero Frontend/CSS/CSS All Course Assignments/assets/assignment-15-solution.png]]

## المصدر
[التكليفات الرسمية لـCSS من الدرس 1 إلى 88](https://elzero.org/css-assignments-lesson-from-1-to-88/)
