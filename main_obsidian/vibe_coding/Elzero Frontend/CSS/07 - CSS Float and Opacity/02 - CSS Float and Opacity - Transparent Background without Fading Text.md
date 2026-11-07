---
title: "02 - CSS Float and Opacity - Transparent Background without Fading Text"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
  - تكليف
aliases:
  - تكليف Transparent Background without Fading Text
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Float</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Opacity</bdi> — <bdi dir="ltr">Transparent</bdi> <bdi dir="ltr">Background</bdi> <bdi dir="ltr">without</bdi> <bdi dir="ltr">Fading</bdi> <bdi dir="ltr">Text</bdi>

> [!question] السؤال
> **المطلوب:** استخدم البنية المحددة. اجعل خلفية العناصر الثلاثة واحدة، وخلفية العنصرين الأخيرين بشفافية 0.1، مع بقاء النص واضحًا.
>
> **<bdi dir="ltr">HTML</bdi> الأصلي**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">normal</bdi>"><bdi dir="ltr">Normal</bdi></<bdi dir="ltr">div</bdi>>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">one</bdi>"><bdi dir="ltr">One</bdi></<bdi dir="ltr">div</bdi>>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">two</bdi>"><bdi dir="ltr">Two</bdi></<bdi dir="ltr">div</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-27-29-2.png)
>
> [!info] حدود المصدر والمطابقة
> لم أتمكن من التحقق من قيمة لون الخلفية في صورة المرجع. أبقيت لون الحل المحلي <bdi dir="ltr">#009688</bdi> مع الإشارة إلى أن المطابقة اللونية غير مؤكدة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">stage</bdi> > <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">300px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">20px</bdi> <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">black</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">1rem</bdi>;
>   <bdi dir="ltr">background-color</bdi>: <bdi dir="ltr">#009688</bdi>;
> }
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">stage</bdi> > .<bdi dir="ltr">one</bdi>,
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">stage</bdi> > .<bdi dir="ltr">two</bdi> {
>   <bdi dir="ltr">background-color</bdi>: <bdi dir="ltr">rgba(0, 150, 136, 0.1)</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> نستخدم <bdi dir="ltr">rgba()</bdi> لتغيير شفافية لون الخلفية وحدها. أما <bdi dir="ltr">opacity</bdi> فتؤثر في العنصر كله بما فيه النص، لذلك تبقى الكتابة معتمة وواضحة عند ضبط <bdi dir="ltr">alpha</bdi> داخل لون الخلفية.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">RGBA</bdi> <bdi dir="ltr">background</bdi>
>
> ##### `rgba(red, green, blue, alpha)`
>
> تحدد قنوات اللون الثلاث ثم قيمة الشفافية من 0 إلى 1.
>
> ##### `0.1`
>
> يعني أن الخلفية تحتفظ بعُشر عتامتها تقريبًا.
>
> ##### `opacity`
>
> تؤثر في العنصر ومحتواه كله؛ لهذا لا نستخدمها هنا.
>
> #### <bdi dir="ltr">Selectors</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">grouping</bdi>
>
> ##### `.stage > div`
>
> يختار عناصر <bdi dir="ltr">div</bdi> الأبناء المباشرين لحاوية <bdi dir="ltr">stage</bdi>.
>
> ##### `.one, .two`
>
> الفاصلة تجمع محددين لتطبيق قاعدة الخلفية الشفافة على الاثنين.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">stage</bdi> > <bdi dir="ltr">div</bdi> {
> ```
>
> يستهدف عناصر <bdi dir="ltr">div</bdi> المباشرة داخل <bdi dir="ltr">stage</bdi>.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
> ```
>
> يجعل قياس العرض شاملًا الحشو والحد.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">300px</bdi>;
> ```
>
> يضبط عرض كل عنصر على <bdi dir="ltr">300px</bdi> كما في المطلوب.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">20px</bdi> <bdi dir="ltr">auto</bdi>;
> ```
>
> يوسّط العناصر أفقيًا ويضيف مسافة رأسية.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi>;
> ```
>
> يضيف حشوًا داخليًا قدره <bdi dir="ltr">20px</bdi>.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">black</bdi>;
> ```
>
> يجعل النص أسود.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
> ```
>
> يجعل وزن الخط عريضًا.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">1rem</bdi>;
> ```
>
> يستخدم حجم الخط الأساسي للمستند.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">background-color</bdi>: <bdi dir="ltr">#009688</bdi>;
> ```
>
> يضع لون الخلفية المشترك على العناصر الثلاثة.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة التنسيق العامة.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">stage</bdi> > .<bdi dir="ltr">one</bdi>,
> ```
>
> يبدأ المجموعة التي ستأخذ الخلفية الشفافة.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">stage</bdi> > .<bdi dir="ltr">two</bdi> {
> ```
>
> يضيف العنصر <bdi dir="ltr">two</bdi> للمجموعة نفسها.
>
> **13.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">background-color</bdi>: <bdi dir="ltr">rgba(0, 150, 136, 0.1)</bdi>;
> ```
>
> يجعل خلفية العنصرين الأخيرة بلون <bdi dir="ltr">alpha</bdi> يساوي 0.1 دون شفافية النص.
>
> **14.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الخلفية الشفافة.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/07 - CSS Float and Opacity/assets/solution-page-task-02.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/07 - CSS Float and Opacity/02 - CSS Float and Opacity - Transparent Background without Fading Text.html|افتح صفحة الشرح المستقلة للتكليف 02]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-27-to-29/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-27-29-2.png)
