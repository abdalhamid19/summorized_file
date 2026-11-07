---
title: "CSS Grid - Full Page Areas"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 02
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi> - <bdi dir="ltr">Full</bdi> <bdi dir="ltr">Page</bdi> <bdi dir="ltr">Areas</bdi>

> [!question] السؤال
> أنشئ توزيع الصفحة بالشكل والألوان المرجعية، واستخدم <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi> فقط. يجب أن يمتد التخطيط إلى كامل مساحة الصفحة، ويحتوي على <bdi dir="ltr">Header</bdi> وSection وAside وFooter.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/reference-task-02.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">grid2</bdi> {
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100vh</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">minmax(0, 2fr)</bdi> <bdi dir="ltr">minmax(220px, 1fr)</bdi>;
>   <bdi dir="ltr">grid-template-rows</bdi>: <bdi dir="ltr">90px</bdi> <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">90px</bdi>;
>   <bdi dir="ltr">grid-template-areas</bdi>:
>     "<bdi dir="ltr">header</bdi> <bdi dir="ltr">header</bdi>"
>     "<bdi dir="ltr">section</bdi> <bdi dir="ltr">aside</bdi>"
>     "<bdi dir="ltr">footer</bdi> <bdi dir="ltr">footer</bdi>";
> }
>
> .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(1) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">header</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#03a9f4</bdi>; }
> .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(2) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">section</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ff5722</bdi>; }
> .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(3) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">aside</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#607d8b</bdi>; }
> .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(4) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">footer</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#009688</bdi>; }
>
> .<bdi dir="ltr">grid2</bdi> > * {
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">28px</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> تحدد `grid-template-areas` أسماء المناطق ومكانها في الصفوف. ثم تربط `grid-area` كل عنصر باسمه لتوزيع `Header` و`Section` و`Aside` و`Footer`.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.grid2`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid2 > *`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid2 > :nth-child(1)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid2 > :nth-child(2)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid2 > :nth-child(3)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid2 > :nth-child(4)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الأبعاد والمسافات
> > ##### `height`
> > تحدد ارتفاع العنصر.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> > ##### `grid-template-columns`
> > تحدد الأعمدة وعرض كل عمود في `Grid`.
> >
> > ##### `grid-template-rows`
> > تحدد الصفوف وارتفاع كل صف.
> >
> > ##### `grid-template-areas`
> > ترسم خريطة الصفوف والأعمدة بأسماء مناطق.
> >
> > ##### `grid-area`
> > تربط العنصر بمنطقة مسماة.
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
> > ##### `,`
> > تفصل القيم أو المحددات بحسب موضعها.
> >
> > ##### `>`
> > تشير إلى الابن المباشر في المحدد؛ وقد تفصل خطوط <bdi dir="ltr">Grid</bdi> في قيم الشبكة.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid2</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">100vh</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">minmax(0, 2fr)</bdi> <bdi dir="ltr">minmax(220px, 1fr)</bdi>;
> > ```
> > تحدد الأعمدة وعرض كل عمود في <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-rows</bdi>: <bdi dir="ltr">90px</bdi> <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">90px</bdi>;
> > ```
> > تحدد الصفوف وارتفاع كل صف.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-areas</bdi>:
> > ```
> > ترسم خريطة الصفوف والأعمدة بأسماء مناطق.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">header</bdi> <bdi dir="ltr">header</bdi>"
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">section</bdi> <bdi dir="ltr">aside</bdi>"
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">footer</bdi> <bdi dir="ltr">footer</bdi>";
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(1) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">header</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#03a9f4</bdi>; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(2) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">section</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ff5722</bdi>; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(3) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">aside</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#607d8b</bdi>; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid2</bdi> > <bdi dir="ltr">:nth-child</bdi>(4) { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">footer</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#009688</bdi>; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid2</bdi> > * {
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">28px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/solution-task-02.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/02 - CSS Grid - Full Page Areas.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/CSS Grid Assignments 57-64.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
