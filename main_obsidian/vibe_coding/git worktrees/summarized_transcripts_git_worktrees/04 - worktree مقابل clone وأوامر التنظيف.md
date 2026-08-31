# 04 - worktree مقابل clone وأوامر التنظيف

## 📌 الملخص العلمي

### لماذا لا تنشئ مجلدًا وتعمل clone للمستودع ([[repo]])؟

يمكن ذلك فعلًا، لكن [[git worktree]] أفضل لأنه:

| وجه المقارنة | git worktree | clone جديد |
|--------------|--------------|------------|
| مشاركة الموارد | يشارك نفس مستودع Git الأساسي فلا انتظار تنزيل ([[clone]]) | ينسخ المستودع كاملًا من جديد |
| التحديث مع الـ remote | يبقي الفروع محدّثة مع التغييرات على الـ remote | كل نسخة منعزلة |
| السرعة والنظافة | أنظف وأسرع عمومًا | أبطأ وأثقل |

### أوامر التنظيف

| الأمر | الوظيفة | التوقيت |
|-------|---------|---------|
| `git worktree remove <path>` | حذف مجلد الـ worktree | بعد رفع ([[push]]) العمل إلى GitHub والانتهاء منه |
| `git worktree prune` | تنظيف الفروع القديمة الراكدة (stale) التي أنشأتها سابقًا | صيانة دورية |

> ⚠️ **تنبيه:** `git worktree remove` يُستخدم فقط **بعد** التأكد من دفع كل عملك إلى GitHub — وإلا قد تضيع تغييرات.

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** النص الأصلي «get worksheet remove» خطأ تحويل صوتي والمراد `git worktree remove`. كما أن المتحدث لم يذكر صراحةً أن `prune` يحذف سجلات worktrees المحذوفة يدويًا — اكتفى بوصفها «تنظيف الفروع القديمة».

## نص المتحدث الكامل

So you might really ask yourself why can't I just create a folder and clone the repo again and work and you can absolutely do that but in this way it's sharing a lot of the resources so you don't have to wait for it to download that clone anymore Moreover it keeps both branches up to date with any changes that happen on the remote So generally it's just a bit cleaner a little bit faster Some other useful commands is get worksheet remove and then the path to the folder that you created earlier This will just remove it once you've obviously pushed it up to GitHub and you've done everything you need to do Another one is Git Work Tree Prune which will clean up any stale branches that you've made in the past So subscribe to my channel if you found it useful or if you want to hear more claw code tips

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** أخطاء تحويل صوتي: `get worksheet remove` = `git worktree remove`، `Git Work Tree Prune` = `git worktree prune`، `claw code` = `Claude Code`.

---

- 📦 **عدد الأجزاء:** 4 (+ ملف خطة تطبيقية)
- ✅ **الجزء الحالي:** 04 (الأخير)
- ⏳ **الأجزاء المتبقية:** 1 (خطة العمل التطبيقية)
