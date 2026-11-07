---
title: "CSS Font Families and Weights"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - typography
  - تكليف
aliases:
  - تكليف أنواع الخطوط وأوزانها
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Typography</bdi> — <bdi dir="ltr">Font</bdi> <bdi dir="ltr">Families</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Weights</bdi>

> [!question] السؤال
> **المطلوب:** أنشئ ثلاثة أسطر بخطوط مختلفة: <bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi> بوزن 300 ومائل، ثم <bdi dir="ltr">Cairo</bdi> بوزن 700، ثم <bdi dir="ltr">Jomhuria</bdi> بوزن 400.
>
> **بنية المعاينة التي تعرض الأسطر الثلاثة**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">open-sans</bdi>"><bdi dir="ltr">elzero</bdi> <bdi dir="ltr">Web</bdi> <bdi dir="ltr">school</bdi></<bdi dir="ltr">p</bdi>>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">cairo</bdi>"><bdi dir="ltr">elzero</bdi> <bdi dir="ltr">Web</bdi> <bdi dir="ltr">school</bdi></<bdi dir="ltr">p</bdi>>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">jomhuria</bdi>"><bdi dir="ltr">elzero</bdi> <bdi dir="ltr">Web</bdi> <bdi dir="ltr">school</bdi></<bdi dir="ltr">p</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-22-26-2.png)
>
> [!info] حدود المصدر والمطابقة
> الأحجام الإضافية في المعاينة اختيارية. الصفحة الرسمية تحدد أسماء الخطوط والأوزان والميلان فقط؛ روابط خطوط <bdi dir="ltr">Google</bdi> تُستخدم لتحسين عرضها عند توفر الشبكة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">open-sans</bdi> {
>   <bdi dir="ltr">font-family</bdi>: "<bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi>", <bdi dir="ltr">sans-serif</bdi>;
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">24px</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: 300;
>   <bdi dir="ltr">font-style</bdi>: <bdi dir="ltr">italic</bdi>;
> }
> .<bdi dir="ltr">cairo</bdi> {
>   <bdi dir="ltr">font-family</bdi>: "<bdi dir="ltr">Cairo</bdi>", <bdi dir="ltr">sans-serif</bdi>;
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">24px</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: 700;
> }
> .<bdi dir="ltr">jomhuria</bdi> {
>   <bdi dir="ltr">font-family</bdi>: "<bdi dir="ltr">Jomhuria</bdi>", <bdi dir="ltr">cursive</bdi>;
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">32px</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: 400;
> }
> ```
>
> **الفكرة الأساسية**
>
> <bdi dir="ltr">font-family</bdi> يختار شكل الخط، وfont-<bdi dir="ltr">weight</bdi> يحدد سماكته، وfont-<bdi dir="ltr">style</bdi> يجعل الخط مائلًا عند طلب ذلك. أسماء العائلات وأوزانها الثلاثة مطلوبة؛ أما الأحجام والفئات البديلة فلدعم المعاينة.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Typography</bdi>
>
> ##### `font-family`
>
> يحدد عائلة الخط؛ وتأتي بعدها عائلة عامة احتياطية.
>
> ##### `font-weight`
>
> يحدد وزن الخط الرقمي مثل 300 أو 700.
>
> ##### `font-style: italic`
>
> يعرض الخط بميلان.
>
> ##### `sans-serif / cursive`
>
> عائلات عامة يستخدمها المتصفح إذا لم يتوفر الخط المحدد.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">open-sans</bdi> {
> ```
>
> يفتح قاعدة خط <bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi>.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-family</bdi>: "<bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi>", <bdi dir="ltr">sans-serif</bdi>;
> ```
>
> يختار <bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi> ويجعل <bdi dir="ltr">sans-serif</bdi> بديلًا عند تعذر تحميله.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">24px</bdi>;
> ```
>
> يضبط حجم النص في المعاينة.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-weight</bdi>: 300;
> ```
>
> يضبط وزن <bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi> على 300.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-style</bdi>: <bdi dir="ltr">italic</bdi>;
> ```
>
> يجعل السطر مائلًا.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة <bdi dir="ltr">Open</bdi> <bdi dir="ltr">Sans</bdi>.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">cairo</bdi> {
> ```
>
> يفتح قاعدة خط <bdi dir="ltr">Cairo</bdi>.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-family</bdi>: "<bdi dir="ltr">Cairo</bdi>", <bdi dir="ltr">sans-serif</bdi>;
> ```
>
> يختار <bdi dir="ltr">Cairo</bdi> مع بديل <bdi dir="ltr">sans-serif</bdi>.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">24px</bdi>;
> ```
>
> يضبط حجم النص.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-weight</bdi>: 700;
> ```
>
> يضبط وزن <bdi dir="ltr">Cairo</bdi> على 700 كما يطلب السؤال.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة <bdi dir="ltr">Cairo</bdi>.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">jomhuria</bdi> {
> ```
>
> يفتح قاعدة خط <bdi dir="ltr">Jomhuria</bdi>.
>
> **13.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-family</bdi>: "<bdi dir="ltr">Jomhuria</bdi>", <bdi dir="ltr">cursive</bdi>;
> ```
>
> يختار <bdi dir="ltr">Jomhuria</bdi> مع بديل <bdi dir="ltr">cursive</bdi>.
>
> **14.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">32px</bdi>;
> ```
>
> يضبط حجم النص للمعاينة.
>
> **15.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-weight</bdi>: 400;
> ```
>
> يضبط وزن <bdi dir="ltr">Jomhuria</bdi> على 400.
>
> **16.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة <bdi dir="ltr">Jomhuria</bdi>.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/06 - CSS Inheritance and Typography/assets/solution-page-task-02.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/06 - CSS Inheritance and Typography/02 - CSS Font Families and Weights.html|افتح صفحة الشرح المستقلة للتكليف 02]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-22-to-26/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-22-26-2.png)
