---
title: "CSS Pseudo Elements — Comment Pointer"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
  - تكليف
aliases:
  - CSS Pseudo Elements — Comment Pointer
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Pseudo</bdi> <bdi dir="ltr">Elements</bdi> — <bdi dir="ltr">Comment</bdi> <bdi dir="ltr">Pointer</bdi>

> [!question] السؤال
> نسّق ثلاثة تعليقات، وأضف لسانًا مثلثًا على الحافة اليسرى لكل تعليق باستخدام <bdi dir="ltr">pseudo-element</bdi>.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">comment</bdi> {
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
>   <bdi dir="ltr">border-left</bdi>: <bdi dir="ltr">5px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#e91e63</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi> <bdi dir="ltr">24px</bdi>;
> }
>
> .<bdi dir="ltr">comment</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: "";
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
>   <bdi dir="ltr">left</bdi>: -<bdi dir="ltr">30px</bdi>;
>   <bdi dir="ltr">top</bdi>: <bdi dir="ltr">50%</bdi>;
>   <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateY(-50%)</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">15px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">transparent</bdi>;
>   <bdi dir="ltr">border-right-color</bdi>: <bdi dir="ltr">#e91e63</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> نرسم لسان التعليق من حدود ::`before` الشفافة. تلوين حد واحد فقط يجعل الجزء الملون مثلثًا، ثم تنقله `transform` إلى منتصف ارتفاع التعليق.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">Pseudo-classes</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Pseudo-elements</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.comment`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.comment::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### التموضع وترتيب الطبقات
> > ##### `position`
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > ##### `left`
> > تحدد المسافة من الحافة اليسرى.
> >
> > ##### `top`
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### الحدود والظلال
> > ##### `border-left`
> > ترسم الحد الأيسر.
> >
> > ##### `border`
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### الألوان والنص
> > ##### `background`
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### الأبعاد والمسافات
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### العناصر الزائفة والعدادات
> > ##### `content`
> > ينشئ محتوى فارغًا حتى يمكن رسم الشكل الزخرفي بالحدود.
> >
> > #### الحركة والتحويل
> > ##### `transform`
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > #### خصائص مساعدة
> > ##### `border-right-color`
> > تضبط هذه الخاصية القيمة #`e91e63`.
> >
> > #### علامات صياغة <bdi dir="ltr">CSS</bdi>
> >
> > ##### `:`
> > تفصل اسم الخاصية عن قيمتها.
> >
> > ##### `;`
> > تنهي تصريح <bdi dir="ltr">CSS</bdi>.
> >
> > ##### `::`
> > تشير إلى عنصر زائف تنشئه <bdi dir="ltr">CSS</bdi>.
> >
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">comment</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-left</bdi>: <bdi dir="ltr">5px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#e91e63</bdi>;
> > ```
> > ترسم الحد الأيسر.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#eee</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi> <bdi dir="ltr">24px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
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
> > .<bdi dir="ltr">comment</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: "";
> > ```
> > ينشئ محتوى فارغًا حتى يمكن رسم الشكل الزخرفي بالحدود.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>;
> > ```
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">left</bdi>: -<bdi dir="ltr">30px</bdi>;
> > ```
> > تحدد المسافة من الحافة اليسرى.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">top</bdi>: <bdi dir="ltr">50%</bdi>;
> > ```
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > #### السطر 12
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateY(-50%)</bdi>;
> > ```
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > #### السطر 13
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border</bdi>: <bdi dir="ltr">15px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">transparent</bdi>;
> > ```
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border-right-color</bdi>: <bdi dir="ltr">#e91e63</bdi>;
> > ```
> > تضبط هذه الخاصية القيمة <bdi dir="ltr">#e91e63</bdi>.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/assets/solution-task-03.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/03 - CSS Pseudo Elements — Comment Pointer.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/09 - CSS Pseudo Classes and Pseudo Elements/CSS Pseudo Classes Assignments 34-37.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-34-to-37/)
