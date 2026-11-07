---
title: "04 - CSS Position, List, and Table - Table-only Layout"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف Table-only Layout
---

# 04 - <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Position</bdi>, <bdi dir="ltr">List</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Table</bdi> - <bdi dir="ltr">Table-only</bdi> <bdi dir="ltr">Layout</bdi>

> [!question] السؤال
> أنشئ الشكل باستخدام الجدول فقط، من دون إضافة عناصر أخرى. يجب أن يكون عرض الجدول <bdi dir="ltr">700px</bdi> وفي منتصف الصفحة.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-30-to-33/>)
>
> [!info] حدود المصدر والمطابقة
> تحدد صفحة التكليف جدولًا فقط بعرض `700px` وتوسيطه. تعذّر علي قراءة تفاصيل الصورة المرجعية، لذلك الصفوف والألوان في المعاينة أمثلة توضيحية، ولا أؤكد مطابقتها للصورة.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">table</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">700px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">24px</bdi> <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">border-collapse</bdi>: <bdi dir="ltr">collapse</bdi>;
>   <bdi dir="ltr">font</bdi>: <bdi dir="ltr">16px</bdi> <bdi dir="ltr">Arial</bdi>, <bdi dir="ltr">sans-serif</bdi>;
> }
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">caption</bdi> { <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#222</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>; <bdi dir="ltr">font-weight</bdi>: 700; }
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">th</bdi>, #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">td</bdi> { <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>; <bdi dir="ltr">border</bdi>: <bdi dir="ltr">2px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#444</bdi>; <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">left</bdi>; }
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">th</bdi> { <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#2196f3</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>; }
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">td</bdi> { <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>; }
> ```
>
> ### الفكرة الأساسية
> نحتفظ بمحتوى الجدول وننسّق خلاياه. توحّد `border-collapse` الحدود المتجاورة، ثم تميّز الخلفية العنوان عن بيانات الصفوف.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Positioning</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `#task-04 table`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر.
> >
> > ##### `#task-04 caption`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر.
> >
> > ##### `#task-04 th, #task-04 td`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر.
> >
> > ##### `#task-04 th`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر.
> >
> > ##### `#task-04 td`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر.
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
> > #### الحدود والظلال
> > ##### `border-collapse`
> > تدمج حدود خلايا الجدول المتجاورة.
> >
> > ##### `border`
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### الألوان والنص
> > ##### `font`
> > تختصر خصائص الخط.
> >
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > ##### `font-weight`
> > تحدد سماكة الحروف.
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
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">table</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">700px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">24px</bdi> <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-collapse</bdi>: <bdi dir="ltr">collapse</bdi>;
> > ```
> > تدمج حدود خلايا الجدول المتجاورة.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font</bdi>: <bdi dir="ltr">16px</bdi> <bdi dir="ltr">Arial</bdi>, <bdi dir="ltr">sans-serif</bdi>;
> > ```
> > تختصر خصائص الخط.
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
> > #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">caption</bdi> { <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#222</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>; <bdi dir="ltr">font-weight</bdi>: 700; }
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. تحدد المساحة الداخلية بين المحتوى والحد. تحدد خلفية العنصر، ومنها اللون أو التدرج. تحدد لون النص أو المحتوى. تحدد سماكة الحروف. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">th</bdi>, #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">td</bdi> { <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>; <bdi dir="ltr">border</bdi>: <bdi dir="ltr">2px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#444</bdi>; <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">left</bdi>; }
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. تحدد المساحة الداخلية بين المحتوى والحد. ترسم حدًا وتحدد سمكه ونمطه ولونه. تحاذي النص داخل العنصر. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">th</bdi> { <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#2196f3</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>; }
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. تحدد خلفية العنصر، ومنها اللون أو التدرج. تحدد لون النص أو المحتوى. يغلق القاعدة في نهاية السطر.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">td</bdi> { <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>; }
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. تحدد خلفية العنصر، ومنها اللون أو التدرج. تحدد لون النص أو المحتوى. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/assets/solution-overview.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/04 - CSS Position, List, and Table - Table-only Layout.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-30-to-33/)
