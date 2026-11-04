---
title: "CSS Flexbox — Center Element and Text"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Center Element and Text
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi> — <bdi dir="ltr">Center</bdi> <bdi dir="ltr">Element</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Text</bdi>

> [!question] السؤال
> استخدم بنية عنصر واحد كما هي. اجعل عرضه وارتفاعه <bdi dir="ltr">100px</bdi>، ووسّطه أفقيًا، ثم وسّط كلمة <bdi dir="ltr">Elzero</bdi> داخله بالطول والعرض باستخدام <bdi dir="ltr">Flex</bdi>، مع الألوان المرجعية.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">align-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#ff5722</bdi>;
>   <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
>   <bdi dir="ltr">box-shadow</bdi>: -<bdi dir="ltr">12px</bdi> 0 <bdi dir="ltr">#03a9f4</bdi>, <bdi dir="ltr">12px</bdi> 0 <bdi dir="ltr">#ff5722</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> يحوّل `display` العنصر إلى `Flex`، ثم توسّط `justify-content` و`align-items` النص على المحورين. يوسّط `margin`: 0 `auto` الدائرة داخل المساحة.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `div`
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
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
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">Flexbox</bdi>
> > ##### `justify-content`
> > توزع العناصر على المحور الرئيسي.
> >
> > ##### `align-items`
> > تحدد محاذاة الأبناء على المحور العرضي.
> >
> > #### الحدود والظلال
> > ##### `border-radius`
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > ##### `box-shadow`
> > ترسم ظلًا حول العنصر أو داخله.
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
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">100px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100px</bdi>;
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
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > توزع العناصر على المحور الرئيسي.
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
> > <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تدوّر زوايا العنصر بقيم يمكن أن تختلف بين الزوايا.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#ff5722</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-weight</bdi>: <bdi dir="ltr">bold</bdi>;
> > ```
> > تحدد سماكة الحروف.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">box-shadow</bdi>: -<bdi dir="ltr">12px</bdi> 0 <bdi dir="ltr">#03a9f4</bdi>, <bdi dir="ltr">12px</bdi> 0 <bdi dir="ltr">#ff5722</bdi>;
> > ```
> > ترسم ظلًا حول العنصر أو داخله.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/solution-task-01.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/01 - CSS Flexbox — Center Element and Text.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
