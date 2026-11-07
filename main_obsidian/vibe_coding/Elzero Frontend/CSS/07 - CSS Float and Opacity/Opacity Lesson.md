---
title: "Opacity Lesson"
date: 2026-11-07
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
aliases:
  - Opacity — شفافية العنصر والخلفية
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Opacity</bdi>

تتحكم الخاصية <bdi dir="ltr">opacity</bdi> (العتامة أو الشفافية) في مدى ظهور العنصر. قيمتها من <bdi dir="ltr">0</bdi> إلى <bdi dir="ltr">1</bdi>: الصفر يجعل العنصر شفافًا تمامًا، والواحد يجعله ظاهرًا بالكامل.

## مثال الدرس

```css
.one {
  background-color: red;
  opacity: 0.1;
}

.two {
  background-color: rgb(255 0 0 / 0.1);
}
```

في العنصر <bdi dir="ltr">.one</bdi>، تؤثر <bdi dir="ltr">opacity: 0.1</bdi> في العنصر كله، بما فيه الخلفية والكتابة داخله. أما <bdi dir="ltr">rgb(255 0 0 / 0.1)</bdi> فتجعل لون الخلفية الأحمر نفسه شفافًا بنسبة <bdi dir="ltr">0.1</bdi>، وتبقي بقية العنصر مثل النص بعتامته الأصلية.

إذًا إذا كان المطلوب تخفيف لون الصندوق مع إبقاء كلمة <bdi dir="ltr">Element</bdi> واضحة، فخفّف شفافية الخلفية نفسها. في تكليف المشروع [[02 - CSS Float and Opacity - Transparent Background without Fading Text]] استُخدمت خلفية بلون <bdi dir="ltr">rgba()</bdi> لهذا السبب.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> <bdi dir="ltr">opacity</bdi> تخفف العنصر ومحتواه كله. أما قيمة الشفافية في لون <bdi dir="ltr">background-color</bdi> فتخفف الخلفية وحدها، لذلك تبقى الكتابة معتمة.

## روابط

- [[Float And Clear Lesson]]
- [[Mastering The CSS Calculation]]
- [[02 - CSS Float and Opacity - Transparent Background without Fading Text]]
- [درس Opacity](https://elzero.org/css-opacity/)
