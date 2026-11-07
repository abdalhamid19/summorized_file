---
title: "03 - CSS Text Formatting - Text Overflow Ellipsis"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Text Overflow Ellipsis
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Formatting</bdi> — <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Overflow</bdi> <bdi dir="ltr">Ellipsis</bdi>

> [!question] السؤال
> **المطلوب:** استخدم <bdi dir="ltr">HTML</bdi> الأصلي دون تعديله، واجعل العرض <bdi dir="ltr">400px</bdi>. أظهر حالة النص الطبيعي وحالة النص القصير وحالة النص المقطوع عند نهاية السطر بنقاط يضيفها المتصفح؛ لا تكتب النقاط يدويًا.
>
> **<bdi dir="ltr">HTML</bdi> الأصلي مع حالات معاينة إضافية**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">div</bdi>>
>   <bdi dir="ltr">Lorem</bdi> <bdi dir="ltr">ipsum</bdi> <bdi dir="ltr">dolor</bdi> <bdi dir="ltr">sit</bdi> <bdi dir="ltr">amet</bdi> <bdi dir="ltr">consectetur</bdi>, <bdi dir="ltr">adipisicing</bdi> <bdi dir="ltr">elit</bdi>.
>   <bdi dir="ltr">Ea</bdi> <bdi dir="ltr">itaque</bdi> <bdi dir="ltr">fugit</bdi> <bdi dir="ltr">vitae</bdi> <bdi dir="ltr">incidunt</bdi> <bdi dir="ltr">quis</bdi> <bdi dir="ltr">dolores</bdi>? <bdi dir="ltr">Id</bdi> <bdi dir="ltr">alias</bdi>
>   <bdi dir="ltr">eveniet</bdi> <bdi dir="ltr">sequi</bdi> <bdi dir="ltr">perspiciatis</bdi> <bdi dir="ltr">iusto</bdi> <bdi dir="ltr">impedit</bdi>,
>   <bdi dir="ltr">accusamus</bdi> <bdi dir="ltr">maxime</bdi> <bdi dir="ltr">reprehenderit</bdi> <bdi dir="ltr">blanditiis</bdi> <bdi dir="ltr">adipisci</bdi> <bdi dir="ltr">sapiente</bdi> <bdi dir="ltr">hic</bdi> <bdi dir="ltr">velit</bdi>.
> </<bdi dir="ltr">div</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-3.png)
>
> [!info] حدود المصدر والمطابقة
> تعرض المعاينة ثلاث حالات لتوضيح المطلوب. صورة المرجع غير محفوظة محليًا؛ الألوان والحدود في الصورة هنا هي من الحل المحلي وليست تأكيدًا للمطابقة الرسمية.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">normal</bdi>,
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">short</bdi>,
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">ellipsis</bdi> {
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">12px</bdi> <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">2px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#009688</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>;
> }
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">ellipsis</bdi> {
>   <bdi dir="ltr">overflow</bdi>: <bdi dir="ltr">hidden</bdi>;
>   <bdi dir="ltr">white-space</bdi>: <bdi dir="ltr">nowrap</bdi>;
>   <bdi dir="ltr">text-overflow</bdi>: <bdi dir="ltr">ellipsis</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> لكي تظهر علامة الحذف عند نهاية سطر واحد، نحتاج عرضًا محدودًا، ومنع التفاف النص، وإخفاء الجزء الزائد، ثم نطلب من المتصفح إظهار <bdi dir="ltr">ellipsis</bdi>. الثلاث نقاط ليست نصًا مكتوبًا في <bdi dir="ltr">HTML</bdi>.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Text</bdi> <bdi dir="ltr">overflow</bdi>
>
> ##### `overflow: hidden`
>
> يقص المحتوى الذي يخرج من حدود الصندوق.
>
> ##### `white-space: nowrap`
>
> يمنع النص من الانتقال إلى سطر جديد.
>
> ##### `text-overflow: ellipsis`
>
> يطلب من المتصفح إظهار علامة الحذف عند القص.
>
> #### تجميع المحددات
>
> ##### `الفاصلة ,`
>
> تجمع المحددات الثلاثة كي تشترك في قياسات الصندوق.
>
> ##### `.ellipsis`
>
> يضيف سلوك القص للحالة الثالثة وحدها.
>
> #### الأبعاد
>
> ##### `width: 400px`
>
> يثبت عرض كل صندوق على المقاس الذي طلبه التكليف.
>
> ##### `box-sizing: border-box`
>
> يجعل العرض شاملًا الحشو والحد.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">normal</bdi>,
> ```
>
> يبدأ مجموعة المحددات المشتركة بين الحالات الثلاث.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">short</bdi>,
> ```
>
> يضيف محدد الحالة القصيرة إلى المجموعة.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">ellipsis</bdi> {
> ```
>
> يضيف محدد الحالة ذات علامة الحذف ويفتح القاعدة المشتركة.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
> ```
>
> يجعل قياس العرض يشمل الحشو والحد.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
> ```
>
> يثبت عرض الصندوق عند <bdi dir="ltr">400px</bdi> كما يطلب السؤال.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">12px</bdi> <bdi dir="ltr">auto</bdi>;
> ```
>
> يوسّط الصندوق أفقيًا ويضيف مسافة رأسية.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">12px</bdi>;
> ```
>
> يضيف حشوًا داخليًا متساويًا حول المحتوى.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">2px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#009688</bdi>;
> ```
>
> يرسم حدًا بلون فيروزي حول الصندوق.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>;
> ```
>
> يضبط لون النص إلى لون داكن.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة التنسيق المشتركة.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-03</bdi> .<bdi dir="ltr">ellipsis</bdi> {
> ```
>
> يفتح قاعدة الحالة التي يظهر فيها القطع.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">overflow</bdi>: <bdi dir="ltr">hidden</bdi>;
> ```
>
> يخفي الجزء الذي يتجاوز الصندوق.
>
> **13.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">white-space</bdi>: <bdi dir="ltr">nowrap</bdi>;
> ```
>
> يبقي النص في سطر واحد.
>
> **14.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">text-overflow</bdi>: <bdi dir="ltr">ellipsis</bdi>;
> ```
>
> يطلب من المتصفح وضع علامة الحذف تلقائيًا.
>
> **15.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة حالة القطع.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/assets/solution-page-task-03.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/03 - CSS Text Formatting - Text Overflow Ellipsis.html|افتح صفحة الشرح المستقلة للتكليف 03]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-17-to-21/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-3.png)
