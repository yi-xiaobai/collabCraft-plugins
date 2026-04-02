# MR Commands Plugin

GitLab Merge Request 工作流命令集合。

## 命令列表

### /mr-title

```bash
/mr-title [target-branch]
```

根据当前分支的 git commits 生成 MR title 和 description。

| 参数 | 说明 |
|------|------|
| `target-branch` | 目标分支（默认 `dev`） |

示例：
```bash
/mr-title           # 对比 dev 分支
/mr-title main      # 对比 main 分支
```

输出示例：
```
📝 MR Title

feat(auth): add OAuth2 login support

📄 MR Description

## 变更概述
实现 OAuth2 登录功能，支持 GitHub 和 Google 账号登录。

## 主要变更
- **feat**: 添加 OAuth2 认证模块
- **feat**: 集成 GitHub/Google 登录按钮

## 提交记录
| Commit | Message |
|--------|---------|
| a1b2c3d | feat(auth): add OAuth2 provider config |
| e4f5g6h | feat(auth): implement login callback |
```

---

### /mr-list

```bash
/mr-list [--all]
```

查看 MR 列表。

| 参数 | 说明 |
|------|------|
| `--all` | 显示所有 MR（默认只显示当前用户的） |

示例：
```bash
/mr-list           # 我的 MR
/mr-list --all     # 所有 MR
```

输出示例：
```
📋 group/project - Open MR List (3)

| # | Title | Author | Branch | Updated |
|---|-------|--------|--------|---------|
| #42 | feat: add login | zhangsan | feat/login → dev | 2026-03-12 |
| #41 | fix: order calc | lisi | fix/order → dev | 2026-03-11 |
```

## 扩展命令（规划中）

| 命令 | 说明 | 优先级 |
|------|------|--------|
| `/mr-create` | 创建 MR | ⭐⭐⭐ |
| `/mr-view` | 查看 MR 详情 | ⭐⭐ |
| `/mr-merge` | 合并 MR | ⭐⭐ |
| `/mr-approve` | 批准 MR | ⭐ |
| `/mr-comment` | 添加评论 | ⭐ |
| `/mr-pipeline` | 查看 Pipeline 状态 | ⭐ |

> 💡 **Tip**: 使用 `/mr-title` 生成 title 和 description 后，可以直接用于 `/mr-create`

## 安装

```bash
/plugin install mr-commands@team-plugins
```

## Troubleshooting

### glab: command not found
运行 `brew install glab` 安装

### glab auth error
运行 `glab auth login` 重新认证

### No MRs shown
- 检查是否有 open 状态的 MR
- 使用 `--all` 查看所有 MR
