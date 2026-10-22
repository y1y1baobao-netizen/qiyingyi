---
name: gitee-commit-push
description: 把项目所有改动 commit 并 push 到 Gitee 指定仓库。当用户说 提交项目 / 上传到gitee / git commit并push / 推送代码 时使用。
---

# 提交项目（Gitee commit & push）

把当前项目的所有改动用 `git commit` 提交，并 `git push` 到
`https://gitee.com/qi-yingyi-711/qiyingyi2026.git`。

## 步骤（在项目根目录执行）

1. **查看状态**：`git status --short`、`git diff --stat`，了解将要提交的内容。
2. **暂存全部**：`git add -A`（本项目所有作业文件都属于交付物，全部提交）。
3. **提交**：`git commit -m "<message>"`。
   - 若用户在提示词里给了提交说明，直接使用它。
   - 否则根据刚才的改动写一条简短中文 message（如 `完成11-x页面与index导航更新`）。
   - 若没有任何改动（nothing to commit），告知用户并停止，不要造空提交。
4. **确认远端**：`git remote get-url origin`。
   - 若未配置：`git remote add origin https://gitee.com/qi-yingyi-711/qiyingyi2026.git`。
   - 若已配置为其他地址，改为上述 URL：`git remote set-url origin <url>`。
5. **推送**：
   - 尚无任何提交/远端无该分支（首次推送）：`git push -u origin master`
     （若 `git branch --show-current` 显示的是 `main`，则推 `main`）。
   - 日常推送：`git push origin HEAD`。

## 认证

- 本机已生成 Gitee 用 SSH 密钥 `~/.ssh/id_ed25519`（公钥已/待添加到 Gitee 账号设置）。
- 如果 HTTPS 推送要求输入账号密码且失败（Gitee 已停用密码方式），自动降级为 SSH：
  1. `git remote set-url origin git@gitee.com:qi-yingyi-711/qiyingyi2026.git`
  2. 重试 `git push origin HEAD`。
  3. 若仍报 `Permission denied (publickey)`，提示用户去 Gitee「设置 → SSH公钥」添加
     `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFPYWz7amaOXZGxgccvRkIfa13J6gBAk48v+0XsKkpOB gitee-qyy`，
     并用 `ssh -T git@gitee.com` 验证。

## 注意事项

- 文件名含中文和空格（如 `3-1 form.html`、`5-1 层叠与继承.html`）：PowerShell 中一律加引号，优先用 `-LiteralPath`。
- 提交信息、读写文件一律用 `-Encoding UTF8`，避免中文乱码。
- 禁止 `git push --force`；若被拒绝，先 `git pull --rebase origin HEAD` 再推送。
- 绝不提交密钥（`~/.ssh/*` 在仓库外，保持如此），也不要提交任何密码/token。
- 推送成功后，向用户报告提交哈希（`git log --oneline -1`）和远端分支。
