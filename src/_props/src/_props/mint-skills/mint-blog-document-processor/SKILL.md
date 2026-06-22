---
name: mint-blog-document-processor
description: Mintlify MDX document processor. Always run mint-blog-formatter first, then format tree blocks, convert structure and flow diagrams into Mermaid, process interview accordions, and process reference tabs while updating the original MDX file.
---

# Mint Blog Document Processor

Use this skill when the user provides an `.mdx` path and asks for document-level processing.

For `docs.json` navigation work such as tabs, groups, page order, route validation, or group icons, use `../companion-skills/mint-navigation-processor/SKILL.md` instead. This skill owns single-document MDX processing, not site navigation.

## Current Scope

0. Required blog formatting:
   * Always process the MDX file with `mint-blog-formatter` first
   * Ensure a Written month Badge appears immediately after the first body Markdown heading
   * Use the current month in `YYYY.MM` format
1. Tree-like text formatting:
   * Identify directory trees, file trees, project structures, and skill folder structures
   * Always process them by using the `mint-treeliketext-formatter` skill
   * Normalize them into titled Mintlify code fences with `icon="folder-tree"`
2. Structure diagram and flow diagram handling:
   * Identify PNG/image diagrams that represent workflows, structures, architecture, or process flows
   * Identify ASCII/text flow blocks that represent workflows, structures, architecture, or process flows
   * Convert them into Mermaid using the `mint-graph2mermaid` skill style
   * Preserve the original structure, content, ordering, and relationships; only improve visual style, color, spacing, and Mermaid syntax
   * Insert the Mermaid block into the original MDX file
   * Comment out the original PNG/text block directly below or above the Mermaid replacement
3. Interview question section handling:
   * Identify interview sections containing `Q1`, `Q2`, or `Qn` question-answer blocks
   * Always process them by using the `mint-interview-questions-processor` skill
   * Convert them into Mintlify `AccordionGroup` and collapsed-by-default `Accordion` components
   * Add `---` at the end of every accordion body
4. Reference section handling:
   * Identify reference sections such as `## 参考资料`, `## References`, or numbered variants like `## 1.7 参考资料`
   * Always process them by using the `mint-reference-processor` skill
   * Convert real references into categorized Mintlify `Tabs` and `Card` components
   * Comment out missing categories instead of rendering empty tabs

## Workflow

1. Read the target MDX file with UTF-8
2. Run `mint-blog-formatter` as the required first pass:
   * Insert or update `<Badge icon="clock" color="green">Written: YYYY.MM</Badge>`
   * Place it immediately after the first body Markdown heading and directly before the first body paragraph, with no blank line after the Badge
   * Do not continue to other processors until this formatting pass is complete
3. Locate candidate tree-like text blocks:
   * Fenced blocks containing `├──`, `└──`, `│`, `|--`, `+--`, or directory/file indentation
   * Sections introduced by labels like `文件结构`, `目录结构`, `项目结构`, `Skill 文件结构`
4. For accepted tree-like blocks:
   * Use `mint-treeliketext-formatter` rules; this is required whenever tree-like code/text blocks are detected
   * Keep the block as copyable code
   * Add or normalize `title="..." icon="folder-tree"` on the fence
5. Locate candidate diagram blocks:
   * Markdown images: `![...](...png...)`, `![...](...jpg...)`, `![...](...webp...)`
   * HTML images: `<img src="...">`
   * ASCII boxes with `┌`, `└`, `│`, arrows, numbered vertical flows, or fenced process text
   * Rough text flows with `->`, `→`, `↓`, `├─`, `└─`
6. Decide whether each candidate is really a structure/process diagram
7. For each accepted candidate:
   * Generate Mermaid according to `mint-graph2mermaid`
   * Prefer VectorPeak light-mode styling for VectorPeak/Mint docs
   * Preserve the original structure, labels, content, ordering, and relationships
   * Do not simplify, merge, reorder, or reinterpret the diagram unless the user explicitly asks
   * Only change presentation: Mermaid syntax, layout direction when needed, colors, spacing, line breaks, classes, and visual polish
8. Replace the original visible block with the Mermaid block
9. Preserve the original source in an MDX comment:
   * Use `{/* ... */}` for one-line sources
   * Use a multi-line MDX comment for long text blocks
10. Locate explicit workflow-to-Steps requests:

* User asks for Mint `<Steps>`, `<Step>`, or "step 格式"
* Workflow text is numbered, arrow-based, or procedural but should not become Mermaid

11. For accepted workflow-to-Steps requests:

* Use `mint-workflow2steps` rules
* Convert the workflow into `<Steps>` and `<Step title="...">`
* Preserve parallel branches as Markdown lists inside the relevant step

12. Locate candidate interview question sections:

* Headings like `## 面试问题`, `## Interview Questions`, `### 面试题`
* Question titles like `Q1：...`, `Q1: ...`, `**Q1：...**`, or `### Q1：...`

13. For accepted interview sections:

* Use `mint-interview-questions-processor` rules; this is required whenever interview questions are detected
* Wrap all Q\&A blocks in one `<AccordionGroup>`
* Use `<Accordion title="Qn: 问题">`
* Keep the answer as the accordion body
* Add `---` before each closing `</Accordion>`

14. Locate candidate reference sections:

* Headings like `## 参考资料`, `## References`, `## 参考文献`, `## Links`
* Numbered headings like `## 1.7 参考资料`
* Link lists containing source code, video, paper, document, author, UP 主, or webpage references

15. For accepted reference sections:

* Use `mint-reference-processor` rules; this is required whenever a reference section is detected
* Convert real references into categorized `<Tabs>` and `<Card>` components
* Render only categories with actual references
* Preserve missing category placeholders as MDX comments

16. Verify the MDX is still syntactically reasonable and, when the local Mintlify server is available, check the page returns HTTP 200
17. In the final response, report changed files and summarize converted blocks

## Required Companion Skill

Before any other processing, read and follow:

`../companion-skills/mint-blog-formatter/SKILL.md`

and, when needed:

`../companion-skills/mint-blog-formatter/references/written-badge.md`

When processing tree-like text blocks, read and follow:

`../companion-skills/mint-treeliketext-formatter/SKILL.md`

and, when needed:

`../companion-skills/mint-treeliketext-formatter/references/tree-code-fences.md`

When producing Mermaid, read and follow:

`../companion-skills/mint-graph2mermaid/SKILL.md`

and, when needed:

`../companion-skills/mint-graph2mermaid/references/vectorpeak-mermaid.md`

When the user explicitly asks for Mintlify Steps, read and follow:

`../companion-skills/mint-workflow2steps/SKILL.md`

and, when needed:

`../companion-skills/mint-workflow2steps/references/mint-steps.md`

When processing interview questions, read and follow:

`../companion-skills/mint-interview-questions-processor/SKILL.md`

and, when needed:

`../companion-skills/mint-interview-questions-processor/references/mint-accordions.md`

When processing reference sections, read and follow:

`../companion-skills/mint-reference-processor/SKILL.md`

and, when needed:

`../companion-skills/mint-reference-processor/references/reference-tabs.md`

## Reference

Read `references/diagram-commenting.md` for comment formats and replacement examples.
