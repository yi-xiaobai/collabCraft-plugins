# 踩坑记录

---

## 新项目第一天该做的

1. 写 `.gitignore` — 先把坑堵上
2. 写 `CLAUDE.md` — 定规矩
3. 定 plugin 模板 — 统一结构
4. 配 pre-commit — 自动检查
5. README 跟代码一起更新 — 别拆开
6. 告诉 LLM 做什么 无需太细致
7. 语言
8. git相关的命令不需要重复封装 告知一些具体规则即可
9. 尽量用终端 ghostty 但是需要具体规则

---

## 参数多的 Plugin 怎么设计

1. 用户记不住 flag — 不要把 flag 当主接口
2. 三层接口：无参 → 菜单、自然语言、显式 flag
3. ≥2 个 flag 或带枚举 — 才值得做成三层
4. 单个 flag / 无参数 — 别过度设计

---

## 总结

1. agents 多个command之间可以复用的 单个command的没必要agents
2. skills 让AI自主执行
3. rule 规则 git适合根据不同的项目写在rules中 但可以考虑动态的rules？ 可以作为一个skills 
    每个项目不同的提交结构和方式 抽离出来
4. hooks 
5. 通用能力交给 LLM，团队知识和软性判断交给 Skills，强制约束交给 Hooks/CI
6. Commands 只保留多步骤、跨系统或需要明确入口的完整工作流
7. 单个 Command 专用的逻辑不拆 Agent，只有跨工作流复用时才值得委派




## team

1. 怎么让agent改变工作流？
2. 团队成员之间的agent交互设计
3. 以什么形式 skills plugins 还是纯md文件
4. 需要什么样的步骤让agent正常运转？

最终：以skills形式来呈现
