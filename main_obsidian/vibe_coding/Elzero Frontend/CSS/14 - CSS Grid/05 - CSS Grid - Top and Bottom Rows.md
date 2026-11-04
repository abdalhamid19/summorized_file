---
title: "CSS Grid - Top and Bottom Rows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 05
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi> - <bdi dir="ltr">Top</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Bottom</bdi> <bdi dir="ltr">Rows</bdi>

> [!question] السؤال
> رتّب أربعة عناصر <bdi dir="ltr">Grid</bdi> في صف علوي وصف سفلي، مع ترك مساحة وسطى فارغة، ووسّط الأب أفقيًا وطابق اللون الوردي في المرجع.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/reference-task-05.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">grid5</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">min(1220px, calc(100% - 40px)</bdi>);
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">620px</bdi>;
>   <bdi dir="ltr">margin-inline</bdi>: <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">35px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">1fr</bdi>;
>   <bdi dir="ltr">grid-template-rows</bdi>: <bdi dir="ltr">70px</bdi> <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">70px</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">35px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ddd</bdi>;
> }
>
> .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#e91e63</bdi>;
> }
>
> .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(1) { <bdi dir="ltr">grid-column</bdi>: 1; <bdi dir="ltr">grid-row</bdi>: 1; }
> .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(2) { <bdi dir="ltr">grid-column</bdi>: 2; <bdi dir="ltr">grid-row</bdi>: 1; }
> .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(3) { <bdi dir="ltr">grid-column</bdi>: 1; <bdi dir="ltr">grid-row</bdi>: 4; }
> .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(4) { <bdi dir="ltr">grid-column</bdi>: 2; <bdi dir="ltr">grid-row</bdi>: 4; }
> ```
>
> ### الفكرة الأساسية
> تعرّف الشبكة صفًا علويًا وصفًا سفليًا مع صفين كبيرين بينهما. توضع العناصر الأربعة في الصف الأول والأخير، وتظل المساحة الوسطى فارغة.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.grid5`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid5 > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid5 > :nth-child(1)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid5 > :nth-child(2)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid5 > :nth-child(3)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid5 > :nth-child(4)`
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الأبعاد والمسافات
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `height`
> > تحدد ارتفاع العنصر.
> >
> > ##### `margin-inline`
> > تضبط الهامشين على محور السطر؛ `auto` يوسّط العنصر أفقيًا.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > ##### `gap`
> > تحدد المسافة بين عناصر التخطيط.
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
> > ##### `place-items`
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > ##### `grid-column`
> > تحدد أعمدة بداية العنصر ونهايته.
> >
> > ##### `grid-row`
> > تحدد صفوف بداية العنصر ونهايته.
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
> > .<bdi dir="ltr">grid5</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">min(1220px, calc(100% - 40px)</bdi>);
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">height</bdi>: <bdi dir="ltr">620px</bdi>;
> > ```
> > تحدد ارتفاع العنصر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin-inline</bdi>: <bdi dir="ltr">auto</bdi>;
> > ```
> > تضبط الهامشين على محور السطر؛ <bdi dir="ltr">auto</bdi> يوسّط العنصر أفقيًا.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">35px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">1fr</bdi>;
> > ```
> > تحدد الأعمدة وعرض كل عمود في <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-rows</bdi>: <bdi dir="ltr">70px</bdi> <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">1fr</bdi> <bdi dir="ltr">70px</bdi>;
> > ```
> > تحدد الصفوف وارتفاع كل صف.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">35px</bdi>;
> > ```
> > تحدد المسافة بين عناصر التخطيط.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ddd</bdi>;
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
> > .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">div</bdi> {
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
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
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(1) { <bdi dir="ltr">grid-column</bdi>: 1; <bdi dir="ltr">grid-row</bdi>: 1; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد أعمدة بداية العنصر ونهايته. تحدد صفوف بداية العنصر ونهايته. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(2) { <bdi dir="ltr">grid-column</bdi>: 2; <bdi dir="ltr">grid-row</bdi>: 1; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد أعمدة بداية العنصر ونهايته. تحدد صفوف بداية العنصر ونهايته. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(3) { <bdi dir="ltr">grid-column</bdi>: 1; <bdi dir="ltr">grid-row</bdi>: 4; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد أعمدة بداية العنصر ونهايته. تحدد صفوف بداية العنصر ونهايته. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid5</bdi> > <bdi dir="ltr">:nth-child</bdi>(4) { <bdi dir="ltr">grid-column</bdi>: 2; <bdi dir="ltr">grid-row</bdi>: 4; }
> > ```
> > يختار العنصر بحسب ترتيبه بين الإخوة؛ الرقم يحدد الموضع المطلوب. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد أعمدة بداية العنصر ونهايته. تحدد صفوف بداية العنصر ونهايته. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/solution-task-05.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/05 - CSS Grid - Top and Bottom Rows.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/CSS Grid Assignments 57-64.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
