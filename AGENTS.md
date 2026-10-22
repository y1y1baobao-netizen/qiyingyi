# AGENTS.md

## What this is

Static HTML/CSS coursework for 《高级网页设计》 (student 齐英伊, ID 24001010829). **No build system, no package manager, no lint/test/typecheck commands, no git repo.** Do not introduce frameworks, bundlers, or CDN libraries — the assignment prompts require 原生代码 (vanilla HTML/CSS only, no CDN).

Preview with VS Code Live Server (configured on port 5501 in `.vscode/settings.json`) or any static file server. There is nothing else to run.

## Layout

- Root `*.html` — numbered in-class exercises (`1.html` … `10-4.html`). Mostly self-contained with inline `<style>`; `5-1 层叠与继承.html` is the only page linking the shared root `css.css`. Images in `img/`.
- `index.html` — course navigation portal. Contains the original assignment prompt verbatim in a "本提示词" box; that text is part of the deliverable — keep it. New pages must be added to its link grid.
- `非遗网/` — static replica of ihchina.cn homepage. `index.html` + `style.css` + local `images/` + a `.docx` report.
- `陶艺工坊/` — pottery studio site. `index.html` + `style.css` + `.docx` report; images load remotely from picsum.photos.
- `*.docx` files are submission artifacts — leave them alone.

## Standing rules from the user (always apply)

- **命名**: 所有 CSS 类、id、JS 变量必须以 `qyy_` 开头 (e.g. `.qyy_card`, `#qyy_box`, `let qyy_count`). 旧文件不改，只对新写/改的代码生效.
- **HTML 注释头**: 所有新写的 `.html` 文件顶部必须包含如下格式的注释块 (功能名按页面实际用途填，日期写创建/修改当天).
  ```html
  <!-- 姓名: 齐英伊 日期: yyyy-mm-dd 功能名称: XXX -->
  ```
- **技术栈约束**: 仅使用原生 HTML/CSS/JavaScript 实现. **严禁** 引入任何第三方库、CDN、框架或打包器. 图标统一使用项目根目录下 `font/iconfont.*` 提供的字体图标, 通过 `<link rel="stylesheet" href="font/iconfont.css">` 引入 (JS 版用 `font/iconfont.js`). 获取服务器端数据必须使用原生 `fetch` API, 不要用 `axios` / `XMLHttpRequest` / jQuery.
- **Prompt log**: before executing any user prompt, append to `qyy_prompt.md` (create if missing, **append only — never overwrite**), in this format:
  ```
  ## yyyy-mm-dd-hh:mm:ss
  - 模型: <model id>
  - 提示词: <verbatim prompt text>
  ```
  Use `-Encoding UTF8` without BOM when writing from PowerShell.
- **New pages link to home**: whenever a new `.html` file is created, immediately add a hyperlink card for it in `index.html`'s nav grid (next free `<a class="card">` in `.grid`, incrementing `<span class="num">`). Creating the page and linking it are one task — never leave a new page unlinked.

## Conventions (enforced by assignment, not just style)

- Layout: Flexbox only. Do **not** use `float`, table layout, or `id` selectors in the two sub-projects (stated in their file-header comments).
- CSS class prefixes: `qyy-` in `非遗网/style.css`, `stu-pottery-` in `陶艺工坊/style.css`. Follow them for any new classes there.
- Keep the existing per-page structure: sub-projects use external `style.css`; root exercises use inline `<style>` unless already linked to `css.css`.

## File-handling gotchas

- Filenames and paths contain **Chinese characters and spaces** (`3-1 form.html`, `5-1 层叠与继承.html`, `10-1 .html` — note the space before `.html`). Always quote paths in shell commands; prefer `-LiteralPath`.
- All HTML/CSS files are **UTF-8 without BOM**. Windows PowerShell's default encoding mangles Chinese — always pass `-Encoding UTF8` when reading/writing these files via PowerShell. Page lang is `zh-CN`.
- Image refs are case-sensitive: `7-1`/`7-2` reference `img/A3.jpg` but the file on disk is `img/a3.jpg`. Harmless on Windows, breaks on case-sensitive hosting — preserve existing casing, don't "fix" one side without the other.

## index.html nav grid

Links currently run `index.html` → `1.html` … `7-2` → `11-1`–`11-3`; `8-1`, `9-1`, `10-1`–`10-4`, and the two sub-project folders are still missing despite the assignment prompt requiring all pages. Extend the `.grid` with `.card` links following the existing pattern (`<span class="num">` + `<span class="meta"><strong>…</strong><small>…</small></span>`); the highest existing `num` is 15.
