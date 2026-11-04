---
title: "CSS Gradients — Multicolor Frame"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-filters-and-gradients
  - تكليف
aliases:
  - CSS Gradients — Multicolor Frame
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Gradients</bdi> — <bdi dir="ltr">Multicolor</bdi> <bdi dir="ltr">Frame</bdi>

> [!question] السؤال
> أنشئ عنصرًا عرضه <bdi dir="ltr">600px</bdi> في وسط الصفحة، بإطار متدرج متعدد الألوان وخلفية داخلية رمادية ونص <bdi dir="ltr">Elzero</bdi>. لا تستخدم <bdi dir="ltr">Box</bdi> <bdi dir="ltr">Shadow</bdi>.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">frame</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">600px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">8px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">linear-gradient</bdi>(
>     <bdi dir="ltr">90deg</bdi>,
>     <bdi dir="ltr">#f44336</bdi> 0 <bdi dir="ltr">20%</bdi>,
>     <bdi dir="ltr">#2196f3</bdi> <bdi dir="ltr">20%</bdi> <bdi dir="ltr">40%</bdi>,
>     <bdi dir="ltr">#4caf50</bdi> <bdi dir="ltr">40%</bdi> <bdi dir="ltr">60%</bdi>,
>     <bdi dir="ltr">#e91e63</bdi> <bdi dir="ltr">60%</bdi> <bdi dir="ltr">80%</bdi>,
>     <bdi dir="ltr">#673ab7</bdi> <bdi dir="ltr">80%</bdi> <bdi dir="ltr">100%</bdi>
>   );
> }
>
> .<bdi dir="ltr">inner</bdi> {
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">86px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
>   <bdi dir="ltr">font</bdi>: <bdi dir="ltr">bold</bdi> <bdi dir="ltr">56px</bdi> <bdi dir="ltr">Georgia</bdi>, <bdi dir="ltr">serif</bdi>;
>   <bdi dir="ltr">letter-spacing</bdi>: <bdi dir="ltr">16px</bdi>;
> }
>
> .<bdi dir="ltr">inner</bdi>:<bdi dir="ltr">:first-letter</bdi> { <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#f44336</bdi>; }
> ```
>
> ### الفكرة الأساسية
> ينشئ `linear-gradient` أشرطة الألوان حول مساحة داخلية رمادية. يترك `padding` سمكًا ظاهرًا حول الداخل، فيبدو كإطار من دون `Box` `Shadow`.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Gradients</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.frame`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.inner`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.inner::first-letter`
> > يختار الحرف الأول من النص لتنسيقه منفصلًا. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الأبعاد والمسافات
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `font`
> > تختصر خصائص الخط.
> >
> > ##### `letter-spacing`
> > تحدد المسافة بين الحروف.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
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
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">frame</bdi> {
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
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">8px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">linear-gradient</bdi>(
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">90deg</bdi>,
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">#f44336</bdi> 0 <bdi dir="ltr">20%</bdi>,
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">#2196f3</bdi> <bdi dir="ltr">20%</bdi> <bdi dir="ltr">40%</bdi>,
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">#4caf50</bdi> <bdi dir="ltr">40%</bdi> <bdi dir="ltr">60%</bdi>,
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">#e91e63</bdi> <bdi dir="ltr">60%</bdi> <bdi dir="ltr">80%</bdi>,
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">#673ab7</bdi> <bdi dir="ltr">80%</bdi> <bdi dir="ltr">100%</bdi>
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > );
> > ```
> > يكمل قاعدة التنسيق السابقة.
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
> > .<bdi dir="ltr">inner</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">86px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
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
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font</bdi>: <bdi dir="ltr">bold</bdi> <bdi dir="ltr">56px</bdi> <bdi dir="ltr">Georgia</bdi>, <bdi dir="ltr">serif</bdi>;
> > ```
> > تختصر خصائص الخط.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">letter-spacing</bdi>: <bdi dir="ltr">16px</bdi>;
> > ```
> > تحدد المسافة بين الحروف.
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
> > .<bdi dir="ltr">inner</bdi>:<bdi dir="ltr">:first-letter</bdi> { <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#f44336</bdi>; }
> > ```
> > يختار الحرف الأول من النص لتنسيقه منفصلًا. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد لون النص أو المحتوى. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/assets/solution-task-01.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/01 - CSS Gradients — Multicolor Frame.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/CSS Filters Gradients Assignments 54-56.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
