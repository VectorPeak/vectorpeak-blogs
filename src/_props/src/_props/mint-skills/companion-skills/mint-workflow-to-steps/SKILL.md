---
name: mint-workflow-to-steps
description: Convert numbered workflows, arrow flows, ASCII process lists, procedure text, Agent loops, RAG flows, or step-by-step process blocks into Mintlify MDX Steps and Step components. Use when the user gives an MDX file path plus workflow text and asks to update the original MDX, or when they ask to turn a flow into Mint Steps instead of Mermaid.
---

# Mint Workflow To Steps

Use this skill to convert workflow/process text into Mintlify-native `<Steps>` components.

## Workflow

1. Locate the exact source block in the target `.mdx` file when a path is provided
2. Preserve the original process semantics and order
3. Convert each numbered stage or major arrow segment into one `<Step title="...">`
4. Keep titles short, action-oriented, and scannable
5. Put details, sub-questions, and output destinations inside the step body
6. Use Markdown lists inside a `<Step>` when one stage contains parallel checks or branches
7. Use backticks for paths, commands, identifiers, filenames, tool names, and code-like terms
8. Avoid trailing punctuation at Chinese paragraph ends when editing this user's docs
9. Replace the original workflow block directly in the MDX file and verify the local Mintlify page when practical

## Reference

Read `references/mint-steps.md` for the exact component pattern and few-shot examples.
