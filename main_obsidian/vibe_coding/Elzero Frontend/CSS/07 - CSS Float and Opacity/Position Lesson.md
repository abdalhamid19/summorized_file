---
title: "Position Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - float-opacity
aliases:
  - Position — موضع العنصر في الصفحة
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Position</bdi>

تحدد الخاصية <bdi dir="ltr">position</bdi> طريقة وضع العنصر في الصفحة، وهل يبقى ضمن ترتيب العناصر الطبيعي أم يخرج منه.

## الوضع الافتراضي: `static`

كل عنصر يبدأ عادةً بوضع <bdi dir="ltr">static</bdi> (الوضع الطبيعي). تظهر العناصر واحدًا بعد الآخر، ويُحجز لكل عنصر مكانه في الصفحة.

## `position: absolute`

يجعل <bdi dir="ltr">absolute</bdi> العنصر خارج ترتيب الصفحة الطبيعي؛ فلا يعود يحجز مكانًا لبقية العناصر. لذلك يمكن أن يظهر فوق عنصر آخر، بينما تتحرك العناصر التالية لتملأ المساحة التي تركها.

في مثال الدرس:

```css
.one {
  background-color: red;
  position: absolute;
}

.two {
  background-color: green;
}
```

العنصر <bdi dir="ltr">.one</bdi> يخرج من الترتيب الطبيعي، لذلك لا تحجز البطاقة الحمراء مكانًا في تدفق الصفحة. أما <bdi dir="ltr">.two</bdi> فتبقى على وضعها الافتراضي <bdi dir="ltr">static</bdi> وتأتي في ترتيب الصفحة الطبيعي. لم يحدد المثال قيم <bdi dir="ltr">top</bdi> أو <bdi dir="ltr">left</bdi>؛ لذا يضع المتصفح العنصر عند موضعه الطبيعي المتوقع، مع أنه لم يعد يحجز ذلك الموضع. لهذا قد يتراكب العنصران.

عند تحديد <bdi dir="ltr">top</bdi> أو <bdi dir="ltr">left</bdi> أو ما يقابلهما، يُقاس الموضع عادةً من أقرب أب لديه <bdi dir="ltr">position</bdi> غير <bdi dir="ltr">static</bdi>. إذا لم يوجد أب كهذا، يكون مرجع التموضع هو الحاوية الابتدائية للصفحة.

> [!tip] الفكرة الأساسية
> `static`: العنصر يبقى في مكانه ضمن ترتيب الصفحة ويحجز مساحة.
> `absolute`: العنصر يخرج من ترتيب الصفحة ولا يحجز مساحة لبقية العناصر.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> العنصر ذو `position: absolute` يخرج من التدفق الطبيعي ولا يحجز مساحة؛ لذلك قد تنتقل العناصر التالية إلى مكانه أو تتراكب معه.

## روابط

- [[Float And Clear Lesson]]
- [[Opacity Lesson]]
- [[Mastering The CSS Calculation]]
- [درس Position](https://elzero.org/css-position/)
