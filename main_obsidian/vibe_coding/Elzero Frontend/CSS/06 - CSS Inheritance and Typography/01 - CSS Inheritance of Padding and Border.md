---
title: "CSS Inheritance of Padding and Border"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - inheritance
  - تكليف
aliases:
  - تكليف وراثة الحشو والحدود في CSS
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Inheritance</bdi> — <bdi dir="ltr">Padding</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Border</bdi>

> [!question] السؤال
> **المطلوب:** استخدم البنية السابقة دون تعديلها. اجعل أي تغيير في <bdi dir="ltr">padding</bdi> أو <bdi dir="ltr">border</bdi> للعنصر الأب <bdi dir="ltr">div</bdi> ينتقل إلى العنصر الابن <bdi dir="ltr">p</bdi> من دون إعادة ضبط الابن يدويًا.
>
> **<bdi dir="ltr">HTML</bdi> تمثيلي للشرح؛ صفحة التكليف تشير إلى بنية سابقة ولا تعرضها كنص**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">div</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">parent</bdi>">
>   <<bdi dir="ltr">p</bdi>>الابن يرث <bdi dir="ltr">padding</bdi> وborder من الأب</<bdi dir="ltr">p</bdi>>
> </<bdi dir="ltr">div</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-22-26-1.png)
>
> [!info] حدود المصدر والمطابقة
> لم تعرض صفحة التكليف البنية السابقة كاملة، لذلك وُسِمت بنية <bdi dir="ltr">HTML</bdi> في الصفحة بأنها تمثيلية. صورة الحل المحلية توضح سلوك الوراثة، أما صورة السؤال الأصلية فتعذّر حفظها من الموقع.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">parent</bdi> {
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#147d73</bdi>;
> }
> .<bdi dir="ltr">parent</bdi> > <bdi dir="ltr">p</bdi> {
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">inherit</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">inherit</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> خاصيتا <bdi dir="ltr">padding</bdi> وborder لا تُورثان تلقائيًا في <bdi dir="ltr">CSS</bdi>. نطلب الوراثة صراحةً بقيمة <bdi dir="ltr">inherit</bdi> على <bdi dir="ltr">p</bdi>، فيأخذ القيم المحسوبة من <bdi dir="ltr">div</bdi> الأب عند تغييرها.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Inheritance</bdi>
>
> ##### `inherit`
>
> يجعل الخاصية تأخذ القيمة المحسوبة من العنصر الأب.
>
> ##### `padding`
>
> مساحة داخلية بين المحتوى وحد العنصر.
>
> ##### `border`
>
> الحد المرئي حول العنصر.
>
> #### علاقة <bdi dir="ltr">HTML</bdi> وCSS
>
> ##### `.parent`
>
> يختار العنصر الأب الذي يحمل الصنف <bdi dir="ltr">parent</bdi>.
>
> ##### `>`
>
> يشترط أن يكون <bdi dir="ltr">p</bdi> ابنًا مباشرًا للأب.
>
> ##### `p`
>
> محدد نوع يختار الفقرة.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">parent</bdi> {
> ```
>
> يفتح قاعدة تنسيق العنصر الأب.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">20px</bdi>;
> ```
>
> يضبط الحشو الأبوي الذي ستأخذه الفقرة.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">3px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">#147d73</bdi>;
> ```
>
> يرسم حد الأب بلون فيروزي وسمك <bdi dir="ltr">3px</bdi>.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الأب.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">parent</bdi> > <bdi dir="ltr">p</bdi> {
> ```
>
> يختار فقرة <bdi dir="ltr">p</bdi> التي تقع مباشرة داخل العنصر الأب.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">inherit</bdi>;
> ```
>
> يطلب من الحشو أن يرث القيمة المحسوبة من الأب.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">inherit</bdi>;
> ```
>
> يطلب من الحد أن يرث قيمة الأب.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الابن.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/06 - CSS Inheritance and Typography/assets/solution-page-task-01.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/06 - CSS Inheritance and Typography/01 - CSS Inheritance of Padding and Border.html|افتح صفحة الشرح المستقلة للتكليف 01]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-22-to-26/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-22-26-1.png)
