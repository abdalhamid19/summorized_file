---
title: "CSS Pseudo Classes — Centered Blocks"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Classes — Centered Blocks
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Pseudo</bdi> <bdi dir="ltr">Classes</bdi> — <bdi dir="ltr">Centered</bdi> <bdi dir="ltr">Blocks</bdi>

> [!question] السؤال
> نفّذ الشكل بثلاثة عناصر بعرض <bdi dir="ltr">300px</bdi> وارتفاع <bdi dir="ltr">60px</bdi>، وسطها أفقيًا، واجعل العنصر الأوسط أحمر والأول والثالث رماديين.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">300px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">60px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi> <bdi dir="ltr">25px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> }
>
> <bdi dir="ltr">div</bdi>:<bdi dir="ltr">nth-child(2)</bdi> {
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f00</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> تحدد قاعدة عامة الأبعاد واللون الرمادي للعناصر الثلاثة، ثم يختار `nth-child(2)` العنصر الثاني وحده ويغيّر لونه إلى الأحمر.
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
> > ##### `div:nth-child(2)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب.
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
> > #### الألوان والنص
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
> > <bdi dir="ltr">div</bdi> {
> > ```
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">300px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">60px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi> <bdi dir="ltr">25px</bdi>;
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
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">div</bdi>:<bdi dir="ltr">nth-child(2)</bdi> {
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f00</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/solution-task-01.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/01 - CSS Pseudo Classes — Centered Blocks.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
