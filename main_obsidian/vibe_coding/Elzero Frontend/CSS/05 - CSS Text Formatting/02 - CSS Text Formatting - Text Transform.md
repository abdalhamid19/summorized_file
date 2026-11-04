---
title: "02 - CSS Text Formatting - Text Transform"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Text Transform
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Formatting</bdi> — <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Transform</bdi>

> [!question] السؤال
> **المطلوب:** استخدم <bdi dir="ltr">HTML</bdi> التالي دون تعديله. نسّق النصوص بالترتيب الظاهر في المرجع: أحرف كبيرة بحجم أكبر، ثم <bdi dir="ltr">Title</bdi> <bdi dir="ltr">Case</bdi> بحجم متوسط، ثم أحرف صغيرة بحجم أصغر.
>
> **<bdi dir="ltr">HTML</bdi> الأصلي**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">one</bdi>"><bdi dir="ltr">elzero</bdi> <bdi dir="ltr">Web</bdi> <bdi dir="ltr">school</bdi></<bdi dir="ltr">p</bdi>>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">two</bdi>"><bdi dir="ltr">elzero</bdi> <bdi dir="ltr">Web</bdi> <bdi dir="ltr">school</bdi></<bdi dir="ltr">p</bdi>>
> <<bdi dir="ltr">p</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">three</bdi>"><bdi dir="ltr">elzero</bdi> <bdi dir="ltr">Web</bdi> <bdi dir="ltr">school</bdi></<bdi dir="ltr">p</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-2.png)
>
> [!info] حدود المصدر والمطابقة
> أحجام الخط المستخدمة في هذا الحل قيم تقريبية للتدرج البصري. الصورة الرسمية غير محفوظة محليًا والموقع حجب طلب التنزيل.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">one</bdi> { <bdi dir="ltr">text-transform</bdi>: <bdi dir="ltr">uppercase</bdi>; <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">48px</bdi>; }
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">two</bdi> { <bdi dir="ltr">text-transform</bdi>: <bdi dir="ltr">capitalize</bdi>; <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">36px</bdi>; }
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">three</bdi> { <bdi dir="ltr">text-transform</bdi>: <bdi dir="ltr">lowercase</bdi>; <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">24px</bdi>; }
> ```
>
> **الفكرة الأساسية**
>
> تغيّر <bdi dir="ltr">text-transform</bdi> شكل الأحرف المعروض من دون تعديل النص الأصلي في <bdi dir="ltr">HTML</bdi>. نستخدم <bdi dir="ltr">uppercase</bdi> ثم <bdi dir="ltr">capitalize</bdi> ثم <bdi dir="ltr">lowercase</bdi>، ونضبط الأحجام لتظهر النتائج كبيرة ومتوسطة وصغيرة.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Text</bdi> <bdi dir="ltr">formatting</bdi>
>
> ##### `text-transform: uppercase`
>
> يعرض الحروف الإنجليزية كبيرة.
>
> ##### `text-transform: capitalize`
>
> يجعل أول حرف من كل كلمة كبيرًا.
>
> ##### `text-transform: lowercase`
>
> يعرض الحروف الإنجليزية صغيرة.
>
> ##### `font-size`
>
> يحدد حجم النص الظاهر.
>
> #### محددات الأصناف
>
> ##### `.one / .two / .three`
>
> كل نقطة تسبق اسم صنف مختلفًا كي ننسق كل فقرة حسب ترتيبها.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">one</bdi> { <bdi dir="ltr">text-transform</bdi>: <bdi dir="ltr">uppercase</bdi>; <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">48px</bdi>; }
> ```
>
> يختار الفقرة الأولى، ويعرض أحرفها كبيرة بحجم <bdi dir="ltr">48px</bdi>.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">two</bdi> { <bdi dir="ltr">text-transform</bdi>: <bdi dir="ltr">capitalize</bdi>; <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">36px</bdi>; }
> ```
>
> يختار الفقرة الثانية، ويجعل بداية كل كلمة كبيرة مع حجم <bdi dir="ltr">36px</bdi>.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-02</bdi> .<bdi dir="ltr">three</bdi> { <bdi dir="ltr">text-transform</bdi>: <bdi dir="ltr">lowercase</bdi>; <bdi dir="ltr">font-size</bdi>: <bdi dir="ltr">24px</bdi>; }
> ```
>
> يختار الفقرة الثالثة، ويعرض أحرفها صغيرة بحجم <bdi dir="ltr">24px</bdi>.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/assets/solution-page-task-02.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/02 - CSS Text Formatting - Text Transform.html|افتح صفحة الشرح المستقلة للتكليف 02]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-17-to-21/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-2.png)
