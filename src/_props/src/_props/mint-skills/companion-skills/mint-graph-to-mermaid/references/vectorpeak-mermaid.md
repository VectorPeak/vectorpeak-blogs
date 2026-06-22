# VectorPeak Mermaid Reference

## Visual Rules

* Match VectorPeak light-mode docs: white page, restrained green accents, clear text, minimal decoration
* Use green borders for structure and pale-green fills for grouped domains
* Emphasize the core execution layer with stronger border width, not heavy dark fills
* Keep helper nodes quieter with `#F8FAFC` fill and soft green border
* Avoid dark terminal-style blocks unless the user explicitly requests dark mode
* Avoid too many colors; use green as the brand signal and slate for readable text

## Base Theme

Use this `init` block for most diagrams:

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "htmlLabels": true,
    "nodeSpacing": 42,
    "rankSpacing": 64,
    "padding": 18
  },
  "themeVariables": {
    "background": "#FFFFFF",
    "mainBkg": "#FFFFFF",
    "primaryColor": "#FFFFFF",
    "primaryTextColor": "#0F172A",
    "primaryBorderColor": "#16A34A",
    "lineColor": "#16A34A",
    "clusterBkg": "#F0FDF4",
    "clusterBorder": "#07C983",
    "fontFamily": "Inter, ui-sans-serif, system-ui",
    "fontSize": "15px"
  }
}}%%
```

## Reusable Classes

Append these classes after graph edges:

```mermaid
classDef entry fill:#FFFFFF,stroke:#16A34A,stroke-width:2px,color:#0F172A;
classDef gateway fill:#F0FDF4,stroke:#15803D,stroke-width:2px,color:#052E16;
classDef core fill:#FFFFFF,stroke:#07C983,stroke-width:3px,color:#064E3B;
classDef aux fill:#F8FAFC,stroke:#86EFAC,stroke-width:1.5px,color:#334155;
classDef output fill:#FFFFFF,stroke:#16A34A,stroke-width:2px,color:#0F172A;
```

Use `style AgentLayer fill:#F0FDF4,stroke:#07C983,stroke-width:3px,color:#15803D` for the most important container

## Few-Shot: Standard Output

Prefer this normalized style:

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "htmlLabels": true,
    "nodeSpacing": 42,
    "rankSpacing": 64,
    "padding": 18
  },
  "themeVariables": {
    "background": "#FFFFFF",
    "mainBkg": "#FFFFFF",
    "primaryColor": "#FFFFFF",
    "primaryTextColor": "#0F172A",
    "primaryBorderColor": "#16A34A",
    "lineColor": "#16A34A",
    "clusterBkg": "#F0FDF4",
    "clusterBorder": "#07C983",
    "fontFamily": "Inter, ui-sans-serif, system-ui",
    "fontSize": "15px"
  }
}}%%
flowchart TD
  Trigger["<b>触发层 Trigger</b><br/>Message · Heartbeat · Cron<br/>Webhook · Hooks"]
  Gateway["<b>网关层 Gateway</b><br/>连接管理 · 协议转换<br/>路由分发 · 安全控制<br/>[不调 LLM，不执行工具]"]

  subgraph AgentLayer["Agent 层"]
    direction TB
    Loop["<b>Think → Act → Remember</b><br/>[循环执行，由 LLM 自主决定继续或结束]"]
    Feedback["[工具结果回灌上下文]"]
    Models["<b>可用模型</b><br/>Claude / GPT / Gemini<br/>Qwen / Ollama / ..."]
    Memory["<b>记忆体系</b><br/>Bootstrap · Transcript<br/>Context · Retrieval Index<br/>+ Skill Library（独有）<br/>+ Honcho 用户画像（独有）"]

    Loop --> Feedback --> Loop
    Loop -.-> Models
    Loop -.-> Memory
  end

  Reply["<b>原渠道送回用户</b>"]

  Trigger -->|"事件"| Gateway
  Gateway -->|"统一事件 → session"| AgentLayer
  AgentLayer -->|"最终回复"| Reply

  classDef entry fill:#FFFFFF,stroke:#16A34A,stroke-width:2px,color:#0F172A;
  classDef gateway fill:#F0FDF4,stroke:#15803D,stroke-width:2px,color:#052E16;
  classDef core fill:#FFFFFF,stroke:#07C983,stroke-width:3px,color:#064E3B;
  classDef aux fill:#F8FAFC,stroke:#86EFAC,stroke-width:1.5px,color:#334155;
  classDef output fill:#FFFFFF,stroke:#16A34A,stroke-width:2px,color:#0F172A;

  class Trigger entry;
  class Gateway gateway;
  class Loop,Feedback core;
  class Models,Memory aux;
  class Reply output;
  style AgentLayer fill:#F0FDF4,stroke:#07C983,stroke-width:3px,color:#15803D
```

## Few-Shot Notes

* Good: `<b>触发层 Trigger</b>` inside node labels
* Good: `[不调 LLM，不执行工具]` when the user wants compact inline emphasis
* Good: manual line breaks such as `连接管理 · 协议转换<br/>路由分发 · 安全控制`
* Good: keep node titles centered, then left-align dense list bodies with `<div style='text-align:left'>...</div>`
* Good: bold the main list items, then put explanatory detail on the next line in parentheses
* Avoid: `subgraph AgentLayer["**Agent 层**"]`; use `subgraph AgentLayer["Agent 层"]`
* Avoid: overly long single-line labels; split with `<br/>`

## Few-Shot: Dense Node With Left-Aligned Body

Use this pattern when a single node contains a title plus many parallel components. Keep the title centered, then left-align the dense body so the reader can scan the list vertically:

```mermaid
%%{init: {
  "theme": "base",
  "flowchart": {
    "curve": "basis",
    "htmlLabels": true,
    "nodeSpacing": 42,
    "rankSpacing": 64,
    "padding": 18
  },
  "themeVariables": {
    "background": "#FFFFFF",
    "mainBkg": "#FFFFFF",
    "primaryColor": "#FFFFFF",
    "primaryTextColor": "#0F172A",
    "primaryBorderColor": "#16A34A",
    "lineColor": "#16A34A",
    "clusterBkg": "#F0FDF4",
    "clusterBorder": "#07C983",
    "fontFamily": "Inter, ui-sans-serif, system-ui",
    "fontSize": "15px"
  }
}}%%
flowchart TD
  Context["<b>上下文窗口 · Context Window</b><br/>[每轮重新拼装]<br/><br/><div style='text-align:left'><b>= System Prompt</b><br/>(Bootstrap 文件拼出来的)<br/><b>+ 近期对话切片</b><br/>(从 .jsonl 尾部加载)<br/><b>+ 检索到的 md 片段</b><br/>(memory_search / memory_get 返回的原文)<br/><b>+ Skill 内容</b><br/>(命中时加载 SKILL.md)<br/><b>+ Honcho 用户画像摘要</b><br/><b>+ 当前用户消息 + 工具结果</b></div>"]

  subgraph Sources["<b>三类数据源</b>"]
    direction LR
    Workspace["<b>数据源 1</b><br/>工作空间 md 文件<br/><br/><div style='text-align:left'>Bootstrap Files<br/>+ memory/ 笔记<br/>+ Skill Library</div>"]
    Transcript["<b>数据源 2</b><br/>Session Transcript<br/><br/>.jsonl 对话日志<br/>系统追加写入"]
    Honcho["<b>数据源 3</b><br/>Honcho User Model<br/><br/>外部用户画像服务<br/>自进化循环持续更新"]
  end

  Index["<b>索引 · Retrieval Index</b><br/>[memory/ 的向量 + 全文索引]<br/>[sqlite 本身不进 Context]"]

  Workspace -->|"md 原文"| Context
  Transcript -->|"对话切片"| Context
  Honcho -->|"画像摘要"| Context
  Workspace -->|"被索引"| Index
  Index -.->|"搜索请求"| Workspace

  classDef context fill:#FFFFFF,stroke:#07C983,stroke-width:3px,color:#064E3B;
  classDef source fill:#FFFFFF,stroke:#16A34A,stroke-width:2px,color:#0F172A;
  classDef index fill:#F8FAFC,stroke:#86EFAC,stroke-width:1.5px,color:#334155;

  class Context context;
  class Workspace,Transcript,Honcho source;
  class Index index;
  style Sources fill:#F0FDF4,stroke:#07C983,stroke-width:3px,color:#15803D
```

## Few-Shot: Bracketed Layer Labels

Use this pattern after finishing a Mermaid graph when each node has a title plus one or more explanatory layers. The title layer stays unwrapped. Every later text layer split by `<br/>` is wrapped in `[]`. Subgraph titles may be bold. Edge labels stay unwrapped.

Good:

```mermaid
flowchart TD
  User["<b>用户任务</b><br/>[自然语言请求进入 Parent Agent]"]

  subgraph AgentLayer["<b>Agent · 中心编排与并行执行层</b>"]
    direction TB
    Parent["<b>Parent Agent</b><br/>[LLM 判断是否拆分任务]<br/>[调用 sessions_spawn]"]

    subgraph ChildLayer["<b>Subagents · 并行执行层</b>"]
      direction LR
      ChildA["<b>Subagent A</b><br/>[执行子任务 A]"]
      ChildB["<b>Subagent B</b><br/>[执行子任务 B]"]
      ChildC["<b>Subagent C</b><br/>[可继续 spawn 孙 Agent]"]
    end

    Merge["<b>结果整合</b><br/>[等待所有子任务完成]<br/>[综合输出最终答案]"]
  end

  Reply["<b>最终回复</b><br/>[Parent Agent 对用户负责]"]

  User --> Parent
  Parent -->|"spawn"| ChildA
  Parent -->|"spawn"| ChildB
  Parent -->|"spawn"| ChildC
  ChildA -->|"push 结果"| Merge
  ChildB -->|"push 结果"| Merge
  ChildC -->|"push 结果"| Merge
  Merge --> Reply
```

Bad:

```mermaid
flowchart TD
  User["<b>用户任务</b><br/[]>自然语言请求进入ParentAgent]"]
```

Corrected:

```mermaid
flowchart TD
  User["<b>用户任务</b><br/>[自然语言请求进入 Parent Agent]"]
```

## Escaping

* Wrap labels in double quotes: `A["文本"]`
* Escape literal brackets in labels only when Mermaid parsing fails:
  * `[` -> `&#91;`
  * `]` -> `&#93;`
* Parentheses are usually safe inside quoted labels; if Mintlify/Mermaid parsing fails, replace:
  * `(` -> `&#40;`
  * `)` -> `&#41;`
* Use `<br/>` for new lines inside node labels
* Avoid unquoted `A[文本(说明)]` when labels contain Chinese punctuation or parentheses
