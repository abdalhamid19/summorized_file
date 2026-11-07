---
title: "Mouse Cursor"
date: 2026-11-04
tags:
  - vibe_coding
  - frontend
  - CSS
  - cursor
  - lesson
aliases:
  - شرح مؤشر الفأرة في CSS
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Mouse Cursor</bdi>

خاصية <bdi dir="ltr">cursor</bdi> تغيّر شكل مؤشر الفأرة عندما يمر فوق العنصر. في مثال الدرس، الزر هو العنصر الوحيد الذي أُعطي قيمة خاصة للمؤشر.

## كود الدرس

```css
button {
  background: transparent;
  border: none;
  color: red;
  font-weight: bold;
  cursor: pointer;
}
```

## التجربة التفاعلية

![[Mouse Cursor Interactive.html]]

## شرح القاعدة

- <bdi dir="ltr">background: transparent</bdi> يجعل خلفية الزر شفافة.
- <bdi dir="ltr">border: none</bdi> يزيل حد الزر الافتراضي.
- <bdi dir="ltr">color: red</bdi> يجعل نص الزر أحمر.
- <bdi dir="ltr">font-weight: bold</bdi> يجعل النص عريضًا.
- <bdi dir="ltr">cursor: pointer</bdi> يعرض شكل اليد عند مرور المؤشر فوق الزر، وهو شكل مألوف للعناصر التي يمكن النقر عليها.

توجد في الصفحة أيضًا وصلة <bdi dir="ltr">Google</bdi>، وعنصر <bdi dir="ltr">span</bdi>، وفقرات. لها أشكال المؤشر المعتادة في المتصفح، بينما يطلب الكود صراحةً شكل <bdi dir="ltr">pointer</bdi> للزر.

**مهم:** تغيير شكل المؤشر لا يضيف وظيفة للعنصر. إنه تلميح بصري فقط؛ وظيفة العنصر تحددها بنية <bdi dir="ltr">HTML</bdi> وسلوك الصفحة. الزر يظل عنصر زر، لكن <bdi dir="ltr">cursor: pointer</bdi> وحدها لا تنفذ إجراءً جديدًا عند النقر.

## المصدر

[درس Mouse Cursor في أكاديمية الزيرو](https://elzero.org/css-mouse-cursor/)

> [!info]- إذا لم تظهر المعاينة داخل الملاحظة
> تحتاج إلى تفعيل إضافة <bdi dir="ltr">Embed HTML</bdi> في <bdi dir="ltr">Obsidian</bdi> لعرض الصفحة التفاعلية داخل الملاحظة.
