---
title: "05 - CSS Identifier Validity"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - تكليف صلاحية أسماء CSS
---

# 05 - CSS Identifier Validity

> [!question] السؤال
> صنّف أسماء الـ `Identifier` التالية إلى `Valid` أو `Not Valid`، واكتب التصنيف في تعليق قبل كل اسم:
>
> ```css
> ._user-name {}
> .-user-name {}
> .1user-name {}
> .@user-name {}
> .user@name {}
> ._user10name {}
> .u {}
> ```
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-1-to-4/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> /* Valid */
> ._user-name {}
>
> /* Valid */
> .-user-name {}
>
> /* Not Valid */
> /* .1user-name {} */
>
> /* Not Valid */
> /* .@user-name {} */
>
> /* Not Valid */
> /* .user@name {} */
>
> /* Valid */
> ._user10name {}
>
> /* Valid */
> .u {}
> ```
>
> أبقيت المحددات غير الصالحة داخل تعليقات CSS حتى لا تُفسد تحليل بقية الكود عند نسخه. يسمح الاسم بالشرطة السفلية أو الشرطة العادية في البداية، لكنه لا يبدأ برقم ولا يحتوي `@`.

## المصدر

[تكليفات CSS للدروس 01–04](https://elzero.org/css-assignments-lesson-from-1-to-4/)
