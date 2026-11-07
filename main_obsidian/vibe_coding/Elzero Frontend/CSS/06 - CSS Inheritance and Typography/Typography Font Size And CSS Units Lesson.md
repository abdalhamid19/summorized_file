---
title: "Typography – Font Size And CSS Units"
date: 2026-11-04
tags:
  - vibe_coding
  - frontend
  - CSS
  - typography
  - lesson
aliases:
  - شرح Font Size And CSS Units
---

# <bdi dir="ltr">CSS</bdi> — <bdi dir="ltr">Typography: Font Size And CSS Units</bdi>

يعرض مثال الدرس نصًا داخل <bdi dir="ltr">div</bdi>، وكلمة <bdi dir="ltr">Test</bdi> داخل <bdi dir="ltr">span</bdi>. يوضح الكود ثلاث وحدات لحجم الخط: <bdi dir="ltr">px</bdi> و<bdi dir="ltr">vw</bdi> و<bdi dir="ltr">rem</bdi>.

## كود الدرس

```css
body {
  font-size: 40px;
}
div {
  font-size: 5vw;
}
div span {
  font-size: 2rem;
}
```

## التجربة التفاعلية

![[Typography Font Size And CSS Units Interactive.html]]

## معنى الوحدات في المثال

- <bdi dir="ltr">px</bdi> وحدة ذات قيمة رقمية ثابتة. يضبط المثال حجم خط <bdi dir="ltr">body</bdi> على <bdi dir="ltr">40px</bdi>.
- <bdi dir="ltr">vw</bdi> تعني واحدًا بالمئة من عرض نافذة المتصفح. لذلك <bdi dir="ltr">5vw</bdi> تساوي خمسة بالمئة من عرض النافذة. إذا كان العرض <bdi dir="ltr">1280px</bdi>، يكون الحجم <bdi dir="ltr">64px</bdi>.
- <bdi dir="ltr">rem</bdi> وحدة نسبية تعتمد على حجم الخط في عنصر الجذر <bdi dir="ltr">html</bdi>. عند الحجم الافتراضي الشائع <bdi dir="ltr">16px</bdi>، تساوي <bdi dir="ltr">2rem</bdi> مقدار <bdi dir="ltr">32px</bdi>.

## أسماء الوحدات والاختصارات

| الوحدة | الاسم بالإنجليزية | معناها بالعربية |
|---|---|---|
| <bdi dir="ltr">vw</bdi> | <bdi dir="ltr">Viewport Width</bdi> | واحد بالمئة من عرض نافذة العرض. مثال: <bdi dir="ltr">5vw</bdi> يساوي خمسة بالمئة من عرض النافذة. |
| <bdi dir="ltr">vh</bdi> | <bdi dir="ltr">Viewport Height</bdi> | واحد بالمئة من ارتفاع نافذة العرض. مثال: <bdi dir="ltr">10vh</bdi> يساوي عشرة بالمئة من ارتفاعها. |
| <bdi dir="ltr">vmin</bdi> | <bdi dir="ltr">Viewport Minimum</bdi> | واحد بالمئة من البُعد الأصغر بين عرض نافذة العرض وارتفاعها. |
| <bdi dir="ltr">vmax</bdi> | <bdi dir="ltr">Viewport Maximum</bdi> | واحد بالمئة من البُعد الأكبر بين عرض نافذة العرض وارتفاعها. |
| <bdi dir="ltr">rem</bdi> | <bdi dir="ltr">Root Em</bdi> | وحدة نسبية إلى حجم خط العنصر الجذر، وغالبًا يكون <bdi dir="ltr">html</bdi>. |
| <bdi dir="ltr">em</bdi> | <bdi dir="ltr">Em</bdi> | وحدة نسبية؛ في حجم الخط تُحسب نسبةً إلى حجم خط العنصر الأب. |
| <bdi dir="ltr">px</bdi> | <bdi dir="ltr">CSS Pixel</bdi> | بكسل CSS، وحدة طول ذات قيمة محددة في التنسيق. |
| <bdi dir="ltr">%</bdi> | <bdi dir="ltr">Percentage</bdi> | نسبة مئوية، ويعتمد العنصر المرجعي للحساب على الخاصية المستخدمة. |

### الفرق بين <bdi dir="ltr">em</bdi> و<bdi dir="ltr">rem</bdi>

تحسب <bdi dir="ltr">em</bdi> حجم الخط نسبةً إلى حجم خط الأب، بينما تحسب <bdi dir="ltr">rem</bdi> نسبةً إلى حجم خط الجذر <bdi dir="ltr">html</bdi>. مثلًا، إذا كان حجم خط الأب <bdi dir="ltr">20px</bdi>، فإن <bdi dir="ltr">1.5em</bdi> تساوي <bdi dir="ltr">30px</bdi>. وإذا كان حجم خط الجذر <bdi dir="ltr">16px</bdi>، فإن <bdi dir="ltr">2rem</bdi> تساوي <bdi dir="ltr">32px</bdi>.

### تطبيق على كود الدرس

إذا كان عرض نافذة العرض <bdi dir="ltr">1000px</bdi>، فإن <bdi dir="ltr">5vw</bdi> تساوي <bdi dir="ltr">50px</bdi>. لذلك يكون حجم خط <bdi dir="ltr">div</bdi> خمسين بكسلًا. أما <bdi dir="ltr">2rem</bdi> في <bdi dir="ltr">span</bdi> فتحسب من حجم خط <bdi dir="ltr">html</bdi>، لا من حجم <bdi dir="ltr">div</bdi>.

## تتبّع القيم

حجم <bdi dir="ltr">body</bdi> هو <bdi dir="ltr">40px</bdi>، لكن <bdi dir="ltr">div</bdi> يحدد حجمه بنفسه باستخدام <bdi dir="ltr">5vw</bdi>، فلا يأخذ <bdi dir="ltr">40px</bdi> لحجم الخط. و<bdi dir="ltr">span</bdi> يحدد حجمه باستخدام <bdi dir="ltr">2rem</bdi>؛ لذلك يرجع إلى جذر الصفحة <bdi dir="ltr">html</bdi>، لا إلى حجم <bdi dir="ltr">body</bdi>. إذا كان حجم الجذر <bdi dir="ltr">16px</bdi>، تصبح كلمة <bdi dir="ltr">Test</bdi> بحجم <bdi dir="ltr">32px</bdi>.

## المصدر

[درس Typography – Font Size And CSS Units في أكاديمية الزيرو](https://elzero.org/css-typography-font-size-and-css-units/)

> [!info]- إذا لم تظهر المعاينة داخل الملاحظة
> تحتاج إلى تفعيل إضافة <bdi dir="ltr">Embed HTML</bdi> في <bdi dir="ltr">Obsidian</bdi> لعرض الصفحة التفاعلية داخل الملاحظة.
