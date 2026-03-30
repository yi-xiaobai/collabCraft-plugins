# Agency Agents Scripts 分析

> 来源：[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents/tree/main/scripts)

该项目提供了一套 AI Agent 管理脚本，用于将统一格式的 Agent 定义文件转换并安装到各种 AI 编码工具中。

---

## 脚本概览

| 脚本 | 功能 | 大小 |
|------|------|------|
| `convert.sh` | 将 Agent `.md` 文件转换为各工具专用格式 | 18KB |
| `install.sh` | 将转换后的文件安装到本地工具配置目录 | 23KB |
| `lint-agents.sh` | 验证 Agent 文件格式是否符合规范 | 2.6KB |

---

## 1. convert.sh — 格式转换器

### 功能

将统一的 Agent Markdown 文件转换为各种 AI 编码工具的专用格式。

### 支持的工具

| 工具 | 输出格式 | 输出目录 |
|------|----------|----------|
| **Antigravity** | SKILL.md (Gemini 技能) | `integrations/antigravity/` |
| **Gemini CLI** | skills/ + gemini-extension.json | `integrations/gemini-cli/` |
| **OpenCode** | .md (YAML frontmatter) | `integrations/opencode/agents/` |
| **Cursor** | .mdc (Cursor 规则) | `integrations/cursor/rules/` |
| **Aider** | 单一 CONVENTIONS.md | `integrations/aider/` |
| **Windsurf** | 单一 .windsurfrules | `integrations/windsurf/` |
| **OpenClaw** | SOUL.md + AGENTS.md + IDENTITY.md | `integrations/openclaw/` |
| **Qwen** | SubAgent .md 文件 | `integrations/qwen/agents/` |
| **Kimi** | agent.yaml + system.md | `integrations/kimi/` |

### 使用方式

```bash
# 转换所有工具
./scripts/convert.sh

# 只转换特定工具
./scripts/convert.sh --tool cursor
./scripts/convert.sh --tool windsurf

# 并行转换（加速）
./scripts/convert.sh --parallel --jobs 8

# 指定输出目录
./scripts/convert.sh --out /path/to/output
```

### 核心设计

1. **统一源格式**：所有 Agent 使用相同的 Markdown + YAML frontmatter 格式
2. **多目标输出**：一次编写，多处使用
3. **Frontmatter 解析**：提取 `name`, `description`, `color`, `emoji`, `vibe` 等字段
4. **Body 分离**：将正文内容与元数据分开处理
5. **颜色映射**：将颜色名称（如 `cyan`, `blue`）转换为十六进制值

### 关键函数

```bash
get_field()    # 从 YAML frontmatter 提取字段值
get_body()     # 获取 frontmatter 之后的正文内容
slugify()      # 将名称转换为 kebab-case slug
```

---

## 2. install.sh — 安装器

### 功能

将 `integrations/` 目录中转换好的文件复制到各工具的配置目录。

### 支持的工具及安装位置

| 工具 | 安装位置 | 作用域 |
|------|----------|--------|
| **Claude Code** | `~/.claude/agents/` | 用户级 |
| **Copilot** | `~/.github/agents/` + `~/.copilot/agents/` | 用户级 |
| **Antigravity** | `~/.gemini/antigravity/skills/` | 用户级 |
| **Gemini CLI** | `~/.gemini/extensions/agency-agents/` | 用户级 |
| **OpenCode** | `.opencode/agents/` | 项目级 |
| **Cursor** | `.cursor/rules/` | 项目级 |
| **Aider** | `./CONVENTIONS.md` | 项目级 |
| **Windsurf** | `./.windsurfrules` | 项目级 |
| **OpenClaw** | `~/.openclaw/agency-agents/` | 用户级 |
| **Qwen** | `.qwen/agents/` | 项目级 |
| **Kimi** | `~/.config/kimi/agents/` | 用户级 |

### 使用方式

```bash
# 交互式选择（默认）
./scripts/install.sh

# 安装特定工具
./scripts/install.sh --tool cursor
./scripts/install.sh --tool windsurf

# 非交互式，安装所有检测到的工具
./scripts/install.sh --no-interactive

# 并行安装
./scripts/install.sh --parallel
```

### 核心设计

1. **自动检测**：扫描系统中已安装的 AI 工具
2. **交互式 UI**：终端中显示复选框界面，用户可选择安装哪些工具
3. **进度显示**：tqdm 风格的进度条
4. **并行支持**：可并行安装多个工具

### 检测逻辑

```bash
detect_claude_code()  # 检查 ~/.claude 目录
detect_cursor()       # 检查 cursor 命令或 ~/.cursor 目录
detect_windsurf()     # 检查 windsurf 命令或 ~/.codeium 目录
# ... 其他工具类似
```

---

## 3. lint-agents.sh — 格式验证器

### 功能

验证 Agent Markdown 文件是否符合规范，用于 CI/CD 或提交前检查。

### 检查规则

| 级别 | 检查项 | 说明 |
|------|--------|------|
| **ERROR** | frontmatter 存在 | 必须以 `---` 开头 |
| **ERROR** | `name` 字段 | 必填 |
| **ERROR** | `description` 字段 | 必填 |
| **ERROR** | `color` 字段 | 必填 |
| **WARN** | `Identity` 章节 | 推荐 |
| **WARN** | `Core Mission` 章节 | 推荐 |
| **WARN** | `Critical Rules` 章节 | 推荐 |
| **WARN** | 正文长度 | 少于 50 词会警告 |

### 使用方式

```bash
# 检查所有 Agent 文件
./scripts/lint-agents.sh

# 检查特定文件
./scripts/lint-agents.sh engineering/frontend-developer.md

# 在 CI 中使用（错误时返回非零退出码）
./scripts/lint-agents.sh || exit 1
```

### 输出示例

```
Linting 45 agent files...

ERROR engineering/new-agent.md: missing frontmatter field 'color'
WARN  engineering/new-agent.md: missing recommended section 'Critical Rules'
WARN  design/ui-designer.md: body seems very short (< 50 words)

Results: 1 error(s), 2 warning(s) in 45 files.
FAILED: fix the errors above before merging.
```

---

## 设计思想总结

### 1. 统一源格式，多目标输出

```
┌─────────────────────────────────────────────────────────┐
│              统一 Agent 定义 (.md)                       │
│  ---                                                    │
│  name: Frontend Developer                               │
│  description: Expert in React, Vue, TypeScript          │
│  color: cyan                                            │
│  ---                                                    │
│  ## Identity                                            │
│  You are a frontend development expert...               │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
         ┌────────────────┼────────────────┐
         │                │                │
         ▼                ▼                ▼
   ┌──────────┐    ┌──────────┐    ┌──────────┐
   │  Cursor  │    │ Windsurf │    │  Claude  │
   │  .mdc    │    │ .rules   │    │  .md     │
   └──────────┘    └──────────┘    └──────────┘
```

### 2. 分层架构

```
Agent 定义 (源)
     │
     ▼
convert.sh (转换层)
     │
     ▼
integrations/ (中间产物)
     │
     ▼
install.sh (安装层)
     │
     ▼
各工具配置目录 (目标)
```

### 3. 质量保证

```
lint-agents.sh
     │
     ├── 必填字段检查 (ERROR)
     ├── 推荐章节检查 (WARN)
     └── 内容长度检查 (WARN)
```

---

## 对 team-plugins 的借鉴意义

| Agency Agents 特性 | 可借鉴点 |
|-------------------|----------|
| **统一源格式** | 定义统一的 Agent/Skill 格式规范 |
| **多工具支持** | 考虑支持 Cursor、Windsurf 等其他 AI 工具 |
| **Lint 脚本** | 为 plugin 文件添加格式验证 |
| **交互式安装** | 提供更友好的安装体验 |
| **颜色/Emoji 支持** | 增强 Agent 的视觉识别度 |

### 可直接复用的设计

1. **Frontmatter 规范**：`name`, `description`, `color` 等标准字段
2. **Lint 检查逻辑**：必填字段 + 推荐章节 + 内容长度
3. **Slugify 函数**：名称转 kebab-case 的通用逻辑

---

*文档生成时间：2024-03-30*
*来源：https://github.com/msitarzewski/agency-agents/tree/main/scripts*
