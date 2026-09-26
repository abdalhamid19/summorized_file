---
title: "من Tawreed إلى تفاصيل الطلب والأسماء"
date: 2026-09-26
tags: [PharmaSupplyBot, Tawreed, API, product-data]
aliases: ["قراءة طلب Tawreed"]
---

# 01 - من Tawreed إلى تفاصيل الطلب والأسماء

## الملخص

تبدأ العملية بقراءة الطلب من API توريد. القائمة تعطي بيانات الطلب الأساسية، ثم تُجلب تفاصيل الطلب المختار بما فيها سطور الأصناف والأسعار. وللحصول على الاسم الإنجليزي الرسمي، يستدعي التطبيق واجهة كتالوج المنتجات باستخدام معرّف منتج توريد.

تُنفذ هذه الخطوات في `purchase_importer/tawreed.py`، ويستدعيها مسار الاستيراد في `eplus_purchase/service.py` وواجهة `eplus_purchase/ui.py`.

ا <span style="color:#0D9488; font-weight:bold;">قاعدة التمييز:</span> اسم المنتج الرسمي واسم المورد حقلان مختلفان؛ واجهة الكتالوج هي مصدر الاسم الإنجليزي الرسمي.

## قائمة الطلبات ثم تفاصيل الطلب

يستخدم التطبيق واجهتين منفصلتين:

| المرحلة | المسار في API | الغرض |
|---|---|---|
| قائمة الطلبات | `rest/v2/orders/purchase/search` | عرض الطلبات المؤكدة ومعرّف الطلب والمورد والتاريخ والإجمالي والحالة |
| تفاصيل طلب | `rest/v2/orders/purchase/get` | جلب بيانات رأس الطلب وكل سطر من سطور الشراء |

عند طلب القائمة، يرسل التطبيق بيانات التصفية داخل غلاف API مثل `mode` و`langCode` و`data`، بينما يرسل `page` و`size` و`sort` كمعاملات في عنوان الطلب. بعد اختيار رقم الطلب، تُجلب تفاصيله باستخدام معرّفه.

## ما الذي يحتويه سطر الطلب؟

تتضمن بيانات الصنف عادةً الحقول الآتية:

| الحقل | معناه في العملية |
|---|---|
| `productId` | معرّف منتج Tawreed العام |
| `storeProductId` | معرّف منتج المورد في Tawreed |
| `productName` | الاسم الذي أرسله Tawreed ضمن تفاصيل الطلب |
| `storeProductName` | الاسم الذي أدخله المورد؛ قد يكون مختصرًا أو مختلفًا |
| `quantity` | الكمية المطلوبة |
| `retailPrice` | سعر الوحدة قبل خصم الشراء |
| `salePrice` | سعر الوحدة الصافي الذي يعيده الطلب |
| `discountPercent` | نسبة الخصم |
| `itemTotal` | إجمالي السطر كما أرسله Tawreed |

هذه الأسماء الثلاثة ليست شيئًا واحدًا: `productName` اسم Tawreed، و`storeProductName` اسم المورد، والاسم الإنجليزي الرسمي يأتي من كتالوج المنتج.

## استخراج الاسم العربي والإنجليزي

يحتفظ طلب الشراء بمعرّف المنتج، ولذلك يستخدم التطبيق هذا المعرّف لطلب سجل المنتج من:

`POST https://api.tawreed.io/rest/v2/products/get`

مبسّطًا، الجزء المسؤول عن الطلب واستخراج الاسمين يعمل بهذا الشكل:

~~~python
body = {
    "mode": "error",
    "langCode": "en",
    "data": product_id,
}
response = session.post("rest/v2/products/get", data=body)
product = response.json().get("data") or {}

name_ar = product.get("productName") or ""
name_en = product.get("productNameEn") or ""
~~~

في الكود الفعلي، تجمع الدالة `enrich_order_product_names` معرّفات المنتجات الفريدة، وتطلب سجل الكتالوج لكل معرّف، ثم تضع `productName` في `item.product_name` و`productNameEn` في `item.product_name_en`. الاسم الإنجليزي لا يُستنتج بالترجمة؛ بل يُقرأ من حقل منفصل في رد API.

## مثال حي

في الطلب `3053985` ظهر السطر الآتي في المعاينة:

| مصدر الاسم | القيمة |
|---|---|
| اسم Tawreed العربي | الوكيتا ليف ان كريم للشعر 120 جم |
| الاسم الإنجليزي الرسمي | ALOEKITA LEAVE IN CREAM 120 GM |
| اسم المورد | الوكيتا كريم ازرق |
| معرّف المنتج في Tawreed | `126077` |

الاختلاف بين اسم المورد والاسم الرسمي متوقع؛ التطبيق يحتفظ بهما منفصلين لكي يستطيع المشغّل التحقق من هوية الصنف.

## كيف تصل بيانات Tawreed إلى بقية التطبيق؟

- `get_order_detail` يعيد كائن تفاصيل الطلب مع سطوره.
- `enrich_order_product_names` يضيف الاسم الإنجليزي الرسمي واسم الكتالوج العربي إلى السطر عند نجاح API الكتالوج.
- `verify_bill` و`build.resolve_line` يستخدمان معرّفات المنتج واسم Tawreed واسم المورد للوصول إلى صنف e-Plus.
- عند فشل إثراء الأسماء في مسار الخدمة، يُسمح باستمرار التحقق؛ قد يبقى الاسم الإنجليزي فارغًا، لكن لا يُفترض أن فشل الاسم وحده يغيّر السعر أو الكمية.

## مفاهيم

| المصطلح | التعريف |
|---|---|
| `productId` | المفتاح الذي يحدد المنتج في كتالوج Tawreed |
| `storeProductId` | هوية المنتج لدى المورد في Tawreed |
| `productNameEn` | حقل الاسم الإنجليزي في سجل كتالوج Tawreed |
| `itemTotal` | إجمالي السطر الذي وصل من طلب الشراء |

## تنبيه

> [!warning] لا تعتبر اسم المورد ترجمة للاسم الإنجليزي
> `storeProductName` نص يكتبه المورد. لا يجوز عرضه أو حفظه على أنه الاسم الإنجليزي الرسمي للمنتج.

## مصادر الكود

- [tawreed.py في مستودع tawreed-importer — commit 34d9148](https://github.com/AnasMahrous/tawreed-importer/blob/34d9148381da8cd207e6a95659b9a3559b99fc7c/purchase_importer/tawreed.py)
- [service.py في مستودع eplus_purchase — commit a5c8572](https://github.com/AnasMahrous/eplus_purchase/blob/a5c8572c3271b88a2cb2848d0a478d2b74d933f7/eplus_purchase/service.py)
- [ui.py في مستودع eplus_purchase — commit a5c8572](https://github.com/AnasMahrous/eplus_purchase/blob/a5c8572c3271b88a2cb2848d0a478d2b74d933f7/eplus_purchase/ui.py)

**عدد الأجزاء التقنية:** 4 · **الجزء الحالي:** 1 · **المتبقي:** 3
