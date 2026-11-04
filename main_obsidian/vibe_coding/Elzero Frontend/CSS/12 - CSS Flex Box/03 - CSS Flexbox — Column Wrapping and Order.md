---
title: "CSS Flexbox — Column Wrapping and Order"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Column Wrapping and Order
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi> — <bdi dir="ltr">Column</bdi> <bdi dir="ltr">Wrapping</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Order</bdi>

> [!question] السؤال
> نسّق العناصر الستة داخل أب 600×<bdi dir="ltr">300px</bdi> بحسب الشكل: ثلاث أعمدة بعناصر متفاوتة الارتفاع والترتيب، مع توسيط الأب أفقيًا.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">parent</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">600px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">300px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">10px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">flex-flow</bdi>: <bdi dir="ltr">column</bdi> <bdi dir="ltr">wrap</bdi>;
>   <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">space-between</bdi>;
>   <bdi dir="ltr">align-content</bdi>: <bdi dir="ltr">space-between</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> }
>
> .<bdi dir="ltr">parent</bdi> > <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">31%</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">align-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#607d8b</bdi>;
> }
>
> .<bdi dir="ltr">one</bdi> { <bdi dir="ltr">order</bdi>: 6; <bdi dir="ltr">height</bdi>: <bdi dir="ltr">25%</bdi>; }
> .<bdi dir="ltr">two</bdi> { <bdi dir="ltr">order</bdi>: 4; }
> .<bdi dir="ltr">three</bdi> { <bdi dir="ltr">order</bdi>: 3; <bdi dir="ltr">height</bdi>: <bdi dir="ltr">25%</bdi>; }
> .<bdi dir="ltr">four</bdi> { <bdi dir="ltr">order</bdi>: 5; }
> .<bdi dir="ltr">five</bdi> { <bdi dir="ltr">order</bdi>: 2; }
> .<bdi dir="ltr">six</bdi> { <bdi dir="ltr">order</bdi>: 1; }
> ```
>
> ### الفكرة الأساسية
> يجعل `flex-flow` اتجاه العناصر عموديًا مع السماح بالتفافها إلى أعمدة. ثم تعيد `order` ترتيب العناصر المرئي، وتضبط النسب ارتفاع العناصر المطلوبة.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.parent`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.parent > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.one`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.two`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.three`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.four`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.five`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.six`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
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
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">Flexbox</bdi>
> > ##### `flex-flow`
> > تختصر اتجاه العناصر والسماح بالتفافها.
> >
> > ##### `justify-content`
> > توزع العناصر على المحور الرئيسي.
> >
> > ##### `align-content`
> > توزع الصفوف أو الأعمدة ككتل على المحور العرضي.
> >
> > ##### `align-items`
> > تحدد محاذاة الأبناء على المحور العرضي.
> >
> > ##### `order`
> > تغير ترتيب العنصر المرئي داخل `Flexbox`.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > #### علامات صياغة <bdi dir="ltr">CSS</bdi>
> >
> > ##### `:`
> > تفصل اسم الخاصية عن قيمتها.
> >
> > ##### `;`
> > تنهي تصريح <bdi dir="ltr">CSS</bdi>.
> >
> > ##### `>`
> > تشير إلى الابن المباشر في المحدد؛ وقد تفصل خطوط <bdi dir="ltr">Grid</bdi> في قيم الشبكة.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">parent</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">600px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">300px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">10px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">flex-flow</bdi>: <bdi dir="ltr">column</bdi> <bdi dir="ltr">wrap</bdi>;
> > ```
> > تختصر اتجاه العناصر والسماح بالتفافها.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">space-between</bdi>;
> > ```
> > توزع العناصر على المحور الرئيسي.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">align-content</bdi>: <bdi dir="ltr">space-between</bdi>;
> > ```
> > توزع الصفوف أو الأعمدة ككتل على المحور العرضي.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">parent</bdi> > <bdi dir="ltr">div</bdi> {
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">31%</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > توزع العناصر على المحور الرئيسي.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">align-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تحدد محاذاة الأبناء على المحور العرضي.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#607d8b</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">one</bdi> { <bdi dir="ltr">order</bdi>: 6; <bdi dir="ltr">height</bdi>: <bdi dir="ltr">25%</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. تحدد ارتفاع العنصر. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">two</bdi> { <bdi dir="ltr">order</bdi>: 4; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">three</bdi> { <bdi dir="ltr">order</bdi>: 3; <bdi dir="ltr">height</bdi>: <bdi dir="ltr">25%</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. تحدد ارتفاع العنصر. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 24
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">four</bdi> { <bdi dir="ltr">order</bdi>: 5; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 25
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">five</bdi> { <bdi dir="ltr">order</bdi>: 2; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 26
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">six</bdi> { <bdi dir="ltr">order</bdi>: 1; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/solution-task-03.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/03 - CSS Flexbox — Column Wrapping and Order.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
