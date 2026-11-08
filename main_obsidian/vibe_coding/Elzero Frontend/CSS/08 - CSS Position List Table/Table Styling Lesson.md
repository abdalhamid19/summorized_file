---
title: "Table Styling Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - position-list-table
aliases:
  - Table Styling — تنسيق الجداول
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Table Styling</bdi>

يعرض الدرس جدولًا بأعمدة الاسم والعمر والبريد الإلكتروني. تنسّق قواعد <bdi dir="ltr">CSS</bdi> عرض الجدول وحدوده ومساحة الخلايا، ثم تميّز صف العناوين عن صفوف البيانات.

## شرح القواعد

```css
body {
  font-family: Arial, Helvetica, sans-serif;
}

table {
  width: 100%;
  border: 1px solid #ccc;
  border-spacing: 0;
}

table td {
  padding: 15px;
  background-color: #eee;
  border: 1px solid #ccc;
}

table thead td {
  background-color: #f44336;
  color: #fff;
  font-weight: bold;
  text-align: center;
  border-color: #f35246;
}
```

- `width: 100%` يجعل الجدول يملأ عرض الحاوية.
- `border` يرسم حدًا حول الجدول والخلايا.
- `border-spacing: 0` يزيل الفراغ الافتراضي بين الخلايا. وهي تعمل هنا مع نمط الجدول الافتراضي الذي يفصل الحدود؛ لهذا قد تلتقي حدود خليتين متجاورتين وتبدو أكثر سماكة.
- `padding: 15px` يضيف مساحة داخل كل خلية بين النص وحدودها.
- `table thead td` يختار خلايا صف الرأس فقط، فيعطيها خلفية حمراء ونصًا أبيض عريضًا ومحاذاة وسطية.

في بيانات المثال، يظهر صف `Name / Age / Email` بلون مختلف، وتبقى أسماء `Osama` و`Ahmed` و`Sayed` و`Ali` في صفوف رمادية.

> [!tip] تحسين دلالي
> استخدم الدرس `td` داخل `thead`، لكن في الجداول الدلالية يُفضّل تمثيل عناوين الأعمدة بعنصر `th`، ويمكن إضافة `scope="col"` لتوضيح أنها عناوين أعمدة لقارئات الشاشة.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> `padding` يضيف مساحة داخل الخلية حول محتواها. أما `border-spacing` فيضبط الفراغ بين الخلايا.

## روابط

- [[04 - CSS Position, List, and Table - Table-only Layout]]
- [درس Table Styling](https://elzero.org/css-table-styling/)
