---
name: github-commit-push
description: 把项目所有改动 commit 并 push 到 GitHub 指定仓库。当用户说 提交到github / 上传到GitHub / git commit并push到github / 推送到github 时使用。
---

# 提交项目（GitHub commit & push）

把当前项目的所有改动用 `git commit` 提交，并 `git push` 到
`https://github.com/y1y1baobao-netizen/qiyingyi`。

## 步骤（在项目根目录执行）

1. **查看状态**：`git status --short`、`git diff --stat`，了解将要提交的内容。
2. **暂存全部**：`git add -A`（本项目所有作业文件都属于交付物，全部提交）。
3. **提交**：`git commit -m "<message>"`。
   - 若用户在提示词里给了提交说明，直接使用它。
   - 否则根据刚才的改动写一条简短中文 message（如 `新增15-1数7游戏页面`）。
   - 若没有任何改动（nothing to commit），告知用户并停止，不要造空提交。
4. **确认远端**：
   - 先检查 `git remote get-url github`：若已配置为目标 URL，直接用。
   - 若不存在：`git remote add github https://github.com/y1y1baobao-netizen/qiyingyi.git`。
   - 若已配置为其他地址：`git remote set-url github https://github.com/y1y1baobao-netizen/qiyingyi.git`。
   - 注意：不要覆盖现有 origin（通常指向 Gitee），保持多个 remote 并存。
5. **推送**：
   - 首次推送（远端仓库可能为空）：`git push -u github master`
     （若 `git branch --show-current` 显示的是 `main`，则推 `main`）。
   - 日常推送：`git push github HEAD`。

## 认证

- 本机已配置 GitHub SSH 公钥（用户已在 GitHub 账号设置中添加）。
- HTTPS 推送若失败，自动降级为 SSH：
  1. `git remote set-url github git@github.com:y1y1baobao-netizen/qiyingyi.git`
  2. 重试 `git push github HEAD`。
  3. 若仍报 `Permission denied (publickey)`，提示用户用 `ssh -T git@github.com` 验证并检查 GitHub SSH 设置。

## 注意事项

- 文件名含中文和空格（如 `3-1 form.html`、`5-1 层叠与继承.html`）：PowerShell 中一律加引号，优先用 `-LiteralPath`。
- 提交信息、读写文件一律用 `-Encoding UTF8`，避免中文乱码。
- 禁止 `git push --force`；若被拒绝，先 `git pull --rebase github HEAD` 再推送。
- 绝不提交密钥（`~/.ssh/*` 在仓库外，保持如此），也不要提交任何密码/token。
- 推送成功后，向用户报告提交哈希（`git log --oneline -1`）、远端名称和分支。
