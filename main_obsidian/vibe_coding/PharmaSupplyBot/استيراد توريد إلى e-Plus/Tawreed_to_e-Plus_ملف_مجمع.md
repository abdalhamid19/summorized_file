---
title: "استيراد طلبات Tawreed إلى e-Plus - ملف مجمع"
date: 2026-09-26
tags: [PharmaSupplyBot, Tawreed, e-Plus, integration, compiled]
aliases: ["شرح استيراد بيانات Tawreed إلى e-Plus"]
---

# استيراد طلبات Tawreed إلى e-Plus — ملف مجمع

> [!abstract] نطاق الملف
> يجمع الشرح التقني للأجزاء [[01 - من Tawreed إلى تفاصيل الطلب والأسماء]] إلى [[04 - Dry-run وApply والكتابة في e-Plus]]. المصدر كود التطبيق، وليس تسجيلًا؛ لذلك لا توجد نصوص متحدث أو توقيتات.

## فهرس الأجزاء

1. [[#1. جلب الطلب والأسماء من Tawreed|جلب الطلب والأسماء من Tawreed]]
2. [[#2. قراءة بيانات المورد والصنف من e-Plus|قراءة بيانات e-Plus والمطابقة]]
3. [[#3. بناء الفاتورة والتحقق من الحسابات|بناء الفاتورة والتحقق]]
4. [[#4. Dry-run وApply والكتابة|Dry-run والكتابة الفعلية]]

## 1. جلب الطلب والأسماء من Tawreed

يبدأ التطبيق بتحميل قائمة الطلبات من `rest/v2/orders/purchase/search`. تعرض القائمة معرّف الطلب والمورد والتاريخ والإجمالي والحالة. عند اختيار الطلب، تُجلب التفاصيل من `rest/v2/orders/purchase/get`.

يحتوي سطر الطلب على معرّف المنتج `productId` ومعرّف منتج المورد `storeProductId`، والاسم `productName`، ونص اسم المورد `storeProductName`، والكمية `quantity` والسعر قبل الخصم `retailPrice` والسعر الصافي `salePrice` والخصم `discountPercent` وإجمالي السطر `itemTotal`.

لجلب الاسم الإنجليزي الرسمي، يرسل التطبيق معرّف المنتج إلى `POST /rest/v2/products/get`، ويقرأ `productName` و`productNameEn`. الاسم لا يُترجم آليًا. ويُعرض اسم المورد مستقلاً لأن المورد قد يسجل وصفًا مختصرًا مختلفًا عن الاسم الرسمي.

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

## 2. قراءة بيانات المورد والصنف من e-Plus

اتصال قاعدة e-Plus يتم عبر SQL Server في كود `purchase_importer/erp.py` باستخدام `pymssql`. جدول كتالوج الصنف هو `Item_Catalog`. سجل الصنف المحلول يعرض `itm_id` و`itm_code` و`itm_code2` واسميه العربي والإنجليزي و`com_id` وسعر البيع `sell_price`.

يحاول `eplus_purchase/build.py:resolve_line` حل الصنف بهذا الترتيب:

1. البحث عن رابط في قاعدة المطابقات المحلية `tawreed_product_map` حسب Tawreed `productId`، أو مفتاح الاسم العربي إذا لم يوجد المعرّف.
2. محاولة قائمة المطابقات المعروفة.
3. المطابقة التقريبية على بيانات الكتالوج المتاحة.
4. جلب سجل الصنف المختار من e-Plus بواسطة كوده.

~~~python
map_key = str(product_id) if product_id else f"name:{normalize(name_ar)}"
mapping = product_map.resolve_product(db_path, map_key)

if mapping and mapping.get("erp_itm_code"):
    item = erp.get_item_by_code(mapping["erp_itm_code"])
~~~

يُحل المورد بشكل مستقل عبر `vendor_map.resolve_vendor`، الذي يربط اسم متجر Tawreed بمعرّف المورد `ven_id` في e-Plus.

في معاينة الطلب `3053985` رُبط منتج Tawreed `126077` بكود e-Plus `92260`. وكان المورد `ven_id=735`. نتيجة المعاينة كانت `PASS` و`5/5` أصناف مطابقة. لا تعني هذه المعاينة إنشاء فاتورة.

## 3. بناء الفاتورة والتحقق من الحسابات

بعد حل الصنف، يبني `eplus_purchase/build.py` سطر `PendingBillLine`. حقول تعريف الصنف والشركة وسعر البيع الحالي تأتي من `ItemRow`، بينما الكمية وسعر الوحدة والخصم تأتي من طلب Tawreed.

~~~python
PendingBillLine(
    erp_itm_id=item_row.itm_id,
    erp_itm_code=item_row.itm_code,
    qnty=int(line.quantity or 0),
    itm_cost=float(line.retail_price or 0),
    itm_pur_price=float(line.sale_price or 0),
    itm_sell=float(item_row.sell_price or 0) or float(line.sale_price or 0),
    itm_dis_per=float(line.discount_percent or 0),
    c_id=item_row.com_id,
)
~~~

يفحص `verify.verify_bill` السطور ويكوّن `LineCheck` يتضمن الكميات والأسعار والخصومات والأسماء وأكواد الصنف ونتيجة المطابقة. يراجع البرنامج إجمالي السطر كما أرسله Tawreed مقابل الحساب:

> **الإجمالي المحسوب للسطر = الكمية × سعر الشراء الصافي للوحدة**

كما يجمع إجماليات البنود ويقارنها بإجمالي تفاصيل الطلب. سعر البيع الحالي من e-Plus يظهر للمقارنة، ولا يدخل في حساب إجمالي شراء الفاتورة. الحالات تشمل `PASS` و`PARTIAL` و`FAIL` و`NO_VENDOR`؛ وتُحجب الفاتورة الجزئية افتراضيًا.

في معاينة الطلب `3053985` ظهر المورد `ven_id=735`، والحالة `PASS` وعدد المطابق `5/5`. أحد الأسطر ربط Tawreed `126077` بـe-Plus `92260`:

| الحقل | القيمة |
|---|---|
| الاسم العربي من Tawreed | الوكيتا ليف ان كريم للشعر 120 جم |
| الاسم الإنجليزي الرسمي | ALOEKITA LEAVE IN CREAM 120 GM |
| اسم المورد | الوكيتا كريم ازرق |
| كود الصنف في e-Plus | `92260` |

لا تتضمن عينة المعاينة التي وثقناها كمية أو سعر هذا السطر، لذلك لم تُضف لهما أرقام تقديرية.

## 4. Dry-run وApply والكتابة

ينفذ `Dry-run` الجلب والمطابقة والتحقق ويعرض ما كان سيُكتب، لكنه يتوقف قبل إدخال فاتورة في e-Plus:

~~~python
if not apply:
    print("  (dry-run: NOT writing to ERP)")
    return None
~~~

قد يحفظ التطبيق سجل تدقيق أو رابط مطابقة في قاعدة SQLite المحلية. هذا لا يعني أنه تم إدخال فاتورة في e-Plus.

عند الضغط على `Apply` وتأكيده، يتصل `erp_write.insert_pending_bill` بـSQL Server ويكتب:

| جدول e-Plus | الدور |
|---|---|
| `pur_trans_h` | رأس فاتورة الشراء: المورد والفرع والتاريخ/الرقم والعدد والإجمالي والحالة |
| `pur_trans_d` | سطور الفاتورة: الصنف والكمية والأسعار والخصم وحقول الوحدة والمخزون |

ينشئ SQL Server `pth_id`، ويربط به سطور التفاصيل. وتُنفذ الكتابة في معاملة واحدة؛ نجاحها ينتهي بـ`commit` وأي فشل يؤدي إلى `rollback`. الفاتورة الناتجة معلّقة وغير مدفوعة بحسب حقول الكود `bill_status=1` و`pth_paid=0`.

سعر البيع الحالي من e-Plus لا يحل محل سعر الشراء القادم من Tawreed. وبعض حقول لقطة المخزون تُقرأ من قاعدة الكتالوج المحلية `catalog.db`.

## الخلاصة العملية

`productId` من Tawreed يقود إلى كود e-Plus عبر جدول الربط أو مراحل المطابقة. يقرأ التطبيق سجل الصنف والمورد لإكمال بيانات الفاتورة، ثم يتحقق من الكميات والأسعار قبل الإرسال. لا تحدث كتابة فاتورة e-Plus في Dry-run؛ يتطلب الأمر Apply وتأكيده.

## مصادر الكود

- [tawreed-importer: tawreed.py](https://github.com/AnasMahrous/tawreed-importer/blob/34d9148381da8cd207e6a95659b9a3559b99fc7c/purchase_importer/tawreed.py)
- [tawreed-importer: erp.py](https://github.com/AnasMahrous/tawreed-importer/blob/34d9148381da8cd207e6a95659b9a3559b99fc7c/purchase_importer/erp.py)
- [tawreed-importer: vendor_map.py](https://github.com/AnasMahrous/tawreed-importer/blob/34d9148381da8cd207e6a95659b9a3559b99fc7c/purchase_importer/vendor_map.py)
- [eplus_purchase: build.py](https://github.com/AnasMahrous/eplus_purchase/blob/a5c8572c3271b88a2cb2848d0a478d2b74d933f7/eplus_purchase/build.py)
- [eplus_purchase: verify.py](https://github.com/AnasMahrous/eplus_purchase/blob/a5c8572c3271b88a2cb2848d0a478d2b74d933f7/eplus_purchase/verify.py)
- [eplus_purchase: service.py](https://github.com/AnasMahrous/eplus_purchase/blob/a5c8572c3271b88a2cb2848d0a478d2b74d933f7/eplus_purchase/service.py)
- [eplus_purchase: erp_write.py](https://github.com/AnasMahrous/eplus_purchase/blob/a5c8572c3271b88a2cb2848d0a478d2b74d933f7/eplus_purchase/erp_write.py)
