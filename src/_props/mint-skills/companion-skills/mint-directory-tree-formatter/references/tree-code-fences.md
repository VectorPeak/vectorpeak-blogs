# Tree Code Fences

## Preferred Pattern

Use this form for tree-like text:

```mdx
**Skill 文件结构**：
~~~text title="Skill 文件结构" icon="folder-tree"
skills/<category>/<skill_name>/
├── SKILL.md       # skill 描述 + 触发条件 + 步骤说明
├── scripts/       # 可执行脚本（可选）
└── templates/     # 模板文件（可选）
~~~
```

## Few-Shot

Input:

```mdx
**Skill 文件结构**：
~~~
`skills/<category>/<skill_name>/`
├── SKILL.md       # skill 描述 + 触发条件 + 步骤说明
├── scripts/       # 可执行脚本（可选）
└── templates/     # 模板文件（可选）
~~~
```

Output:

```mdx
**Skill 文件结构**：
~~~text title="Skill 文件结构" icon="folder-tree"
skills/<category>/<skill_name>/
├── SKILL.md       # skill 描述 + 触发条件 + 步骤说明
├── scripts/       # 可执行脚本（可选）
└── templates/     # 模板文件（可选）
~~~
```

## Formatting Rules

* Remove inline backticks around the root path inside the code fence
* Keep the surrounding bold label if it exists
* Prefer `~~~text title="..." icon="folder-tree"` because it is explicit, compact in MDX, and avoids escaping triple backticks in examples
* Use `title="目录结构"` if no more specific title is available
* Use `title="项目结构"` when the block describes an app/project root
* Use `title="Skill 文件结构"` when the block describes a skill folder
* Keep Chinese comments aligned when practical, but do not over-format spacing
