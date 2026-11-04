---
title: "CSS Border Radius — Soft Asymmetric Shape"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-border-radius-and-box-shadow
  - تكليف
aliases:
  - CSS Border Radius — Soft Asymmetric Shape
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Border</bdi> <bdi dir="ltr">Radius</bdi> — <bdi dir="ltr">Soft</bdi> <bdi dir="ltr">Asymmetric</bdi> <bdi dir="ltr">Shape</bdi>

> [!question] السؤال
> أنشئ عنصرًا 100×<bdi dir="ltr">100px</bdi> في منتصف الشاشة، مع زاوية دائرية غير متماثلة وظل داخلي، وأضف بادئات الخواص اللازمة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">shape</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
>   -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">15%</bdi> <bdi dir="ltr">50%</bdi> 0 <bdi dir="ltr">50%</bdi>;
>   -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">15%</bdi> <bdi dir="ltr">50%</bdi> 0 <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">15%</bdi> <bdi dir="ltr">50%</bdi> 0 <bdi dir="ltr">50%</bdi>;
>   -<bdi dir="ltr">webkit-box-shadow</bdi>: <bdi dir="ltr">inset</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#777</bdi>, <bdi dir="ltr">inset</bdi> -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#888</bdi>;
>   -<bdi dir="ltr">moz-box-shadow</bdi>: <bdi dir="ltr">inset</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#777</bdi>, <bdi dir="ltr">inset</bdi> -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#888</bdi>;
>   <bdi dir="ltr">box-shadow</bdi>: <bdi dir="ltr">inset</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#777</bdi>, <bdi dir="ltr">inset</bdi> -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#888</bdi>;
> }
>
> <bdi dir="ltr">body</bdi> {
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">100vh</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> ترسم قيم `border-radius` زوايا مختلفة لتكوين الشكل غير المتماثل، بينما تضيف `inset` ظلًا داخل العنصر بدل إسقاطه خارجه.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">Borders</bdi>, <bdi dir="ltr">Radius</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Shadows</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.shape`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `body`
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > #### الأبعاد والمسافات
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `height`
> > تحدد ارتفاع العنصر.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### الحدود والظلال
> > ##### `-webkit-border-radius`
> > صيغة ببادئة `WebKit` لدعم أقدم.
> >
> > ##### `-moz-border-radius`
> > صيغة ببادئة `Mozilla` لدعم أقدم.
> >
> > ##### `border-radius`
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > ##### `-webkit-box-shadow`
> > صيغة ببادئة `WebKit` لدعم أقدم.
> >
> > ##### `-moz-box-shadow`
> > صيغة ببادئة `Mozilla` لدعم أقدم.
> >
> > ##### `box-shadow`
> > ترسم ظلًا حول العنصر أو داخله.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> > ##### `place-items`
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### علامات صياغة <bdi dir="ltr">CSS</bdi>
> >
> > ##### `:`
> > تفصل اسم الخاصية عن قيمتها.
> >
> > ##### `;`
> > تنهي تصريح <bdi dir="ltr">CSS</bdi>.
> >
> > ##### `,`
> > تفصل القيم أو المحددات بحسب موضعها.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">shape</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">15%</bdi> <bdi dir="ltr">50%</bdi> 0 <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">15%</bdi> <bdi dir="ltr">50%</bdi> 0 <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">15%</bdi> <bdi dir="ltr">50%</bdi> 0 <bdi dir="ltr">50%</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-box-shadow</bdi>: <bdi dir="ltr">inset</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#777</bdi>, <bdi dir="ltr">inset</bdi> -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#888</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-box-shadow</bdi>: <bdi dir="ltr">inset</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#777</bdi>, <bdi dir="ltr">inset</bdi> -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#888</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">box-shadow</bdi>: <bdi dir="ltr">inset</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#777</bdi>, <bdi dir="ltr">inset</bdi> -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">8px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">#888</bdi>;
> > ```
> > ترسم ظلًا حول العنصر أو داخله.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">body</bdi> {
> > ```
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">100vh</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/assets/solution-task-02.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/02 - CSS Border Radius — Soft Asymmetric Shape.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/CSS Border Radius and Box Shadow Assignments 38-41.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
