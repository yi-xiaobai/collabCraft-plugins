# MR Commands Plugin

GitLab Merge Request 工作流命令集合。

## 命令列表

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

| # | Title | Author | Branch | Updated | Pipeline |
|---|-------|--------|--------|---------|----------|
| #42 | feat: add login | zhangsan | feat/login → dev | 2026-03-12 | ✅ |
| #41 | fix: order calc | lisi | fix/order → dev | 2026-03-11 | ❌ |
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

## 安装

```bash
/plugin install mr-commands@team-plugins
```

## 配置

在 `~/.config/git-agent/.env` 中配置：

```bash
GITLAB_TOKEN=glpat-xxxxxxxxxx
GITLAB_HOST=gitlab.company.com
```

## Troubleshooting

### 401 Unauthorized
- Token 过期或无效
- Token 缺少 `api` 权限

### No MRs shown
- 检查是否有 open 状态的 MR
- 使用 `--all` 查看所有 MR
