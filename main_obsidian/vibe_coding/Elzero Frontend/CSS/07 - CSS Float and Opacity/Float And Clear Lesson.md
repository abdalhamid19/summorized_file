---
title: "Float And Clear"
date: 2026-11-04
tags:
  - vibe_coding
  - frontend
  - CSS
  - float
  - lesson
aliases:
  - شرح Float و Clear
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Float And Clear</bdi>

في مثال الدرس، تطفو أربعة صناديق منتجات إلى اليسار. استخدم <bdi dir="ltr">clear</bdi> لمنع المحتوى التالي من الظهور بجانب العناصر العائمة.

## كود الدرس

```css
.parent {
  background-color: red;
  padding: 10px;
}
.parent div {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  background-color: #eee;
  width: 25%;
  float: left;
}
.clear {
  clear: both;
}
```

وفي <bdi dir="ltr">HTML</bdi> يأتي عنصر التنظيف بعد الأب:

```html
</div>
<div class="clear"></div>
<p>This Is P For Testing Float</p>
```

## التجربة التفاعلية

![[Float And Clear Interactive.html]]

## كيف يعمل المثال؟

1. <bdi dir="ltr">float: left</bdi> يضع كل صندوق عائمًا عند الجهة اليسرى، ويسمح للمحتوى اللاحق بالالتفاف حوله عند توفر مساحة.
2. <bdi dir="ltr">width: 25%</bdi> يجعل عرض كل صندوق ربع عرض الأب. أربعة صناديق × <bdi dir="ltr">25%</bdi> = <bdi dir="ltr">100%</bdi>، لذلك تصطف في صف واحد إذا كان عرض المحتوى كافيًا.
3. لأن الصناديق عائمة، لا يحسبها الأب بالطريقة المعتادة ضمن ارتفاعه. في هذا المثال، عنصر <bdi dir="ltr">.clear</bdi> موجود خارج الأب؛ لذلك لا يجعل خلفية الأب الحمراء تحيط بالمنتجات.
4. <bdi dir="ltr">clear: both</bdi> يضع عنصر التنظيف بعد العوامات على الجهتين. وبذلك يبدأ نص الفقرة التالية تحتها بدل الالتفاف بجانبها.

في المثال المحدد، تشغل المنتجات الأربعة الصف كاملًا، لذا قد تبدأ الفقرة أسفلها حتى دون <bdi dir="ltr">clear</bdi>. تظهر فائدة <bdi dir="ltr">clear</bdi> بوضوح إذا قل عرض المنتجات وبقي فراغ في الصف؛ عندها قد يلتف نص الفقرة بجانبها ما لم يُنظَّف التعويم.

## جعل الأب يحتوي العوامات

إذا كان المطلوب أن تمتد خلفية الأب الحمراء حول المنتجات أيضًا، يمكن إنشاء سياق تنسيق مستقل للأب باستخدام <bdi dir="ltr">display: flow-root</bdi>:

```css
.parent {
  display: flow-root;
}
```

عندها يحتوي الأب العناصر العائمة ويأخذ ارتفاعها في الحسبان. هذا يختلف عن عنصر <bdi dir="ltr">.clear</bdi> الموجود بعد الأب، الذي يضع المحتوى التالي أسفل العوامات ولا يوسّع الأب.

## المصدر

[درس Float And Clear في أكاديمية الزيرو](https://elzero.org/css-float-and-clear/)

> [!info]- إذا لم تظهر المعاينة داخل الملاحظة
> تحتاج إلى تفعيل إضافة <bdi dir="ltr">Embed HTML</bdi> في <bdi dir="ltr">Obsidian</bdi> لعرض الصفحة التفاعلية داخل الملاحظة.
