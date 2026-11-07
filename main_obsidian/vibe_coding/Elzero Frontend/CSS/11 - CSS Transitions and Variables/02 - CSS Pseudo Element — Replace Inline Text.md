---
title: "CSS Pseudo Element — Replace Inline Text"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-transitions-and-variables
  - تكليف
aliases:
  - CSS Pseudo Element — Replace Inline Text
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Pseudo</bdi> <bdi dir="ltr">Element</bdi> — <bdi dir="ltr">Replace</bdi> <bdi dir="ltr">Inline</bdi> <bdi dir="ltr">Text</bdi>

> [!question] السؤال
> حافظ على بنية العنصر ذات التنسيق المضمن. أخفِ النص <bdi dir="ltr">Hello</bdi> <bdi dir="ltr">Div</bdi> وأظهر <bdi dir="ltr">Elzero</bdi> بخط <bdi dir="ltr">20px</bdi> داخل عنصر بعرض <bdi dir="ltr">400px</bdi> في وسط الصفحة.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/assets/reference-task-02.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
>   <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
>   <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">center</bdi>;
>   <bdi dir="ltr">font-size</bdi>: 0 !<bdi dir="ltr">important</bdi>;
> }
>
> <bdi dir="ltr">div</bdi>:<bdi dir="ltr">:before</bdi> {
>   <bdi dir="ltr">content</bdi>: "<bdi dir="ltr">Elzero</bdi>";
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">20px</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> يخفي حجم الخط الصفري النص المضمّن في نموذج المعاينة، ثم يعرض ::`before` كلمة بديلة بحجم `20px` من دون تعديل `HTML`.
>
> > [!<bdi dir="ltr">info</bdi>]- معاني الرموز المستخدمة في الحل — اضغط للفتح
> >
> > ### معاني الرموز المستخدمة في الحل
> >
> > #### <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Transitions</bdi> <bdi dir="ltr">and</bdi> <bdi dir="ltr">Variables</bdi>
> >
> > #### المحددات في <bdi dir="ltr">CSS</bdi>
> > ##### `div`
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > ##### `div::before`
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص.
> >
> > #### الأبعاد والمسافات
> > ##### `width`
> > تحدد عرض العنصر.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### الألوان والنص
> > ##### `text-align`
> > تحاذي النص داخل العنصر.
> >
> > ##### `font-size`
> > تحدد حجم النص.
> >
> > #### العناصر الزائفة والعدادات
> > ##### `content`
> > يضيف النص المحدد إلى العنصر الزائف من دون إنشاء عنصر `HTML` جديد.
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
> > <bdi dir="ltr">div</bdi> {
> > ```
> > يحدد العناصر التي ستأخذ قواعد التنسيق التالية.
> >
> > #### السطر 02
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">width</bdi>: <bdi dir="ltr">400px</bdi>;
> > ```
> > تحدد عرض العنصر.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: 0 <bdi dir="ltr">auto</bdi>;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">text-align</bdi>: <bdi dir="ltr">center</bdi>;
> > ```
> > تحاذي النص داخل العنصر.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-size</bdi>: 0 !<bdi dir="ltr">important</bdi>;
> > ```
> > تحدد حجم النص.
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
> > <bdi dir="ltr">div</bdi>:<bdi dir="ltr">:before</bdi> {
> > ```
> > يختار عنصرًا زائفًا ينشأ قبل المحتوى لإضافة علامة أو نص.
> >
> > #### السطر 08
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">content</bdi>: "<bdi dir="ltr">Elzero</bdi>";
> > ```
> > يضيف النص المحدد إلى العنصر الزائف من دون إنشاء عنصر <bdi dir="ltr">HTML</bdi> جديد.
> >
> > #### السطر 09
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">20px</bdi>;
> > ```
> > تحدد حجم النص.
> >
> > #### السطر 10
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/assets/solution-task-02.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/02 - CSS Pseudo Element — Replace Inline Text.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/CSS Transitions and Variables Assignments 42-45.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
