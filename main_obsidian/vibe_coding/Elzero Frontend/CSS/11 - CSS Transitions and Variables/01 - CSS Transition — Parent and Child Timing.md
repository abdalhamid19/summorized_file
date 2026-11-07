---
title: "CSS Transition — Parent and Child Timing"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-transitions-and-variables
  - تكليف
aliases:
  - CSS Transition — Parent and Child Timing
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Transition</bdi> — <bdi dir="ltr">Parent</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Child</bdi> <bdi dir="ltr">Timing</bdi>

> [!question] السؤال
> عند مرور المؤشر فوق الأب، تحركه للأعلى خلال نصف ثانية، ثم تحرك الابن للأسفل بعد تأخير نصف ثانية، مع ألوان المرجع.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/assets/reference-task-01.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> .<bdi dir="ltr">parent</bdi> {
>   <bdi dir="ltr">transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi>;
>   -<bdi dir="ltr">webkit-transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi>;
> }
>
> .<bdi dir="ltr">parent</bdi>:<bdi dir="ltr">hover</bdi> {
>   <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateY(-40px)</bdi>;
>   -<bdi dir="ltr">webkit-transform</bdi>: <bdi dir="ltr">translateY(-40px)</bdi>;
> }
>
> .<bdi dir="ltr">child</bdi> {
>   <bdi dir="ltr">transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi> <bdi dir="ltr">0.5s</bdi>;
>   -<bdi dir="ltr">webkit-transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi> <bdi dir="ltr">0.5s</bdi>;
> }
>
> .<bdi dir="ltr">parent</bdi>:<bdi dir="ltr">hover</bdi> .<bdi dir="ltr">child</bdi> {
>   <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateY(40px)</bdi>;
>   -<bdi dir="ltr">webkit-transform</bdi>: <bdi dir="ltr">translateY(40px)</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> تحدد `transition` مدة الحركة، وتبدأ حركة الأب عند `hover`. يحصل الابن على المدة نفسها مع تأخير نصف ثانية، فيتحرك بعد الأب.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Transitions</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Variables</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `.parent`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.parent:hover`
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.child`
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > ##### `.parent:hover .child`
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### الحركة والتحويل
> > ##### `transition`
> > تحدد مدة الحركة وطريقة تغير القيمة، وقد تتضمن التأخير.
> >
> > ##### `-webkit-transition`
> > صيغة ببادئة `WebKit` لدعم أقدم لبعض المتصفحات.
> >
> > ##### `transform`
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > ##### `-webkit-transform`
> > صيغة ببادئة `WebKit` لدعم أقدم لبعض المتصفحات.
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
> > .<bdi dir="ltr">parent</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi>;
> > ```
> > تحدد مدة الحركة وطريقة تغير القيمة، وقد تتضمن التأخير.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم لبعض المتصفحات.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">parent</bdi>:<bdi dir="ltr">hover</bdi> {
> > ```
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateY(-40px)</bdi>;
> > ```
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-transform</bdi>: <bdi dir="ltr">translateY(-40px)</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم لبعض المتصفحات.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > .<bdi dir="ltr">child</bdi> {
> > ```
> > يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi> <bdi dir="ltr">0.5s</bdi>;
> > ```
> > تحدد مدة الحركة وطريقة تغير القيمة، وقد تتضمن التأخير.
> >
> > #### السطر 11
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-transition</bdi>: <bdi dir="ltr">transform</bdi> <bdi dir="ltr">0.5s</bdi> <bdi dir="ltr">ease</bdi> <bdi dir="ltr">0.5s</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم لبعض المتصفحات.
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
> > .<bdi dir="ltr">parent</bdi>:<bdi dir="ltr">hover</bdi> .<bdi dir="ltr">child</bdi> {
> > ```
> > يطبق القاعدة عند مرور المؤشر فوق العنصر. يستهدف العناصر التي تحمل اسم الفئة في المحدد.
> >
> > #### السطر 14
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">transform</bdi>: <bdi dir="ltr">translateY(40px)</bdi>;
> > ```
> > تحرك العنصر دون تعديل تدفق الصفحة.
> >
> > #### السطر 15
> >
> > ```<bdi dir="ltr">css</bdi>
> > -<bdi dir="ltr">webkit-transform</bdi>: <bdi dir="ltr">translateY(40px)</bdi>;
> > ```
> > صيغة ببادئة <bdi dir="ltr">WebKit</bdi> لدعم أقدم لبعض المتصفحات.
> >
> > #### السطر 16
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/assets/solution-task-01.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/01 - CSS Transition — Parent and Child Timing.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/CSS Transitions and Variables Assignments 42-45.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
