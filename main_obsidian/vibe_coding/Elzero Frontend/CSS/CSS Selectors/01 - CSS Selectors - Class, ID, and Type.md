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
> <p dir="rtl">اكتب تعليقًا يوضح ما الذي يختاره كل <bdi dir="ltr"><code>CSS Selector</code></bdi> (محدد <bdi dir="ltr"><code>CSS</code></bdi>: نمط يختار عناصر الصفحة المطلوب تنسيقها). أكمل التعليقات الناقصة:</p>
>
> ```css
> /* Any Element With Class Title */
> .title {
> }
>
> /* ? */
> #nav {
> }
>
> /* ? */
> div {
> }
>
> /* ? */
> h2 {
> }
> ```

> [!success]- الإجابة وشرح الحل — اضغط لفتحهما
>
> ```css
> /* أي عنصر يحمل الصنف title */
> .title {
> }
>
> /* العنصر الذي يحمل المعرّف nav */
> #nav {
> }
>
> /* جميع عناصر div */
> div {
> }
>
> /* جميع عناصر h2 */
> h2 {
> }
> ```
>
> <ul dir="rtl">
> <li dir="rtl">يختار المحدد <bdi dir="ltr"><code>.title</code></bdi> أي عنصر يحمل <bdi dir="ltr"><code>class="title"</code></bdi>؛ ويُسمّى <bdi dir="ltr"><code>class selector</code></bdi> (محدد الصنف). ويمكن لعناصر متعددة حمل الصنف نفسه.</li>
> <li dir="rtl">يختار المحدد <bdi dir="ltr"><code>#nav</code></bdi> العنصر الذي يحمل <bdi dir="ltr"><code>id="nav"</code></bdi>؛ ويُسمّى <bdi dir="ltr"><code>ID selector</code></bdi> (محدد المعرّف).</li>
> <li dir="rtl">يختار المحدد <bdi dir="ltr"><code>div</code></bdi> أو <bdi dir="ltr"><code>h2</code></bdi> كل الوسوم التي تحمل الاسم نفسه؛ ويُسمّى <bdi dir="ltr"><code>type selector</code></bdi> (محدد نوع الوسم).</li>
> </ul>
>
> <p dir="rtl"><strong>قاعدة سريعة:</strong> الصنف <bdi dir="ltr"><code>class</code></bdi> تسبقه النقطة <bdi dir="ltr"><code>.</code></bdi>، والمعرّف <bdi dir="ltr"><code>id</code></bdi> تسبقه العلامة <bdi dir="ltr"><code>#</code></bdi>، أما <bdi dir="ltr"><code>type selector</code></bdi> فيستخدم اسم الوسم.</p>

## HTML Lesson Reference

<p dir="rtl">المحدد الأخير يختار الوسم <bdi dir="ltr"><code>h2</code></bdi> لعنوان من المستوى الثاني.</p>

راجع [[vibe_coding/Elzero Frontend/HTML 2021/07 - العناوين واستخداماتها/02 - ملخص مختصر|درس العناوين]] للاستزادة.
