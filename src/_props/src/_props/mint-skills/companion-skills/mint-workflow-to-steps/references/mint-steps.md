# Mint Steps Reference

## Component Pattern

Use this structure:

```mdx
<Steps>
  <Step title="第一步标题">
    第一步说明
  </Step>

  <Step title="第二步标题">
    第二步说明

    - 并列项 A
    - 并列项 B
  </Step>
</Steps>
```

## Style Rules

* Use `<Steps>` as the container and `<Step title="...">` for each stage
* Keep each title short; prefer 4-10 Chinese characters when possible
* Do not include the step number in the title unless the user explicitly wants numbering
* Put code-like strings in backticks: `periodic nudge`, `memory/YYYY-MM-DD.md`, `SKILL.md`
* Use arrows `→` inside body text for mappings
* When one step branches into multiple outputs, use a Markdown bullet list inside that `<Step>`
* Avoid double closing parentheses and fix obvious punctuation issues from rough input
* Do not use Mermaid for workflows when the user explicitly asks for Mint `<Steps>`

## Few-Shot: Agent Self-Evolution Workflow

Input:

```text
1. 用户下达任务（自然语言）
   ↓
2. Agent 执行（Think -> Act 循环）
   ↓
3. 每 ~10 次 tool call，Agent 主动暂停（periodic nudge）
   ↓
4. 自问三件事：
   ① 这次学到的东西值不值得保留？
   ② 有没有失败的步骤需要记下来避免？
   ③ 成功的流程能不能抽象成可复用 skill？
   ↓
5. 值得保留 -> 分三路沉淀到对应记忆层：
   ├─ 事实性知识 -> memory/YYYY-MM-DD.md        （更新 Retrieval Index）
   ├─ 程序性流程 -> skills/xxx/SKILL.md          （更新 Skill Library）
   └─ 用户偏好   -> Honcho User Model            （更新用户画像）
   ↓
6. 下次遇到类似任务 -> 直接命中 skill，跳过重新推理
```

Output:

```mdx
<Steps>
  <Step title="用户下达任务">
    用户用自然语言提出任务
  </Step>

  <Step title="Agent 执行任务">
    Agent 进入 Think → Act 循环，持续推理、调用工具、观察结果并继续决策
  </Step>

  <Step title="周期性触发反思">
    每约 10 次 tool call，Agent 主动暂停一次，触发 `periodic nudge`
  </Step>

  <Step title="自问三件事">
    Agent 会判断这次执行是否值得沉淀：

    - 这次学到的东西值不值得保留？
    - 有没有失败步骤需要记下来，避免下次重复？
    - 成功流程能不能抽象成可复用 skill？
  </Step>

  <Step title="三路沉淀到记忆层">
    如果值得保留，Hermes 会把结果写入三个位置：

    - 事实性知识 → `memory/YYYY-MM-DD.md`，更新 Retrieval Index
    - 程序性流程 → `skills/xxx/SKILL.md`，更新 Skill Library
    - 用户偏好 → Honcho User Model，更新用户画像
  </Step>

  <Step title="下次直接复用">
    下次遇到类似任务时，Agent 可以直接命中 skill，减少重复推理
  </Step>
</Steps>
```
