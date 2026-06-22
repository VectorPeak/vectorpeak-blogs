---
name: mint-blog-formatter
description: Format Mintlify MDX blog documents and ensure the required Written month badge exists. Use when processing an MDX article to insert or update a Written Badge immediately after the first body Markdown heading and before the first body paragraph, localize frontmatter description, conservatively wrap whitelisted technical terms in inline code, fix paragraph/list spacing, and normalize fenced code block language tags and text block content.
---

# Mint Blog Formatter

Use this skill as the required first formatting pass for Mintlify blog/document MDX files.

## Required Badge

Every processed MDX article must contain a Written badge immediately after the first body Markdown heading and before the first body paragraph:

```mdx
<Badge icon="clock" color="green">Written: YYYY.MM</Badge>
```

Rules:

1. Use the current month from the runtime date in `YYYY.MM` format
2. For 2026-05-30, the badge must be:
   ```mdx
   <Badge icon="clock" color="green">Written: 2026.05</Badge>
   ```
3. If a `Written:` Badge already exists near the top of the document, move it to immediately after the first body Markdown heading and update it to the current month and required icon/color
4. Do not insert duplicate Written badges
5. Place the Badge directly after the first body Markdown heading, then put the first body paragraph immediately after the Badge with no blank line
6. Keep YAML frontmatter unchanged except for the `description:` localization rule below or when the user explicitly asks

## Required Frontmatter Description

When the MDX file has YAML frontmatter, normalize the `description:` value into Chinese.

Rules:

1. If `description:` is English, translate it into concise natural Chinese
2. If the original description is too generic, inaccurate, or keyword-stuffed, replace it with a one-sentence Chinese summary of the full article
3. Keep the same YAML key, quoting style, and frontmatter order when practical
4. Do not change `title`, `icon`, `iconType`, or other frontmatter fields unless the user explicitly asks
5. Keep the Chinese description short enough for Mintlify navigation and SEO snippets, usually one sentence

## Required Technical Term Inline Code

For body text only, conservatively wrap whitelisted technical terms with inline code backticks.

Rules:

1. Do not process Markdown headings, YAML frontmatter, fenced code blocks, Mermaid blocks, MDX component tags, component attributes, URLs, or existing inline code
2. Do process normal paragraphs, list items, blockquote body text, and Accordion body text
3. Only wrap terms that match the whitelist below or an obvious versioned/qualified expansion of a whitelist term
4. Prefer the longest safe match:
   * `Node.js 22+` instead of only `Node`
   * `TypeScript` instead of only `Type`
   * `memory_search` as a whole token
5. Do not wrap common product/article titles unless they are in the whitelist and clearly used as technical terms
6. Avoid wrapping the same term twice; preserve existing backticks
7. If unsure, leave the text unchanged

Default whitelist:

```text
Node
Node.js
TypeScript
JavaScript
ESM
npm
CLI
API
Subagent
WebSocket
HTTP
SQLite
JSONL
Markdown
BM25
embedding
prompt
Context Window
Compaction
Bootstrap Files
Session Transcript
Retrieval Index
memory_search
memory_get
sessions_spawn
subagent
ACP
CDP
Shell
cron
```

## Required Parentheses Normalization

Normalize Chinese parentheses in article body text.

Rules:

1. Replace Chinese full-width parentheses `（` and `）` with ASCII parentheses `(` and `)`
2. Do not process YAML frontmatter, fenced code blocks, Mermaid blocks, MDX component tags, component attributes, URLs, or existing inline code
3. Do not change Markdown heading text unless the user explicitly asks
4. Do process normal paragraphs, list items, blockquote body text, and Accordion body text
5. Preserve the text inside the parentheses unchanged
6. If a line mixes MDX syntax and body text, only normalize the body text portion when it is clearly safe

## Required Paragraph And List Spacing

Normalize spacing between body paragraphs, bold labels, and lists so Mintlify/MDX does not collapse adjacent text and list items into one paragraph.

Rules:

1. Do not process YAML frontmatter, fenced code blocks, Mermaid blocks, MDX component tags, component attributes, URLs, or existing inline code
2. Treat a standalone bold-only line such as `**索引范围**` or `**混合搜索**` as a small body heading, and insert one blank line after it before any paragraph, list, code fence, or tree block
3. Insert one blank line between a bold label line and the following explanatory paragraph
4. Insert one blank line before a list when a normal paragraph or bold label is immediately followed by `-`, `*`, or `•`
5. For explanatory body lists, keep one blank line between list items to produce a readable loose list in Mintlify; this includes list items that start with a bold keyword such as `• **只索引文件** - ...`, contain parentheses explanations, or contain full-sentence descriptions
6. Preserve compact lists only when they are inside cards, tables, navigation-like short lists, or clearly intentional dense reference blocks
7. Prefer standard Markdown list markers `-` for newly formatted content; keep existing `•` only when changing it would create noisy churn

## Required Code Fence Normalization

Normalize fenced code blocks so Mintlify renders them predictably.

Decision table:

1. Preserve an existing correct tag and metadata
2. `flowchart`, `sequenceDiagram`, `classDiagram`, or Mermaid init blocks -> `mermaid`
3. Tree glyphs (`├──`, `└──`, `│`) or clear file/folder hierarchy -> `text title="..." icon="folder-tree"` and route to `mint-directory-tree-formatter`
4. JSON object/array with quoted keys -> `json`
5. YAML frontmatter/config only -> `yaml`; if prose or Markdown follows the YAML, split into a second `text` or `mdx` fence
6. TypeScript/JavaScript syntax such as `type`, `interface`, `const`, `import`, `export` -> `ts` or `js`
7. Shell commands, aliases, npm/git commands -> `bash`; PowerShell-specific commands -> `powershell`
8. Logs, command output, API signatures, pseudo-code, ASCII flows, and uncertain blocks -> `text`

Rules:

1. Every fenced code block must have a language tag after the opening fence
   * Use `mermaid` for Mermaid diagrams
   * Use `python`, `json`, `ts`, `tsx`, `js`, `bash`, `powershell`, `yaml`, `mdx`, or other precise tags when obvious
   * Use `text` for plain text, command snippets, logs, API signatures, tool names, or pseudo-code
2. Preserve existing correct language tags and Mintlify code fence metadata such as `title="..."` or `icon="..."`
3. For `text` code fences, lightly clean prose/pseudo-code content:
   * Remove Markdown list markers that were accidentally placed inside a plain text code block when the block is not intended to be a list, for example `- \`sessions\_spawn\`: ...`becomes`sessions\_spawn: ...\`
   * Remove stray inline-code backticks around standalone identifiers when the whole block is already a code fence, for example `` `sessions_spawn` `` becomes `sessions_spawn`
   * Preserve real directory trees and file structures; those should be handled by `mint-directory-tree-formatter`
   * Preserve intentional bullets only when the block is clearly a copied list or checklist
   * Do not clean blocks that contain URLs, `Q1/Q2`, numbered steps, task checkboxes, Markdown tables, tree characters, or arrow-heavy workflows; route them to the relevant processor or leave them unchanged
4. Do not clean inside `mermaid`, `python`, `json`, `ts`, `tsx`, `js`, `bash`, `powershell`, `yaml`, or `mdx` fences except to add a missing language tag when it is obvious
5. Prefer `~~~` fences in MDX examples that themselves contain triple backticks; otherwise preserve the existing fence marker to avoid noisy churn
6. If a code fence contains tree characters such as `├──`, `└──`, or `│`, route it to `mint-directory-tree-formatter` instead of generic text cleanup
7. On Windows, avoid embedding Chinese replacement constants in shell-piped scripts unless UTF-8 is verified; use `apply_patch` for Chinese text or verify immediately that no `??` replacement appeared

Example:

```mdx
~~~text
sessions_spawn: Spawn an isolated sub-agent session
~~~
```

## Workflow

1. Read the target `.mdx` file as UTF-8
2. Detect YAML frontmatter at the top of the file
3. Compute the current month as `YYYY.MM`
4. Find the first body Markdown heading after frontmatter, usually `# ...` or `## ...`
5. Normalize the frontmatter `description:` into Chinese when frontmatter exists
6. Insert or update the Written badge immediately after that heading
7. Wrap whitelisted technical terms in body text with inline code, using the conservative rules above
8. Normalize Chinese parentheses in body text using the rules above
9. Normalize paragraph/list spacing so explanatory lists render as lists instead of collapsed inline text
10. Normalize fenced code block language tags and clean `text` fence content using the rules above
11. Route tree-like fenced text blocks to `mint-directory-tree-formatter`
12. Preserve the rest of the document content
13. Verify the file remains valid MDX text

## Reference

Read `references/written-badge.md` for exact examples and edge cases.
