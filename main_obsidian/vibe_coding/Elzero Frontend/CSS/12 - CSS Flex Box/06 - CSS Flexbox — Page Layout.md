---
title: "CSS Flexbox — Page Layout"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Page Layout
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi> — <bdi dir="ltr">Page</bdi> <bdi dir="ltr">Layout</bdi>

> [!question] السؤال
> استخدم <bdi dir="ltr">Flex</bdi> فقط لتوزيع الرأس والمحتوى والشريط الجانبي والتذييل. اجعل القيم المتكررة متغيرات <bdi dir="ltr">CSS</bdi>.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/reference-task-06.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">:root</bdi> {
>   <bdi dir="ltr">--gap</bdi>: <bdi dir="ltr">12px</bdi>;
>   <bdi dir="ltr">--surface</bdi>: <bdi dir="ltr">#ddd</bdi>;
>   <bdi dir="ltr">--pad</bdi>: <bdi dir="ltr">14px</bdi>;
> }
>
> .<bdi dir="ltr">page</bdi> {
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">500px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">flex-direction</bdi>: <bdi dir="ltr">column</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">var(--gap)</bdi>;
> }
>
> .<bdi dir="ltr">header</bdi>, .<bdi dir="ltr">main-area</bdi>, .<bdi dir="ltr">footer</bdi> {
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">var(--gap)</bdi>;
> }
>
> .<bdi dir="ltr">logo</bdi>, .<bdi dir="ltr">links</bdi>, .<bdi dir="ltr">content</bdi>, .<bdi dir="ltr">sidebar</bdi>, .<bdi dir="ltr">copyright</bdi>, .<bdi dir="ltr">design</bdi> {
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">var(--pad)</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">var(--surface)</bdi>;
> }
>
> .<bdi dir="ltr">links</bdi> {
>   <bdi dir="ltr">flex</bdi>: 1;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
>   <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">flex-end</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">list-style</bdi>: <bdi dir="ltr">none</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0;
> }
>
> .<bdi dir="ltr">main-area</bdi> { <bdi dir="ltr">flex</bdi>: 1; }
> .<bdi dir="ltr">content</bdi> { <bdi dir="ltr">flex</bdi>: 3; }
> .<bdi dir="ltr">sidebar</bdi> { <bdi dir="ltr">flex</bdi>: 1; }
> .<bdi dir="ltr">copyright</bdi>, .<bdi dir="ltr">design</bdi> { <bdi dir="ltr">flex</bdi>: 1; }
> .<bdi dir="ltr">design</bdi> { <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">right</bdi>; }
> ```
>
> ### الفكرة الأساسية
> تقسم الصفحة إلى رأس ومحتوى وتذييل باستخدام `Flex` عمودي. توحّد متغيرات `CSS` المسافات والحشو والخلفية، بينما توزع قيم `flex` المساحة بين المناطق.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Flexbox</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `:root`
> > يشير إلى جذر المستند، وهو مكان شائع لتعريف المتغيرات العامة.
> >
> > ##### `.page`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.header, .main-area, .footer`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.logo, .links, .content, .sidebar, .copyright, .design`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.links`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.main-area`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.content`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.sidebar`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.copyright, .design`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.design`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### متغيرات <bdi dir="ltr">CSS</bdi>
> > ##### `--gap`
> > يعرّف متغير `CSS` باسم --`gap` ويحفظ فيه القيمة `12px` لإعادة استخدامها.
> >
> > ##### `--surface`
> > يعرّف متغير `CSS` باسم --`surface` ويحفظ فيه القيمة #`ddd` لإعادة استخدامها.
> >
> > ##### `--pad`
> > يعرّف متغير `CSS` باسم --`pad` ويحفظ فيه القيمة `14px` لإعادة استخدامها.
> >
> > #### الأبعاد والمسافات
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > ##### `gap`
> > تحدد المسافة بين عناصر التخطيط.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">Flexbox</bdi>
> > ##### `flex-direction`
> > تحدد اتجاه المحور الرئيسي لعناصر `Flex`.
> >
> > ##### `flex`
> > تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي.
> >
> > ##### `justify-content`
> > توزع العناصر على المحور الرئيسي.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `list-style`
> > تتحكم في علامة القائمة الافتراضية.
> >
> > ##### `text-align`
> > تحاذي النص داخل العنصر.
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
> > ##### `--` و `var()`
> > تخزن قيمة في متغير <bdi dir="ltr">CSS</bdi> ثم تعيد استخدامها أو تحدد قيمة بديلة.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">:root</bdi> {
> > ```
> > يشير إلى جذر المستند، وهو مكان شائع لتعريف المتغيرات العامة.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">--gap</bdi>: <bdi dir="ltr">12px</bdi>;
> > ```
> > يعرّف متغير <bdi dir="ltr">CSS</bdi> باسم <bdi dir="ltr">--gap</bdi> ويحفظ فيه القيمة <bdi dir="ltr">12px</bdi> لإعادة استخدامها.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">--surface</bdi>: <bdi dir="ltr">#ddd</bdi>;
> > ```
> > يعرّف متغير <bdi dir="ltr">CSS</bdi> باسم <bdi dir="ltr">--surface</bdi> ويحفظ فيه القيمة <bdi dir="ltr">#ddd</bdi> لإعادة استخدامها.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">--pad</bdi>: <bdi dir="ltr">14px</bdi>;
> > ```
> > يعرّف متغير <bdi dir="ltr">CSS</bdi> باسم <bdi dir="ltr">--pad</bdi> ويحفظ فيه القيمة <bdi dir="ltr">14px</bdi> لإعادة استخدامها.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">page</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">500px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">flex-direction</bdi>: <bdi dir="ltr">column</bdi>;
> > ```
> > تحدد اتجاه المحور الرئيسي لعناصر <bdi dir="ltr">Flex</bdi>.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">var(--gap)</bdi>;
> > ```
> > تحدد المسافة بين عناصر التخطيط.
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
> > .<bdi dir="ltr">header</bdi>, .<bdi dir="ltr">main-area</bdi>, .<bdi dir="ltr">footer</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">var(--gap)</bdi>;
> > ```
> > تحدد المسافة بين عناصر التخطيط.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">logo</bdi>, .<bdi dir="ltr">links</bdi>, .<bdi dir="ltr">content</bdi>, .<bdi dir="ltr">sidebar</bdi>, .<bdi dir="ltr">copyright</bdi>, .<bdi dir="ltr">design</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">var(--pad)</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">var(--surface)</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">links</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">flex</bdi>: 1;
> > ```
> > تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">flex</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">justify-content</bdi>: <bdi dir="ltr">flex-end</bdi>;
> > ```
> > توزع العناصر على المحور الرئيسي.
> >
> > #### السطر 24
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">20px</bdi>;
> > ```
> > تحدد المسافة بين عناصر التخطيط.
> >
> > #### السطر 25
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">list-style</bdi>: <bdi dir="ltr">none</bdi>;
> > ```
> > تتحكم في علامة القائمة الافتراضية.
> >
> > #### السطر 26
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 27
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 28
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">main-area</bdi> { <bdi dir="ltr">flex</bdi>: 1; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 29
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">content</bdi> { <bdi dir="ltr">flex</bdi>: 3; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 30
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">sidebar</bdi> { <bdi dir="ltr">flex</bdi>: 1; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 31
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">copyright</bdi>, .<bdi dir="ltr">design</bdi> { <bdi dir="ltr">flex</bdi>: 1; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد تمدد العنصر المرن أو انكماشه وحجمه الأساسي. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 32
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">design</bdi> { <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">right</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحاذي النص داخل العنصر. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/assets/solution-task-06.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/06 - CSS Flexbox — Page Layout.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/12 - CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
