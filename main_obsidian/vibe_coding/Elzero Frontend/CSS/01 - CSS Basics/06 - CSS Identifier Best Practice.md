---
title: "06 - CSS Identifier Best Practice"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف أفضل ممارسات أسماء CSS
---

# 06 - CSS Identifier Best Practice

> [!question] السؤال
> صنّف كل اسم إلى `Good` أو `Bad`، واكتب التصنيف في تعليق قبل الاسم:
>
> ```css
> .USERNAME {}
> .UserName {}
> .user-name {}
> .userName {}
> .usernameprofile {}
> ```
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-1-to-4/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> /* Bad */
> .USERNAME {}
>
> /* Bad */
> .UserName {}
>
> /* Good */
> .user-name {}
>
> /* Bad */
> .userName {}
>
> /* Bad */
> .usernameprofile {}
> ```
>
> الاسم `user-name` واضح لأنه مكتوب بأحرف صغيرة وتفصل الشرطة بين كلماته. الأسماء الأخرى تخالف هذا الأسلوب بكتابة الأحرف الكبيرة أو دمج الكلمات دون فاصل.

## المصدر

[تكليفات CSS للدروس 01–04](https://elzero.org/css-assignments-lesson-from-1-to-4/)
