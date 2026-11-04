---
title: "CSS Position, List, and Table - Positioning and Layer Order"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف ترتيب الطبقات والتموضع
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Position</bdi>, <bdi dir="ltr">List</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Table</bdi> — <bdi dir="ltr">Positioning</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Layer</bdi> <bdi dir="ltr">Order</bdi>

> [!question] السؤال
> استخدم البنية السابقة دون تعديلها. اجعل العناصر مربعة بمقاس `100×100px`، واضبط ترتيب الطبقات. يجب أن يبعد العنصر الأزرق `20px` من أعلى الصفحة ويسارها.
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-30-to-33/)

> [!info] حدود المصدر والمطابقة
> تثبت صفحة التكليف مقاس المربعات `100×100px`، وإزاحة المربع الأزرق `20px` من الأعلى واليسار، وترتيب الطبقات. البنية السابقة وألوان بقية الأشكال غير ظاهرة في النص المتاح؛ لذلك ألوان المربعات الأخرى والمعاينة توضيحية.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">stage</bdi> {
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">static</bdi>;
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">280px</bdi>;
> }
>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">square</bdi> {
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> }
>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">red</bdi> {
>   <bdi dir="ltr">top</bdi>: <bdi dir="ltr">80px</bdi>;
>   <bdi dir="ltr">left</bdi>: <bdi dir="ltr">80px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#e91e63</bdi>;
>   <bdi dir="ltr">z-index</bdi>: 1;
> }
>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">green</bdi> {
>   <bdi dir="ltr">top</bdi>: <bdi dir="ltr">50px</bdi>;
>   <bdi dir="ltr">left</bdi>: <bdi dir="ltr">50px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#4caf50</bdi>;
>   <bdi dir="ltr">z-index</bdi>: 2;
> }
>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">blue</bdi> {
>   <bdi dir="ltr">top</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">left</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#2196f3</bdi>;
>   <bdi dir="ltr">z-index</bdi>: 3;
> }
> ```
>
> ### الفكرة الأساسية
> تُخرج المربعات من التدفق العادي بواسطة التموضع المطلق، ثم تحدد قيم الأعلى واليسار مواضعها. يظل الحاوي غير المتموضع بلا مرجع خاص، لذلك يبدأ المربع الأزرق عند إزاحة `20px` من حافة الصفحة، وتضع قيمة `z-index` الأعلى فوق البقية.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Positioning</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `#task-01 .stage`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-01 .square`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-01 .red`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-01 .green`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-01 .blue`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
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
> > ##### `z-index`
> > تحدد ترتيب العنصر فوق العناصر المتداخلة؛ الرقم الأكبر يظهر أمام الأصغر.
> >
> > #### الأبعاد والمسافات
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `height`
> > تحدد ارتفاع العنصر.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> > ##### `place-items`
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### الألوان والنص
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### علامات صياغة <bdi dir="ltr">CSS</bdi>
> >
> > ##### `:`
> > تفصل اسم الخاصية عن قيمتها.
> >
> > ##### `;`
> > تنهي تصريح <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">stage</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">static</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">280px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">square</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
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
> > #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">red</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: <bdi dir="ltr">80px</bdi>;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: <bdi dir="ltr">80px</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#e91e63</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">z-index</bdi>: 1;
> > ```
> > تحدد ترتيب العنصر فوق العناصر المتداخلة؛ الرقم الأكبر يظهر أمام الأصغر.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">green</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: <bdi dir="ltr">50px</bdi>;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: <bdi dir="ltr">50px</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#4caf50</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">z-index</bdi>: 2;
> > ```
> > تحدد ترتيب العنصر فوق العناصر المتداخلة؛ الرقم الأكبر يظهر أمام الأصغر.
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
> > #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">blue</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 26
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: <bdi dir="ltr">20px</bdi>;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 27
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: <bdi dir="ltr">20px</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 28
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#2196f3</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 29
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">z-index</bdi>: 3;
> > ```
> > تحدد ترتيب العنصر فوق العناصر المتداخلة؛ الرقم الأكبر يظهر أمام الأصغر.
> >
> > #### السطر 30
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/assets/solution-overview.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/01 - CSS Position, List, and Table - Positioning and Layer Order.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية للدروس 30–33](https://elzero.org/css-assignments-lesson-from-30-to-33/)
