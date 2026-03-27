# deploy-commands

通用构建发布工作流插件，适用于任何 Node.js/前端项目。

## 命令

| 命令 | 说明 |
|------|------|
| `/build` | 构建当前项目 |
| `/publish [type]` | 发布到 npm registry |
| `/release [type]` | 完整发布流程：build → version → publish → push |

## 使用示例

```bash
# 构建项目
/build

# 发布 patch 版本
/publish patch

# 发布 minor 版本到 beta 标签
/publish minor --tag=beta

# 完整发布流程
/release patch

# 预览发布流程（不执行）
/release minor --dry-run
```

## 特性

- **自动检测包管理器**: npm / yarn / pnpm
- **智能构建**: 自动识别 build/compile/dist 脚本
- **安全检查**: 
  - 检查工作目录是否干净
  - 检查是否在正确分支
  - 检查 npm 登录状态
- **完整发布**: 版本号、git tag、npm publish 一步完成

## 版本类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `patch` | 补丁版本 | 1.0.0 → 1.0.1 |
| `minor` | 次版本 | 1.0.0 → 1.1.0 |
| `major` | 主版本 | 1.0.0 → 2.0.0 |
| `prerelease` | 预发布 | 1.0.0 → 1.0.1-0 |

## 前置条件

- 项目根目录有 `package.json`
- 已配置 npm registry（默认或私有）
- 已登录 npm: `npm login`
