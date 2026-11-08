---
title: "Z-Index Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
aliases:
  - Z-Index — ترتيب الطبقات
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Z-Index</bdi>

تحدد الخاصية <bdi dir="ltr">z-index</bdi> ترتيب ظهور العناصر المتداخلة: أيّها يظهر فوق الآخر. القيمة الأكبر تعني طبقة أعلى عندما تكون العناصر في سياق التكديس نفسه.

## مثال الدرس

العناصر الثلاثة في المثال تستخدم <bdi dir="ltr">position: absolute</bdi>، لذلك يمكنها التداخل، ثم تحدد قيم <bdi dir="ltr">z-index</bdi> ترتيبها:

```css
.one {
  left: 20px;
  top: 20px;
  z-index: 3;
}

.two {
  left: 15px;
  top: 15px;
  z-index: 2;
}

.three {
  z-index: 1;
}
```

الترتيب من الأعلى إلى الأسفل هو <bdi dir="ltr">One</bdi> ثم <bdi dir="ltr">Two</bdi> ثم <bdi dir="ltr">Three</bdi>، لأن القيم <bdi dir="ltr">3</bdi> ثم <bdi dir="ltr">2</bdi> ثم <bdi dir="ltr">1</bdi>. لا تحرك <bdi dir="ltr">z-index</bdi> العنصر في الصفحة؛ إنها تغيّر ترتيب رسمه أمام العناصر الأخرى فقط.

في هذا الدرس، الخاصية مؤثرة لأن العناصر موضوعة بـ<bdi dir="ltr">absolute</bdi>. ويمكن استخدامها أيضًا مع عناصر <bdi dir="ltr">flex</bdi> أو <bdi dir="ltr">grid</bdi>. وإذا وُضعت العناصر داخل سياقات تكديس مختلفة، تُقارن قيمها داخل سياقها؛ فالقيمة الكبيرة لعنصر ابن لا تتجاوز تلقائيًا سياق أبيه.

> [!tip] تذكّر
> <bdi dir="ltr">z-index</bdi> الأعلى يظهر أمام القيم الأقل داخل السياق نفسه، لكنه لا يغير إحداثيات العنصر.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> تظهر <bdi dir="ltr">One</bdi> فوق <bdi dir="ltr">Two</bdi> ثم <bdi dir="ltr">Three</bdi>، لأن قيم <bdi dir="ltr">z-index</bdi> هي <bdi dir="ltr">3</bdi> ثم <bdi dir="ltr">2</bdi> ثم <bdi dir="ltr">1</bdi>.

## روابط

- [[Position Lesson]]
- [[Opacity Lesson]]
- [درس Z-Index](https://elzero.org/css-z-index/)
