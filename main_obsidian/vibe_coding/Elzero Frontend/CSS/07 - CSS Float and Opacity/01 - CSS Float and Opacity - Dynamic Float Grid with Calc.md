---
title: "01 - CSS Float and Opacity - Dynamic Float Grid with Calc"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
  - تكليف
aliases:
  - تكليف Dynamic Float Grid with Calc
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Float</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Opacity</bdi> — <bdi dir="ltr">Dynamic</bdi> <bdi dir="ltr">Float</bdi> <bdi dir="ltr">Grid</bdi> <bdi dir="ltr">with</bdi> <bdi dir="ltr">calc()</bdi>

> [!question] السؤال
> **المطلوب:** اجعل عرض العنصر الأب <bdi dir="ltr">800px</bdi> بلا <bdi dir="ltr">padding</bdi>، والفواصل الأفقية والرأسية <bdi dir="ltr">15px</bdi>. اجعل عرض العناصر ديناميكيًا، ثم غيّر عرض الأب إلى <bdi dir="ltr">1000px</bdi> وتأكد أن التخطيط يبقى سليمًا.
>
> **<bdi dir="ltr">HTML</bdi> تمثيلي للمعاينة؛ عدد الأعمدة والعناصر ليس مثبتًا في نص صفحة التكليف**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">parent</bdi>">
>   <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">1</<bdi dir="ltr">div</bdi>><<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">2</<bdi dir="ltr">div</bdi>><<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">3</<bdi dir="ltr">div</bdi>><<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">4</<bdi dir="ltr">div</bdi>>
>   <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">5</<bdi dir="ltr">div</bdi>><<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">6</<bdi dir="ltr">div</bdi>><<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">7</<bdi dir="ltr">div</bdi>><<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">item</bdi>">8</<bdi dir="ltr">div</bdi>>
> </<bdi dir="ltr">div</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-27-29-1.png)
>
> [!info] حدود المصدر والمطابقة
> عدد الأعمدة والعناصر في المعاينة تقدير محفوظ من الحل السابق وليس موضحًا في النص الرسمي. صورة التكليف الأصلية محجوبة عند تنزيلها؛ لذلك لا أؤكد أن هذا الجزء يطابق شكلها.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">parent</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">800px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">--gap</bdi>: <bdi dir="ltr">15px</bdi>;
> }
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">parent</bdi>:<bdi dir="ltr">:after</bdi> {
>   <bdi dir="ltr">content</bdi>: "";
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">block</bdi>;
>   <bdi dir="ltr">clear</bdi>: <bdi dir="ltr">both</bdi>;
> }
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">item</bdi> {
>   <bdi dir="ltr">float</bdi>: <bdi dir="ltr">left</bdi>;
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">calc((100% - 3 * var(--gap)</bdi>) / 4);
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">100px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">var(--gap)</bdi> <bdi dir="ltr">var(--gap)</bdi> 0;
> }
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">item</bdi>:<bdi dir="ltr">nth-child(4n)</bdi> { <bdi dir="ltr">margin-right</bdi>: 0; }
> @<bdi dir="ltr">media</bdi> (<bdi dir="ltr">min-width</bdi>: <bdi dir="ltr">900px</bdi>) {
>   #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">parent</bdi> { <bdi dir="ltr">width</bdi>: <bdi dir="ltr">1000px</bdi>; }
> }
> ```
>
> **الفكرة الأساسية**
>
> تحسب <bdi dir="ltr">calc()</bdi> عرض الأعمدة اعتمادًا على عرض الأب، بعد طرح الفواصل الأفقية، فيظل التخطيط قابلًا للتغيير. يزيل <bdi dir="ltr">nth-child</bdi> الفاصل عن آخر عنصر في كل صف، ويجعل <bdi dir="ltr">clear</bdi> الأب يحتوي العناصر العائمة.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">custom</bdi> <bdi dir="ltr">property</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">calc()</bdi>
>
> ##### `--gap: 15px`
>
> يخزن قياس الفاصل في متغير <bdi dir="ltr">CSS</bdi> لإعادة استخدامه.
>
> ##### `calc((100% - 3 * var(--gap)) / 4)`
>
> يطرح ثلاثة فواصل من عرض الأب ثم يقسم المساحة على أربعة أعمدة.
>
> ##### `var(--gap)`
>
> يستدعي قيمة المتغير <bdi dir="ltr">--gap</bdi>.
>
> #### <bdi dir="ltr">Float</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">clearing</bdi>
>
> ##### `float: left`
>
> يرتب العنصر العائم إلى اليسار ويسمح بتجاور العناصر.
>
> ##### `clear: both`
>
> يمنع العنصر التالي من الالتفاف حول أي عناصر عائمة سابقة.
>
> ##### `::after`
>
> ينشئ عنصرًا زائفًا بعد محتوى الأب.
>
> #### <bdi dir="ltr">Grid-like</bdi> <bdi dir="ltr">placement</bdi>
>
> ##### `:nth-child(4n)`
>
> يختار كل عنصر رابع، أي نهاية كل صف من أربعة أعمدة.
>
> ##### `@media (min-width: 900px)`
>
> يطبق تغيير عرض الأب عندما يبلغ <bdi dir="ltr">viewport</bdi> هذا العرض.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">parent</bdi> {
> ```
>
> يفتح قاعدة العنصر الأب في نطاق التكليف.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">800px</bdi>;
> ```
>
> يضبط العرض الأولي للأب على <bdi dir="ltr">800px</bdi>.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
> ```
>
> يوسّط الأب أفقيًا.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">--gap</bdi>: <bdi dir="ltr">15px</bdi>;
> ```
>
> يحفظ الفاصل المطلوب في متغير <bdi dir="ltr">CSS</bdi>.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الأب.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">parent</bdi>:<bdi dir="ltr">:after</bdi> {
> ```
>
> يفتح عنصرًا زائفًا بعد محتويات الأب لتنظيف <bdi dir="ltr">float</bdi>.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">content</bdi>: "";
> ```
>
> يجعل العنصر الزائف بلا محتوى مرئي.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">block</bdi>;
> ```
>
> يجعله كتلة حتى يقبل <bdi dir="ltr">clear</bdi>.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">clear</bdi>: <bdi dir="ltr">both</bdi>;
> ```
>
> يمسح تأثير التعويم من الجهتين فيضم الأب ارتفاع العناصر.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة العنصر الزائف.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">item</bdi> {
> ```
>
> يفتح قاعدة العناصر الداخلية.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">float</bdi>: <bdi dir="ltr">left</bdi>;
> ```
>
> يعوم كل عنصر إلى اليسار لتكوين الصفوف.
>
> **13.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">box-sizing</bdi>: <bdi dir="ltr">border-box</bdi>;
> ```
>
> يجعل الحشو والحد داخل قياس عرض العنصر.
>
> **14.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">calc((100% - 3 * var(--gap)</bdi>) / 4);
> ```
>
> يحسب عرض العمود من عرض الأب والفواصل بدل تثبيته بالبكسل.
>
> **15.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">100px</bdi>;
> ```
>
> يحدد ارتفاعًا أدنى لظهور الصناديق بوضوح.
>
> **16.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">var(--gap)</bdi> <bdi dir="ltr">var(--gap)</bdi> 0;
> ```
>
> يضع فاصلًا يمين كل عنصر وأسفل الصف.
>
> **17.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة العنصر.
>
> **18.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">item</bdi>:<bdi dir="ltr">nth-child(4n)</bdi> { <bdi dir="ltr">margin-right</bdi>: 0; }
> ```
>
> يزيل الفاصل الأيمن من كل عنصر رابع في نهاية الصف.
>
> **19.**
>
> ```<bdi dir="ltr">css</bdi>
> @<bdi dir="ltr">media</bdi> (<bdi dir="ltr">min-width</bdi>: <bdi dir="ltr">900px</bdi>) {
> ```
>
> يفتح شرط العرض للشاشات التي تبلغ <bdi dir="ltr">900px</bdi> فأكثر.
>
> **20.**
>
> ```<bdi dir="ltr">css</bdi>
>   #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">parent</bdi> { <bdi dir="ltr">width</bdi>: <bdi dir="ltr">1000px</bdi>; }
> ```
>
> يغيّر عرض الأب إلى <bdi dir="ltr">1000px</bdi> عند تحقق الشرط.
>
> **21.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة <bdi dir="ltr">media</bdi>.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/07 - CSS Float and Opacity/assets/solution-page-task-01.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/07 - CSS Float and Opacity/01 - CSS Float and Opacity - Dynamic Float Grid with Calc.html|افتح صفحة الشرح المستقلة للتكليف 01]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-27-to-29/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-27-29-1.png)
