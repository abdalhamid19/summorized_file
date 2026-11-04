---
title: "CSS Grid - Company Team Challenge"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 06
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi> - <bdi dir="ltr">Company</bdi> <bdi dir="ltr">Team</bdi> <bdi dir="ltr">Challenge</bdi>

> [!question] السؤال
> حل التحدي ببناء بطاقات فريق باستخدام <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>، وتوزيعها في المساحات كما في الصورة. استخدم نصوصًا وصورًا من اختيارك، ونسّق البطاقات والألوان.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/reference-challenge-company-team.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">challenge</bdi> {
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">repeat(4, minmax(0, 1fr)</bdi>);
>   <bdi dir="ltr">grid-template-areas</bdi>:
>     "<bdi dir="ltr">one</bdi> <bdi dir="ltr">one</bdi> <bdi dir="ltr">two</bdi> <bdi dir="ltr">three</bdi>"
>     "<bdi dir="ltr">four</bdi> <bdi dir="ltr">five</bdi> <bdi dir="ltr">five</bdi> <bdi dir="ltr">three</bdi>"
>     "<bdi dir="ltr">four</bdi> <bdi dir="ltr">six</bdi> <bdi dir="ltr">six</bdi> <bdi dir="ltr">three</bdi>"
>     "<bdi dir="ltr">seven</bdi> <bdi dir="ltr">eight</bdi> <bdi dir="ltr">nine</bdi> <bdi dir="ltr">ten</bdi>";
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">10px</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">10px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> }
>
> .<bdi dir="ltr">card</bdi> { <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">22px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">white</bdi>; <bdi dir="ltr">border-bottom</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#f4511e</bdi>; }
> .<bdi dir="ltr">card</bdi>.<bdi dir="ltr">dark</bdi> { <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#000</bdi>; }
>
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">a</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">one</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">b</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">two</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">c</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">three</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">d</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">four</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">e</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">five</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">f</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">six</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">g</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">seven</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">h</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">eight</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">i</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">nine</bdi>; }
> .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">j</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">ten</bdi>; }
> ```
>
> ### الفكرة الأساسية
> تقسم `grid-template-areas` الصفحة إلى مساحات مسماة، ثم تربط كل بطاقة بمنطقتها. تتكرر بعض الأسماء لتوسيع البطاقة عبر أكثر من خلية.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.challenge`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.card`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.card.dark`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .a`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .b`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .c`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .d`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .e`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .f`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .g`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .h`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .i`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.challenge .j`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### طريقة الترتيب
> > ##### `display`
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل `Flex` أو `Grid`.
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> > ##### `grid-template-columns`
> > تحدد الأعمدة وعرض كل عمود في `Grid`.
> >
> > ##### `grid-template-areas`
> > ترسم خريطة الصفوف والأعمدة بأسماء مناطق.
> >
> > ##### `grid-area`
> > تربط العنصر بمنطقة مسماة.
> >
> > #### الأبعاد والمسافات
> > ##### `gap`
> > تحدد المسافة بين عناصر التخطيط.
> >
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > #### الحدود والظلال
> > ##### `border-bottom`
> > ترسم الحد السفلي.
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
> > .<bdi dir="ltr">challenge</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">repeat(4, minmax(0, 1fr)</bdi>);
> > ```
> > تحدد الأعمدة وعرض كل عمود في <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-areas</bdi>:
> > ```
> > ترسم خريطة الصفوف والأعمدة بأسماء مناطق.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">one</bdi> <bdi dir="ltr">one</bdi> <bdi dir="ltr">two</bdi> <bdi dir="ltr">three</bdi>"
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">four</bdi> <bdi dir="ltr">five</bdi> <bdi dir="ltr">five</bdi> <bdi dir="ltr">three</bdi>"
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">four</bdi> <bdi dir="ltr">six</bdi> <bdi dir="ltr">six</bdi> <bdi dir="ltr">three</bdi>"
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > "<bdi dir="ltr">seven</bdi> <bdi dir="ltr">eight</bdi> <bdi dir="ltr">nine</bdi> <bdi dir="ltr">ten</bdi>";
> > ```
> > يكمل قاعدة التنسيق السابقة.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">10px</bdi>;
> > ```
> > تحدد المسافة بين عناصر التخطيط.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">10px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">card</bdi> { <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">22px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">white</bdi>; <bdi dir="ltr">border-bottom</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#f4511e</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد المساحة الداخلية بين المحتوى والحد. تحدد خلفية العنصر، ومنها اللون أو التدرج. ترسم الحد السفلي. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">card</bdi>.<bdi dir="ltr">dark</bdi> { <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#000</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تحدد لون النص أو المحتوى. تحدد خلفية العنصر، ومنها اللون أو التدرج. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">a</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">one</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">b</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">two</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">c</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">three</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">d</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">four</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 19
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">e</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">five</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 20
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">f</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">six</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">g</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">seven</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">h</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">eight</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 23
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">i</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">nine</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 24
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">challenge</bdi> .<bdi dir="ltr">j</bdi> { <bdi dir="ltr">grid-area</bdi>: <bdi dir="ltr">ten</bdi>; }
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد. تربط العنصر بمنطقة مسماة. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/solution-task-06.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/06 - CSS Grid - Company Team Challenge.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/CSS Grid Assignments 57-64.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
