---
title: "CSS Style Types — External, Internal, and Inline"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - stylesheets
  - تكليف
aliases:
  - CSS Assignment 02
  - أنواع طرق تنسيق CSS
---

# CSS Style Types — External, Internal, and Inline

> [!question] السؤال
> اكتب في تعليق نوع كل Style من التالي:
>
> ```html
> <!-- ? -->
> <link rel="stylesheet" href="css/file.css" />
>
> <!-- ? -->
> <style>
> p {
>   color: red;
> }
> </style>
>
> <!-- ? -->
> <p style="color: blue;">This Is Our Paragraph</p>
> ```

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```html
> <!-- External Style -->
> <link rel="stylesheet" href="css/file.css" />
>
> <!-- Internal Style -->
> <style>
> p {
>   color: red;
> }
> </style>
>
> <!-- Inline Style -->
> <p style="color: blue;">This Is Our Paragraph</p>
> ```
>
> ### `External Style`
>
> يكون التنسيق في ملف CSS منفصل، ويربطه عنصر `link` بصفحة HTML.
>
> ### `Internal Style`
>
> تُكتب قواعد CSS داخل عنصر `style` في صفحة HTML نفسها.
>
> ### `Inline Style`
>
> تُكتب قاعدة CSS مباشرةً في خاصية `style` داخل عنصر HTML.
