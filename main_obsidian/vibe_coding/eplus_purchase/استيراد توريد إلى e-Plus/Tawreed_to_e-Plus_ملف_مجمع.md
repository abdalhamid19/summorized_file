---
title: "استيراد طلبات Tawreed إلى e-Plus - ملف مجمع"
date: 2026-09-26
tags: [eplus_purchase, Tawreed, e-Plus, integration, compiled]
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

## 2. قراءة بيانات e-Plus وحل هوية الصنف

يملك التطبيق موائم القراءة في <code>eplus_purchase/erp.py</code>. يقرأ سجل الصنف من <code>Item_Catalog</code> ويحمل <code>itm_id</code> و<code>itm_code</code> واسمي ERP العربي والإنجليزي و<code>com_id</code> وسعر البيع الحالي. يستخدم المطابق أيضًا قاعدة كتالوج محلية للأصناف النشطة لاسترجاع مرشحين، مع بحث ERP بديل عند الحاجة.

يحل <code>build.resolve_line</code> السطر بهذا الترتيب:

1. قرار مراجعة محفوظ للمفتاح ونطاق سلعة المورد وبصمة الاسم الحالية.
2. خريطة <code>tawreed_product_map</code> ذات علامة اعتماد بشرية ونطاق إدراج مطابق، إذا لم يوجد قرار مراجعة.
3. مصادر مطابقة منسقة: قرارات مراجعة معتمدة، و<code>data/confirmed_matches.csv</code> الاختياري، ثم الاتجاه المعكوس لملف <code>known_matches.csv</code>. أي تعارض في الهوية يمنع اختيار كود تلقائي.
4. بحث fuzzy وتقييم التوافق؛ لا يقبل أفضل مرشح آليًا إلا عند بلوغ 0.90، وعدم طلب مراجعة، وفارق 0.05 على الأقل عن الثاني إن وجد.

التفصيل مقسم إلى [[مطابقة الأصناف/01 - هوية الصنف ومصادر المرشحين]] و[[مطابقة الأصناف/02 - ترتيب حل الصنف والمطابقات المنسقة]] و[[مطابقة الأصناف/03 - بوابة التوافق والدرجة والقبول]] و[[مطابقة الأصناف/04 - المراجعة اليدوية والحفظ وآثار التشغيل]]. المورد يحل بصورة مستقلة عبر <code>vendor_map</code> إلى <code>ven_id</code>.

في بعض معاينات الإصدار السابق للشرح، ورد المثال <code>productId=126077</code> و<code>itm_code=92260</code>. هذه إحالة تاريخية إلى معاينة سابقة لا نعيد التحقق منها هنا ولا نستخدمها لإثبات سلوك بيانات الإصدار الحالي.
## 3. بناء الفاتورة والتحقق من الحسابات

> [!note] مصدر المثال
> بيانات الطلب <code>3053985</code> مأخوذة من معاينة موثقة في حزمة إصدار سابق. لم نعد تشغيلها؛ لا تستخدمها بوصفها نتيجة للنسخة الحالية أو لقاعدة إنتاج حالية.

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

في معاينة سابقة موثقة للطلب `3053985` ظهر المورد `ven_id=735`، والحالة `PASS` وعدد المطابق `5/5`. أحد الأسطر ربط Tawreed `126077` بـe-Plus `92260`:

| الحقل | القيمة |
|---|---|
| الاسم العربي من Tawreed | الوكيتا ليف ان كريم للشعر 120 جم |
| الاسم الإنجليزي الرسمي | ALOEKITA LEAVE IN CREAM 120 GM |
| اسم المورد | الوكيتا كريم ازرق |
| كود الصنف في e-Plus | `92260` |

لا تتضمن عينة المعاينة التي وثقناها كمية أو سعر هذا السطر، لذلك لم تُضف لهما أرقام تقديرية.



## 4. Dry-run وApply والكتابة

في CLI، ينفذ Dry-run جلب الطلب والمطابقة والتحقق، ويمرر سياسة <code>store_matches=False</code> و<code>queue_unresolved=False</code>. تعيين <code>apply=False</code> في <code>erp_write.insert_pending_bill</code> يوقف المسار قبل إدخالات SQL إلى e-Plus. تسجل خدمة CLI النتيجة المحلية بحالة <code>dry_run</code> في <code>tawreed_imported_orders</code>؛ هذا سجل تدقيق محلي وليس فاتورة.

تستخدم المعاينة في واجهة Streamlit أيضًا سياسة بلا حفظ للمطابقات أو طابور المراجعة. في المقابل، شاشة Item Mapping تستعمل bootstrap بإعداد افتراضي يسمح بحفظ المطابقات المؤهلة في SQLite وطابور الأصناف غير المحلولة.

عند Apply، تسمح السياسة بتخزين بعض المصادر المنسقة وتضع غير المحلول للمراجعة قبل التحقق من بوابة الفاتورة. لذلك قد تبقى آثار محلية حتى لو حُجب إنشاء الفاتورة لاحقًا بسبب PARTIAL؛ وهذا لا يعني أن e-Plus استقبل الفاتورة.

عند اجتياز بوابة Apply وتأكيده، يكتب التطبيق داخل معاملة SQL Server واحدة:

| جدول e-Plus | الدور |
|---|---|
| <code>pur_trans_h</code> | رأس الفاتورة: المورد والفرع والتاريخ والرقم والحالة والإجمالي |
| <code>pur_trans_d</code> | سطور الأصناف: الكود والكمية والأسعار والخصم والحقول المرتبطة |

يُنشأ <code>pth_id</code> للرأس وتربط به التفاصيل. نجاح المعاملة ينتهي بـ<code>commit</code> والفشل يؤدي إلى <code>rollback</code>. السجل المضاف معلق وغير مدفوع حسب <code>bill_status=1</code> و<code>pth_paid=0</code>.


## الخلاصة العملية

يبدأ حل السطر بقرار مراجعة مطابق لهوية المصدر، ثم خريطة ذات اعتماد بشري، ثم المصادر المنسقة، ثم المرشحين التقريبيين. لا يُبنى سطر الفاتورة من مرشح غير مقبول آليًا أو بشريًا. بعد ذلك يفحص التطبيق الحسابات؛ ولا تُكتب الفاتورة في e-Plus إلا عبر Apply وتأكيده.

## مصادر الكود

روابط التنفيذ مثبتة على نسخة المستودع التي تمت مراجعتها (<code>b9bb6ef987d86e272c4022a2ea07d8144cf121ad</code>):

- [tawreed.py — واجهات الطلب وأسماء المنتجات](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/tawreed.py)
- [erp.py — قراءة كتالوج e-Plus](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/erp.py)
- [build.py — بناء الفاتورة وحل الصنف](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/build.py)
- [matcher.py — استرجاع المرشحين وفحص التوافق والترتيب](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/matcher.py)
- [manual_review.py — قرارات المراجعة وسجلها](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/manual_review.py)
- [verify.py — تحقق سطور الفاتورة](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/verify.py)
- [service.py — تنسيق المعاينة وApply](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/service.py)
- [erp_write.py — الكتابة في قاعدة ERP](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/erp_write.py)
- [storage.py — جداول SQLite المحلية](https://github.com/AnasMahrous/eplus_purchase/blob/b9bb6ef987d86e272c4022a2ea07d8144cf121ad/eplus_purchase/storage.py)

لم نعاين قاعدة الإنتاج ولا بيانات ملفات المطابقة الخادمية أو ملف <code>confirmed_matches.csv</code> المحلي.
