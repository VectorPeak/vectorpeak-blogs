from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify


SRC = Path("F:/Heima_coures/RAG/01_\u8bfe\u4ef6/site")
PROJECT = Path("E:/Github/VectorPeak/VectorPeakBlogs")
OUT = PROJECT / "RAG"
BADGE = '<Badge icon="clock" color="green">Written: 2026.06</Badge>'


PAGES = [
    ("总览", "index.html", "RAG/index.mdx", "RAG", "整理 RAG 技术体系、工程实践和课程讲义内容", "magnifying-glass"),
    ("基础入门", "01-project-overview.html", "RAG/foundations/project-overview.mdx", "项目概述与环境搭建", "介绍 KnowForge RAG 项目的整体架构、环境搭建和模块职责", "rocket"),
    ("基础入门", "02-rag-fundamentals.html", "RAG/foundations/rag-fundamentals.mdx", "RAG 基础", "系统梳理 RAG 的核心概念、流程、价值和边界", "book-open"),
    ("基础入门", "03-langchain-ecosystem.html", "RAG/foundations/langchain-ecosystem.mdx", "LangChain 生态", "整理 LangChain 在 RAG 工程中的组件体系和生态位置", "link"),
    ("检索工程", "appendix/appendix-g-chunking-strategy.html", "RAG/retrieval/chunking-strategy.mdx", "文档切分策略", "整理父子块切分、递归切分和 RAG 文档分块设计", "scissors"),
    ("检索工程", "appendix/appendix-f-embedding-models.html", "RAG/retrieval/embedding-and-bge-m3.mdx", "Embedding 与 BGE-M3", "整理 Embedding 模型选型、BGE-M3 特性和向量化实践", "binary"),
    ("检索工程", "04-milvus-index-and-operations.html", "RAG/retrieval/milvus-index-and-operations.mdx", "Milvus 索引与运维", "介绍 Milvus 索引机制、集合操作和向量数据库运维要点", "database"),
    ("检索工程", "06-retrieval-strategy.html", "RAG/retrieval/retrieval-strategy.mdx", "检索策略", "整理 RAG 检索计划、召回策略和动态检索链路", "search"),
    ("检索工程", "07-query-rewrite-variants.html", "RAG/retrieval/query-rewrite-variants.mdx", "查询改写与多路变体", "整理查询改写、多查询变体和检索召回增强方法", "route"),
    ("检索工程", "08-milvus-hybrid-search.html", "RAG/retrieval/milvus-hybrid-search.mdx", "Milvus 混合检索", "整理 Milvus Hybrid Search、稠密稀疏召回和分数融合", "database"),
    ("检索工程", "appendix/appendix-d-crossencoder-reranker.html", "RAG/retrieval/cross-encoder-reranker.mdx", "Cross-Encoder 重排序", "整理 Cross-Encoder Reranker 的原理、使用方式和工程边界", "list-check"),
    ("链路编排", "05-intent-classification.html", "RAG/pipeline/intent-classification.mdx", "意图识别", "整理 RAG 问答链路中的意图分类、路由和边界判断", "split"),
    ("链路编排", "09-qaservice-orchestration.html", "RAG/pipeline/qaservice-orchestration.mdx", "QAService 编排", "介绍 QAService 如何统一编排意图、检索、上下文和生成", "cubes"),
    ("链路编排", "10-rag-pipeline.html", "RAG/pipeline/rag-pipeline.mdx", "RAG Pipeline 主链路", "完整梳理 RAG Pipeline 从提问到生成的核心执行流程", "route"),
    ("链路编排", "11-prompt-engineering.html", "RAG/pipeline/prompt-engineering.mdx", "Prompt 工程", "整理 RAG Prompt Profile、模板选择和答案生成约束", "brain"),
    ("链路编排", "12-fastapi-async.html", "RAG/pipeline/fastapi-asynchronous-service.mdx", "FastAPI 异步服务", "整理 FastAPI、WebSocket 和异步服务在 RAG 系统中的使用", "server"),
    ("链路编排", "13-app-entry-preflight.html", "RAG/pipeline/app-entry-preflight.mdx", "应用入口与启动校验", "介绍应用入口、环境前置校验和服务启动流程", "shield-check"),
    ("生产治理", "14-kb-versioning.html", "RAG/production/kb-versioning.mdx", "知识库版本管理", "整理知识库多版本管理、灰度切换和版本隔离策略", "database"),
    ("生产治理", "15-data-isolation.html", "RAG/production/data-isolation.mdx", "数据隔离", "介绍多租户、数据范围和权限隔离在 RAG 系统中的设计", "lock-keyhole"),
    ("生产治理", "16-ingestion-pipeline.html", "RAG/production/ingestion-pipeline.mdx", "入库流水线", "整理文档加载、切分、向量化、索引和入库处理链路", "upload"),
    ("生产治理", "17-quality-evaluation.html", "RAG/production/quality-evaluation.mdx", "质量评估", "整理 RAG 回归验收、入库质量和效果评估方法", "chart-simple"),
    ("生产治理", "18-testing-system.html", "RAG/production/testing-system.mdx", "测试体系", "介绍接口验收、回归测试和 RAG 系统测试设计", "list-check"),
    ("生产治理", "19-observability-tracing.html", "RAG/production/observability-tracing.mdx", "可观测性与链路追踪", "整理 LangSmith Trace、日志和 RAG 链路观测方法", "chart-line"),
    ("进阶专题", "course-outline.html", "RAG/advanced/rag-optimization.mdx", "RAG 优化", "从课程大纲视角整理 RAG 系统优化方向和学习路径", "sliders"),
    ("进阶专题", "17-quality-evaluation.html", "RAG/advanced/rag-evaluation.mdx", "RAG 评估", "整理 RAG 评估指标、评测方法和质量诊断思路", "chart-simple"),
    ("进阶专题", "animation/business-flow.html", "RAG/advanced/graph-rag.mdx", "Graph RAG", "结合流程图整理 RAG 系统业务流、结构关系和图式表达", "route"),
    ("进阶专题", "animation/pipeline-demo.html", "RAG/advanced/agentic-rag.mdx", "Agentic RAG", "结合 Pipeline 演示整理多阶段 RAG 执行、路由和动态决策", "robot"),
    ("技术附录", "appendix/appendix-a-pydantic.html", "RAG/appendix/pydantic.mdx", "Pydantic 数据校验", "整理 Pydantic 数据校验与 Settings 管理基础", "badge-check"),
    ("技术附录", "appendix/appendix-b-sha256-fingerprint.html", "RAG/appendix/sha256-fingerprint.mdx", "SHA256 指纹", "整理文件指纹、去重和版本识别中的 SHA256 使用方式", "fingerprint"),
    ("技术附录", "appendix/appendix-c-hnsw-index.html", "RAG/appendix/hnsw-index.mdx", "HNSW 索引", "整理 HNSW 索引原理、参数和向量检索调优要点", "network"),
    ("技术附录", "appendix/appendix-e-recursive-splitter.html", "RAG/appendix/recursive-splitter.mdx", "Recursive Splitter", "整理 RecursiveCharacterTextSplitter 的机制和使用场景", "braces"),
    ("技术附录", "appendix/appendix-f-embedding-models.html", "RAG/appendix/embedding-models.mdx", "Embedding 模型", "整理 RAG 中 Embedding 模型选择、部署和效果权衡", "binary"),
    ("技术附录", "appendix/appendix-g-chunking-strategy.html", "RAG/appendix/chunking-strategy-appendix.mdx", "切分策略附录", "补充整理文档切分、父子块和 chunk 设计细节", "scissors"),
    ("技术附录", "appendix/appendix-h-tool-foundations.html", "RAG/appendix/tool-foundations.mdx", "工具基础", "整理项目工具类、辅助函数和工程基础能力", "wrench"),
    ("流程演示", "animation/business-flow.html", "RAG/demos/business-flow.mdx", "业务流程动画", "整理 KnowForge RAG Platform 业务流程动画中的 Mermaid 图和流程视图", "play"),
    ("流程演示", "animation/pipeline-demo.html", "RAG/demos/pipeline-demo.mdx", "Pipeline 执行流程动画", "整理 RAG Pipeline 执行流程动画中的阶段、步骤和关键链路", "play"),
]

REL_TO_ROUTE = {
    rel: Path(mdx).with_suffix("").as_posix()
    for _, rel, mdx, _, _, _ in PAGES
}


LANG_BY_CLASS = {
    "language-python": "python",
    "language-py": "python",
    "language-bash": "bash",
    "language-shell": "bash",
    "language-sh": "bash",
    "language-json": "json",
    "language-yaml": "yaml",
    "language-yml": "yaml",
    "language-sql": "sql",
    "language-javascript": "js",
    "language-js": "js",
    "language-typescript": "ts",
    "language-ts": "ts",
    "language-mermaid": "mermaid",
    "language-text": "text",
    "language-plain": "text",
    "language-console": "console",
}


def infer_lang(code: str, classes=()) -> str:
    for cls in classes or []:
        if cls in LANG_BY_CLASS:
            return LANG_BY_CLASS[cls]
        if cls.startswith("language-"):
            return cls.split("language-", 1)[1]
    text = code.strip()
    if text.startswith(("flowchart", "sequenceDiagram", "classDiagram", "graph ", "erDiagram", "mindmap")):
        return "mermaid"
    if re.search(r"\b(from\s+[\w.]+\s+import|import\s+[\w.]+|def\s+\w+\(|class\s+\w+|async\s+def)\b", text):
        return "python"
    if re.search(r"\b(const|let|async function|function\s+\w+|=>|JSON\.stringify|fetch\()\b", text):
        return "js"
    if re.search(r"\b(docker|kubectl|curl|npm|pnpm|uvicorn|python\s+-m|grep|rg|pip\s+install)\b", text):
        return "bash"
    if re.search(r"\b(SELECT|CREATE TABLE|INSERT INTO|UPDATE\s+\w+\s+SET)\b", text, re.I):
        return "sql"
    if (text.startswith("{") and '"' in text) or (text.startswith("[") and '"' in text):
        return "json"
    if re.match(r"^[\w.-]+:\s", text):
        return "yaml"
    return "text"


def frontmatter(title: str, description: str, icon: str) -> str:
    return (
        "---\n"
        f'title: "{title.replace(chr(34), chr(92) + chr(34))}"\n'
        f'description: "{description.replace(chr(34), chr(92) + chr(34))}"\n'
        f'icon: "{icon}"\n'
        "---\n\n"
    )


def preclean_article(article: BeautifulSoup) -> BeautifulSoup:
    for el in article.select(".headerlink, .md-source-file, .md-feedback, script, style"):
        el.decompose()
    for heading in article.find_all(re.compile("^h[1-6]$")):
        heading.string = re.sub(r"\s*¶\s*$", "", heading.get_text(" ", strip=True)).strip()

    for admonition in list(article.select("div.admonition, details")):
        kind = "提示"
        classes = admonition.get("class") or []
        for cls in classes:
            if cls != "admonition":
                kind = cls
                break
        title_el = admonition.select_one(".admonition-title, summary")
        title = title_el.get_text(" ", strip=True) if title_el else kind
        if title_el:
            title_el.decompose()
        block = article.new_tag("blockquote")
        p = article.new_tag("p")
        p.string = title
        block.append(p)
        for child in list(admonition.contents):
            block.append(child.extract())
        admonition.replace_with(block)

    for mermaid in list(article.select(".mermaid")):
        code = mermaid.get_text("\n", strip=False).strip()
        pre = article.new_tag("pre")
        code_tag = article.new_tag("code")
        code_tag["class"] = ["language-mermaid"]
        code_tag.string = code
        pre.append(code_tag)
        mermaid.replace_with(pre)

    for table in list(article.select("table.highlighttable")):
        code_el = table.select_one("td.code pre code") or table.select_one("td.code pre") or table.select_one("pre code") or table.select_one("pre")
        if not code_el:
            continue
        code = code_el.get_text("", strip=False).rstrip("\n")
        lang = infer_lang(code, code_el.get("class") or [])
        outer = table.find_parent("div", class_="highlight") or table
        pre = article.new_tag("pre")
        code_tag = article.new_tag("code")
        code_tag["class"] = [f"language-{lang}"]
        code_tag.string = code
        pre.append(code_tag)
        outer.replace_with(pre)

    for div in list(article.select("div.highlight")):
        code_el = div.select_one("pre code") or div.select_one("pre")
        if not code_el:
            continue
        code = code_el.get_text("", strip=False).rstrip("\n")
        lang = infer_lang(code, code_el.get("class") or [])
        pre = article.new_tag("pre")
        code_tag = article.new_tag("code")
        code_tag["class"] = [f"language-{lang}"]
        code_tag.string = code
        pre.append(code_tag)
        div.replace_with(pre)

    return article


def clean_markdown(text: str, title: str) -> str:
    text = text.replace("\xa0", " ")
    lines = text.splitlines()
    out = []
    in_fence = False
    code_lines = []
    opener = None
    for line in lines:
        if line.startswith("```"):
            if not in_fence:
                lang = line[3:].strip() or "text"
                opener = len(out)
                out.append(f"```{lang}")
                code_lines = []
                in_fence = True
            else:
                if opener is not None:
                    lang = out[opener][3:].strip()
                    if lang in ("", "text", "txt"):
                        out[opener] = "```" + infer_lang("\n".join(code_lines))
                out.append("```")
                in_fence = False
                opener = None
            continue
        if in_fence:
            code_lines.append(line)
        out.append(line)
    if in_fence:
        out.append("```")
    text = "\n".join(out)
    text = text.replace("```text\n\n横向为时间轴", "```\n\n横向为时间轴")
    text = text.replace("\n```\n# qa_core/api/dependencies.py\nimport time", "\n```python\n# qa_core/api/dependencies.py\nimport time")
    text = re.sub(r"(?m)^\s*¶\s*$", "", text)
    text = re.sub(r"(?m)^(#{1,6}\s+.+?)\s*¶\s*$", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not re.match(r"^#\s+", text):
        text = f"# {title}\n{text}" if text else f"# {title}"
    text = re.sub(r'\n<Badge icon="clock" color="green">Written: [^<]+</Badge>\n?', "\n", text)
    split = text.splitlines()
    for i, line in enumerate(split):
        if re.match(r"^#{1,6}\s+", line):
            split.insert(i + 1, BADGE)
            break
    text = "\n".join(split)
    text = re.sub(r'(<Badge icon="clock" color="green">Written: 2026\.06</Badge>)\n\n+', r"\1\n", text)
    return text.strip() + "\n"


def normalize_rel(base_rel: str, href: str) -> str:
    href_no_fragment = href.split("#", 1)[0]
    if not href_no_fragment:
        return ""
    base = Path(base_rel).parent
    parts = []
    for part in (base / href_no_fragment).as_posix().split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if parts:
                parts.pop()
        else:
            parts.append(part)
    return "/".join(parts)


def rewrite_links(text: str, src_rel: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, href = match.group(1), match.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#", "/")):
            return match.group(0)
        target, *fragment = href.split("#", 1)
        if not target.endswith(".html"):
            return match.group(0)
        norm = normalize_rel(src_rel, target)
        route = REL_TO_ROUTE.get(norm)
        if not route:
            return match.group(0)
        suffix = "#" + fragment[0] if fragment else ""
        return f"[{label}](/" + route.replace(" ", "%20") + suffix + ")"

    return re.sub(r"\[([^\]\n]+)\]\(([^)\n]+)\)", repl, text)


def protect_mdx_text(text: str) -> str:
    text = re.sub(r"\\\[(.*?)\\\]", lambda m: "```text\n" + m.group(1).strip() + "\n```", text, flags=re.S)
    text = re.sub(r"\\\((.*?)\\\)", lambda m: "`" + m.group(1).strip() + "`", text, flags=re.S)

    protected = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            protected.append(line)
            continue
        if in_fence or line.startswith("---") or line.startswith("<Badge "):
            protected.append(line)
            continue
        protected.append(line.replace("{", "&#123;").replace("}", "&#125;").replace("<", "&lt;"))
    return "\n".join(protected)


def convert_article(src: Path, title: str) -> str:
    soup = BeautifulSoup(src.read_text(encoding="utf-8", errors="replace"), "html.parser")
    article = soup.select_one("article.md-content__inner") or soup.select_one(".md-content__inner") or soup.select_one("main") or soup.body
    if article is None:
        return f"# {title}\n{BADGE}\n"
    article_soup = BeautifulSoup(str(article), "html.parser")
    preclean_article(article_soup)
    md = markdownify(
        str(article_soup),
        heading_style="ATX",
        bullets="-",
        code_language_callback=lambda el: infer_lang(el.get_text("", strip=False), el.get("class") or []),
    )
    return clean_markdown(md, title)


def convert_business_flow(src: Path, title: str) -> str:
    soup = BeautifulSoup(src.read_text(encoding="utf-8", errors="replace"), "html.parser")
    labels = {
        "diagram-online": "在线提问流程",
        "diagram-offline": "离线建库流程",
        "diagram-overview": "系统总览流程",
        "diagram-codealong": "代码跟练流程",
    }
    parts = [f"# {title}", BADGE, "本页整理业务流程动画中的 Mermaid 流程图。"]
    for script in soup.select('script[type="text/plain"]'):
        sid = script.get("id", "")
        code = script.get_text("\n", strip=False).strip()
        if not code:
            continue
        parts.append(f"## {labels.get(sid, sid or '流程图')}")
        parts.append("```mermaid\n" + code + "\n```")
    return "\n\n".join(parts).strip() + "\n"


def convert_pipeline_demo(src: Path, title: str) -> str:
    raw = src.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw, "html.parser")
    heading = soup.find("h1")
    page_title = title or (heading.get_text(" ", strip=True) if heading else title)
    parts = [f"# {page_title}", BADGE, "本页整理 Pipeline 执行流程动画中的场景和阶段说明。"]
    scenario_labels = re.findall(r'<option value="([^"]+)">([^<]+)</option>', raw)
    if scenario_labels:
        parts.append("## 场景")
        for _, label in scenario_labels:
            parts.append(f"- {BeautifulSoup(label, 'html.parser').get_text(' ', strip=True)}")
    infos = re.findall(r"info\('([^']*)','([^']*)'", raw)
    if infos:
        parts.append("## 时间线步骤")
        for idx, (step_title, desc) in enumerate(infos, 1):
            step_title = BeautifulSoup(step_title, "html.parser").get_text(" ", strip=True)
            desc = BeautifulSoup(desc, "html.parser").get_text(" ", strip=True)
            parts.append(f"### {idx}. {step_title}")
            parts.append(desc)
    return "\n\n".join(parts).strip() + "\n"


def convert_one(rel: str, title: str, desc: str, icon: str) -> str:
    src = SRC / rel
    if rel == "animation/business-flow.html":
        body = convert_business_flow(src, title)
    elif rel == "animation/pipeline-demo.html":
        body = convert_pipeline_demo(src, title)
    else:
        body = convert_article(src, title)
    body = re.sub(r"^#\s+.*$", f"# {title}", body, count=1, flags=re.M)
    body = rewrite_links(body, rel)
    body = protect_mdx_text(body)
    body = re.sub(r'(<Badge icon="clock" color="green">Written: 2026\.06</Badge>)\n\n+', r"\1\n", body)
    return frontmatter(title, desc, icon) + body


def update_docs_json() -> None:
    docs_path = PROJECT / "docs.json"
    data = json.loads(docs_path.read_text(encoding="utf-8"))
    order = ["总览", "基础入门", "检索工程", "链路编排", "生产治理", "进阶专题", "技术附录", "流程演示"]
    rag_groups = []
    for group in order:
        pages = [Path(mdx).with_suffix("").as_posix() for g, _, mdx, _, _, _ in PAGES if g == group]
        rag_groups.append({"group": group, "pages": pages})
    for tab in data["navigation"]["tabs"]:
        if tab.get("tab") == "RAG":
            tab["groups"] = rag_groups
            break
    else:
        data["navigation"]["tabs"].append({"tab": "RAG", "groups": rag_groups})
    docs_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"missing source: {SRC}")
    OUT.mkdir(parents=True, exist_ok=True)
    for child in OUT.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        elif child.name != ".gitkeep":
            child.unlink()
    written = []
    for _, rel, mdx, title, desc, icon in PAGES:
        src = SRC / rel
        if not src.exists():
            raise SystemExit(f"missing html: {src}")
        out_path = PROJECT / mdx
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(convert_one(rel, title, desc, icon), encoding="utf-8")
        written.append(out_path)
    update_docs_json()
    print(f"wrote {len(written)} mdx files")
    for path in written:
        print(path.relative_to(PROJECT).as_posix())


if __name__ == "__main__":
    main()
