# Branch Commands Plugin

Git 分支工作流命令集合。

## 命令列表

### /branch-create

创建新分支，自动版本号。

```bash
/branch-create [type] [base_branch] [ide]
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `type` | feat, fix, hotfix | 必填 |
| `base_branch` | 基础分支 | dev |
| `ide` | windsurf, vscode | windsurf |

示例：
```bash
/branch-create feat              # feat-xxx-v3
/branch-create fix master        # fix-xxx-v2 基于 master
```

### /branch-switch

智能切换分支（模糊搜索）。

```bash
/branch-switch [keyword]
```

示例：
```bash
/branch-switch                   # 显示最近分支列表
/branch-switch login             # 匹配包含 login 的分支
/branch-switch 3                 # 切换到列表第 3 个分支
```

### /branch-delete

清理已合并/过期分支。

```bash
/branch-delete [option]
```

示例：
```bash
/branch-delete                   # 显示可清理的分支
/branch-delete merged            # 删除所有已合并分支
/branch-delete feat-old-v1       # 删除指定分支
```

## 安全规则

- 永不删除：main, master, dev
- 永不删除当前分支
- 删除远端分支需确认

## 安装

```bash
/plugin install branch-commands@team-plugins
```
