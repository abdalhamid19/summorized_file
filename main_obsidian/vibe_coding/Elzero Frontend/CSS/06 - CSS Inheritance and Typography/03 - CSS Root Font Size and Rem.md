---
title: "CSS Root Font Size and Rem"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - typography
  - rem
  - تكليف
aliases:
  - تكليف أحجام الخط بوحدة rem
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Root</bdi> <bdi dir="ltr">Font</bdi> <bdi dir="ltr">Size</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">rem</bdi>

> [!question] السؤال
> **المطلوب:** اجعل حجم الخط في <bdi dir="ltr">Root</bdi> <bdi dir="ltr">Element</bdi> يساوي <bdi dir="ltr">20px</bdi>، واستخدم <bdi dir="ltr">rem</bdi> للحصول على <bdi dir="ltr">50px</bdi> للعنصر الأول، و40px للثاني، و30px للثالث.
>
> **بنية تمثيلية للمعاينة؛ التكليف يذكر العناصر الثلاثة ولا يورد <bdi dir="ltr">markup</bdi> كاملًا**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">first</bdi>"><bdi dir="ltr">First</bdi></<bdi dir="ltr">p</bdi>>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">second</bdi>"><bdi dir="ltr">Second</bdi></<bdi dir="ltr">p</bdi>>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">third</bdi>"><bdi dir="ltr">Third</bdi></<bdi dir="ltr">p</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-22-26-3.png)
>
> [!info] حدود المصدر والمطابقة
> أسماء الفئات <bdi dir="ltr">HTML</bdi> تمثيلية في المعاينة؛ المطلوب الرسمي هو أحجام الجذر والوحدات والقيم الرقمية المذكورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">html</bdi> {
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">20px</bdi>;
> }
> .<bdi dir="ltr">first</bdi> {
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">2.5rem</bdi>;
> }
> .<bdi dir="ltr">second</bdi> {
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">2rem</bdi>;
> }
> .<bdi dir="ltr">third</bdi> {
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">1.5rem</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> وحدة <bdi dir="ltr">rem</bdi> تعتمد على حجم الخط في عنصر الجذر <bdi dir="ltr">html</bdi>. عندما يكون الجذر <bdi dir="ltr">20px</bdi>، تصبح <bdi dir="ltr">2.5rem</bdi> مساوية <bdi dir="ltr">50px</bdi>، و2rem مساوية <bdi dir="ltr">40px</bdi>، و1.<bdi dir="ltr">5rem</bdi> مساوية <bdi dir="ltr">30px</bdi>.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Root</bdi> <bdi dir="ltr">size</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">rem</bdi>
>
> ##### `html`
>
> عنصر الجذر الذي يحدد قيمة <bdi dir="ltr">rem</bdi> الأساسية.
>
> ##### `font-size: 20px`
>
> يجعل حجم الجذر <bdi dir="ltr">20px</bdi>.
>
> ##### `rem`
>
> وحدة نسبية مضروبة في حجم خط الجذر.
>
> ##### `2.5 × 20 / 2 × 20 / 1.5 × 20`
>
> يوضح حساب أحجام النصوص المطلوبة.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">html</bdi> {
> ```
>
> يختار عنصر الجذر في المستند.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">20px</bdi>;
> ```
>
> يضبط أساس وحدة <bdi dir="ltr">rem</bdi> على <bdi dir="ltr">20px</bdi>.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الجذر.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">first</bdi> {
> ```
>
> يختار العنصر الأول.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">2.5rem</bdi>;
> ```
>
> يضرب حجم الجذر في 2.5 ليعطي <bdi dir="ltr">50px</bdi>.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة العنصر الأول.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">second</bdi> {
> ```
>
> يختار العنصر الثاني.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">2rem</bdi>;
> ```
>
> يضرب حجم الجذر في 2 ليعطي <bdi dir="ltr">40px</bdi>.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة العنصر الثاني.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">third</bdi> {
> ```
>
> يختار العنصر الثالث.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">1.5rem</bdi>;
> ```
>
> يضرب حجم الجذر في 1.5 ليعطي <bdi dir="ltr">30px</bdi>.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة العنصر الثالث.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/06 - CSS Inheritance and Typography/assets/solution-page-task-03.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/06 - CSS Inheritance and Typography/CSS Root Font Size Rem Assignment 22-26.html|افتح صفحة الشرح المستقلة للتكليف 03]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-22-to-26/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-22-26-3.png)
