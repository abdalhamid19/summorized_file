---
title: "Pseudo Elements Content And Counters Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
aliases:
  - Pseudo Elements — Content, Attr, Counters, Training
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Pseudo Elements: Content, Attr, Counters</bdi>

يجمع الدرس بين إنشاء نص أو رقم باستخدام <bdi dir="ltr">content</bdi>، وقراءة قيمة خاصية <bdi dir="ltr">HTML</bdi> باستخدام <bdi dir="ltr">attr()</bdi>، وترقيم العناصر باستخدام عدّاد <bdi dir="ltr">CSS</bdi>.

## إظهار قيمة `data-text`

في أول بطاقة فقط توجد الخاصية <bdi dir="ltr">data-text="Something"</bdi>. تقرأ <bdi dir="ltr">attr(data-text)</bdi> قيمتها وتضعها في محتوى <bdi dir="ltr">::before</bdi>:

```css
.one::before {
  content: attr(data-text);
  display: none;
}
```

لكن <bdi dir="ltr">display: none</bdi> يخفي هذا الجزء، فلا تظهر كلمة <bdi dir="ltr">Something</bdi> في النتيجة الحالية. إذا أزلنا الإخفاء، تظهر القيمة قبل نص البطاقة الأولى. أما البطاقتان الأخريان فلا تحتويان على <bdi dir="ltr">data-text</bdi>، فتكون نتيجة <bdi dir="ltr">attr()</bdi> فيهما فارغة.

## عدّ بطاقات التعليق

تزيد <bdi dir="ltr">counter-increment</bdi> قيمة العداد مرة عند كل عنصر <bdi dir="ltr">.parent</bdi>. ثم تعرض <bdi dir="ltr">counter(members-counter)</bdi> القيمة الحالية داخل <bdi dir="ltr">.one::after</bdi>، لتظهر كشارة حمراء بجانب النص.

**ينقص الكود المعروض إعادة ضبط للعداد** إذا كان المطلوب تسلسلًا مستمرًا مثل <bdi dir="ltr">1، 2، 3</bdi>. أضفها إلى الحاوية المشتركة للبطاقات، مثل <bdi dir="ltr">body</bdi>:

```css
body {
  counter-reset: members-counter;
}
```

ثم أبقِ الزيادة على كل بطاقة:

```css
.parent {
  counter-increment: members-counter;
}
```

بهذا يبدأ العداد من الصفر في الحاوية ويزداد عند كل بطاقة، فتقرأ الشارة بعد الزيادة <bdi dir="ltr">1</bdi> ثم <bdi dir="ltr">2</bdi> ثم <bdi dir="ltr">3</bdi>. من دون نطاق إعادة ضبط مشترك، لا يعطي المقطع تسلسلًا متتابعًا مضمونًا.

## مثلثات القائمة

تزيل <bdi dir="ltr">list-style: none</bdi> العلامات الافتراضية للقائمة. ويستخدم <bdi dir="ltr">li::before</bdi> علامة مثلثية مرسومة من الحدود بدلها. تجعل <bdi dir="ltr">position: relative</bdi> على <bdi dir="ltr">li</bdi> عنصر القائمة مرجعًا لوضع المثلث خارجه. الحد الأخضر وبقية الحدود الشفافة هي ما يصنع شكل السهم.

في المشروع استُخدمت الفكرة نفسها في [[03 - CSS Pseudo Elements — Comment Pointer]]، واستُخدمت <bdi dir="ltr">counter-reset</bdi> مع <bdi dir="ltr">counter-increment</bdi> في [[04 - CSS Pseudo Elements — Numbered Product Rows]].

> [!tip] طريقة تذكّر
> `attr()` يقرأ قيمة من `HTML`، و`counter()` يعرض قيمة عداد، و`counter-reset` يحدد بداية نطاق العد، و`counter-increment` يزيده.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> `attr(data-text)` يقرأ قيمة `data-text`. وللحصول على أرقام متتابعة، نعيد ضبط العداد في الحاوية المشتركة، ثم نزيده عند كل بطاقة.

## روابط

- [[Pseudo Elements Before After Content Lesson]]
- [[03 - CSS Pseudo Elements — Comment Pointer]]
- [[04 - CSS Pseudo Elements — Numbered Product Rows]]
- [درس Pseudo Elements – Content And Training’s](https://elzero.org/css-pseudo-elements-content-and-trainings/)
- [مواصفة CSS 2.2 عن المحتوى المولّد والعدادات](https://www.w3.org/TR/CSS22/generate.html)
