---
title: "Pseudo Elements First Letter First Line Selection Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
aliases:
  - Pseudo Elements — First Letter, First Line, Selection
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Pseudo Elements: First Letter, First Line, Selection</bdi>

العنصر الزائف <bdi dir="ltr">pseudo-element</bdi> ينسّق جزءًا محددًا من العنصر، ويُكتب عادةً بنقطتين مثل <bdi dir="ltr">::first-letter</bdi>.

## حرف البداية: `::first-letter`

في مثال الدرس، أُحيط الحرف الأول يدويًا بعنصر <bdi dir="ltr">span</bdi> في <bdi dir="ltr">.one</bdi>. أما <bdi dir="ltr">.two::first-letter</bdi> فينسّق أول حرف ظاهر من النص مباشرةً، من دون إضافة <bdi dir="ltr">span</bdi> إلى <bdi dir="ltr">HTML</bdi>. لذلك يكبّر الحرف ويجعله أبيض على خلفية حمراء.

## السطر الأول: `::first-line`

يختار <bdi dir="ltr">.three::first-line</bdi> السطر الأول الذي يظهر على الشاشة، فيجعله أخضر وعريضًا. طول هذا السطر يتغير مع عرض الحاوية وحجم الخط؛ فهو ليس بالضرورة جملة أو سطرًا ثابتًا في ملف <bdi dir="ltr">HTML</bdi>.

## النص المحدد: `::selection`

يُطبّق <bdi dir="ltr">::selection</bdi> التنسيق على الجزء الذي يحدده المستخدم من النص. في مثال الدرس، يصبح خلف النص المحدد أسود ولون الحروف أصفر. جرّب سحب المؤشر فوق أي فقرة في المثال لتحديدها.

```css
.two::first-letter {
  background-color: red;
  color: white;
  font-size: 60px;
  font-weight: bold;
}

.three::first-line {
  font-weight: bold;
  color: green;
}

::selection {
  background-color: black;
  color: yellow;
}
```

> [!tip] فرق سريع
> `span` عنصر حقيقي أضفناه في `HTML`، بينما `::first-letter` و`::first-line` و`::selection` محددات تنشئها `CSS` لتنسيق أجزاء من المحتوى دون إضافة عناصر مقابلة إليها.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> `::first-letter` ينسّق أول حرف، و`::first-line` ينسّق أول سطر معروض، و`::selection` ينسّق النص أثناء تحديده.

## روابط

- [[Pseudo Classes Lesson]]
- [[02 - CSS Pseudo Elements — Number Badge]]
- [درس Pseudo Elements – First Letter, First Line, Selection](https://elzero.org/css-pseudo-elements-first-letter-first-line-selection/)
