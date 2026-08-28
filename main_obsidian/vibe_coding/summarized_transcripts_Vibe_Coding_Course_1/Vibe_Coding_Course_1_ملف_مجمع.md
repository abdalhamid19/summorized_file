---
title: "Vibe Coding - الدرس الأول - ملف مجمع"
date: 2026-08-28
tags:
  - vibe_coding
  - ملف_مجمع
aliases:
  - تلخيص الدرس الأول مجمع
---

# Vibe Coding — الدرس الأول (ملف مجمع)

> [!info]
> تجميع الخلاصات العلمية للأجزاء 01–11 بلا ملفات مراجعة/اختبار وبلا توقيتات مختلقة. المصدر: إبراهيم الشربيني — قناة سيكويشن. التفاصيل ونص المتحدث في الأجزاء المنفصلة.

## تعريف الكورس والمجاني والمدفوع

[[Vibe Coding]] = البرمجة بالذكاء الاصطناعي / البرمجة الحدثية. الاسم جديد أطلقه YouTuber مشهور ثم صار معروفًا للمجال كله.

| العنصر | الحكم |
|---|---|
| فيديو YouTube | مجاني؛ الأسئلة تحت الفيديو |
| Claude / ChatGPT / Gemini | مدفوعة 100%؛ لا نسخة مجانية ولا DeepSeek للعمل |
| الدعم | Group School؛ غير مجاني |
| Code | غير مجاني؛ مع Package School؛ يُعرف في الفيديو القادم |

من يفكر Business يستثمر في المدفوع اليوم. من يرفض حزمة المتحدث يأخذ الفكرة بحساباته؛ أدوات الذكاء تبقى مدفوعة.

## الست مهارات

المتحدّث ليس مبرمجًا؛ عمل أدوات وE-commerce وExtension بلا سطر Code. الكورس **Web Application** لا Mobile.

| جهة | مهارة |
|---|---|
| شمال (Business) | [[رؤية المنتج]] — فكرة حاضرة مدروسة |
| شمال | [[عقلية Business]] — لا استنفاذ عقل في شكل Code |
| شمال | [[اكتشاف الـ Bug]] — نسخ Bug للذكاء الاصطناعي (بعد Sonnet 4.5 وGPT-5: Copy-Paste فقط) |
| يمين | [[VS Code]] + [[GitHub]] — الربط يكفي؛ Deployment من GitHub |
| يمين | [[Docker]] — ملف واحد يشغّل الـ Application |
| يمين | قشور [[Server Administration]] |

هذا الفيديو: قشور اليمين. القادم: الشمال مع عمل الأداة.

## Frontend / Backend / Headless

لا يلزم فهم كتابة الـ Code؛ يلزم فهم استعمال كل لغة ومفاهيم البناء.

| مصطلح | تعريف المصدر |
|---|---|
| [[Frontend]] | واجهة المستخدم؛ هنا JavaScript |
| [[Backend]] | API + قاعدة بيانات + بحث |
| [[Headless]] | فصل الطرفين عبر [[API]] أو [[GraphQL]] من 2021 |

مزايا Headless: تغيير طرف دون الآخر؛ Security (لا سرقة API من Chrome Console) بنظام Proxy؛ سرعة (Stacks منفصلة). WordPress Frontend+Backend معًا؛ Headless يفصل.

Frameworks JS: Next، Astro، React، Nuxt، Vue، Remix، Svelte. للVibe Coder كلهم واحد.

## كيف تعمل الصفحة

أي موقع: HTML + CSS + JavaScript. مكتبات JS من 2011: Angular ثم React (2013، Facebook، منها Next وRemix) ثم Vue (2014) ثم Svelte (2016).

عند الطلب: المتصفح يرسل request → [[Routing]] → [[Authentication]] → جلب من API/DB → [[Rendering]]. هذه الألفاظ تُكتب في Prompt. Lovable — بحسب المصدر — لا يعمل Authentication إلا عبر Supabase.

## أربع استراتيجيات Rendering

| | CSR | SSR | SSG | ISR |
|---|---|---|---|---|
| أين المعالجة | المتصفح | Server | HTML محفوظ | HTML + تعديل بسيط |
| SEO | لا | نعم | وسط | وسط |
| متى | تفاعل كثير؛ لا يهمك Server | تريد SEO وتتحمل Serverًا قويًا | Landing ثابت | منتج بمراجعات/Update |

صفحة checkout: لا CSR ولا SSG؛ يلزم SSR.

| Framework | ملاحظة المصدر |
|---|---|
| React | أصل CSR؛ Desktop/Chrome/Workflow؛ لا لـ Marketplace SEO |
| Next.js | من React؛ SSR+SSG+ISR؛ الأشهر |
| Vue | تفاعل/Cards/Workflow؛ SSR+SSG+ISR؛ لا CSR؛ يحتاج Serverًا قويًا |
| Svelte | Forms كثيرة |
| Angular | انسَها |
| Astro | static أساسًا؛ SEO ممتاز |
| Nuxt | من Vue كالـ Next من React |

بعد Rendering: [[Caching]] على CDN وRedis لـ API المتكرر.

## Deployment

**Serverless:** لا بيانات Server؛ رفع GitHub يتحول SSG أو SSR. Security قصوى.

Static: Cloudflare Pages (حتى 500 زائر/يوم ثم 5$/شهر)، Firebase، GitHub Pages، Surge.sh.

Dynamic: أصلها AWS App Runner. Railway المفضّل (20$ من الـ Link وإلا 5$). البعد عن Vercel. Netlify/Render مكلفان. Fly.io للشركات الكبيرة.

**Self-host:** Full Control ومشكلة Security عليك. Docker أساسي؛ الواجهة [[Portainer]] لا Terminal.

## Backend

| مكوّن | اختيار المصدر |
|---|---|
| بحث | Typesense (مفتوح/مجاني على Portainer) |
| API | Python + FastAPI + DSPy (ضبط Prompt) |
| DB | PostgreSQL |
| Serverless DB | Neon، Supabase (أشهر)، Railway (من 5$)، PlanetScale (من 60$ بلا مجاني) |
| ذاكرة/Vector | [[Redis]] |
| Analytics | ClickHouse |

أخطر Security: Database ثم الـ API.

## VS Code وGitHub

[[Cursor]] وWindsurf وTrae مبنية على Code VS Code. ثبّت VS Code أولًا. Node.js + Python (نحو 3.11؛ وقت التسجيل 3.13 والذكاء لم يصلها في أكتوبر 2025). Git for Windows. Extension GitHub Pull Requests. `.gitignore` يمنع node_modules و`.next`. Extensions العمل: Claude Code وCodex. يكفي ربط GitHub بـ VS Code؛ الباقي يُسأل للذكاء.

عرض: `create next.js project` → `npm run dev` على 3000 → Commit/Push.

## Servers

Postgres أعلى DB؛ MySQL مرتفع بسبب WordPress فقط. Cloud: Amazon ثم Microsoft ثم Google ثم Cloudflare. ويب: Node وReact الأعلى.

| | Hetzner | Vultr |
|---|---|---|
| السعر | أرخص (مثال 4CPU/16GB ≈ 30$) | أقوى وأغلى (لا أقل من 40$ Dedicated) |
| تفعيل | PayPal أو Visa+جواز؛ Limit Server أول شهر | بلا Verification |
| Ports | مفتوحة كلها | مغلقة |
| Credit الـ Link | 20$ | 300$ أول شهر |
| موقع عربي | ألمانيا أقرب | مدينة أمريكية (نيويورك) |

Ubuntu 24. دخول بـ PuTTY: IP + root + لصق Password right-click.

## Docker وPortainer وNPM

[[Portainer]] مجاني 100%. تثبيت عبر أوامر الذكاء على Ubuntu 24. دخول `https://IP:9443`. على Vultr افتح الـ Ports بـ UFW.

المسار: Home → Environment → Local → Stacks. مصادر: hub.docker.com، elestio (Mautic، WordPress، Redis، Flowise، Odoo…).

أول تثبيت: [[Nginx Proxy Manager]] Port 81؛ افتراضي `admin@example.com` / `changeme`.

نمط أي تطبيق: Document → الذكاء → Volume قبل التثبيت → Deploy → Subdomain Cloudflare (A record) → NPM Proxy HTTP ثم SSL → WebSocket إن كانت Data instant. مثال n8n Port 5678. بـ Terminal ساعات؛ هنا دقائق.

## Railway ختامًا

لا بيانات Server. Limitation: ملفات بشكل معيّن؛ تفرض `railway.toml`. اسأل الذكاء: اعمل ملفات Deployment.

قوالب Docker بنقرة: n8n، Flowise، Redis، Postgres. مشروع GitHub (مثال Astro): أربع خطوات ≈ خمس دقائق حتى Live → Generate domain → Port غالبًا 8080.

هذا الفيديو **بوابة** للجانب الأيمن. الجانب الأيسر (رؤية، Business، حل Bug) في الفيديو القادم. نحو ساعة ونصف.

## خريطة سريعة
[[Vibe Coding]] ← [[Headless]] ← [[Rendering]] ← [[Deployment]] ← [[Docker]] / [[Railway]]

- الأجزاء: [[00 - الفهرس والخطة]]
- الخريطة: [[MOC_Vibe_Coding_الدرس_الأول]]
