---
title: "CSS Box Shadow — Layered Circles"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-border-radius-and-box-shadow
  - تكليف
aliases:
  - CSS Box Shadow — Layered Circles
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Box</bdi> <bdi dir="ltr">Shadow</bdi> — <bdi dir="ltr">Layered</bdi> <bdi dir="ltr">Circles</bdi>

> [!question] السؤال
> أنشئ ثلاثة عناصر دائرية قطرها <bdi dir="ltr">100px</bdi>، مع إطار أسود وظلين متداخلين بالوردي والأزرق، وأضف بادئات المتصفح عند الحاجة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">circles</bdi> {
>   <bdi dir="ltr">counter-reset</bdi>: <bdi dir="ltr">item</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">space-around</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">24px</bdi>;
> }
>
> .<bdi dir="ltr">circle</bdi> {
>   <bdi dir="ltr">counter-increment</bdi>: <bdi dir="ltr">item</bdi>;
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#000</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
>   -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   -<bdi dir="ltr">webkit-box-shadow</bdi>: -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>, <bdi dir="ltr">8px</bdi> <bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>;
>   -<bdi dir="ltr">moz-box-shadow</bdi>: -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>, <bdi dir="ltr">8px</bdi> <bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>;
>   <bdi dir="ltr">box-shadow</bdi>: -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>, <bdi dir="ltr">8px</bdi> <bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>;
> }
>
> .<bdi dir="ltr">circle</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: <bdi dir="ltr">counter(item)</bdi>;
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
>   <bdi dir="ltr">top</bdi>: -<bdi dir="ltr">12px</bdi>;
>   <bdi dir="ltr">left</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateX(-50%)</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">24px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">24px</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#000</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">center</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> تتحول العناصر إلى دوائر عبر `border-radius`، وتضيف `box-shadow` طبقتين لونيتين حول كل دائرة. يحفظ العداد رقم كل دائرة ليظهر داخل شارة صغيرة.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">Borders</bdi>, <bdi dir="ltr">Radius</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Shadows</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.circles`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.circle`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.circle::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### العناصر الزائفة والعدادات
> > ##### `counter-reset`
> > تنشئ عدادًا عند بداية الحاوية.
> >
> > ##### `counter-increment`
> > تزيد قيمة العداد لكل عنصر يطابق القاعدة.
> >
> > ##### `content`
> > يعرض رقم العداد داخل العنصر الزائف، ويمكن ضم نص توضيحي له.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">Flexbox</bdi>
> > ##### `justify-content`
> > توزع العناصر على المحور الرئيسي.
> >
> > #### الأبعاد والمسافات
> > ##### `gap`
> > تحدد المسافة بين عناصر التخطيط.
> >
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `height`
> > تحدد ارتفاع العنصر.
> >
> > #### التموضع وترتيب الطبقات
> > ##### `position`
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > ##### `top`
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > ##### `left`
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> > ##### `place-items`
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### الحدود والظلال
> > ##### `border`
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
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
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > ##### `text-align`
> > تحاذي النص داخل العنصر.
> >
> > #### الحركة والتحويل
> > ##### `transform`
> > تحرك العنصر دون تعديل تدفق الصفحة.
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
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">circles</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">counter-reset</bdi>: <bdi dir="ltr">item</bdi>;
> > ```
> > تنشئ عدادًا عند بداية الحاوية.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">space-around</bdi>;
> > ```
> > توزع العناصر على المحور الرئيسي.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">24px</bdi>;
> > ```
> > تحدد المسافة بين عناصر التخطيط.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">circle</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">counter-increment</bdi>: <bdi dir="ltr">item</bdi>;
> > ```
> > تزيد قيمة العداد لكل عنصر يطابق القاعدة.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#000</bdi>;
> > ```
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-box-shadow</bdi>: -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>, <bdi dir="ltr">8px</bdi> <bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-box-shadow</bdi>: -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>, <bdi dir="ltr">8px</bdi> <bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">box-shadow</bdi>: -<bdi dir="ltr">8px</bdi> -<bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>, <bdi dir="ltr">8px</bdi> <bdi dir="ltr">6px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>;
> > ```
> > ترسم ظلًا حول العنصر أو داخله.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">circle</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 24
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: <bdi dir="ltr">counter(item)</bdi>;
> > ```
> > يعرض رقم العداد داخل العنصر الزائف، ويمكن ضم نص توضيحي له.
> >
> > #### السطر 25
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 26
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: -<bdi dir="ltr">12px</bdi>;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 27
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 28
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateX(-50%)</bdi>;
> > ```
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > #### السطر 29
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">24px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 30
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">24px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 31
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 32
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#000</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 33
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 34
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تحاذي النص داخل العنصر.
> >
> > #### السطر 35
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/assets/solution-task-01.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/01 - CSS Box Shadow — Layered Circles.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/CSS Border Radius and Box Shadow Assignments 38-41.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
