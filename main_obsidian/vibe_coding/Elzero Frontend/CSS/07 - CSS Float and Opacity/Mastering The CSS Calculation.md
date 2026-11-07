---
title: "Mastering The CSS Calculation"
date: 2026-11-07
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
aliases:
  - CSS calc() — حساب العرض وتوزيع المنتجات
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Mastering The CSS Calculation</bdi>

تُستخدم دالة <bdi dir="ltr">calc()</bdi> لإجراء عملية حسابية ضمن قيمة خاصية <bdi dir="ltr">CSS</bdi>. في هذا الدرس نحسب عرض كل منتج بعد طرح المساحة التي تشغلها الفواصل.

## مثال الدرس

```html
<div>Product One</div>
<div>Product Two</div>
<div>Product Three</div>
<div>Product Four</div>
```

```css
width: calc((100% - 60px) / 5);
```

تقرأ الصيغة هكذا: اطرح <bdi dir="ltr">60px</bdi> من عرض المساحة المتاحة، ثم اقسم الباقي على خمسة. بهذه الطريقة يمكن أن يعتمد عرض المنتجات على عرض الحاوية بدل تثبيته بقياس واحد.

## مطابقة الأرقام مع العناصر

في المثال المرسل توجد أربعة عناصر <bdi dir="ltr">div</bdi>، لكن القسمة في الصيغة على خمسة. كما أن لكل عنصر <bdi dir="ltr">margin-left: 10px</bdi>، فيكون مجموع الهوامش الظاهرة أربعة هوامش، أي <bdi dir="ltr">40px</bdi>، وليس <bdi dir="ltr">60px</bdi>. لذلك لا تتطابق الصيغة والتعليق مع عدد العناصر وقواعد الهوامش كما وردت.

لأربع بطاقات مع ثلاثة فواصل مقدار كل منها <bdi dir="ltr">10px</bdi>، تكون الصيغة المناسبة عند استخدام <bdi dir="ltr">gap</bdi>:

```css
.products {
  display: flex;
  gap: 10px;
}

.products > div {
  width: calc((100% - 30px) / 4);
}
```

نطرح <bdi dir="ltr">30px</bdi> لأنها ثلاثة فواصل بين أربع بطاقات، ثم نقسم المساحة المتبقية على أربعة. مثلًا، إذا كان عرض الحاوية <bdi dir="ltr">1000px</bdi>، يكون عرض كل بطاقة <bdi dir="ltr">242.5px</bdi>، ويضاف إليها مجموع الفواصل <bdi dir="ltr">30px</bdi> ليكتمل العرض.

> [!tip] طريقة العد
> إذا كان لدينا <bdi dir="ltr">N</bdi> عناصر في صف واحد، فعدد الفواصل بينها هو <bdi dir="ltr">N - 1</bdi>. اطرح مجموع الفواصل أولًا، ثم اقسم المساحة المتبقية على عدد العناصر.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> بين أربع بطاقات توجد ثلاثة فواصل. عند <bdi dir="ltr">10px</bdi> لكل فاصل، نطرح <bdi dir="ltr">30px</bdi> من عرض الحاوية، ثم نقسم الباقي على أربعة.

## روابط

- [[Float And Clear Lesson]]
- [[01 - CSS Float and Opacity - Dynamic Float Grid with Calc]]
- [درس Mastering The CSS Calculation](https://elzero.org/css-mastering-the-css-calculation/)
