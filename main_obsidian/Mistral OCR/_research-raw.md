# Mistral AI Free Tier / Rate Limits / OCR — Primary-Source Research

Date: 2026-08-07. Sources: docs.mistral.ai, mistral.ai, help.mistral.ai only.
Tags: [DOCS]=docs.mistral.ai, [VENDOR]=mistral.ai/help.mistral.ai, UNVERIFIED=not confirmable from primary sources.

## 1. Free tier existence & requirements
- "Free mode" is the default state for new accounts; API keys are enabled by default, **no credit card required**. [DOCS] https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key
- Plans are global across Vibe/Studio/API: Free mode, Pro, Education, Team, Enterprise. [DOCS] https://docs.mistral.ai/admin/billing-usage/subscriptions
- Phone verification: NOT mentioned anywhere in current docs/help. The old "Experiment plan" tier page (docs.mistral.ai/deployment/laplateforme/tiers/) is removed (404) and has no Wayback snapshot → historical requirement UNVERIFIED.

## 2. Rate limits / quotas
- Enforced at organization level, three dimensions: requests per second, tokens per minute (per model), tokens per month. [VENDOR] https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them
- "Free mode (default) has the lowest limits, intended for evaluation and prototyping." Exact numbers are NOT published; viewable only behind login at https://admin.mistral.ai/plateforme/limits → exact free-tier RPS/TPM/monthly cap UNVERIFIED.
- Limit types per service [DOCS] https://docs.mistral.ai/admin/billing-usage/usage-limits :
  - Completion: tokens/min + requests/sec per model
  - Audio: audio seconds/min, audio seconds/month
  - Document OCR: pages per minute
  - Documents: max upload file size

## 3. OCR API on free tier
- Nothing in official sources excludes `/v1/ocr` from Free mode; OCR usage appears in the org usage dashboard and has org-level pages-per-minute limits. [DOCS] https://docs.mistral.ai/admin/billing-usage/usage-limits
- No published OCR-specific free quota (e.g., free pages/month) → UNVERIFIED.
- OCR price (paid): OCR 4 = $4/1000 pages, Document AI (annotated) = $5/1000 pages. [VENDOR] https://mistral.ai/pricing/api/

## 4. Tiers / upgrade model
- Old names (Experiment/Build/Scale/Enterprise) retired. Current API model: Free mode → Scale plan (pay-as-you-go). [VENDOR] help article 698531
- Scale tiers upgrade automatically by **cumulative billed amount** (not prepaid credits):
  - Tier 1: Scale upgrade; Tier 2: >$20 billed; Tier 3: >$100; Tier 4: >$500; beyond: >$2000 + contact support. [VENDOR] same article
- Pay-as-you-go is a setting, not a plan; enable in Admin Panel > Subscription. [DOCS] https://docs.mistral.ai/admin/billing-usage/subscriptions
- Vibe plans: Free / Pro $14.99/mo / Team $24.99/user/mo / Education $5.99 / Enterprise custom. [VENDOR] https://mistral.ai/pricing/

## 5. Deprecated OCR models
- [DOCS] https://docs.mistral.ai/models/overview (deprecated table):
  - `mistral-ocr-2503` (OCR 25.03): deprecated 2025-12-02, **retired 2025-12-31** → no longer callable.
  - `mistral-ocr-2505` (OCR 2): deprecated 2026-02-27, retires 2026-05-31 → callable until retirement.
  - OCR 3 (`mistral-ocr-2512`, v25.12): still available for existing integrations.
  - OCR 4 (`mistral-ocr-4-0`): current; `mistral-ocr-latest` alias used in docs.
- No free OCR checkpoint exists; only free APIs listed are Labs Leanstral endpoint and Mistral Moderation. [VENDOR] https://mistral.ai/pricing/api/

## 6. Programmatic usage/quota checks
- Admin API (admin key, `x-api-key` header, base `https://api.mistral.ai/v1/admin`): [DOCS] https://docs.mistral.ai/admin/admin-api/usage-metrics
  - `GET /v1/admin/usage?month=&year=&workspace_id=` — consumption by category incl. `ocr`
  - `GET /v1/admin/rate-limit` — current RPS + per-model token limits
  - `GET|POST /v1/admin/spend-limit` — org monthly spending cap
- Console: usage dashboard admin.mistral.ai/organization/usage; limits admin.mistral.ai/plateforme/limits. [DOCS] usage-limits page
- `x-ratelimit-*` response headers: NOT documented in any official source → UNVERIFIED.
