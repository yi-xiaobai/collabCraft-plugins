# CollabCraft Plugins

团队级 Git 工作流插件，通过 Marketplace 统一分发。

## 插件列表

| 插件 | 命令 | 说明 |
|------|------|------|
| **branch-commands** | `/branch-create`, `/branch-switch`, `/branch-delete` | Git 分支工作流 |
| **commit-commands** | `/commit`, `/commit-push`, `/commit-push-mr` | Git 提交工作流 |
| **mr-commands** | `/mr-list` | GitLab MR 工作流 |

> **个人效率工具**（Skills，非插件）：
> - `/log`, `/generate-week` → work-log skill
> - `/build` → turtle-build skill
> - `/trending` → github-trending skill

## 目录结构

```
plugins/
├── branch-commands/
│   ├── .claude-plugin/plugin.json
│   ├── commands/
│   │   ├── branch-create.md
│   │   ├── branch-switch.md
│   │   └── branch-merge.md
│   ├── agents/
│   │   └── branch-namer.md
│   └── README.md
├── commit-commands/
│   ├── .claude-plugin/plugin.json
│   ├── commands/
│   │   ├── commit.md
│   │   ├── commit-push.md
│   │   └── commit-push-mr.md
│   ├── agents/
│   │   └── commit-message-writer.md
│   └── README.md
└── mr-commands/
    ├── .claude-plugin/plugin.json
    ├── commands/
    │   ├── mr-list.md
    │   ├── mr-beautify.md
    │   └── mr-update.md
    ├── agents/
    │   └── mr-summarizer.md
    └── README.md
```

每个 plugin 目录约定：

- `commands/*.md` — 用户主动触发的 slash 命令
- `agents/*.md` — 可被命令委派的子代理（subagent），用于复用复杂的 AI 任务
- `.claude-plugin/plugin.json` — 插件清单

## Plugin vs Skill

| 类型 | 用途 | 示例 |
|------|------|------|
| **Plugin** | 团队共享、标准化工作流 | branch-commands, commit-commands |
| **Skill** | 个人效率、本地配置 | work-log, turtle-build, github-trending |

## 命令文件格式

```markdown
---
allowed-tools: Bash(git add:*), Bash(git commit:*)
description: Short description
---

## Context

- Current status: !`git status`

## Your task

Instructions for Claude...
```
