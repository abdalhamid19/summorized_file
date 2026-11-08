---
title: "List Styling Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
aliases:
  - List Styling — تنسيق القوائم
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">List Styling</bdi>

يعرض الدرس قائمة لغات برمجة وقائمة متداخلة داخل <bdi dir="ltr">JS</bdi>. يغيّر <bdi dir="ltr">list-style-type</bdi> شكل العلامة التي تظهر بجانب كل عنصر، بينما تضيف <bdi dir="ltr">margin-bottom</bdi> مسافة بعد عنصر القائمة.

## مثال الدرس

```css
ul {
  list-style-type: lower-armenian;
}

li {
  background-color: #eee;
  margin-bottom: 20px;
}
```

تجعل <bdi dir="ltr">lower-armenian</bdi> العلامات على شكل الحروف الأرمنية الصغيرة بدل العلامات النقطية المعتادة. تنطبق القاعدة على كل من القائمة الخارجية والقائمة المتداخلة، لأن المحدد <bdi dir="ltr">ul</bdi> يختار الاثنين. وتضيف قاعدة <bdi dir="ltr">li</bdi> خلفية رمادية ومسافة أسفل كل عنصر، بما فيها عناصر القائمة الداخلية.

في قائمة الدرس، ستتبع عناصر <bdi dir="ltr">HTML</bdi> و<bdi dir="ltr">CSS</bdi> و<bdi dir="ltr">JS</bdi> العلامة المختارة للقائمة الخارجية، وكذلك <bdi dir="ltr">Reactjs</bdi> و<bdi dir="ltr">Vuejs</bdi> و<bdi dir="ltr">Angular</bdi> داخل القائمة الفرعية.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> يغيّر `list-style-type` شكل العلامات بجانب عناصر القائمة. أما `margin-bottom` فيضيف مسافة أسفل كل عنصر.

## روابط

- [[03 - CSS Position, List, and Table - Styled List with Attributes]]
- [درس List Styling](https://elzero.org/css-list-styling/)
