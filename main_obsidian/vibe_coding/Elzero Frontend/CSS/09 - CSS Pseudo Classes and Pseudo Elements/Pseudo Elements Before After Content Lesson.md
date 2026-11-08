---
title: "Pseudo Elements Before After Content Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
aliases:
  - Pseudo Elements — Before, After, Content
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Pseudo Elements: Before, After, Content</bdi>

ينشئ <bdi dir="ltr">::before</bdi> جزءًا قبل محتوى العنصر، وينشئ <bdi dir="ltr">::after</bdi> جزءًا بعده. الخاصية <bdi dir="ltr">content</bdi> مطلوبة لإنشاء هذا الجزء. حتى القيمة الفارغة <bdi dir="ltr">""</bdi> تنشئه، ويمكن بعدها تنسيقه كصندوق عادي.

## ترتيب بطاقة التعليق

يطفو كل من `.user` و`.one` إلى اليسار ليظهرا بجانب بعضهما، وتضيف `margin-right` مسافة بين الحرف والنص. يحتوي `.parent` العناصر العائمة باستخدام `overflow: hidden`، ويضيف `margin-bottom` مسافة بين البطاقات.
## المثلث والشريط في مثال الدرس

العنصر <bdi dir="ltr">.one</bdi> لديه <bdi dir="ltr">position: relative</bdi>، لذلك يستخدمه العنصران الزائفان مرجعًا لمواضعهما:

- <bdi dir="ltr">.one::after</bdi> ينشئ شريطًا أخضر عرضه <bdi dir="ltr">5px</bdi> وارتفاعه <bdi dir="ltr">100%</bdi> عند يمين الصندوق. قيمة <bdi dir="ltr">right: -10px</bdi> تضعه خارج الحافة قليلًا.
- <bdi dir="ltr">.one::before</bdi> ينشئ مثلثًا بجانب الصندوق. يوسّطه <bdi dir="ltr">top: 50%</bdi> مع إزاحة لأعلى، وتضعه <bdi dir="ltr">left: -20px</bdi> خارج الحافة. لا يحتوي نصًا؛ بل تصنع حدوده المائلة شكل السهم.
- <bdi dir="ltr">content: ""</bdi> ينشئ الصندوقين من دون إضافة أحرف.

```css
.one {
  position: relative;
}

.one::after {
  content: "";
  position: absolute;
  width: 5px;
  height: 100%;
  right: -10px;
  top: 0;
  background-color: #009688;
}

.one::before {
  content: "";
  position: absolute;
  top: 50%;
  left: -20px;
  width: 0;
  height: 0;
  margin-top: -10px;
  border: 10px solid transparent;
  border-right-color: #009688;
}
```

السهم يعتمد على أن بقية الحدود شفافة، بينما الحد الأيمن أخضر؛ فتظهر منه هيئة مثلث. وتُكرر بنية <bdi dir="ltr">.parent</bdi> ثلاث مرات لتكوين ثلاث بطاقات أحرفها <bdi dir="ltr">O</bdi> و<bdi dir="ltr">A</bdi> و<bdi dir="ltr">E</bdi>.

> [!tip] استخدام مناسب
> استخدم هذه العناصر للزخرفة مثل الشريط والسهم. أما النص أو المعلومات المهمة، فضعها في <bdi dir="ltr">HTML</bdi> نفسه حتى تبقى واضحة وسهلة الوصول.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> `::before` ينشئ جزءًا قبل محتوى العنصر، و`::after` ينشئ جزءًا بعده. وكلاهما يحتاج إلى خاصية `content` كي يظهر.

## روابط

- [[Pseudo Elements First Letter First Line Selection Lesson]]
- [[03 - CSS Pseudo Elements — Comment Pointer]]
- [درس Pseudo Elements – Before, After, Content](https://elzero.org/css-pseudo-elements-before-after-content/)
