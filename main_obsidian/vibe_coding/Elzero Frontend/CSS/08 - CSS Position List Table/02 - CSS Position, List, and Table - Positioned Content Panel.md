---
title: "02 - CSS Position, List, and Table - Positioned Content Panel"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
  - تكليف
aliases:
  - تكليف Positioned Content Panel
---

# 02 - <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Position</bdi>, <bdi dir="ltr">List</bdi>, <bdi dir="ltr">and</bdi> <bdi dir="ltr">Table</bdi> - <bdi dir="ltr">Positioned</bdi> <bdi dir="ltr">Content</bdi> <bdi dir="ltr">Panel</bdi>

> [!question] السؤال
> اجعل الحاوية الرئيسية بعرض <bdi dir="ltr">400px</bdi>، ووسّطها أفقيًا. طابق ألوان الخلفية والحدود مع الصورة.
>
> [صفحة التكليف الرسمية](<https://elzero.org/css-assignments-lesson-from-30-to-33/>)
>
> [!info] حدود المصدر والمطابقة
> تطلب صفحة التكليف حاوية بعرض `400px` وتوسيطها ومطابقة ألوان الصورة، لكنها تشير إلى بنية <bdi dir="ltr">HTML</bdi> سابقة لا تظهر في النص المتاح، وتعذّر علي قراءة ألوان الصورة. لذلك <bdi dir="ltr">HTML</bdi> والألوان في المعاينة أمثلة توضيحية، ويجب تطبيق قواعد التموضع على بنية المصدر الأصلية.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">panel</bdi> {
>   <bdi dir="ltr">position</bdi>: <bdi dir="ltr">relative</bdi>;
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">180px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">30px</bdi> <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">28px</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#e91e63</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f5f5f5</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>;
> }
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">badge</bdi> { <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>; <bdi dir="ltr">top</bdi>: -<bdi dir="ltr">14px</bdi>; <bdi dir="ltr">right</bdi>: <bdi dir="ltr">18px</bdi>; <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">4px</bdi> <bdi dir="ltr">10px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#2196f3</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>; }
> ```
>
> ### الفكرة الأساسية
> نجعل اللوحة نفسها مرجعًا للشارة: اللوحة `relative`، والشارة `absolute`. بهذه الطريقة تتحرك الشارة بالنسبة إلى اللوحة، بينما يوسّط الهامش التلقائي اللوحة ذات العرض الثابت.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Positioning</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `#task-02 .panel`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `#task-02 .badge`
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### التموضع وترتيب الطبقات
> > ##### `position`
> > تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله.
> >
> > ##### `top`
> > تحدد المسافة من أعلى مرجع التموضع.
> >
> > ##### `right`
> > تحدد المسافة من الحافة اليمنى.
> >
> > #### الأبعاد والمسافات
> > ##### `box-sizing`
> > تحدد طريقة حساب العرض والارتفاع بالنسبة إلى الحشو والحدود.
> >
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `min-height`
> > تمنع الارتفاع من النزول عن القيمة المحددة.
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
> > [!<bdi dir="ltr">note</bdi>]- شرح الحل سطرًا بسطر — اضغط للفتح
> >
> > #### السطر 01
> >
> > ```<bdi dir="ltr">css</bdi>
> > #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">panel</bdi> {
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
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
> > <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
> > ```
> > تحدد طريقة حساب العرض والارتفاع بالنسبة إلى الحشو والحدود.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">180px</bdi>;
> > ```
> > تمنع الارتفاع من النزول عن القيمة المحددة.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">30px</bdi> <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">28px</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#e91e63</bdi>;
> > ```
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#f5f5f5</bdi>;
> > ```
> > تحدد خلفية العنصر، ومنها اللون أو التدرج.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
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
> > #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">badge</bdi> { <bdi dir="ltr">position</bdi>: <bdi dir="ltr">absolute</bdi>; <bdi dir="ltr">top</bdi>: -<bdi dir="ltr">14px</bdi>; <bdi dir="ltr">right</bdi>: <bdi dir="ltr">18px</bdi>; <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">4px</bdi> <bdi dir="ltr">10px</bdi>; <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#2196f3</bdi>; <bdi dir="ltr">color</bdi>: <bdi dir="ltr">white</bdi>; }
> > ```
> > يستهدف المعرّف ويحصر القاعدة في ذلك العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد. تختار طريقة التموضع؛ تستخدم هنا لإخراج العنصر من التدفق أو جعله مرجعًا للعناصر داخله. تحدد المسافة من أعلى مرجع التموضع. تحدد المسافة من الحافة اليمنى. تحدد المساحة الداخلية بين المحتوى والحد. تحدد خلفية العنصر، ومنها اللون أو التدرج. تحدد لون النص أو المحتوى. يغلق القاعدة في نهاية السطر.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/assets/solution-overview.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/02 - CSS Position, List, and Table - Positioned Content Panel.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/08 - CSS Position List Table/CSS Position, List, and Table Assignments 30–33 Demo.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية للدروس المذكورة](https://elzero.org/css-assignments-lesson-from-30-to-33/)
