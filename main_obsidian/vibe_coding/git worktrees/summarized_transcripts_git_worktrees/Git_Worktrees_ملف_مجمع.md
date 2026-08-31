# Git Worktrees for Multi-Agent Claude Code Workflows - ملف مجمع

> 📦 **الملف المجمع النهائي** — يجمع محتوى جميع أجزاء فيديو "Git Worktrees for Multi-Agent Claude Code Workflows" في ملف واحد: الملخص العلمي المنظّم + نص المتحدث الكامل.

## 📑 فهرس الأجزاء

1. [[#الجزء 1 – المشكلة: القفل أثناء المهام الطويلة|الجزء 1 – المشكلة: القفل أثناء المهام الطويلة]]
2. [[#الجزء 2 – الحل: إنشاء git worktree|الجزء 2 – الحل: إنشاء git worktree]]
3. [[#الجزء 3 – الأتمتة عبر Warp agent mode|الجزء 3 – الأتمتة عبر Warp agent mode]]
4. [[#الجزء 4 – worktree مقابل clone وأوامر التنظيف|الجزء 4 – worktree مقابل clone وأوامر التنظيف]]

> ⚠️ **تنبيه:** المصدر لا يحتوي على توقيتات زمنية، فلم تُضَف أي توقيتات. وجميع ما هو موسوم بـ «إضافة من المُلخِّص» ليس من كلام المتحدث.

---

## الجزء 1 – المشكلة: القفل أثناء المهام الطويلة

### الملخص العلمي

عندما يعمل [[Claude Code]] على مهمة طويلة المدى ([[long horizon tasks]]) — مثل إصلاح الاختبارات على فرع ([[branch]]) معيّن — فأنت <span style="color:#E11D48; font-weight:bold;">مقفل تمامًا</span> عن أي عمل آخر معه حتى تنتهي المهمة. أثناء الانتظار لا يفعل المتحدث سوى التفكير في الميزات القادمة وتدوين الملاحظات.

> <span style="color:#D97706; font-weight:bold;">الفكرة:</span> تشغيل عدة نسخ (instances) من Claude Code على فروع مختلفة تعمل على ميزات متعددة في آنٍ واحد، لتصبح «وحش إنتاجية».

| المفهوم | التعريف |
|---------|---------|
| <span style="color:#0D9488; font-weight:bold;">Multi-instance workflow</span> | أكثر من نسخة Claude Code بالتوازي، كل نسخة على فرع مستقل |
| <span style="color:#0D9488; font-weight:bold;">Isolation</span> | كل نسخة في مجلد/فرع معزول فلا تتداخل مع الأخرى |

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** «Multi-Agent» في العنوان تعني أن كل نسخة وكيل ([[agent]]) مستقل؛ المتحدث لم يشرح المصطلح صراحة. كما أن `clawed code` في النص خطأ تحويل صوتي والمراد **Claude Code**.

### نص المتحدث الكامل

what are you doing while clawed code is running those long horizon tasks Sometimes if I'm not thinking about the next features and making notes on things I notice I'm often just twiddling my thumbs But what if we could have multiple clawed code instances running on separate branches working on multiple features making you a performance beast when it comes to clawed code Well let's dig into how you can achieve exactly that So this is a typical example where I've got clawed code working on a branch fixing tests doing its thing I'm pretty much completely locked out of doing any work from clawed code until now So if I create a new window I'm using warp here which I'll leave links to down below That will become relevant in just a second

---

## الجزء 2 – الحل: إنشاء git worktree

### الملخص العلمي

الخطوات داخل المشروع:

1. `git worktree add -b <اسم_الفرع> <مسار_المجلد_الجديد> <الفرع_الأساسي>`
2. تسمية الفرع باسم الميزة — في المثال `feature/add-MFA` ([[MFA]] = المصادقة متعددة العوامل).
3. تحديد مجلد جديد خارج المشروع (`../add-MFA`).
4. نقطة التفرّع: `origin main`، أو تركها فارغة للتفرّع من الفرع الحالي، أو أي فرع من GitHub.
5. بعد التنفيذ: `cd` إلى المجلد ثم `ls` — نسخة كاملة من الكود على فرع جديد.
6. تشغيل `claude` والعمل **معزولًا تمامًا** عن المهمة الجارية في المجلد الآخر.

| العنصر | النتيجة |
|--------|---------|
| المجلد الجديد | نسخة عمل كاملة من الكود |
| الفرع | فرع جديد باسم الميزة |
| العزل | كل مجلد على فرع مستقل دون تداخل |

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** الصيغة الدقيقة للأمر (مع تصحيح `get work tree add-b` → `git worktree add -b`):
> ```bash
> git worktree add -b feature/add-MFA ../add-MFA origin main
> ```

### نص المتحدث الكامل

What we can do is inside of my project I can simply type get work tree add-b and then I'm going to name this branch So in this case I'm going to type feature add MFA cuz I want to work on adding multiffactor authentication to my app Then you're going to want to specify a folder in wherever it is you want to create this new instance of clawed code So I'm going to go back a folder here and then create a new folder called add MFA And I want to branch that from origin main You can branch it from the current branch that you're on by by leaving this blank or indeed you can choose another branch to branch this from on GitHub Whatever you choose really So I'm going to branch out from name I'm going to hit add and it's going to create that folder Pull down the code into that And I'm going to cd into that folder And if I ls here I've got a copy of all of that code a new branch of that code and I can work safely within here And of course I can just run claude and everything as I expect it and I can start to implement my add MFA feature completely isolated from the current task that's probably still doing its thing over in the other folder

---

## الجزء 3 – الأتمتة عبر Warp agent mode

### الملخص العلمي

يمكن بدل الأمر اليدوي طلب المهمة طبيعيًا من [[Warp]] في agent mode: «create a new worktree branch to implement new UI fixes branch».

ما فعله Warp فعليًا:

1. عمل fetch من [[GitHub]].
2. أنشأ فرع `UI-fixes` عبر `git worktree add` في مجلد جديد داخل المشروع.
3. فرّعه من `origin main`.
4. أرشد المتحدث إلى `cd` ثم تشغيل `claude`.

> <span style="color:#D97706; font-weight:bold;">ملاحظة المتحدث:</span> «كثيرًا لا أعرف ما الذي يفعله Warp — وهذا بالضبط سبب استخدامه.»

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** «lens leaves UI fixes» خطأ تحويل صوتي والمرجّح «and name it UI fixes». موضع المجلد هذه المرة **داخل** المشروع بينما في الجزء السابق **خارجه** — وكلاهما صالح.

### نص المتحدث الكامل

And now I said I'm using warp and I said that will come in handy later on So realistically I could probably just ask Warp to say back into my main folder here switch agent mode on here and say create a new work tree branch to implement new UIXes branch Let's see if Warp can figure this out It's going to fetch I mean to be honest oftent times I have no idea what warp is doing which is exactly why I use it Now I understand this get work tree add new branch called UI fixes and it's going to add it to a new folder inside of here called lens leaves UI fixes from origin main And there we go It's telling us we should cd into that folder now Fire up claude and we're good to go

---

## الجزء 4 – worktree مقابل clone وأوامر التنظيف

### الملخص العلمي

لماذا لا تعمل [[clone]] جديدًا للمستودع؟ يمكن، لكن [[git worktree]] يشارك الموارد فلا انتظار تنزيل، ويبقي الفروع محدّثة مع التغييرات على الـ remote — أنظف وأسرع.

| وجه المقارنة | git worktree | clone جديد |
|--------------|--------------|------------|
| مشاركة الموارد | يشارك نفس مستودع Git الأساسي | ينسخ المستودع كاملًا |
| التحديث مع الـ remote | يبقي الفروع محدّثة | كل نسخة منعزلة |
| السرعة والنظافة | أنظف وأسرع | أبطأ وأثقل |

### أوامر التنظيف

| الأمر | الوظيفة | التوقيت |
|-------|---------|---------|
| `git worktree remove <path>` | حذف مجلد الـ worktree | بعد الـ push والانتهاء |
| `git worktree prune` | تنظيف الفروع القديمة الراكدة (stale) | صيانة دورية |

> ⚠️ **تنبيه:** لا تستخدم `git worktree remove` إلا بعد دفع كل عملك إلى GitHub.

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** `get worksheet remove` خطأ تحويل صوتي والمراد `git worktree remove`. ولم يذكر المتحدث صراحةً أن remove يفشل عند وجود تغييرات غير مرحّلة — سلوك عام في Git يُستحسن التحقق منه.

### نص المتحدث الكامل

So you might really ask yourself why can't I just create a folder and clone the repo again and work and you can absolutely do that but in this way it's sharing a lot of the resources so you don't have to wait for it to download that clone anymore Moreover it keeps both branches up to date with any changes that happen on the remote So generally it's just a bit cleaner a little bit faster Some other useful commands is get worksheet remove and then the path to the folder that you created earlier This will just remove it once you've obviously pushed it up to GitHub and you've done everything you need to do Another one is Git Work Tree Prune which will clean up any stale branches that you've made in the past So subscribe to my channel if you found it useful or if you want to hear more claw code tips
