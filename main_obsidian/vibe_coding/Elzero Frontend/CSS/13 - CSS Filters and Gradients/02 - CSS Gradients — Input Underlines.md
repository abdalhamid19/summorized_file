---
title: "CSS Gradients — Input Underlines"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-filters-and-gradients
  - تكليف
aliases:
  - CSS Gradients — Input Underlines
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Gradients</bdi> — <bdi dir="ltr">Input</bdi> <bdi dir="ltr">Underlines</bdi>

> [!question] السؤال
> نسّق ثلاثة حقول إدخال بعرض <bdi dir="ltr">600px</bdi> ووسطها أفقيًا، بألوان المرجع ومؤشر كتابة أحمر، دون استخدام <bdi dir="ltr">Box</bdi> <bdi dir="ltr">Shadow</bdi>. اجعل قيمة الحقل الأول <bdi dir="ltr">Elzero</bdi>.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">fields</bdi> <bdi dir="ltr">input</bdi> {
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">block</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">600px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">60px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi> <bdi dir="ltr">16px</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">16px</bdi> <bdi dir="ltr">24px</bdi>;
>   <bdi dir="ltr">border</bdi>: 0;
>   <bdi dir="ltr">border-bottom</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">transparent</bdi>;
>   <bdi dir="ltr">border-image</bdi>: <bdi dir="ltr">linear-gradient(90deg, #f44336 0 50%, #009688 50% 100%)</bdi> 1;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f4f4f4</bdi>;
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">26px</bdi>;
>   <bdi dir="ltr">caret-color</bdi>: <bdi dir="ltr">red</bdi>;
> }
>
> .<bdi dir="ltr">fields</bdi> <bdi dir="ltr">input</bdi>:<bdi dir="ltr">:placeholder</bdi> { <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#777</bdi>; <bdi dir="ltr">opacity</bdi>: 1; }
> ```
>
> ### الفكرة الأساسية
> يرسم `border-image` تدرجًا على الحد السفلي لكل حقل. ويغيّر `caret-color` لون مؤشر الكتابة إلى الأحمر، بينما ينسق ::`placeholder` النص الإرشادي.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Gradients</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.fields input`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.fields input::placeholder`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
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
> > #### الحدود والظلال
> > ##### `border`
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > ##### `border-bottom`
> > ترسم الحد السفلي.
> >
> > ##### `border-image`
> > تستخدم صورة أو تدرجًا لملء الحدود.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `font-size`
> > تحدد حجم النص.
> >
> > ##### `caret-color`
> > تغير لون مؤشر الكتابة.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > ##### `opacity`
> > تحدد درجة شفافية العنصر.
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
> > .<bdi dir="ltr">fields</bdi> <bdi dir="ltr">input</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">block</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
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
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">60px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi> <bdi dir="ltr">16px</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">16px</bdi> <bdi dir="ltr">24px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border</bdi>: 0;
> > ```
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-bottom</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">transparent</bdi>;
> > ```
> > ترسم الحد السفلي.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-image</bdi>: <bdi dir="ltr">linear-gradient(90deg, #f44336 0 50%, #009688 50% 100%)</bdi> 1;
> > ```
> > تستخدم صورة أو تدرجًا لملء الحدود.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f4f4f4</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">26px</bdi>;
> > ```
> > تحدد حجم النص.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">caret-color</bdi>: <bdi dir="ltr">red</bdi>;
> > ```
> > تغير لون مؤشر الكتابة.
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
> > .<bdi dir="ltr">fields</bdi> <bdi dir="ltr">input</bdi>:<bdi dir="ltr">:placeholder</bdi> { <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#777</bdi>; <bdi dir="ltr">opacity</bdi>: 1; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد لون النص أو المحتوى. تحدد درجة شفافية العنصر. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/assets/solution-task-02.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/02 - CSS Gradients — Input Underlines.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/13 - CSS Filters and Gradients/CSS Filters Gradients Assignments 54-56.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-54-to-56/)
