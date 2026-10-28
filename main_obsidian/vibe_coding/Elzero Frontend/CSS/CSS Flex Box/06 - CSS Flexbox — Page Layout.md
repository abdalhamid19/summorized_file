---
title: "CSS Flexbox — Page Layout"
date: 2026-10-28
tags:
  - vibe_coding
  - frontend
  - CSS
  - css-flex-box
  - تكليف
aliases:
  - CSS Flexbox — Page Layout
---

# CSS Flexbox — Page Layout

> [!question] السؤال
> استخدم Flex فقط لتوزيع الرأس والمحتوى والشريط الجانبي والتذييل. اجعل القيم المتكررة متغيرات CSS.
>
> **الصورة المرجعية**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/reference-task-06.png]]
>
> [صفحة التكليف الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)

> [!success]- الإجابة وشرح الحل — اضغط لفتحه
>
> ```css
> :root {
>   --gap: 12px;
>   --surface: #ddd;
>   --pad: 14px;
> }
>
> .page {
>   min-height: 500px;
>   display: flex;
>   flex-direction: column;
>   gap: var(--gap);
> }
>
> .header, .main-area, .footer {
>   display: flex;
>   gap: var(--gap);
> }
>
> .logo, .links, .content, .sidebar, .copyright, .design {
>   padding: var(--pad);
>   background: var(--surface);
> }
>
> .links {
>   flex: 1;
>   display: flex;
>   justify-content: flex-end;
>   gap: 20px;
>   list-style: none;
>   margin: 0;
> }
>
> .main-area { flex: 1; }
> .content { flex: 3; }
> .sidebar { flex: 1; }
> .copyright, .design { flex: 1; }
> .design { text-align: right; }
> ```
>
> البنية تصطف عموديًا باستخدام Flex، ويأخذ المحتوى حصة أكبر من الشريط الجانبي. جعلت روابط الرأس صفًا مرنًا إلى اليمين، ووحّدت المسافة والخلفية والحشو في متغيرات قابلة لإعادة الاستخدام.
>
> **معاينة الحل**
>
> ![[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/assets/solution-task-06.png]]
>
> [[vibe_coding/Elzero Frontend/CSS/CSS Flex Box/CSS Flex Box Assignments 46-53.html|افتح صفحة المعاينة]]

## المصدر

[تكليفات CSS الرسمية](https://elzero.org/css-assignments-lesson-from-46-to-53/)
