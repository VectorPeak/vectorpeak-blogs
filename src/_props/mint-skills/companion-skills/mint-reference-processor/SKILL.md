---
name: mint-reference-processor
description: Convert reference sections in Mintlify MDX documents into categorized Tabs and Card components. Use when the user provides an MDX file path and wants the reference materials section organized by source code, videos, documents, papers, webpages, authors, or related links, with missing categories commented out instead of shown.
---

# Mint Reference Processor

Use this skill to process the reference section of a Mintlify `.mdx` document.

## Workflow

1. Locate the reference section:
   * `## 参考资料`
   * `## References`
   * numbered headings such as `## 1.7 参考资料`
2. Parse reference items from links, headings, labels, or plain URLs
3. Classify each item:
   * Source code: GitHub/GitLab repository, source code, 源码
   * Official website: official homepage, 官网, official site, project root domain
   * Video: Bilibili, YouTube, 视频, 讲解, UP 主
   * Document: official docs, blog docs, technical documentation, 文档, 官方文档
   * Paper: arXiv, DOI, PDF paper, 论文, paper
   * Webpage: article, blog, website, webpage, 网页
4. Generate a `<Tabs>` block
5. Add a visible `<Tab>` only when that category has real references
6. For missing categories, add an MDX comment with the omitted Tab placeholder
7. Use `<Card ... horizontal>` for each reference item
8. Preserve useful metadata:
   * title
   * URL
   * author or UP 主
   * short usage note
9. Replace the original reference section content in the MDX file
10. Verify the page when practical

## Reference

Read `references/reference-tabs.md` for templates, classification rules, and few-shot examples.
