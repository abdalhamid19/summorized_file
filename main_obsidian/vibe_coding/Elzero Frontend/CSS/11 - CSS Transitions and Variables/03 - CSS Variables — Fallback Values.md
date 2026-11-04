---
title: "CSS Variables — Fallback Values"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-transitions-and-variables
  - تكليف
aliases:
  - CSS Variables — Fallback Values
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Variables</bdi> — <bdi dir="ltr">Fallback</bdi> <bdi dir="ltr">Values</bdi>

> [!question] السؤال
> نسّق العناصر الثلاثة باستخدام المتغيرين الموجودين في <bdi dir="ltr">:root</bdi>. لا تعدّل <bdi dir="ltr">:root</bdi>؛ وعند تعطيلها أظهر اللون الأخضر المزرق والحشو في الحالة الأولى، ثم <bdi dir="ltr">fallback</bdi> بالأحمر والأسود في الحالة الثانية.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/assets/reference-task-03.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
>
> [!info] حدود المصدر
> صفحة التكليف تعرض المعايير والصورة المرجعية، ولا تتضمن بنية <bdi dir="ltr">HTML</bdi> السابقة المشار إليها؛ لذلك يستخدم ملف المعاينة عناصر بديلة لإعادة بناء الشكل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```<bdi dir="ltr">css</bdi>
> <bdi dir="ltr">div</bdi> {
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">var(--mainColor, red)</bdi>;
>   <bdi dir="ltr">border</bdi>: <bdi dir="ltr">5px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">var(--mainColor, #000)</bdi>;
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">var(--mainPadding, 10px)</bdi>;
>   <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">20px</bdi> 0;
>   <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">30px</bdi>;
> }
> ```
>
> ### الفكرة الأساسية
> تقرأ قواعد التنسيق قيمتها من متغيرات `CSS`، وتوفر `var()` قيمة بديلة داخلها. إذا لم يوجد المتغير أو عُطّل، تظهر قيمة `fallback` مثل `red` أو `10px`.
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
> > #### الألوان والنص
> > ##### `color`
> > تحدد لون النص أو المحتوى.
> >
> > ##### `font-size`
> > تحدد حجم النص.
> >
> > #### الحدود والظلال
> > ##### `border`
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### الأبعاد والمسافات
> > ##### `padding`
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > ##### `margin`
> > تحدد المسافة خارج الحد؛ و`auto` توسّط العنصر أفقيًا عند توفر عرض محدد.
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
> > ##### `--` و `var()`
> > تخزن قيمة في متغير <bdi dir="ltr">CSS</bdi> ثم تعيد استخدامها أو تحدد قيمة بديلة.
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
> > <bdi dir="ltr">color</bdi>: <bdi dir="ltr">var(--mainColor, red)</bdi>;
> > ```
> > تحدد لون النص أو المحتوى.
> >
> > #### السطر 03
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">border</bdi>: <bdi dir="ltr">5px</bdi> <bdi dir="ltr">solid</bdi> <bdi dir="ltr">var(--mainColor, #000)</bdi>;
> > ```
> > ترسم حدًا وتحدد سمكه ونمطه ولونه.
> >
> > #### السطر 04
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">var(--mainPadding, 10px)</bdi>;
> > ```
> > تحدد المساحة الداخلية بين المحتوى والحد.
> >
> > #### السطر 05
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">margin</bdi>: <bdi dir="ltr">20px</bdi> 0;
> > ```
> > تحدد المسافة خارج الحد؛ وauto توسّط العنصر أفقيًا عند توفر عرض محدد.
> >
> > #### السطر 06
> >
> > ```<bdi dir="ltr">css</bdi>
> > <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">30px</bdi>;
> > ```
> > تحدد حجم النص.
> >
> > #### السطر 07
> >
> > ```<bdi dir="ltr">css</bdi>
> > }
> > ```
> > يغلق كتلة قواعد <bdi dir="ltr">CSS</bdi> التي بدأها المحدد السابق.
> >
> **صورة النتيجة المحفوظة**
>
> ![[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/assets/solution-task-03.png]]
>
> **صفحة الشرح المستقلة لهذا التكليف**
>
> [[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/03 - CSS Variables — Fallback Values.html|افتح صفحة الشرح المرئية]]
>
> **المعاينة المجمعة للتكليفات**
>
> [[vibe_coding/Elzero Frontend/CSS/11 - CSS Transitions and Variables/CSS Transitions and Variables Assignments 42-45.html|افتح معاينة المجموعة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-42-to-45/)
