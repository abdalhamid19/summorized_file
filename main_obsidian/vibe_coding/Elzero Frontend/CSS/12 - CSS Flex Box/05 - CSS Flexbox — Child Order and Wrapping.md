---
title: "CSS Flexbox — Child Order and Wrapping"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Child Order and Wrapping
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi> — <bdi dir="ltr">Child</bdi> <bdi dir="ltr">Order</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Wrapping</bdi>

> [!question] السؤال
> أنشئ أبًا 600×<bdi dir="ltr">300px</bdi> وأربعة عناصر بألوان وأحجام الشكل، ووزّع اثنين في الصف العلوي واثنين في السفلي.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/reference-task-05.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">parent</bdi> {
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">content-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">600px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">300px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">10px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">flex-wrap</bdi>: <bdi dir="ltr">wrap</bdi>;
>   <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">space-between</bdi>;
>   <bdi dir="ltr">align-content</bdi>: <bdi dir="ltr">space-between</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> }
>
> .<bdi dir="ltr">slot</bdi> {
>   <bdi dir="ltr">flex</bdi>: 0 0 <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">150px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> }
>
> .<bdi dir="ltr">slot</bdi> > <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">150px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> }
>
> .<bdi dir="ltr">one</bdi> { <bdi dir="ltr">order</bdi>: 1; }
> .<bdi dir="ltr">three</bdi> { <bdi dir="ltr">order</bdi>: 2; }
> .<bdi dir="ltr">four</bdi> { <bdi dir="ltr">order</bdi>: 3; }
> .<bdi dir="ltr">two</bdi> { <bdi dir="ltr">order</bdi>: 4; }
> .<bdi dir="ltr">one</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">margin-left</bdi>: <bdi dir="ltr">160px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ff9800</bdi>; }
> .<bdi dir="ltr">three</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">margin-left</bdi>: <bdi dir="ltr">auto</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#795548</bdi>; }
> .<bdi dir="ltr">four</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#673ab7</bdi>; }
> .<bdi dir="ltr">two</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">margin-left</bdi>: <bdi dir="ltr">34px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#8bc34a</bdi>; }
> ```
>
> ### الفكرة الأساسية
> يمثل كل `slot` نصف صف مرن ويضم عنصرًا داخليًا. يسمح `flex-wrap` بصفين، وتحدد `order` ترتيب الخانات، ثم تحرك الهوامش عناصرها إلى مواضعها.
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
> > ##### `.slot`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.slot > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.one`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.three`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.four`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.two`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.one > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.three > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.four > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.two > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الأبعاد والمسافات
> > ##### `box-sizing`
> > تحدد طريقة حساب العرض والارتفاع بالنسبة إلى الحشو والحدود.
> >
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
> > ##### `margin-left`
> > تحدد المسافة الخارجية اليسرى.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">Flexbox</bdi>
> > ##### `flex-wrap`
> > تسمح بنقل العناصر إلى سطر أو عمود إضافي.
> >
> > ##### `justify-content`
> > توزع العناصر على المحور الرئيسي.
> >
> > ##### `align-content`
> > توزع الصفوف أو الأعمدة ككتل على المحور العرضي.
> >
> > ##### `flex`
> > تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي.
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
> > <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">content-box</bdi>;
> > ```
> > تحدد طريقة حساب العرض والارتفاع بالنسبة إلى الحشو والحدود.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">600px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">300px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">10px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">flex-wrap</bdi>: <bdi dir="ltr">wrap</bdi>;
> > ```
> > تسمح بنقل العناصر إلى سطر أو عمود إضافي.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">space-between</bdi>;
> > ```
> > توزع العناصر على المحور الرئيسي.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">align-content</bdi>: <bdi dir="ltr">space-between</bdi>;
> > ```
> > توزع الصفوف أو الأعمدة ككتل على المحور العرضي.
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
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">slot</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">flex</bdi>: 0 0 <bdi dir="ltr">50%</bdi>;
> > ```
> > تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">150px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">slot</bdi> > <bdi dir="ltr">div</bdi> {
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">150px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 24
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 25
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">one</bdi> { <bdi dir="ltr">order</bdi>: 1; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 26
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">three</bdi> { <bdi dir="ltr">order</bdi>: 2; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 27
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">four</bdi> { <bdi dir="ltr">order</bdi>: 3; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 28
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">two</bdi> { <bdi dir="ltr">order</bdi>: 4; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تغير ترتيب العنصر المرئي داخل <bdi dir="ltr">Flexbox</bdi>. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 29
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">one</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">margin-left</bdi>: <bdi dir="ltr">160px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ff9800</bdi>; }
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد المسافة الخارجية اليسرى. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 30
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">three</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">margin-left</bdi>: <bdi dir="ltr">auto</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#795548</bdi>; }
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد المسافة الخارجية اليسرى. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 31
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">four</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#673ab7</bdi>; }
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 32
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">two</bdi> > <bdi dir="ltr">div</bdi> { <bdi dir="ltr">margin-left</bdi>: <bdi dir="ltr">34px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#8bc34a</bdi>; }
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد المسافة الخارجية اليسرى. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/solution-task-05.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/05 - CSS Flexbox — Child Order and Wrapping.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
