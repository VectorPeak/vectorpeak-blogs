---
name: mint-directory-tree-formatter
description: Format tree-like text blocks in Mintlify MDX documents as titled code fences with a folder-tree icon. Use when the user provides an MDX path or a tree-like directory structure block containing lines such as skills/category/name, tree branch characters, folders, or file hierarchy text and wants a cleaner Mint presentation.
---

# Mint Directory Tree Formatter

Use this skill to normalize directory tree and file structure blocks in MDX documents.

## Workflow

1. Detect tree-like text blocks:
   * fenced blocks containing `├──`, `└──`, `│`, `|--`, `+--`, or repeated folder/file indentation
   * blocks introduced by labels such as `文件结构`, `目录结构`, `项目结构`, `Skill 文件结构`
2. Keep the tree content as a code block so it remains copyable
3. Add a Mintlify code fence title and icon:
   * `title="Skill 文件结构"` when the nearby label says Skill 文件结构
   * `title="目录结构"` for general directory trees
   * `icon="folder-tree"` by default
4. Preserve existing comments to the right of tree lines
5. Do not convert tree blocks into Mermaid unless the user explicitly asks
6. If the tree block already has a title/icon, normalize it rather than duplicating metadata

## Reference

Read `references/tree-code-fences.md` for examples and exact fence patterns.
