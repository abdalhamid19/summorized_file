# 03 - الأتمتة عبر Warp agent mode

## 📌 الملخص العلمي

### الفكرة

بدل كتابة الأمر يدويًا، يمكن طلب المهمة بصيغة طبيعية من [[Warp]] في وضع الـ agent mode:

> «Create a new worktree branch to implement new UI fixes branch»

### ما فعله Warp فعليًا (كما سرده المتحدث)

1. قام بـ fetch من [[GitHub]].
2. أنشأ فرع ([[branch]]) جديدًا باسم `UI-fixes` عبر `git worktree add`.
3. وضعه في مجلد جديد داخل المشروع.
4. فرّعه من `origin main`.
5. أخبر المتحدث أن عليه `cd` إلى المجلد الجديد ثم تشغيل `claude` — «وأنتم جاهزون».

### ملاحظة المتحدث عن Warp

> <span style="color:#D97706; font-weight:bold;">«في كثير من الأحيان لا أعرف ما الذي يفعله Warp — وهذا بالضبط سبب استخدامه.»</span>

أي: الأتمتة العمياء مقبولة هنا لأن النتيجة (worktree جاهز) هي المطلوبة.

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** النص الأصلي «lens leaves UI fixes» هو خطأ تحويل صوتي، والمرجّح أنه «and name it UI fixes» أو ما يشابهه — أي أن Warp سمّى الفرع `UI-fixes`. كما أن عبارة «add it to a new folder inside of here» تعني أن Warp وضع المجلد هذه المرة **داخل** المشروع (بينما في الجزء 02 وضعه المتحدث خارج المشروع مجلدًا للخلف) — وكلا الموضعين صالح.

## نص المتحدث الكامل

And now I said I'm using warp and I said that will come in handy later on So realistically I could probably just ask Warp to say back into my main folder here switch agent mode on here and say create a new work tree branch to implement new UIXes branch Let's see if Warp can figure this out It's going to fetch I mean to be honest oftent times I have no idea what warp is doing which is exactly why I use it Now I understand this get work tree add new branch called UI fixes and it's going to add it to a new folder inside of here called lens leaves UI fixes from origin main And there we go It's telling us we should cd into that folder now Fire up claude and we're good to go

> 💡 **إضافة من المُلخِّص (ليست في المصدر):** أخطاء تحويل صوتي: `work tree` = `worktree`، `UIXes` = `UI fixes`، `oftent times` = `oftentimes`، `get work tree add` = `git worktree add`.

---

- 📦 **عدد الأجزاء:** 4 (+ ملف خطة تطبيقية)
- ✅ **الجزء الحالي:** 03
- ⏳ **الأجزاء المتبقية:** 2
