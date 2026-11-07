---
title: "CSS Pseudo Elements — Numbered Product Rows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Elements — Numbered Product Rows
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Pseudo</bdi> <bdi dir="ltr">Elements</bdi> — <bdi dir="ltr">Numbered</bdi> <bdi dir="ltr">Product</bdi> <bdi dir="ltr">Rows</bdi>

> [!question] السؤال
> أنشئ ستة صفوف للعناوين مع أرقام متتابعة يسارها وشريط أحمر رفيع عند اليمين، باستخدام <bdi dir="ltr">pseudo-elements</bdi>.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/reference-task-04.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">products</bdi> {
>   <bdi dir="ltr">counter-reset</bdi>: <bdi dir="ltr">product</bdi>;
> }
>
> .<bdi dir="ltr">product</bdi> {
>   <bdi dir="ltr">counter-increment</bdi>: <bdi dir="ltr">product</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">align-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">60px</bdi>;
>   <bdi dir="ltr">border-right</bdi>: <bdi dir="ltr">5px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#f44336</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> }
>
> .<bdi dir="ltr">product</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: <bdi dir="ltr">counter(product)</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">60px</bdi>;
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">60px</bdi>;
>   <bdi dir="ltr">margin-right</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f44336</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> يبدأ العداد من الحاوية ويزداد مرة لكل صف. يعرض ::`before` قيمة العداد بجوار النص، فتتولد الأرقام تلقائيًا من ترتيب العناصر.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">Pseudo-classes</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Pseudo-elements</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.products`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.product`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.product::before`
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
> > ##### `align-items`
> > تحدد محاذاة الأبناء على المحور العرضي.
> >
> > #### الأبعاد والمسافات
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `margin-right`
> > تحدد المسافة الخارجية اليمنى.
> >
> > #### الحدود والظلال
> > ##### `border-right`
> > ترسم الحد الأيمن.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > ##### `font-weight`
> > تحدد سماكة الحروف.
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
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">products</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">counter-reset</bdi>: <bdi dir="ltr">product</bdi>;
> > ```
> > تنشئ عدادًا عند بداية الحاوية.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">product</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">counter-increment</bdi>: <bdi dir="ltr">product</bdi>;
> > ```
> > تزيد قيمة العداد لكل عنصر يطابق القاعدة.
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
> > <bdi dir="ltr">align-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تحدد محاذاة الأبناء على المحور العرضي.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">60px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-right</bdi>: <bdi dir="ltr">5px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#f44336</bdi>;
> > ```
> > ترسم الحد الأيمن.
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
> > .<bdi dir="ltr">product</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: <bdi dir="ltr">counter(product)</bdi>;
> > ```
> > يعرض رقم العداد داخل العنصر الزائف، ويمكن ضم نص توضيحي له.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">60px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">60px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin-right</bdi>: <bdi dir="ltr">20px</bdi>;
> > ```
> > تحدد المسافة الخارجية اليمنى.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f44336</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
> > ```
> > تحدد سماكة الحروف.
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
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/solution-task-04.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/04 - CSS Pseudo Elements — Numbered Product Rows.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
