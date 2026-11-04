---
title: "CSS Box Shadow — Basic and Pro Cards"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-border-radius-and-box-shadow
  - تكليف
aliases:
  - CSS Box Shadow — Basic and Pro Cards
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Box</bdi> <bdi dir="ltr">Shadow</bdi> — <bdi dir="ltr">Basic</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Pro</bdi> <bdi dir="ltr">Cards</bdi>

> [!question] السؤال
> أنشئ مقارنة بطاقتين داخل أب بعرض <bdi dir="ltr">550px</bdi>، مع دائرتي السعر والعناوين الزرقاء والفاصل الوسطي، وأضف بادئات الخواص عند الحاجة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">pricing</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">550px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">24px</bdi>;
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
> }
>
> .<bdi dir="ltr">plan</bdi> {
>   <bdi dir="ltr">flex</bdi>: 1;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
>   <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">center</bdi>;
> }
>
> .<bdi dir="ltr">plan</bdi> <bdi dir="ltr">h2</bdi> {
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#03a9f4</bdi>;
>   -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
>   -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
> }
>
> .<bdi dir="ltr">plan</bdi> .<bdi dir="ltr">price</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">200px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">200px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">35px</bdi> <bdi dir="ltr">auto</bdi> 0;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ddd</bdi>;
> }
>
> .<bdi dir="ltr">pricing</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: "<bdi dir="ltr">Or</bdi>";
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
>   <bdi dir="ltr">left</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">top</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translate(-50%, -50%)</bdi>;
>   -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#03a9f4</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> يرتب `Flex` البطاقتين بجانب بعضهما، ويضيف العنصر الزائف `Or` في منتصف المسافة. يتكوّن السعر كدائرة باستخدام `border-radius`: `50%`.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">Borders</bdi>, <bdi dir="ltr">Radius</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Shadows</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.pricing`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.plan`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.plan h2`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.plan .price`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.pricing::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الأبعاد والمسافات
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > ##### `gap`
> > تحدد المسافة بين عناصر التخطيط.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > ##### `height`
> > تحدد ارتفاع العنصر.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### التموضع وترتيب الطبقات
> > ##### `position`
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > ##### `left`
> > تحدد المسافة من الحافة اليسرى.
> >
> > ##### `top`
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### <bdi dir="ltr">Flexbox</bdi>
> > ##### `flex`
> > تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `text-align`
> > تحاذي النص داخل العنصر.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
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
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> > ##### `place-items`
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### العناصر الزائفة والعدادات
> > ##### `content`
> > يضيف النص المحدد إلى العنصر الزائف من دون إنشاء عنصر `HTML` جديد.
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
> > .<bdi dir="ltr">pricing</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">550px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
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
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">plan</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">flex</bdi>: 1;
> > ```
> > تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تحاذي النص داخل العنصر.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">plan</bdi> <bdi dir="ltr">h2</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#03a9f4</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">plan</bdi> .<bdi dir="ltr">price</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">200px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 24
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">200px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 25
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">35px</bdi> <bdi dir="ltr">auto</bdi> 0;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 26
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 27
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 28
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 29
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 30
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 31
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ddd</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 32
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 33
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">pricing</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 34
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: "<bdi dir="ltr">Or</bdi>";
> > ```
> > يضيف النص المحدد إلى العنصر الزائف من دون إنشاء عنصر <bdi dir="ltr">HTML</bdi> جديد.
> >
> > #### السطر 35
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 36
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 37
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 38
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translate(-50%, -50%)</bdi>;
> > ```
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > #### السطر 39
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم.
> >
> > #### السطر 40
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">moz-border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">Mozilla</bdi> لدعم أقدم.
> >
> > #### السطر 41
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 42
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 43
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 44
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#03a9f4</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 45
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/assets/solution-task-03.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/03 - CSS Box Shadow — Basic and Pro Cards.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/10 - CSS Border Radius and Box Shadow/CSS Border Radius and Box Shadow Assignments 38-41.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-38-to-41/)
