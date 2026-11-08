---
title: "Pseudo Classes Lesson"
date: 2026-11-08
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-pseudo-classes-and-pseudo-elements
aliases:
  - Pseudo Classes — تحديد العناصر حسب حالتها
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Pseudo Classes</bdi>

الفئة الزائفة <bdi dir="ltr">pseudo-class</bdi> محدد يبدأ بنقطتين، ويختار العنصر عندما تتحقق حالة أو صفة فيه، مثل تحويم المؤشر فوق رابط أو تحديد مربع اختيار.

## المحددات في مثال الدرس

- `a:hover` يغير لون الرابط أثناء مرور المؤشر فوقه.
- `a:visited` يغير لون الرابط الذي سبق فتحه. الحالة تعتمد على سجل المتصفح، وقد تقيد المتصفحات التنسيقات المسموح بها لحماية الخصوصية.
- `:empty` يختار عنصرًا بلا محتوى أو عناصر أبناء؛ في المثال يطابق `div.two` و`p` الفارغين.
- `.ch:checked` يطابق مربع الاختيار بعد تحديده.
- `.in:focus` يطابق حقل النص عندما يكون نشطًا ويستقبل الكتابة.

مثلًا، قاعدة `a:hover` تنطبق فقط ما دام المؤشر فوق الرابط، فلا تحتاج إلى JavaScript لتبديل اللون عند التحويم.

```css
a {
  color: green;
  text-decoration: none;
}

a:hover {
  color: red;
}

a:visited {
  color: blue;
}

:empty {
  border: 10px solid red;
}

.ch:checked {
  display: none;
}

.in:focus {
  border-color: red;
  outline: none;
}
```

## ملاحظتان لتحسين المثال

إخفاء مربع الاختيار نفسه بعد تحديده يجعله صعب الإلغاء؛ الأفضل إبقاؤه ظاهرًا وتغيير مظهر الملصق المجاور:

```css
.ch:checked + label {
  color: green;
}
```

كما أن `outline: none` يزيل إطار التركيز المرئي لمستخدم لوحة المفاتيح. الأفضل الإبقاء على مؤشر واضح، مثل:

```css
.in:focus {
  border-color: red;
  outline: 2px solid red;
}
```

في مثال المشروع السابق [[CSS Pseudo Classes Assignments 34-37.html]] توجد مساحة فارغة بين `One` و`Three`، وقد استُخدمت لتوضيح اختيار عنصر فارغ في تكليف الفئات الزائفة.

## مراجعة سريعة

> [!faq]- الإجابة — افتح بعد المحاولة
> `:focus` يختار العنصر الذي يستقبل التفاعل أو الكتابة حاليًا، بينما `:checked` يختار مربع الاختيار المحدد.

## روابط

- [[01 - CSS Pseudo Classes — Centered Blocks]]
- [درس Pseudo Classes](https://elzero.org/css-pseudo-classes/)
- [مواصفة Selectors Level 4 من W3C](https://www.w3.org/TR/selectors-4/)
