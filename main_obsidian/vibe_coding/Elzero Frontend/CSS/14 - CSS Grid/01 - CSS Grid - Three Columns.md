---
title: "CSS Grid - Three Columns"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - grid
  - تكليف
aliases:
  - تكليف CSS Grid 01
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi> - <bdi dir="ltr">Three</bdi> <bdi dir="ltr">Columns</bdi>

> [!question] السؤال
> استعمل بنية <bdi dir="ltr">HTML</bdi> السابقة دون تعديلها، وأنشئ التخطيط الأساسي باستخدام <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>. أظهر كلمات العناصر من <bdi dir="ltr">CSS</bdi>، ووسّط النص داخل كل عنصر. أضف تنسيقات الأب لتوضيح أبعاده، ووسّطه أفقيًا، وطابق الألوان المرجعية.
>
> صورة السؤال:
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/reference-task-01.png|700]]

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">grid1</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">min(1220px, calc(100% - 40px)</bdi>);
>   <bdi dir="ltr">height</bdi>: <bdi dir="ltr">620px</bdi>;
>   <bdi dir="ltr">margin-inline</bdi>: <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">30px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">repeat(3, 1fr)</bdi>;
>   <bdi dir="ltr">grid-template-rows</bdi>: <bdi dir="ltr">60px</bdi> <bdi dir="ltr">1fr</bdi>;
>   <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">30px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#ddd</bdi>;
>   <bdi dir="ltr">counter-reset</bdi>: <bdi dir="ltr">item</bdi>;
> }
>
> .<bdi dir="ltr">grid1</bdi> > <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#607d8b</bdi>;
>   <bdi dir="ltr">counter-increment</bdi>: <bdi dir="ltr">item</bdi>;
> }
>
> .<bdi dir="ltr">grid1</bdi> > <bdi dir="ltr">div</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: "<bdi dir="ltr">Element</bdi> " <bdi dir="ltr">counter(item)</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> تقسم `Grid` الحاوية إلى ثلاثة أعمدة متساوية باستخدام `repeat`(3, `1fr`). ويظهر العداد داخل كل خلية عن طريق ::`before` من دون تغيير `HTML`.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Grid</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.grid1`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid1 > div`
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.grid1 > div::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
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
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > #### العناصر الزائفة والعدادات
> > ##### `counter-reset`
> > تنشئ عدادًا عند بداية الحاوية.
> >
> > ##### `counter-increment`
> > تزيد قيمة العداد لكل عنصر يطابق القاعدة.
> >
> > ##### `content`
> > يعرض رقم العداد داخل العنصر الزائف، ويمكن ضم نص توضيحي له.
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
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">grid1</bdi> {
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
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">30px</bdi>;
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
> > <bdi dir="ltr">grid-template-columns</bdi>: <bdi dir="ltr">repeat(3, 1fr)</bdi>;
> > ```
> > تحدد الأعمدة وعرض كل عمود في <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">grid-template-rows</bdi>: <bdi dir="ltr">60px</bdi> <bdi dir="ltr">1fr</bdi>;
> > ```
> > تحدد الصفوف وارتفاع كل صف.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">gap</bdi>: <bdi dir="ltr">30px</bdi>;
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
> > <bdi dir="ltr">counter-reset</bdi>: <bdi dir="ltr">item</bdi>;
> > ```
> > تنشئ عدادًا عند بداية الحاوية.
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
> > .<bdi dir="ltr">grid1</bdi> > <bdi dir="ltr">div</bdi> {
> > ```
> > علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> > ```
> > تحدد طريقة ترتيب العنصر وأبنائه، مثل <bdi dir="ltr">Flex</bdi> أو <bdi dir="ltr">Grid</bdi>.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تختصر محاذاة عناصر الخلية أفقيًا وعموديًا.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 17
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#607d8b</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 18
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">counter-increment</bdi>: <bdi dir="ltr">item</bdi>;
> > ```
> > تزيد قيمة العداد لكل عنصر يطابق القاعدة.
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
> > .<bdi dir="ltr">grid1</bdi> > <bdi dir="ltr">div</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. علامة > تقصر المطابقة على الابن المباشر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 21
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: "<bdi dir="ltr">Element</bdi> " <bdi dir="ltr">counter(item)</bdi>;
> > ```
> > يعرض رقم العداد داخل العنصر الزائف، ويمكن ضم نص توضيحي له.
> >
> > #### السطر 22
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/assets/solution-task-01.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/01 - CSS Grid - Three Columns.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/14 - CSS Grid/CSS Grid Assignments 57-64.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS للدروس 57–64](https://elzero.org/css-assignments-lesson-from-57-to-64/)
