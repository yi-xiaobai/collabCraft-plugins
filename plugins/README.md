# CollabCraft Plugins

团队级知识与工作流插件，通过仓库内 marketplace 向 Claude Code 统一分发。

## 插件列表

| 插件 | 能力 | 说明 |
|------|------|------|
| **git-workflow** | 自动 Skill、`/commit-push-mr` | Git 团队规范与 GitLab 交付 |
| **gitlab-mr** | `/mr-list`、`/mr-beautify`、`/mr-update` | GitLab MR 管理 |
| **dependency-upgrade** | `/turtle-upgrade` | 团队依赖升级流程 |
| **plugin-linter** | `/plugin-lint` | 插件结构检查 |

## 设计分层

```text
LLM 原生能力
  通用编码、Git 操作、分析、总结

Skills
  团队知识、约定、检查清单和需要上下文的判断

Commands
  用户需要明确触发的多步骤或跨系统工作流

Scripts / Hooks / CI
  必须确定执行和强制满足的约束
```

Plugin 是团队能力的分发容器，并不等同于 slash command。一个 Plugin
可以同时包含 Skill、Command、Agent 或确定性工具。

## 目录结构

```text
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json
├── skills/                 # optional
│   └── <skill-name>/
│       └── SKILL.md
├── commands/               # optional
│   └── <command>.md
├── agents/                 # optional
│   └── <agent>.md
├── scripts/                # optional
└── README.md
```

- `skills/*/SKILL.md`：仅在相关场景加载的团队知识和软性决策规则。
- `commands/*.md`：多步骤、跨系统或需要明确入口的工作流。
- `agents/*.md`：被多个工作流复用的专业上下文；单个 Command 专用逻辑直接内联。
- `scripts/`、Hooks、CI：确定执行、可机械验证的动作和门禁。

## 封装判断

设计一项能力前依次判断：

1. LLM 能否仅凭自然语言稳定完成？能则直接使用，不增加封装。
2. 是否反复需要团队专有知识或相同决策规则？是则使用 Skill。
3. 是否是有独立价值的多步骤或跨系统流程？是则提供 Command 入口。
4. 是否必须百分之百执行或阻止错误？是则使用 Script、Hook 或 CI。

不要把普通 CLI 操作包装成 Command，也不要为只使用一次的推理创建 Agent。

## Marketplace

Marketplace 文件位于 `.claude-plugin/marketplace.json`，每个条目指向
`./plugins/<plugin-name>`。

每个 manifest 至少包含：

- `name`
- `description`
- `author.name`

修改后运行：

```bash
bash scripts/lint-plugins.sh
```
