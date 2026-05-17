# CollabCraft Plugins 设计思想

## 核心理念

借鉴 [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) 的设计思想，聚焦解决团队两大痛点：

1. **Git 规范** — 统一团队的 Git 工作流
2. **开发效率** — 帮助开发者理清思路，避免盲目开发

---

## 设计原则

### 1. Skills = 知识沉淀

**思想**：把团队的最佳实践沉淀为可复用的知识库。

```
skills/
├── git-workflow/        # Git 工作流规范
│   ├── commit-convention.md   # Commit 规范
│   ├── branch-naming.md       # 分支命名规范
│   └── mr-checklist.md        # MR 检查清单
│
└── task-breakdown/      # 任务拆解方法
    ├── feature-template.md    # 新功能模板
    ├── bugfix-template.md     # Bug 修复模板
    └── refactor-template.md   # 重构模板
```

**价值**：
- 新人快速上手，不用口口相传
- 规范统一，减少 review 成本
- 知识可迭代，持续优化

### 2. Commands = 用户入口

**思想**：命令是用户与 AI 交互的入口，自动应用对应的 Skills。

```
用户输入: /plan 实现登录功能
    ↓
plan.md 命令被触发
    ↓
自动应用 task-breakdown/feature-template.md
    ↓
输出结构化的任务计划
```

**价值**：
- 用户不需要记住所有规范
- AI 自动应用正确的知识
- 输出格式统一

### 3. 先规划，后执行

**思想**：借鉴 "Plan Before Execute" 原则，复杂任务先拆解再动手。

```
传统流程:
  需求 → 直接写代码 → 发现遗漏 → 返工

改进流程:
  需求 → /plan 规划 → 任务清单 → 逐个完成 → 一次成功
```

**价值**：
- 减少返工
- 可预估工作量
- 进度可追踪

### 4. 模板驱动

**思想**：不同类型的任务使用不同的思考模板。

| 任务类型 | 模板 | 核心问题 |
|----------|------|----------|
| 新功能 | feature-template | 需求边界？技术方案？任务拆分？ |
| Bug 修复 | bugfix-template | 复现步骤？根因分析？修复方案？ |
| 重构 | refactor-template | 重构动机？影响范围？验收标准？ |

**价值**：
- 强制思考关键问题
- 避免遗漏重要环节
- 输出结构化文档

---

## 架构图

```
┌─────────────────────────────────────────────────┐
│                  用户命令层                      │
│  /plan  /branch-create  /commit  /commit-push-mr │
├─────────────────────────────────────────────────┤
│                  知识库层 (Skills)               │
│  ┌─────────────────┐  ┌─────────────────┐       │
│  │  git-workflow   │  │  task-breakdown │       │
│  │  - commit规范   │  │  - 新功能模板   │       │
│  │  - 分支规范     │  │  - Bug修复模板  │       │
│  │  - MR检查清单   │  │  - 重构模板     │       │
│  └─────────────────┘  └─────────────────┘       │
└─────────────────────────────────────────────────┘
```

---

## 与 Everything Claude Code 的关系

| ECC 概念 | 我们的实现 | 说明 |
|----------|------------|------|
| Agents | `/plan` 命令 | 简化为单一规划命令 |
| Skills | `skills/` 目录 | 知识库，沉淀最佳实践 |
| Commands | `plugins/*/commands/` | 用户入口 |
| Rules | `skills/git-workflow/` | 合并到 skills 中 |
| Hooks | 暂不实现 | 后续可扩展 |
| Contexts | 暂不实现 | 后续可扩展 |

**我们的选择**：
- 不追求大而全，聚焦解决 2 个核心问题
- 渐进式采用，先跑通再扩展
- 团队定制，针对前端团队的实际需求

---

## 扩展方向

当前方案稳定后，可考虑扩展：

1. **Hooks（自动化触发）**
   - pre-commit: 提交前自动检查
   - on-mr-create: MR 创建时自动审查

2. **更多 Skills**
   - vue-patterns: Vue 最佳实践
   - testing-patterns: 测试模式
   - security-checklist: 安全检查清单

3. **更多 Agents**
   - code-reviewer: 代码审查
   - security-reviewer: 安全审查

---

## 参考资料

- [Everything Claude Code](https://github.com/affaan-m/everything-claude-code)
- [Conventional Commits](https://www.conventionalcommits.org/)

---
