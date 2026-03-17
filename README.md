# Team Claude Code Plugins

团队 Git 工作流插件集合。

## 插件列表

| 插件 | 命令 | 说明 |
|------|------|------|
| **branch-commands** | `/branch-create`, `/branch-switch`, `/branch-delete` | Git 分支工作流 |
| **commit-commands** | `/commit`, `/commit-push`, `/commit-push-mr`, `/commit-undo` | Git 提交工作流 |
| **mr-commands** | `/mr-list` | GitLab MR 工作流 |
| **plugin-linter** | `/plugin-lint` | 插件规范检查 |

> **个人效率工具**（Skills）：
> - `/log` → work-log skill
> - `/build` → turtle-build skill
> - `/trending` → github-trending skill

## 快速开始

### 0. 环境配置（首次使用）

#### 安装 glab CLI

```bash
# macOS
brew install glab

# Linux (Debian/Ubuntu)
sudo apt install glab

# Linux (RHEL/Fedora)
sudo dnf install glab
```

#### 认证

```bash
glab auth login
```

> 按提示选择 GitLab 实例（gitlab.com 或私有实例），选择认证方式（token 或浏览器）

### 1. 添加 Marketplace

```bash
# 本地测试
/plugin marketplace add ./team-plugins
```

### 2. 安装插件

```bash
/plugin install branch-commands commit-commands mr-commands plugin-linter@team-plugins
```

### 3. 使用

```bash
# 分支管理
/branch-create feat              # 创建功能分支
/branch-switch login             # 切换到包含 login 的分支
/branch-delete merged            # 删除已合并分支

# 提交工作流
/commit                          # 提交
/commit-push                     # 提交并推送
/commit-push-mr                  # 提交、推送并创建 MR
/commit-undo                     # 撤销最后一次提交

# MR 管理
/mr-list                         # 查看我的 MR
/mr-list --all                   # 查看所有 MR

# 插件开发
/plugin-lint                     # 检查所有插件规范
/plugin-lint path/to/file.md     # 检查单个文件
```

## 目录结构

```
team-plugins/
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   ├── branch-commands/
│   │   ├── commands/
│   │   │   ├── branch-create.md
│   │   │   ├── branch-switch.md
│   │   │   └── branch-delete.md
│   │   └── README.md
│   ├── commit-commands/
│   │   ├── commands/
│   │   │   ├── commit.md
│   │   │   ├── commit-push.md
│   │   │   ├── commit-push-mr.md
│   │   │   └── commit-undo.md
│   │   └── README.md
│   ├── mr-commands/
│   │   ├── commands/mr-list.md
│   │   └── README.md
│   └── plugin-linter/
│       ├── commands/plugin-lint.md
│       └── README.md
└── README.md
```

## Plugin vs Skill

| 类型 | 用途 | 分发方式 |
|------|------|----------|
| **Plugin** | 团队共享、标准化工作流 | Marketplace |
| **Skill** | 个人效率、本地配置 | `~/.claude/skills/` |

**判断标准**：
- 需要团队统一版本 → Plugin
- 个人配置（路径、webhook）→ Skill


## 贡献指南

1. 创建功能分支
2. 添加/修改插件
3. 更新 README.md
4. 提交 MR 审核
