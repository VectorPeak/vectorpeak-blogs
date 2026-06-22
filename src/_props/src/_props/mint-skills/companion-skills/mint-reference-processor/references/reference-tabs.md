# Reference Tabs

## Component Template

Use this shape:

```mdx
<Tabs>
  <Tab title="源码" icon="github">
    <Card
      title="Hermes Agent 源代码"
      icon="github"
      href="https://github.com/nousresearch/hermes-agent"
      horizontal
    >
      Nous Research 开源的 Hermes Agent 主仓库，适合查看架构实现、记忆系统和自进化循环源码
    </Card>
  </Tab>
</Tabs>
```

## Category Mapping

| Category         | Tab title | Icon      | Detection                                        |
| ---------------- | --------- | --------- | ------------------------------------------------ |
| Source code      | 源码        | github    | GitHub/GitLab URL, source code, 源码               |
| Official website | 官网        | globe     | 官网, official site, homepage, project root domain |
| Video            | 视频        | play      | Bilibili, YouTube, 视频, 讲解, UP 主                  |
| Document         | 文档        | file-text | docs, documentation, official docs, 文档, 官方文档     |
| Paper            | 论文        | book-open | arXiv, DOI, PDF paper, 论文, paper                 |
| Webpage          | 网页        | globe     | blog, article, website, 网页, 文章                   |

## Source Code Card Format

Source code cards must use this fixed writing pattern:

* Card title: `{ProjectName} 源代码`
* Card body first sentence: `{OwnerName} 开源的 {ProjectName} 主仓库`
* Add one short usage clause only when useful, for example `适合查看架构实现、记忆系统和工具调用源码`

Example:

```mdx
<Card
  title="Hermes Agent 源代码"
  icon="github"
  href="https://github.com/nousresearch/hermes-agent"
  horizontal
>
  Nous Research 开源的 Hermes Agent 主仓库
</Card>
```

## Official Website Card Format

Official website cards must use this fixed writing pattern:

* Tab title: `官网`
* Tab icon: `globe`
* Card title: `{ProjectName} 官网`
* Card body: `{ProjectName} 的官方入口，适合了解产品定位、功能介绍、安装方式和最新动态`

Example:

```mdx
<Tab title="官网" icon="globe">
  <Card
    title="OpenClaw 官网"
    icon="globe"
    href="https://clawcn.net/"
    horizontal
  >
    OpenClaw 的官方入口，适合了解产品定位、功能介绍、安装方式和最新动态
  </Card>
</Tab>
```

## Video Card Format

Video cards must use this fixed writing pattern:

* Card title: use a concise Chinese title that explains what the video is for
* Card body line 1: `Youtuber: {ChannelName}` for YouTube, or `UP 主：{AuthorName}` for Bilibili
* If the author is unavailable, use `来源：YouTube` or `来源：Bilibili` instead of inventing a name
* Card body line 2: one short usage note starting with `用于...` or `适合...`
* Keep the two lines separated by two trailing spaces after the author line
* Keep card bodies to at most two lines

Example:

```mdx
<Card
  title="Hermes Agent 面试问题讲解"
  icon="play"
  href="https://www.bilibili.com/video/BV1J9o4BnE2n/"
  horizontal
>
  UP 主：骑猪撞宝马71  
  用于快速复习 Hermes Agent 的面试高频问题
</Card>
```

## Missing Category Comments

If a category has no real references, do not render a visible tab. Preserve the placeholder as an MDX comment:

```mdx
{/* No 文档 references detected.
<Tab title="文档" icon="file-text">
  <Card title="待补充" icon="file-text" horizontal>
    后续可以放官方文档、技术文档、项目文档等资料
  </Card>
</Tab>
*/}
```

## Few-Shot

Input:

```mdx
## 1.7 参考资料
**Hermes 源代码**
[https://github.com/nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)

**Bili视频讲解**
[Bili_骑猪撞宝马71_一个视频讲透 Hermes Agent 面试问题](https://www.bilibili.com/video/BV1J9o4BnE2n/)
```

Output:

```mdx
## 1.7 参考资料

<Tabs>
  <Tab title="源码" icon="github">
    <Card
      title="Hermes Agent 源代码"
      icon="github"
      href="https://github.com/nousresearch/hermes-agent"
      horizontal
    >
      Nous Research 开源的 Hermes Agent 主仓库，适合查看架构实现、记忆系统和自进化循环源码
    </Card>
  </Tab>

  <Tab title="视频" icon="play">
    <Card
      title="一个视频讲透 Hermes Agent 面试问题"
      icon="play"
      href="https://www.bilibili.com/video/BV1J9o4BnE2n/"
      horizontal
    >
      UP 主：骑猪撞宝马71  
      用于快速复习 Hermes Agent 的面试高频问题
    </Card>
  </Tab>
</Tabs>

{/* No 文档 references detected.
<Tab title="文档" icon="file-text">
  <Card title="待补充" icon="file-text" horizontal>
    后续可以放官方文档、技术文档、项目文档等资料
  </Card>
</Tab>
*/}

{/* No 论文 references detected.
<Tab title="论文" icon="book-open">
  <Card title="待补充" icon="book-open" horizontal>
    后续可以放论文、arXiv、PDF 等资料
  </Card>
</Tab>
*/}
```

## Writing Notes

* Keep card descriptions short and useful
* Prefer the actual title over raw URL text
* If a title contains author information, extract it into the card body
* Use two spaces before a line break inside card body only when a visual line break is useful
* Do not invent papers or documents that are not present in the source section
