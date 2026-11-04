---
title: "Typography – Font Style And Variant And Weight"
date: 2026-11-04
tags:
  - vibe_coding
  - frontend
  - CSS
  - typography
  - lesson
aliases:
  - شرح Font Style And Variant And Weight
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Typography: Font Style And Variant And Weight</bdi>

يعرض الدرس نصًا داخل <bdi dir="ltr">div</bdi> وفق شكل الحروف ووزنها، ثم يحوّل حالة أحرف النص داخل <bdi dir="ltr">p</bdi>. ويشرح عنوان الدرس أيضًا خاصية ميلان الخط <bdi dir="ltr">font-style</bdi>، مع أنها غير مكتوبة في الكود المرسل.

## كود الدرس

~~~html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>CSS</title>
    <link rel="stylesheet" href="css/master.css" />
  </head>
  <body>
    <div>elzero web school</div>
    <p>Elzero Web School</p>
  </body>
</html>
~~~

~~~css
div {
  font-variant: small-caps;
  font-weight: bold;
}
p {
  text-transform: uppercase;
}
~~~

## التجربة التفاعلية

غيّر كل خاصية ولاحظ الفرق بين شكل حروف <bdi dir="ltr">div</bdi> وحالة أحرف <bdi dir="ltr">p</bdi>.

![[Typography Font Style Variant And Weight Interactive.html]]

## شرح الخصائص

### <bdi dir="ltr">font-variant: small-caps</bdi>

تعرض الحروف الصغيرة بهيئة حروف كبيرة أصغر من الحروف الكبيرة المعتادة. لذلك تتحول كلمة <bdi dir="ltr">elzero</bdi> بصريًا إلى حروف كبيرة صغيرة، مع بقاء النص الأصلي في <bdi dir="ltr">HTML</bdi> كما كُتب. يعتمد شكلها الدقيق على الخط المستخدم ودعمه لهذه الهيئة.

### <bdi dir="ltr">font-weight: bold</bdi>

تزيد سماكة الحروف. القيمة <bdi dir="ltr">bold</bdi> تعادل عادةً الرقم <bdi dir="ltr">700</bdi>، بينما <bdi dir="ltr">normal</bdi> تعادل <bdi dir="ltr">400</bdi>.

### <bdi dir="ltr">font-style</bdi>

تحدد هيئة الخط: <bdi dir="ltr">normal</bdi> عادي، و<bdi dir="ltr">italic</bdi> مائل، و<bdi dir="ltr">oblique</bdi> مائل اصطناعيًا. الكود الذي أرسلته لا يضبط هذه الخاصية، لذلك يبقى النص عادي الميل ما لم توجد قاعدة أخرى تؤثر عليه.

### <bdi dir="ltr">text-transform: uppercase</bdi>

تعرض أحرف الفقرة <bdi dir="ltr">p</bdi> كبيرة. هذه الخاصية تغيّر طريقة العرض؛ فلا تعيد كتابة النص الأصلي داخل ملف <bdi dir="ltr">HTML</bdi>.

## الفرق بين <bdi dir="ltr">small-caps</bdi> و<bdi dir="ltr">uppercase</bdi>

- <bdi dir="ltr">small-caps</bdi> تغيّر هيئة الحروف الصغيرة إلى حروف كبيرة أصغر حجمًا، وتبقي اختلاف الأحجام ظاهرًا.
- <bdi dir="ltr">uppercase</bdi> تعرض الحروف كلها بحجم الحروف الكبيرة المعتاد.

## قراءة كود <bdi dir="ltr">CSS</bdi>

1. <bdi dir="ltr">div</bdi> يختار عنصر <bdi dir="ltr">div</bdi> في الصفحة.
2. <bdi dir="ltr">font-variant: small-caps</bdi> يغيّر هيئة أحرف النص داخله.
3. <bdi dir="ltr">font-weight: bold</bdi> يجعل النص عريضًا.
4. <bdi dir="ltr">p</bdi> يختار عنصر الفقرة.
5. <bdi dir="ltr">text-transform: uppercase</bdi> يعرض نص الفقرة بأحرف كبيرة.

## المصدر والمراجع

- [درس Typography – Font Style And Variant And Weight في أكاديمية الزيرو](https://elzero.org/css-typography-font-style-and-variant-and-weight/)
- [MDN: font-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
- [MDN: font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
- [MDN: font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
- [MDN: text-transform](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
- [[02 - CSS Font Families and Weights]]

> [!info]- إذا لم تظهر المعاينة داخل الملاحظة
> تحتاج إلى تفعيل إضافة <bdi dir="ltr">Embed HTML</bdi> في <bdi dir="ltr">Obsidian</bdi> لعرض الصفحة التفاعلية.
