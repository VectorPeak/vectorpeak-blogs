# Written Badge Reference

## Preferred Form

```mdx
---
title: "Hermes Agent"
description: "介绍 Hermes Agent 的自我进化循环、记忆系统、Skill Library 以及与 OpenClaw 的核心差异"
icon: "horse-head"
iconType: "regular"
---

## Hermes Agent

<Badge icon="clock" color="green">Written: 2026.05</Badge>
如果说 2025 年的风向标是 Manus，2026 年初是 OpenClaw...
```

## Replacement Rules

If the frontmatter description is English:

```mdx
description: "OpenClaw Agent architecture, memory system, multi-agent communication, and interview notes"
```

Translate or summarize it in Chinese while keeping the `description:` key:

```mdx
description: "介绍 OpenClaw Agent 的架构设计、记忆系统、多智能体通信机制与面试重点"
```

If this exists:

```mdx
<Badge icon="clock" color="green">Written: 2026.04</Badge>
```

Move it below the first body Markdown heading and replace it with the required current-month form:

```mdx
## Hermes Agent

<Badge icon="clock" color="green">Written: 2026.05</Badge>
如果说 2025 年的风向标是 Manus，2026 年初是 OpenClaw...
```

If this exists:

```mdx
<Badge>Written: 2026.04</Badge>
```

Normalize icon and color:

```mdx
<Badge icon="clock" color="green">Written: 2026.05</Badge>
```

## Edge Cases

* If there is no frontmatter but a heading exists, insert the Badge immediately after the first heading
* If there is no heading, insert the Badge at the very top, then a blank line
* If multiple Written badges exist near the top, keep the first normalized one and remove duplicates
* Do not modify other badges that do not contain `Written:`
