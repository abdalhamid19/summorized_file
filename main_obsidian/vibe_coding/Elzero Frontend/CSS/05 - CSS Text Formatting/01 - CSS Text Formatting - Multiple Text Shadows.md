---
title: "01 - CSS Text Formatting - Multiple Text Shadows"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - text-formatting
  - تكليف
aliases:
  - تكليف Multiple Text Shadows
---

# <bdi dir="ltr">CSS</bdi> <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Formatting</bdi> — <bdi dir="ltr">Multiple</bdi> <bdi dir="ltr">Text</bdi> <bdi dir="ltr">Shadows</bdi>

> [!question] السؤال
> **المطلوب:** أنشئ الشكل الظاهر في صورة التكليف، مع استخدام الألوان نفسها. تلميح المصدر: يمكن إضافة أكثر من ظل داخل خاصية واحدة.
>
> **البنية المستخدمة في المعاينة؛ المصدر لا يعرض <bdi dir="ltr">HTML</bdi> محددًا**
>
> ```<bdi dir="ltr">html</bdi>
> <<bdi dir="ltr">h2</bdi> <bdi dir="ltr">class</bdi>="<bdi dir="ltr">text-shadow</bdi>"><bdi dir="ltr">Elzero</bdi></<bdi dir="ltr">h2</bdi>>
> ```
>
> [افتح صورة التكليف الرسمية](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-1.png)
>
> [!info] حدود المصدر والمطابقة
> الصورة الرسمية لا تتوفر ضمن الملفات المحلية، والموقع حجب طلب تنزيلها. لذلك تعرض الصفحة مثال الظلال بالقيم المحفوظة سابقًا، ولا تزعم مطابقة اللون المرجعي.

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">text-shadow</bdi> {
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>;
>   <bdi dir="ltr">text-shadow</bdi>:
>     <bdi dir="ltr">2px</bdi> <bdi dir="ltr">2px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>,
>     -<bdi dir="ltr">2px</bdi> -<bdi dir="ltr">2px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>,
>     <bdi dir="ltr">4px</bdi> <bdi dir="ltr">4px</bdi> 0 <bdi dir="ltr">#ff9800</bdi>;
> }
> ```
>
> **الفكرة الأساسية**
>
> تقبل <bdi dir="ltr">text-shadow</bdi> عدة ظلال في تصريح واحد. لكل ظل إزاحة أفقية ورأسية ولون، وتسمح الفواصل بتراكب الألوان حول النص. قيم الألوان هنا هي القيم الموجودة في الحل المحلي، لكن لا يمكن تأكيد مطابقتها للصورة الرسمية المحجوبة.
>
> ### معاني الرموز المستخدمة في الحل
>
> #### <bdi dir="ltr">Text</bdi> <bdi dir="ltr">formatting</bdi>
>
> ##### `text-shadow`
>
> تضيف ظلًا للنص من دون إنشاء عناصر إضافية.
>
> ##### `2px 2px 0 color`
>
> يمثل الإزاحة الأفقية ثم الرأسية ثم التمويه ثم اللون.
>
> ##### `الفاصلة ,`
>
> تفصل ظلًا عن الظل الذي يليه داخل القيمة نفسها.
>
> #### محددات <bdi dir="ltr">CSS</bdi>
>
> ##### `#task-01`
>
> يحدّ نطاق النمط إلى معاينة التكليف الأول.
>
> ##### `.text-shadow`
>
> يختار العنصر الذي يحمل الصنف <bdi dir="ltr">text-shadow</bdi>.
>
> ### شرح الحل سطرًا بسطر
>
> هذا الشرح يتناول أسطر <bdi dir="ltr">CSS</bdi> التي أضافها الحل؛ بنية <bdi dir="ltr">HTML</bdi> الأصلية موضحة في صندوق السؤال.
>
> **1.**
>
> ```<bdi dir="ltr">css</bdi>
> #<bdi dir="ltr">task-01</bdi> .<bdi dir="ltr">text-shadow</bdi> {
> ```
>
> يفتح قاعدة تنسيق عنصر النص في المعاينة الأولى.
>
> **2.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">color</bdi>: <bdi dir="ltr">#222</bdi>;
> ```
>
> يضبط لون النص الأساسي قبل رسم الظلال حوله.
>
> **3.**
>
> ```<bdi dir="ltr">css</bdi>
>   <bdi dir="ltr">text-shadow</bdi>:
> ```
>
> يبدأ قيمة الظلال؛ ويمكن أن تحتوي القائمة على أكثر من ظل.
>
> **4.**
>
> ```<bdi dir="ltr">css</bdi>
>     <bdi dir="ltr">2px</bdi> <bdi dir="ltr">2px</bdi> 0 <bdi dir="ltr">#e91e63</bdi>,
> ```
>
> يرسم أول ظل بإزاحة موجبة أفقية ورأسية ومن دون تمويه.
>
> **5.**
>
> ```<bdi dir="ltr">css</bdi>
>     -<bdi dir="ltr">2px</bdi> -<bdi dir="ltr">2px</bdi> 0 <bdi dir="ltr">#2196f3</bdi>,
> ```
>
> يفصل الظل الأول عن الثاني ويضع ظلًا في الاتجاه المعاكس.
>
> **6.**
>
> ```<bdi dir="ltr">css</bdi>
>     <bdi dir="ltr">4px</bdi> <bdi dir="ltr">4px</bdi> 0 <bdi dir="ltr">#ff9800</bdi>;
> ```
>
> يفصل الظل الثاني عن الثالث ويضيف ظلًا ثالثًا بإزاحة أكبر.
>
> **7.**
>
> ```<bdi dir="ltr">css</bdi>
> }
> ```
>
> يغلق قاعدة النص.
>
> **معاينة الصفحة المستقلة**
>
> ![[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/assets/solution-page-task-01.png|1100]]
>
> [[vibe_coding/Elzero Frontend/CSS/05 - CSS Text Formatting/01 - CSS Text Formatting - Multiple Text Shadows.html|افتح صفحة الشرح المستقلة للتكليف 01]]
>
> ## المصدر
>
> [صفحة التكليفات الرسمية](https://elzero.org/css-assignments-lesson-from-17-to-21/) · [صورة التكليف](https://elzero.org/wp-content/uploads/2021/02/css-assignments-lessons-17-21-1.png)
