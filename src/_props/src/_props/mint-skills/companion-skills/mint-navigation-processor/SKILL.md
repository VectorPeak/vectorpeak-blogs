---
name: mint-navigation-processor
description: Maintain Mintlify docs.json navigation. Use when creating, renaming, ordering, or validating tabs, groups, page routes, group icons, and sidebar links in a Mintlify project.
---

# Mint Navigation Processor

Use this skill for `docs.json` navigation work. It is responsible for Mintlify structure, not MDX正文 formatting.

## Scope

* Add, remove, or reorder `navigation.tabs`
* Add, remove, or reorder `groups`
* Add, remove, or reorder `pages`
* Validate every page route maps to an existing `.mdx` file
* Keep group-level visual rules consistent with VectorPeak docs

## Rules

1. Do not add `icon` to ordinary sidebar groups
   * Group names such as `Agent Framework`, `LangChain`, `Modern Agent`, and `LangGraph` should be plain text
   * Put icons in each page's MDX frontmatter instead
2. Keep page paths in `docs.json` without `.mdx`
3. Preserve existing group order unless the user asks to move a group
4. For new topical groups, use this shape:

```json
{
  "group": "LangChain",
  "pages": [
    "Agent/Agent_Framework/LangChain/LangChain"
  ]
}
```

5. After editing `docs.json`, verify:

```bash
node -e "const fs=require('fs');const d=JSON.parse(fs.readFileSync('docs.json','utf8'));const missing=[];for(const tab of d.navigation.tabs){for(const g of tab.groups||[]){for(const p of g.pages||[]){if(!fs.existsSync(p+'.mdx')) missing.push(p+'.mdx')}}} if(missing.length){console.log(missing.join('\n')); process.exit(1)} console.log('all docs.json pages exist')"
```

6. Run `mint validate` when practical

## Ownership

* `mint-navigation-processor`: `docs.json` tabs/groups/pages/routes
* `mint-blog-formatter`: single MDX page frontmatter, Badge, body formatting
* `mint-blog-document-processor`: orchestrates one MDX document and delegates content transforms
