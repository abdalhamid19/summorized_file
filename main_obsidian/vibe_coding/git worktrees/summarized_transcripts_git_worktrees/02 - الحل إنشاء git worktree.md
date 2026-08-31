# 02 - الحل: إنشاء git worktree خطوة بخطوة

## 📌 الملخص العلمي

### الأداة المستخدمة

المتحدث يستخدم [[Warp]] (terminal) — وسيذكر سببًا لأهميته لاحقًا في الجزء 03.

### الخطوات العملية

1. داخل مجلد المشروع، نفّذ الأمر: `git worktree add -b <اسم_الفرع> <مسار_المجلد_الجديد> <الفرع_الأساسي>`
2. سمِّ الفرع بالميزة المطلوبة — في المثال: `feature/add-MFA` (إضافة [[MFA]] — المصادقة متعددة العوامل).
3. حدّد مجلدًا **خارج** المشروع (العودة مجلدًا للخلف `../`) وسمِّه باسم المهمة مثل `add-MFA`.
4. اختر الفرع الأساسي:
   - `origin main` — التفرّع من آخر نسخة على [[GitHub]] (ما فعله المتحدث).
   - تركه فارغًا — التفرّع من الفرع الحالي.
   - أو أي فرع آخر تختاره من على GitHub.
5. نفّذ الإضافة — سيُنشئ Git المجلد ويسحب ([[pull]]) الكود إليه.
6. `cd` إلى المجلد الجديد، ثم `ls` — ستجد نسخة كاملة من الكود على فرع جديد.
7. شغّل `claude` كالمعتاد وابدأ تنفيذ الميزة **معزولًا تمامًا** عن المهمة الجارية في المجلد الآخر.

### ما يحدث فعليًا عند `git worktree add`

| العنصر | النتيجة |
|--------|---------|
| المجلد الجديد | نسخة عمل ([[working copy]]) كاملة من الكود |
| الفرع | فرع جديد باسم الميزة |
| العزل | كل مجلد يعمل على فرع مستقل دون تداخل |

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** الصيغة الدقيقة للأمر كما نفّذه المتحدث (مع تصحيح أخطاء التحويل الصوتي `get work tree add-b` → `git worktree add -b`) هي:
> ```bash
> git worktree add -b feature/add-MFA ../add-MFA origin main
> ```
> حيث `feature/add-MFA` اسم الفرع، و`../add-MFA` مسار المجلد الجديد، و`origin main` نقطة التفرّع.

## نص المتحدث الكامل

What we can do is inside of my project I can simply type get work tree add-b and then I'm going to name this branch So in this case I'm going to type feature add MFA cuz I want to work on adding multiffactor authentication to my app Then you're going to want to specify a folder in wherever it is you want to create this new instance of clawed code So I'm going to go back a folder here and then create a new folder called add MFA And I want to branch that from origin main You can branch it from the current branch that you're on by by leaving this blank or indeed you can choose another branch to branch this from on GitHub Whatever you choose really So I'm going to branch out from name I'm going to hit add and it's going to create that folder Pull down the code into that And I'm going to cd into that folder And if I ls here I've got a copy of all of that code a new branch of that code and I can work safely within here And of course I can just run claude and everything as I expect it and I can start to implement my add MFA feature completely isolated from the current task that's probably still doing its thing over in the other folder

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** أخطاء تحويل صوتي في النص أعلاه: `get work tree add-b` = `git worktree add -b`، `clawed code` = `Claude Code`، `multiffactor` = `multi-factor`، `branch out from name` = `branch out from main`.

---

- 📦 **عدد الأجزاء:** 4 (+ ملف خطة تطبيقية)
- ✅ **الجزء الحالي:** 02
- ⏳ **الأجزاء المتبقية:** 3
