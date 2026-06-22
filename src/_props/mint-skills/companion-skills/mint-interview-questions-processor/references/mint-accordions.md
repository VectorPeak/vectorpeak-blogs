# Mint Accordions Reference

## Component Pattern

Use the collapsed-by-default Mintlify Accordion structure:

```mdx
<AccordionGroup>
  <Accordion title="Q1: 问题 1">
    回答内容

    ---
  </Accordion>

  <Accordion title="Q2: 问题 2">
    回答内容

    ---
  </Accordion>
</AccordionGroup>
```

## Conversion Rules

* Convert Chinese full-width colon `：` to ASCII colon `:` in accordion titles
* Keep the question number in the title
* Remove Markdown bold wrappers from question headings before putting them into `title`
* Keep the answer body as Markdown inside the accordion
* Add `---` at the end of each accordion body, immediately before `</Accordion>`, to create a visible divider in expanded panels
* Keep accordions closed by default; do not add `defaultOpen` unless requested
* Leave one blank line between accordions for readability
* If the answer contains a table, keep the table inside the accordion body unchanged
* If the answer contains code, keep backticks unchanged

## Few-Shot

Input:

```mdx
**Q1：你看过 Hermes Agent 源码吗？简单讲讲它的架构和 OpenClaw 的区别**

看过。Hermes 是 Nous Research 开源的自主 AI Agent 平台...

---
**Q2: Hermes 的架构是几层？每层做什么？**

Hermes 的架构是主干 3 层加 1 个自进化闭环
```

Output:

```mdx
<AccordionGroup>
  <Accordion title="Q1: 你看过 Hermes Agent 源码吗？简单讲讲它的架构和 OpenClaw 的区别">
    看过。Hermes 是 Nous Research 开源的自主 AI Agent 平台...

    ---
  </Accordion>

  <Accordion title="Q2: Hermes 的架构是几层？每层做什么？">
    Hermes 的架构是主干 3 层加 1 个自进化闭环

    ---
  </Accordion>
</AccordionGroup>
```
