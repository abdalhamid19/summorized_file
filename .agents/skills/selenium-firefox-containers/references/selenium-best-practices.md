# ممارسات Selenium وgeckodriver مع Firefox

## الإصدارات وتشغيل الجلسة

- استخدم إصدار Selenium 4 حديثًا مع Firefox مدعوم. إذا لم تُحدد مسار geckodriver، اترك Selenium Manager يحاول العثور على نسخة متوافقة أو تنزيلها؛ لا تضف ملف تعريف ثابتًا إلى Git.
- حدّد binary_location فقط إذا كان على الجهاز أكثر من Firefox أو لم يعثر Selenium على النسخة المطلوبة.
- استخدم Firefox Service (مشغّل geckodriver الذي تديره Selenium) وسجّل إصدار Firefox وgeckodriver عند تشخيص مشكلة، من دون تضمين أسرار.
- أنشئ جلسة واحدة واضحة للمهمة. استخدم try/finally واستدعِ driver.quit() لإغلاق كل نوافذ جلسة WebDriver التي بدأتها.
- driver.close() يغلق نافذة التصفح الحالية فقط؛ لا تستخدمه بديلًا عن quit() عند إنهاء الجلسة.

مثال تشغيل بسيط؛ استدعاء Firefox عبر Selenium Manager افتراضيًا، وانتظار اكتمال التحميل بشرط محدد، ثم إغلاق الجلسة التي أنشأها السكربت:

~~~python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
try:
    driver.get("https://example.org")
    WebDriverWait(driver, 15).until(
        lambda browser: browser.execute_script("return document.readyState") == "complete"
    )
    print(driver.capabilities.get("browserVersion"))
    print(driver.capabilities.get("moz:geckodriverVersion"))
finally:
    driver.quit()
~~~

binary_location خيار يحدد ملف Firefox التنفيذي عند الحاجة. لا تضبطه ما دام Selenium يجد النسخة الصحيحة.

## ملفات Firefox الشخصية

- إذا احتاجت المهمة جلسة محفوظة، حدّد ملفًا شخصيًا مخصصًا أو الملف الذي اختاره المستخدم. لا تستخدم ملفه اليومي دون طلب صريح.
- لا تشغّل الملف الشخصي نفسه في Firefox العادي وفي Selenium في الوقت نفسه؛ قد يمنع Firefox ذلك أو تتضرر بيانات الملف.
- لا تفترض أن driver.quit() يحفظ الجلسة: geckodriver يستخدم ملفًا مؤقتًا افتراضيًا عادة. تحقّق من moz:profile ضمن قدرات الجلسة عند الحاجة إلى التأكد من الملف الذي بدأه Firefox.
- لا تنسخ مجلد الملف الشخصي، ولا ترفع cookies.sqlite أو logins.json أو قواعد بيانات الجلسات أو لقطات شاشة تتضمن رموزًا إلى Git أو سجلات مشتركة.
- لا تُنهِ عمليات Firefox الموجودة بالقوة لإخلاء ملف شخصي. دع المستخدم يغلقها، أو أنشئ ملفًا آخر معزولًا.

## انتظار وتحديد العناصر

- استخدم WebDriverWait مع expected_conditions (شروط جاهزة للانتظار) أو شرط واضح، مثل ظهور العنصر أو تغيّر عنوان الصفحة.
- تجنب time.sleep() إلا لتشخيص عابر. ولا تجمع implicit wait (انتظار ضمني) مع explicit wait (انتظار صريح)، لأن الجمع قد ينتج أزمنة انتظار يصعب توقعها.
- فضّل محددات مستقرة: id أو name أو أسماء الوصول مثل aria-label. تجنب محددات XPath طويلة مرتبطة ببنية الصفحة المؤقتة.
- بعد التنقل أو فتح تبويب، أعد فحص المقابض والعناصر؛ لا تحتفظ بمراجع قديمة إلى عناصر من صفحة سابقة.

## استخدام سياق واجهة Firefox

- الأفضل أن تنفذ Selenium أوامر الصفحات في content، وأن تستخدم واجهة إضافة Firefox الرسمية لأعمال الحاويات.
- لا تنتقل إلى CHROME إلا لعمل محلي محدد يتطلب واجهة المتصفح. بدءًا من Firefox 138 يحتاج هذا إلى geckodriver --allow-system-access، وهو يرفع صلاحيات WebDriver بشكل كبير. استخدم مدير السياق الموثق في Selenium لتعود الجلسة إلى CONTENT تلقائيًا بعد كتلة التحكم الداخلية.
- لا تعرض خدمة WebDriver على الشبكة. الإعداد الافتراضي لـgeckodriver هو 127.0.0.1؛ لا تضف --allow-origins أو --allow-hosts دون حاجة مبررة.
- اجعل سجلات debug (تفاصيل تشخيصية) وtrace (تفاصيل شديدة التفصيل) مؤقتة عند التشخيص فقط، وراجعها قبل مشاركتها لأن عناوين الصفحات ومحتوى الطلبات قد يكون حساسًا.

## حدود تسجيل الدخول

- لا تضع كلمات المرور أو رموز التحقق في الشيفرة أو الأوامر أو السجلات. اسمح للمستخدم بإدخالها يدويًا.
- عند ظهور CAPTCHA أو رسالة رفض أمان من مزود الحساب، لا تستخدم أدوات التخفي أو تجاوز التحقق. أوقف الأتمتة عند تلك الخطوة واتركها للمستخدم أو استخدم تكامل OAuth رسميًا إذا كان مناسبًا.
- إذا كانت الخدمة ترفض WebDriver، لا تدّعِ أن تعديل User-Agent أو إخفاء الأتمتة حل مدعوم. سجّل رسالة الخطأ غير الحساسة واشرح المسار الرسمي المتاح، مثل OAuth (تفويض آمن بين الخدمات) إذا كان متوفرًا.

## توثيق Selenium وMozilla

- [Selenium: Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/)
- [Selenium: استراتيجيات الانتظار](https://www.selenium.dev/documentation/webdriver/waits/)
- [Selenium: النوافذ وعلامات التبويب](https://www.selenium.dev/documentation/webdriver/interactions/windows/)
- [Selenium: وظائف Firefox الخاصة](https://www.selenium.dev/documentation/webdriver/browsers/firefox/)
- [Mozilla: ملفات Firefox في geckodriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/Profiles.html)
- [Mozilla: حماية واجهة WebDriver عن بُعد](https://firefox-source-docs.mozilla.org/remote/Security.html)
- [Mozilla: سجلات geckodriver التفصيلية](https://firefox-source-docs.mozilla.org/testing/geckodriver/TraceLogs.html)
