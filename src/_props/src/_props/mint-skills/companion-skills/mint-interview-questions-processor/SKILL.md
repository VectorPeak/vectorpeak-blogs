---
name: mint-interview-questions-processor
description: Convert interview question and answer sections in Mintlify MDX documents into AccordionGroup and Accordion components. Use when the user provides an MDX path or interview Q&A paragraphs and wants Q1, Q2, Qn style questions rendered as collapsed Mintlify accordions by default, with each question as the accordion title and each answer as the accordion body.
---

# Mint Interview Questions Processor

Use this skill to process interview-question sections in `.mdx` documents.

## Boundaries

Stop processing when reaching a same-level or higher-level heading, `## 参考资料`, `## References`, `<Tabs>`, or a new numbered chapter. Do not consume reference sections, source lists, or unrelated follow-up chapters.

Escape question text before placing it in an Accordion title attribute. Replace double quotes with `&quot;` and avoid raw `{`, `}`, `<`, or `>` in title attributes.

## Workflow

1. Locate the interview section in the target MDX file
2. Identify each question title:
   * `Q1：...`
   * `Q1: ...`
   * `**Q1：...**`
   * `### Q1：...`
3. Treat all content after a question title and before the next question title as that question's answer
4. Convert the section into:
   * one `<AccordionGroup>`
   * one `<Accordion title="Qn: 问题">` per question
5. Add a Markdown horizontal rule `---` at the end of every accordion body, immediately before `</Accordion>`
6. Preserve answer Markdown formatting, including lists, code spans, tables, and paragraphs
7. Use `Q{n}: 问题` as the accordion title
8. Keep accordions closed by default; do not add `defaultOpen` unless the user explicitly asks
9. Do not rewrite answers unless needed to make MDX valid
10. After editing a file, verify the local Mintlify page when practical

## Reference

Read `references/mint-accordions.md` for the component pattern and conversion example.
