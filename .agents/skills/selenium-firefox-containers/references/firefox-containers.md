# فتح تبويبات Firefox داخل الحاويات

## ما الذي تعنيه الحاوية؟

Contextual identity (هوية سياقية) هي حاوية Firefox لها cookieStoreId (معرّف مخزن ملفات الارتباط). تفصل الحاويات ملفات الارتباط عن بعضها داخل ملف Firefox الشخصي نفسه. الحاوية ليست ملف Firefox مستقلًا، ولا يساوي معرّفها window handle (معرّف نافذة أو تبويب WebDriver).

توفّر Mozilla واجهتي إضافة Firefox الأساسيتين:

- browser.contextualIdentities.query() للعثور على الحاويات وإرجاع أسمائها ومعرّفاتها الحالية.
- browser.tabs.create({url, cookieStoreId}) لإنشاء تبويب في مخزن حاوية محدد.

يجب أن يعمل هذا الرمز داخل إضافة Firefox، مثل background script (برنامج خلفي للإضافة). لا يعمل من JavaScript صفحة موقع ولا من driver.execute_script() في Selenium. إذا كانت الميزة غير متاحة أو أعادت الواجهة قائمة فارغة، أوقف المحاولة واشرح أن الحاويات غير مفعّلة أو غير موجودة في ملف Firefox الحالي.

## النمط الموصى به: إضافة وسيطة صغيرة

عندما تكون هناك حاجة لفتح تبويب آليًا في حاوية، اجعل إضافة محلية موثوقة مسؤولة عن عمليات الحاويات، واترك Selenium مسؤولًا عن صفحات الويب. يجب أن تنفّذ الإضافة الخطوات التالية:

1. تستقبل اسم الحاوية والرابط من قناة محلية محددة بوضوح. عند الحاجة إلى طلب/استجابة بين Selenium والإضافة، يمكن تصميم Native Messaging (واجهة رسائل Firefox بين الإضافة وبرنامج محلي)؛ تتطلب صلاحية nativeMessaging وتسجيل برنامج وسيط محلي. لا تستخدم نقطة HTTP محلية مفتوحة بلا مصادقة وضوابط.
2. تتحقق من الرابط وتقبل https أو http فقط، وترفض بيانات الاعتماد المضمّنة في الرابط.
3. تستدعي contextualIdentities.query({}) في كل تشغيل، ثم تطابق الاسم بعد إزالة المسافات وتوحيد حالة الأحرف.
4. تتوقف برسالة واضحة إذا لم تجد الحاوية أو وجدت أكثر من حاوية بالاسم نفسه؛ لا تختَر أول نتيجة بصمت.
5. تستخدم cookieStoreId الذي أعادته الواجهة في tabs.create()، ولا تثبّت معرّفًا رقميًا في إعدادات المهارة.
6. تعيد نتيجة يمكن التحقق منها، مثل معرّف التبويب والرابط وcookieStoreId، دون تسجيل ملفات الارتباط أو بيانات الصفحة الحساسة.

مثال الفكرة داخل كود الإضافة:

~~~javascript
const identities = await browser.contextualIdentities.query({});
const matches = identities.filter(
  (identity) => identity.name.trim().toLowerCase() === requestedName.trim().toLowerCase(),
);

if (matches.length !== 1) {
  throw new Error("Expected one container, found " + matches.length);
}

const tab = await browser.tabs.create({
  url: validatedUrl,
  cookieStoreId: matches[0].cookieStoreId,
  active: true,
});
~~~

هذا المثال يوضح مكان تنفيذ API فقط. requestedName وvalidatedUrl يجب أن يأتيا من قناة الإضافة المحلية بعد التحقق، ولا ينبغي السماح لموقع ويب عشوائي بإرسال أوامر تحكم للمتصفح.

## صلاحيات الإضافة

- استخدام contextualIdentities يتطلب صلاحية "contextualIdentities" في manifest.json (ملف إعداد الإضافة).
- استخدام cookieStoreId عند tabs.create() يتطلب صلاحية "cookies"؛ تشرح MDN أن التبويب المفتوح يستطيع قراءة ملفات الارتباط وتعديلها.
- إذا استُخدم Native Messaging، أضف nativeMessaging فقط عندما تحتاج قناة الإضافة إلى برنامج محلي.
- لا تضف صلاحيات history أو webRequest أو صلاحيات المواقع الواسعة إن لم تكن مطلوبة.
- افحص مصدر الإضافة ومحتواها قبل التثبيت، واشرح للمستخدم سبب صلاحيات ملفات الارتباط قبل الموافقة عليها.

## التحقق بعد الفتح

لا تكتفِ بوجود تبويب جديد. تحقق من الآتي:

1. الإضافة أكدت نجاح tabs.create() وأعادت cookieStoreId المتوقع.
2. Selenium لاحظ التبويب ضمن window_handles (مقابض نوافذ التصفح) وانتقل إلى المقبض الذي يحمل الرابط المطلوب.
3. إذا لم تستطع Selenium تحديد الحاوية من WebDriver، اطلب من الإضافة الاستعلام عن التبويب بواسطة معرّفه ومقارنة cookieStoreId بالهوية التي اختيرت.

معرّف WebDriver ومعرّف إضافة Firefox نوعان مختلفان من المعرّفات. لا تخلط بينهما، ولا تفترض أن كل تبويب فتحته الإضافة ظهر تلقائيًا في جلسة Selenium نفسها. إذا تعذر إثبات الربط بين الجلسة والتبويب، أوقف الخطوات اللاحقة وبيّن القيد.

## خيار احتياطي: واجهة Firefox الداخلية

تتيح Selenium بعض وظائف Firefox الخاصة عبر سياق CHROME. استخدم واجهة السياق الموثقة في نسخة Selenium المثبتة؛ توثيق Python الحالي يعرض driver.context(driver.CONTEXT_CHROME) كمدير سياق يعيد الجلسة إلى CONTENT تلقائيًا بعد الكتلة. بدءًا من Firefox 138 يتطلب اختبار واجهة المتصفح تشغيل geckodriver مع --allow-system-access. تحذر Mozilla من أن هذا يمنح WebDriver صلاحيات عملية Firefox الأم، بما فيها وصول واسع إلى واجهات النظام.

استخدم هذا المسار فقط عند تعذر الإضافة الوسيطة، وعلى جهاز محلي وملف شخصي مخصص. احصر السياق المرتفع في أقل عدد من الأوامر، واستخدم مدير السياق كي يعود تلقائيًا إلى CONTENT. واجهات Firefox الداخلية مثل gBrowser أو openWebLinkIn ليست عقدًا عامًا ثابتًا؛ تحقق منها على إصدار Firefox الفعلي ولا تجعلها افتراضًا عامًا أو أساسًا للاعتماد طويل الأجل.

## المصادر الرسمية

- [Mozilla: العمل مع الهويات السياقية](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Work_with_contextual_identities)
- [MDN: contextualIdentities API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities)
- [MDN: tabs.create()](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/tabs/create)
- [MDN: Native Messaging](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging)
- [Selenium: وظائف Firefox الخاصة](https://www.selenium.dev/documentation/webdriver/browsers/firefox/)
- [Mozilla: خيارات geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/Flags.html)
