---
name: mint-graph-to-mermaid
description: Convert rough process text, ASCII structure diagrams, architecture notes, Agent/RAG flows, layered system graphs, or existing Mermaid drafts into Mintlify-ready Mermaid diagrams using VectorPeak light-mode visual style. Use when the user asks for Mermaid output, graph-to-Mermaid conversion, structure/process/architecture diagrams, or diagrams matching https://vectorpeak.cn/.
---

# Mint Graph To Mermaid

Use this skill to produce polished Mermaid blocks for Mintlify documents, especially VectorPeak docs in light mode.

## Boundaries

Use Mermaid for relationship diagrams: layered systems, data flow, Agent/RAG pipelines, loops, parallel branches, and architecture maps.

Do not use this skill for directory trees, file structures, pure command output, reference link lists, interview Q\&A, plain tables, or linear install/checklist steps. Route those to the matching formatter or leave them as code/text.

## Workflow

1. Preserve the user's structure and content first, then improve layout and styling
   * Do not add, remove, merge, split, reorder, or reinterpret nodes and relationships unless the user explicitly asks
   * For existing diagrams or text diagrams, treat the input as the source of truth and change only the visual presentation
2. Use `flowchart TD` for layered flows, Agent loops, RAG pipelines, gateway structures, and architecture overviews
3. Use VectorPeak light-mode colors by default:
   * primary green `#16A34A`
   * light green `#07C983`
   * dark green `#15803D`
   * pale green `#F0FDF4`
   * text `#0F172A`
4. Use quoted labels for all non-trivial nodes
5. Use `<br/>` for controlled line breaks inside labels
6. Use `<b>...</b>` for emphasis inside Mermaid labels; avoid Markdown emphasis such as `**Agent 层**` inside node or subgraph labels
7. Use subgraphs for large containers such as Agent 层、Gateway、Memory、RAG Pipeline、Deployment
8. Prefer white nodes with green borders and pale-green containers; avoid dark mode unless explicitly requested
9. After completing the Mermaid graph, run a label cleanup pass:
   * Keep the title layer unwrapped, usually as `<b>Title</b>`
   * Treat each `<br/>` as a visual layer separator
   * Wrap every non-title text layer after `<br/>` in square brackets, for example `<b>Parent Agent</b><br/>[LLM 判断是否拆分任务]<br/>[调用 sessions_spawn]`
   * Do not wrap edge labels such as `spawn`, `事件`, `最终回复`
   * Keep bracket syntax valid inside quoted labels; use `<br/>[text]`, never `<br/[]>text]`
   * Before applying this rule, read the "Few-Shot: Bracketed Layer Labels" section in `references/vectorpeak-mermaid.md`
10. When editing an existing Mermaid block, keep its semantic structure and content stable; update the init block, classes, colors, spacing, and label line breaks only
11. When editing a project file, replace the old ASCII or Mermaid block directly and verify the local Mintlify page when practical

## Reference

Read `references/vectorpeak-mermaid.md` before generating or editing the actual Mermaid block. It contains the default init block, class definitions, escaping rules, and few-shot examples.
