---
title: "04 - CSS Text Formatting - Centered Styled Link"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Centered Styled Link
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Formatting</bdi> — <bdi dir="ltr">Centered</bdi> <bdi dir="ltr">Styled</bdi> <bdi dir="ltr">Link</bdi>

> [!question] السؤال
> **المطلوب:** استخدم الرابط الأصلي دون تعديل <bdi dir="ltr">HTML</bdi>. ضعه في منتصف الصفحة تمامًا ونسّق ألوانه وشكله كما في الصورة المرجعية.
>
> **<bdi dir="ltr">HTML</bdi> الأصلي**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">a</bdi> <bdi dir="ltr">href</bdi>="<bdi dir="ltr">https</bdi>://<bdi dir="ltr">elzero</bdi>.<bdi dir="ltr">org</bdi>"><bdi dir="ltr">elzero</bdi></<bdi dir="ltr">a</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-4.png)
>
> [!info] حدود المصدر والمطابقة
> ألوان المعاينة وأبعاد الزر هي القيم الموجودة في الحل السابق. صورة المصدر الرسمية غير محفوظة محليًا ولا أؤكد تطابق هذه القيم معها.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-04</bdi> {
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">260px</bdi>;
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> }
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">a</bdi> {
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">18px</bdi> <bdi dir="ltr">30px</bdi>;
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#009688</bdi>;
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
>   <bdi dir="ltr">font</bdi>: 700 <bdi dir="ltr">24px</bdi> <bdi dir="ltr">Arial</bdi>, <bdi dir="ltr">sans-serif</bdi>;
>   <bdi dir="ltr">text-decoration</bdi>: <bdi dir="ltr">none</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> نحوّل الحاوية إلى <bdi dir="ltr">Grid</bdi> ونستخدم <bdi dir="ltr">place-items</bdi> لتوسيط الرابط أفقيًا ورأسيًا. بعد ذلك نضيف مساحة داخلية وخلفية ولونًا للرابط، ونزيل خطه السفلي.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Grid</bdi> <bdi dir="ltr">alignment</bdi>
>
> ##### `display: grid`
>
> ينشئ حاوية <bdi dir="ltr">Grid</bdi> لعنصر الرابط.
>
> ##### `place-items: center`
>
> يوسّط العنصر داخل مساحة الحاوية أفقيًا ورأسيًا.
>
> ##### `min-height`
>
> يوفر ارتفاعًا كافيًا لتظهر عملية التوسيط في المعاينة.
>
> #### تنسيق الرابط
>
> ##### `a`
>
> محدد نوع يختار عنصر الرابط.
>
> ##### `padding: 18px 30px`
>
> القيمة الأولى للحشو الرأسي والثانية للأفقي.
>
> ##### `border-radius`
>
> يليّن زوايا الخلفية.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-04</bdi> {
> ```
>
> يفتح قاعدة تنسيق حاوية الرابط.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">min-height</bdi>: <bdi dir="ltr">260px</bdi>;
> ```
>
> يعطي الحاوية حدًا أدنى للارتفاع كي يظهر التوسيط.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">display</bdi>: <bdi dir="ltr">grid</bdi>;
> ```
>
> يجعل الحاوية شبكة <bdi dir="ltr">CSS</bdi>.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">place-items</bdi>: <bdi dir="ltr">center</bdi>;
> ```
>
> يضع الرابط في منتصف الحاوية في الاتجاهين.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الحاوية.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-04</bdi> <bdi dir="ltr">a</bdi> {
> ```
>
> يختار الرابط الموجود داخل الحاوية ذات المعرّف <bdi dir="ltr">task-04</bdi>.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">padding</bdi>: <bdi dir="ltr">18px</bdi> <bdi dir="ltr">30px</bdi>;
> ```
>
> يضيف <bdi dir="ltr">18px</bdi> رأسيًا و30px أفقيًا حول نص الرابط.
>
> **8.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">border-radius</bdi>: <bdi dir="ltr">8px</bdi>;
> ```
>
> يجعل زوايا الخلفية مستديرة.
>
> **9.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">background</bdi>: <bdi dir="ltr">#009688</bdi>;
> ```
>
> يضبط خلفية الرابط على اللون الموجود في الحل المحلي.
>
> **10.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#fff</bdi>;
> ```
>
> يجعل النص أبيض.
>
> **11.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">font</bdi>: 700 <bdi dir="ltr">24px</bdi> <bdi dir="ltr">Arial</bdi>, <bdi dir="ltr">sans-serif</bdi>;
> ```
>
> يضبط وزن الخط وحجمه وعائلته.
>
> **12.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">text-decoration</bdi>: <bdi dir="ltr">none</bdi>;
> ```
>
> يزيل خط الرابط الافتراضي.
>
> **13.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة الرابط.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/assets/solution-page-task-04.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/04 - CSS Text Formatting - Centered Styled Link.html|افتح صفحة الشرح المستقلة للتكليف 04]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-17-to-21/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-4.png)
