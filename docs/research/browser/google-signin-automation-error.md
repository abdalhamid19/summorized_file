# رسالة Google: “This browser or app may not be secure”

**تاريخ التحقق:** 14 أكتوبر 2026
**النطاق:** تفسير رسالة رفض تسجيل الدخول الظاهرة في الصورة، في سياق Firefox الذي جرى تشغيله والتحكم به عبر Selenium وgeckodriver. أُدخل عنوان الحساب إلى النموذج وظهرت رسالة الرفض؛ لم تُدخل كلمة مرور أو رمز تحقق، ولم نغيّر إعدادات الحساب أو نحاول تجاوز الرفض.

## الخلاصة

Firefox متصفح مدعوم لتسجيل الدخول إلى Google. لكن صفحة مساعدة Google تذكر صراحةً أن تسجيل الدخول قد يُمنع عندما يتحكم بالمتصفح برنامج أتمتة بدلًا من شخص. لذلك، وبالنظر إلى أن Firefox في هذه الجلسة كان يُدار عبر **Selenium** (أداة تحكم آلي بالمتصفح) و**geckodriver** (مشغّل Selenium الخاص بـFirefox)، فهذا هو **السبب الأرجح** للرسالة.

هذا ترجيح وليس تشخيصًا مؤكدًا: الصورة وحدها لا تحدد السبب. تذكر Google احتمالات أخرى، منها تعطيل JavaScript، أو إضافة غير آمنة/غير مدعومة، أو إعداد خصوصية صارم، أو برنامج أمان/Proxy يتدخل في الاتصال. كذلك لا يوجد في المصادر الرسمية التي راجعتها ما يثبت أن إضافة **Multi-Account Containers** نفسها هي السبب.

## ما تقوله Google رسميًا

1. في صفحة [تسجيل الدخول باستخدام متصفح مدعوم](https://support.google.com/accounts/answer/7675428?co=GENIE.Platform%3DDesktop&hl=en)، تسرد Google المتصفحات المدعومة ومنها Firefox، وتقول إنها قد تمنع تسجيل الدخول إذا كان المتصفح يتحكم به برنامج أتمتة، أو كانت JavaScript متوقفة، أو أضيفت إليه إضافات غير آمنة أو غير مدعومة، أو كان مضمّنًا داخل تطبيق آخر.
2. الصفحة نفسها تقترح، عند وجود مشكلة: التأكد من تشغيل JavaScript، تحديث المتصفح، فحص الإضافات، ومراجعة إعدادات الخصوصية. إذا كانت الخصوصية على مستوى “High” أو “Strict”، تذكر Google السماح للموقع `www.google.com`. وتوصي بفحص تأثير Firewall أو Proxy أو Antivirus، ثم الرجوع إلى دعم البرنامج إذا ثبت أنه يتدخل.
3. في [سياسات OAuth 2.0](https://developers.google.com/identity/protocols/oauth2/policies)، تمنع Google مطوّر التطبيق من توجيه طلب تفويض Google إلى متصفح مضمّن يتحكم به التطبيق، وتطلب أن يستطيع المستخدم التحقق من عنوان Google واتصال HTTPS.
4. في [دليل تطبيقات سطح المكتب](https://developers.google.com/identity/protocols/oauth2/native-app)، توضح Google أن التطبيق المثبّت الذي يحتاج تفويضًا للوصول إلى Google APIs يفتح **متصفح النظام** لإجراء OAuth 2.0 (طريقة تفويض تسمح للمستخدم بمنح التطبيق صلاحيات محددة دون إعطائه كلمة المرور). هذا مسار للمطوّرين لتفويض تطبيق، وليس طريقة لتسجيل الدخول إلى واجهة Gmail عبر Selenium.
5. وتشرح [إرشادات Google للمطوّرين بشأن المتصفحات الأقل أمانًا](https://developers.googleblog.com/en/guidance-to-developers-affected-by-our-effort-to-block-less-secure-browsers-and-applications/) أن برامج أتمتة النقرات أو ضغطات المفاتيح، خصوصًا لتسجيل الدخول التلقائي، غير مقبولة لتسجيل الدخول. وتوضح أيضًا عدم انتحال **User-Agent** (النص الذي يعرّف نوع المتصفح للموقع) بصفة متصفح آخر.

## ما يربط الرسالة بجلسة Selenium الحالية

1. يشرح [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webdriver) أن `navigator.webdriver` (علامة يعلن بها المتصفح للصفحة أنه تحت تحكم WebDriver) تكون `true` في Firefox عند تشغيل Marionette أو تفعيله في الإعدادات.
2. فحص العملية المحلية في ذلك التشغيل أظهر أن Firefox كان يعمل بخيار `--marionette` وتحت عملية `geckodriver`. هذا يتطابق مع فئة الأتمتة التي تحذر منها Google. لا تكشف صفحة الخطأ وحدها الإشارة الدقيقة التي أدت إلى قرار Google، لذلك يظل هذا تفسيرًا مرجحًا جدًا لا إثباتًا لآلية الكشف الداخلية.
3. [توثيق Selenium نفسه](https://www.selenium.dev/documentation/test_practices/discouraged/gmail_email_and_facebook_logins/) لا يوصي بتسجيل الدخول إلى Gmail عبر WebDriver؛ ويذكر عدم الموثوقية واحتمال مخالفة شروط المواقع وتعطيل الحساب، وينصح باستخدام واجهة Gmail البرمجية بدل ذلك.

## حالة الجلسة عند إعداد التقرير

بعد انتهاء محاولة التحكم، أُغلقت جلسة Selenium طبيعيًا وأُعيد تشغيل Firefox مباشرةً على ملف المستخدم نفسه، دون `geckodriver` أو `--marionette`. وصل Firefox إلى صفحة Gmail، وكان تبويب تسجيل الدخول داخل Personal وفق سجل الجلسة. لم تُدخل كلمة مرور أو رمز تحقق، لذلك كان يلزم أن يستكمل المستخدم تسجيل الدخول بنفسه.

## الحل العملي المتوافق مع هذه الإرشادات

1. أوقف التحكم الآلي في صفحة تسجيل الدخول. أغلق جلسة Selenium إغلاقًا طبيعيًا، ثم افتح ملف Firefox المستخدم في الجلسة مباشرةً، من دون Selenium أو Playwright أو سكربت يتحكم بالنقر والكتابة.
2. سجّل الدخول يدويًا في Firefox المدعوم، وأكمل أي تحقق أمني بنفسك. لا ترسل كلمة المرور أو رموز التحقق إلى أي شخص أو أداة.
3. إذا استمرت الرسالة في Firefox العادي غير المُدار آليًا، اتبع فحوص Google الرسمية بالترتيب: حدّث Firefox، تأكد من JavaScript، عطّل مؤقتًا الإضافات التي لا تحتاجها للاختبار، ثم راجع إعداد الخصوصية. أبقِ إضافة الحاويات إذا كنت تحتاجها؛ لا يوجد في المصدر ما يحددها سببًا. إذا كانت الخصوصية على “High/Strict”، جرّب إضافة `www.google.com` إلى قائمة السماح كما توصي Google.
4. إذا لم ينجح ذلك، افحص ما إذا كان Firewall أو Proxy أو Antivirus يتدخل. توصي Google باختبار مؤقت ثم إعادة تفعيل الحماية، والتواصل مع دعم البرنامج إذا كان هو السبب. على جهاز عمل أو مدرسة، اسأل المسؤول عن السياسة.
5. إذا كان الغرض ربط **تطبيق** بخدمات Google، فاستخدم OAuth 2.0 بالطريقة الرسمية ومتصفح النظام وموافقة المستخدم على صلاحيات محدودة. لا تستخدم أتمتة واجهة Gmail لهذا الغرض.

قد تبقى جلسة الحساب محفوظة في ملف Firefox نفسه بعد تسجيل دخول يدوي، لكن لا تضمن Google في المصادر المذكورة قبول إعادة المصادقة أو استمرار الوصول عندما يعود Selenium للتحكم في المتصفح. تعامل مع تسجيل الدخول نفسه على أنه إجراء يدوي داخل متصفح غير مؤتمت.

## ما لا يثبته الدليل وما ينبغي تجنبه

- لا تثبت الرسالة أن كلمة المرور خطأ أو أن الحساب معطّل.
- لا تثبت وحدها أن إضافة الحاويات هي السبب؛ Google لا تسميها تحديدًا.
- لا تستخدم إضافة **stealth** أو تعديل User-Agent أو إخفاء علامات الأتمتة أو حل CAPTCHA لإجبار صفحة تسجيل الدخول على قبول Selenium. هذا لا يعالج السبب وفق إرشادات Google، ويتعارض مع توجيهها بعدم أتمتة تسجيل الدخول.
- لا أجد في وثائق Google الرسمية التي راجعتها إعدادًا يسمح للمستخدم بإضافة Selenium إلى قائمة استثناءات تسجيل الدخول.

## المصادر

- [Google Account Help — Sign in with a supported browser](https://support.google.com/accounts/answer/7675428?co=GENIE.Platform%3DDesktop&hl=en)
- [Google for Developers — OAuth 2.0 Policies](https://developers.google.com/identity/protocols/oauth2/policies)
- [Google for Developers — OAuth 2.0 for iOS & Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app)
- [Google Developers Blog — Guidance to developers affected by blocking less secure browsers and applications](https://developers.googleblog.com/en/guidance-to-developers-affected-by-our-effort-to-block-less-secure-browsers-and-applications/)
- [MDN — `Navigator.webdriver`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/webdriver)
- [Selenium — Gmail, email and Facebook logins](https://www.selenium.dev/documentation/test_practices/discouraged/gmail_email_and_facebook_logins/)
- [Google for Developers — Gmail API overview](https://developers.google.com/workspace/gmail/api/guides)
