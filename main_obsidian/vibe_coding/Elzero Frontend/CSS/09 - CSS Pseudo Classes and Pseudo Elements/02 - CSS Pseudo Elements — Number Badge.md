---
title: "CSS Pseudo Elements — Number Badge"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Elements — Number Badge
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Pseudo</bdi> <bdi dir="ltr">Elements</bdi> — <bdi dir="ltr">Number</bdi> <bdi dir="ltr">Badge</bdi>

> [!question] السؤال
> أضف الرقم 1 بجانب شريط رمادي يحتوي النص، مع المحافظة على شكل المرجع.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">90%</bdi>;
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">88px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">40px</bdi> <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi> <bdi dir="ltr">40px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#d3d3d3</bdi>;
> }
>
> <bdi dir="ltr">div</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: "1";
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
>   <bdi dir="ltr">top</bdi>: 0;
>   <bdi dir="ltr">left</bdi>: -<bdi dir="ltr">46px</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">44px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100%</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f00</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> ننشئ الرقم بعنصر ::`before` بدل إضافته إلى `HTML`، ونضع الحاوية في `position`: `relative` لتكون مرجعًا لموضع الرقم المطلق.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">Pseudo-classes</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Pseudo-elements</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `div`
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > ##### `div::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص.
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
> > #### الأبعاد والمسافات
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > ##### `height`
> > تحدد ارتفاع العنصر.
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
> > #### العناصر الزائفة والعدادات
> > ##### `content`
> > يضيف النص المحدد إلى العنصر الزائف من دون إنشاء عنصر `HTML` جديد.
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
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">div</bdi> {
> > ```
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">90%</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">88px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">40px</bdi> <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi> <bdi dir="ltr">40px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#d3d3d3</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
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
> > <bdi dir="ltr">div</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: "1";
> > ```
> > يضيف النص المحدد إلى العنصر الزائف من دون إنشاء عنصر <bdi dir="ltr">HTML</bdi> جديد.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: 0;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: -<bdi dir="ltr">46px</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">44px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100%</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f00</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
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
> > <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
> > ```
> > تحدد سماكة الحروف.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/solution-task-02.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/02 - CSS Pseudo Elements — Number Badge.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
