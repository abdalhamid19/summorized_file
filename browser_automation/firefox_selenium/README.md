# التحكم في حاويات Firefox عبر Selenium

`Selenium` أداة للتحكم الآلي بالمتصفح، و`geckodriver` البرنامج الوسيط الذي يربط Selenium بمتصفح Firefox. يحتوي هذا المجلد على متحكم محلي يفتح التبويبات في حاويات Firefox الموجودة في الملف الشخصي المحدد.

## الإعداد

تحتاج الأداة إلى Python وFirefox 138 أو أحدث وإضافة Multi-Account Containers مع الحاويات المطلوبة. أنشئ بيئة Python مستقلة وثبّت اعتماد الأداة:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r browser_automation\firefox_selenium\requirements.txt
```

يستخدم Selenium Manager مدير التعريفات المرفق مع Selenium للعثور على `geckodriver` أو تنزيل نسخة مناسبة عند الحاجة. تُخزّن الملفات التي ينزّلها محليًا خارج المستودع. [توثيق Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/).

## التشغيل

أغلق Firefox الذي يستخدم الملف الشخصي أولًا، ثم شغّل المتحكم مع مسار الملف الشخصي:

```powershell
.\.venv\Scripts\python.exe browser_automation\firefox_selenium\selenium_firefox_control.py --profile "C:\path\to\firefox-profile"
```

إذا لم يعثر Selenium على Firefox تلقائيًا، أضف `--firefox` مع مسار `firefox.exe`:

```powershell
.\.venv\Scripts\python.exe browser_automation\firefox_selenium\selenium_firefox_control.py --profile "C:\path\to\firefox-profile" --firefox "C:\Program Files\Mozilla Firefox\firefox.exe"
```

يقرأ المتحكم أمرًا واحدًا في كل سطر بصيغة `JSON Lines` (كائن JSON مستقل في كل سطر)، ويعيد النتيجة بالطريقة نفسها:

```json
{"action":"list"}
{"action":"open","container":"Personal","url":"https://example.com"}
{"action":"navigate","url":"https://example.com"}
{"action":"quit"}
```

الأوامر المتاحة هي `list` لعرض التبويبات ومعرّفات الحاويات، و`open` لفتح رابط في حاوية، و`navigate` للتنقل في التبويب المحدد، و`quit` لإنهاء جلسة Selenium وإغلاق نافذة Firefox التي بدأها.

## الحاويات والملف الشخصي

تتوقع الأداة أن تكون معرّفات الحاويات في الملف الشخصي المحدد هي Personal=1 وWork=2 وBanking=3 وShopping=4؛ هذه المعرّفات خاصة بالملف الشخصي وليست ثابتة بين كل ملفات Firefox. استخدم `list` للتحقق من معرّفات ملفك، وعدّل جدول `CONTAINERS` في السكربت إذا اختلفت.

لا تضع ملف Firefox الشخصي أو ملفات الجلسة أو ملفات تعريف الارتباط أو مجلد البيئة الافتراضية أو ملفات `geckodriver` في Git. الملف الشخصي يحفظ حالة تسجيل الدخول والبيانات الخاصة. لا تشغّل Selenium والملف نفسه مفتوح في Firefox العادي.

## صلاحية التحكم

يستخدم المتحكم `--allow-system-access` في `geckodriver` لأن فتح تبويب داخل حاوية موجودة يحتاج سياق Firefox الداخلي (`chrome context`، أي واجهة المتصفح نفسها بدل محتوى صفحة الويب). توضح وثائق Mozilla أن هذا الخيار يمنح عميل WebDriver صلاحيات مماثلة لعملية واجهة Firefox، ولذلك أبقِ الأداة و`geckodriver` محليين ولا تعرّضهما للشبكة. [توثيق Mozilla للخيار](https://firefox-source-docs.mozilla.org/testing/geckodriver/Flags.html#allow-system-access) و[توثيق Selenium لسياق Firefox](https://www.selenium.dev/documentation/webdriver/browsers/firefox/#context).

هذه الأداة لا تكتب كلمات مرور أو رموز تحقق ولا تحل `CAPTCHA` (اختبار لتمييز المستخدم البشري من البرنامج الآلي). سجّل الدخول يدويًا في نافذة Firefox العادية. راجع [تقرير رفض تسجيل الدخول إلى Google](../../docs/research/browser/google-signin-automation-error.md) لتفسير الرسالة وخيارات المعالجة.
