---
title: "CSS Dimensions and Overflow"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - dimensions
  - overflow
  - تكليف
aliases:
  - تكليف أبعاد العناصر وOverflow في CSS
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Dimensions</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Overflow</bdi>

> [!question] السؤال
> **المطلوب:** أنشئ الصناديق بالنصوص والألوان الظاهرة في المثال. اترك <bdi dir="ltr">display</bdi> على قيمته الأصلية <bdi dir="ltr">block</bdi>، واجعل عرض العنصر لا يتجاوز <bdi dir="ltr">400px</bdi>، ثم أخفِ أي جزء من النص يخرج من الصندوق الأخير.
>
> **<bdi dir="ltr">HTML</bdi> المستخدم في المعاينة؛ صفحة التكليف لا تفرض نص <bdi dir="ltr">HTML</bdi> كاملًا**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">box</bdi>"><bdi dir="ltr">Title</bdi> <bdi dir="ltr">One</bdi></<bdi dir="ltr">div</bdi>>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">box</bdi>"><bdi dir="ltr">Title</bdi> <bdi dir="ltr">Two</bdi> <bdi dir="ltr">With</bdi> <bdi dir="ltr">More</bdi> <bdi dir="ltr">Words</bdi></<bdi dir="ltr">div</bdi>>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">box</bdi>"><bdi dir="ltr">Title</bdi> <bdi dir="ltr">Three</bdi> <bdi dir="ltr">With</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Words</bdi></<bdi dir="ltr">div</bdi>>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">box</bdi>">
>   <bdi dir="ltr">Title</bdi> <bdi dir="ltr">Three</bdi> <bdi dir="ltr">With</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Words</bdi> <bdi dir="ltr">Title</bdi> <bdi dir="ltr">Three</bdi> <bdi dir="ltr">With</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Words</bdi>
>   <bdi dir="ltr">Title</bdi> <bdi dir="ltr">Three</bdi> <bdi dir="ltr">With</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Words</bdi> <bdi dir="ltr">Title</bdi> <bdi dir="ltr">Three</bdi> <bdi dir="ltr">With</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Many</bdi> <bdi dir="ltr">Words</bdi>
> </<bdi dir="ltr">div</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-13-16-1.png)
>
> [!info] حدود المصدر والمطابقة
> رابط صورة التكليف هو المصدر الرسمي المتاح. تعذّر حفظ الصورة محليًا لأن الموقع حجب طلب التنزيل؛ أبقيت رابطها بدل ادعاء مطابقة بصرية غير متحققة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">box</bdi> {
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">fit-content</bdi>;
>   <bdi dir="ltr">max-width</bdi>: <bdi dir="ltr">400px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">15px</bdi> 0;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">15px</bdi>;
>   <bdi dir="ltr">background-color</bdi>: <bdi dir="ltr">brown</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>;
>   <bdi dir="ltr">font</bdi>: <bdi dir="ltr">16px</bdi> / 1.2 "<bdi dir="ltr">Times</bdi> <bdi dir="ltr">New</bdi> <bdi dir="ltr">Roman</bdi>", <bdi dir="ltr">serif</bdi>;
> }
>
> .<bdi dir="ltr">box</bdi>:<bdi dir="ltr">last-child</bdi> {
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">72px</bdi>;
>   <bdi dir="ltr">overflow</bdi>: <bdi dir="ltr">hidden</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> العرض المناسب للمحتوى يظل محدودًا بسقف <bdi dir="ltr">400px</bdi>. وعندما يزيد النص داخل الصندوق الأخير، تخفي <bdi dir="ltr">overflow</bdi> الجزء الخارج عن ارتفاعه. لا نكتب <bdi dir="ltr">display</bdi> لأن المطلوب إبقاء عناصر <bdi dir="ltr">div</bdi> على سلوكها الأصلي.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">dimensions</bdi>
>
> ##### `width: fit-content`
>
> يجعل عرض الصندوق مناسبًا لمحتواه، بدل فرض عرض ثابت.
>
> ##### `max-width: 400px`
>
> يضع سقفًا للعرض؛ فلا يتجاوز الصندوق <bdi dir="ltr">400px</bdi>.
>
> ##### `box-sizing: border-box`
>
> يجعل <bdi dir="ltr">padding</bdi> والحد ضمن العرض الأقصى المحسوب.
>
> ##### `height: 72px`
>
> يحدد ارتفاع الصندوق الأخير في هذا المثال المرئي؛ هذه قيمة توضيحية لأن المصدر لا يحددها.
>
> #### تحديد العنصر وإخفاء الزائد
>
> ##### `.box:last-child`
>
> يختار الصندوق ذي <bdi dir="ltr">class</bdi> <bdi dir="ltr">box</bdi> عندما يكون آخر عنصر بين إخوته.
>
> ##### `overflow: hidden`
>
> يخفي الجزء الذي يتجاوز حدود الصندوق.
>
> #### قيم التنسيق
>
> ##### `margin / padding`
>
> الأولى تضيف مسافة خارج العنصر والثانية مساحة داخل حدوده.
>
> ##### `font: 16px / 1.2 ...`
>
> يجمع حجم الخط وارتفاع السطر وعائلة الخط في تصريح واحد.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">box</bdi> {
> ```
>
> يفتح قاعدة تنسيق جميع الصناديق ذات الصنف <bdi dir="ltr">box</bdi>.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
> ```
>
> يجعل قياس العرض المحسوب شاملًا الحشو والحدود.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">fit-content</bdi>;
> ```
>
> يجعل العرض يتبع المحتوى ما دام لا يتجاوز السقف المحدد.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">max-width</bdi>: <bdi dir="ltr">400px</bdi>;
> ```
>
> يمنع الصندوق من تجاوز العرض الأقصى المطلوب.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">15px</bdi> 0;
> ```
>
> يضيف مسافة خارجية رأسية قدرها <bdi dir="ltr">15px</bdi> دون توسيط أفقي.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">15px</bdi>;
> ```
>
> يضيف <bdi dir="ltr">15px</bdi> من المساحة داخل الصندوق حول النص.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">background-color</bdi>: <bdi dir="ltr">brown</bdi>;
> ```
>
> يضبط خلفية الصناديق على اللون البني المستخدم في المعاينة.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>;
> ```
>
> يجعل النص أبيض ليتباين مع الخلفية البنية.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font</bdi>: <bdi dir="ltr">16px</bdi> / 1.2 "<bdi dir="ltr">Times</bdi> <bdi dir="ltr">New</bdi> <bdi dir="ltr">Roman</bdi>", <bdi dir="ltr">serif</bdi>;
> ```
>
> يضبط حجم الخط وارتفاع السطر وعائلة الخط.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة تنسيق الصناديق العامة.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">box</bdi>:<bdi dir="ltr">last-child</bdi> {
> ```
>
> يستهدف آخر صندوق فقط كي ينطبق عليه القص.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">72px</bdi>;
> ```
>
> يحدد ارتفاعًا يسمح بإظهار النص الزائد الذي سنقصه.
>
> **13.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">overflow</bdi>: <bdi dir="ltr">hidden</bdi>;
> ```
>
> يخفي أي محتوى يتجاوز حدود الصندوق الأخير.
>
> **14.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الصندوق الأخير.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/04 - CSS Nesting, Dimensions, and Overflow/assets/solution-page-task-02.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/04 - CSS Nesting, Dimensions, and Overflow/02 - CSS Dimensions and Overflow.html|افتح صفحة الشرح المستقلة للتكليف 02]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-13-to-16/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-13-16-1.png)
