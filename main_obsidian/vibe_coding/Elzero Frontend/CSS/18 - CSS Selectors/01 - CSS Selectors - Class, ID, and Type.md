---
title: "CSS Selectors — Class, ID, and Type"
date: 2026-10-21
tags:
  - vibe_coding
  - frontend
  - CSS
  - selectors
  - تكليف
aliases:
  - CSS Selectors Assignment 01
  - محددات الصنف والمعرّف واسم الوسم
---

# CSS Selectors — Class, ID, and Type

> [!question] السؤال
> اكتب تعليقًا يوضح وظيفة كل محدد في الشيفرة التالية.
>
> ```css
> .title {
> }
>
> #nav {
> }
>
> div {
> }
>
> h2 {
> }
> ```

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> /* Any Element With Class Title */
> .title {
> }
>
> /* Element with ID nav */
> #nav {
> }
>
> /* All div elements */
> div {
> }
>
> /* All h2 elements */
> h2 {
> }
> ```
>
> ### `class selector`
>
> يختار كل عنصر يحمل قيمة الصنف التالية:
>
> `class="title"`
>
> وصيغته في هذا المثال:
>
> `.title`
>
> ### `ID selector`
>
> يختار العنصر الذي يحمل المعرّف التالي:
>
> `id="nav"`
>
> وصيغته في هذا المثال:
>
> `#nav`
>
> ### `type selector`
>
> يختار جميع العناصر التي تحمل أحد الاسمين التاليين:
>
> `div`
>
> `h2`
>
> **قاعدة سريعة:** النقطة تدل على الصنف، وعلامة الهاش تدل على المعرّف، واسم الوسم يختار جميع العناصر من نوعه.
