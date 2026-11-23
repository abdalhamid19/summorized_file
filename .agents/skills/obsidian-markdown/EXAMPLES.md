# Obsidian Markdown Examples

## Preserve a `؟؟؟؟` placeholder while highlighting an ayah

In this vault, `main_obsidian/دين/تفسير/المختصر في التفسير - نسخة شخصية/056 - الواقعة.md` contains a standalone `؟؟؟؟` after the citation for Al-Waqi'ah 28. When highlighting later verses in the same note, leave that line in the same place:

```markdown
<div dir="rtl">﴿فِي سِدۡرٖ مَّخۡضُودٖ﴾</div>
<div dir="rtl">سورة الواقعة: ٢٨</div>
؟؟؟؟
<div dir="rtl">﴿وَطَلۡحٖ مَّنضُودٖ﴾</div>
```

For the requested highlight in that note, wrap only the ayah text and leave its citation and every placeholder untouched:

```markdown
<div dir="rtl">﴿<mark style="background-color: #d9fdd3; color: #173b20;">أَفَرَءَيۡتُم مَّا تُمۡنُونَ</mark>﴾</div>
<div dir="rtl">سورة الواقعة: ٥٨</div>
```

After editing, search the note for `؟؟؟؟` and confirm the same line remains. A corresponding placeholder also exists in `main_obsidian/دين/تفسير/المختصر في التفسير - نسخة شخصية/053 - النجم.md`; editing another surah must not remove it.
