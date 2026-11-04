---
title: "03 - CSS Position, List, and Table - Styled List with Attributes"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف Styled List with Attributes
---

# 03 - <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Position</bdi>, <bdi dir="ltr">List</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Table</bdi> - <bdi dir="ltr">Styled</bdi> <bdi dir="ltr">List</bdi> <bdi dir="ltr">with</bdi> <bdi dir="ltr">Attributes</bdi>

> [!question] السؤال
> أنشئ قائمة بعرض <bdi dir="ltr">400px</bdi> ووسّطها أفقيًا. يمكنك إضافة `class` أو `attribute` لتحقيق الشكل، مع الحفاظ على الألوان كما في الصورة.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-30-to-33/>)
>
> [!info] حدود المصدر والمطابقة
> تحدد صفحة التكليف قائمة بعرض `400px` وتوسيطها، وتسمح باستخدام `class` أو `attribute`. تعذّر علي قراءة تفاصيل الصورة المرجعية؛ لذلك القائمة والألوان في المعاينة مثال توضيحي، ولا أؤكد مطابقتها للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> {
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">24px</bdi> <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: 0;
>   <bdi dir="ltr">list-style</bdi>: <bdi dir="ltr">none</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">2px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#2196f3</bdi>;
> }
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> <bdi dir="ltr">li</bdi> {
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">14px</bdi> <bdi dir="ltr">18px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">64px</bdi>;
>   <bdi dir="ltr">border-bottom</bdi>: <bdi dir="ltr">1px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#bbb</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f5f5f5</bdi>;
> }
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> <bdi dir="ltr">li</bdi>:<bdi dir="ltr">last-child</bdi> { <bdi dir="ltr">border-bottom</bdi>: 0; }
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> <bdi dir="ltr">li</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: <bdi dir="ltr">attr(data-number)</bdi>;
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
>   <bdi dir="ltr">left</bdi>: <bdi dir="ltr">14px</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: 700;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#e91e63</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> نستخدم العنصر `li` مرجعًا لموضع الرقم، وننشئ الرقم قبل النص من قيمة `data-number`. هكذا تبقى الأرقام مرتبطة بعناصر القائمة من دون إضافة عنصر `HTML` مستقل لكل رقم.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Positioning</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `#task-03 .menu`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-03 .menu li`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-03 .menu li::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-03 .menu li:last-child`
> > يختار آخر ابن داخل الحاوية. يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الأبعاد والمسافات
> > ##### `box-sizing`
> > تحدد طريقة حساب العرض والارتفاع بالنسبة إلى الحشو والحدود.
> >
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### الألوان والنص
> > ##### `list-style`
> > تتحكم في علامة القائمة الافتراضية.
> >
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `font-weight`
> > تحدد سماكة الحروف.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > #### الحدود والظلال
> > ##### `border`
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > ##### `border-bottom`
> > ترسم الحد السفلي.
> >
> > #### التموضع وترتيب الطبقات
> > ##### `position`
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > ##### `left`
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### العناصر الزائفة والعدادات
> > ##### `content`
> > يضيف إلى العنصر الزائف قيمة خاصية `HTML` `data-number`.
> >
> > #### علامات صياغة <bdi dir="ltr">CSS</bdi>
> >
> > ##### `:`
> > تفصل اسم الخاصية عن قيمتها.
> >
> > ##### `;`
> > تنهي تصريح <bdi dir="ltr">CSS</bdi>.
> >
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
> > ```
> > تحدد طريقة حساب العرض والارتفاع بالنسبة إلى الحشو والحدود.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">24px</bdi> <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: 0;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">list-style</bdi>: <bdi dir="ltr">none</bdi>;
> > ```
> > تتحكم في علامة القائمة الافتراضية.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border</bdi>: <bdi dir="ltr">2px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#2196f3</bdi>;
> > ```
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> <bdi dir="ltr">li</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">14px</bdi> <bdi dir="ltr">18px</bdi> <bdi dir="ltr">14px</bdi> <bdi dir="ltr">64px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-bottom</bdi>: <bdi dir="ltr">1px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#bbb</bdi>;
> > ```
> > ترسم الحد السفلي.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f5f5f5</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> <bdi dir="ltr">li</bdi>:<bdi dir="ltr">last-child</bdi> { <bdi dir="ltr">border-bottom</bdi>: 0; }
> > ```
> > يختار آخر ابن داخل الحاوية. يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. ترسم الحد السفلي. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">menu</bdi> <bdi dir="ltr">li</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: <bdi dir="ltr">attr(data-number)</bdi>;
> > ```
> > يضيف إلى العنصر الزائف قيمة خاصية <bdi dir="ltr">HTML</bdi> <bdi dir="ltr">data-number</bdi>.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: <bdi dir="ltr">14px</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-weight</bdi>: 700;
> > ```
> > تحدد سماكة الحروف.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#e91e63</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 22
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
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/03 - CSS Position, List, and Table - Styled List with Attributes.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-30-to-33/)
