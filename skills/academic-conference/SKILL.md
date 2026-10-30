---
name: academic-conference
description: '学术会议发言稿/PPT提纲/学术报告智能生成工具。适配教育类学术会议、 研讨会、论坛等场景。可生成会议发言稿、PPT分页提纲、海报摘要等。 触发词：「学术会议」「会议发言」「学术报告」「PPT提纲」「研讨会发言」

  '
metadata:
  short-description: 学术会议 · 让每一场发言都有准备
  routing:
    scenarios:
    - name: 学术发言
      keywords:
      - 学术会议
      - 会议发言
      - 学术报告
      - 研讨会发言
      - 论坛发言
    - name: 会议PPT
      keywords:
      - 学术PPT
      - 论文报告PPT
      - 研究汇报PPT
      - 课题汇报PPT
    typical_users:
    - 教师
    - 课题负责人
    - 科研主任
    - 校领导
    subjects: []
    trigger_intents:
    - intent: 学术准备
      weight: 1.0
      keywords:
      - 学术会议
      - 会议发言
      - 学术报告
      - 研讨会
      - 论文报告
      - 论坛发言
    disambiguation:
    - similar_skill: 论文转PPT-SKILL
      differentiator: 学术会议 从零开始生成发言稿和PPT提纲；论文转PPT 基于已有论文生成汇报PPT
    skill_chain:
      upstream:
      - 论文写作-SKILL
      downstream: []
      parallel:
      - 论文转PPT-SKILL
    confidence_rules:
      high: 用户提到具体会议名称+研究方向+发言时长
      medium: 用户说'准备学术会议发言'+ 有研究内容
      low: 用户只说'做个会议PPT'
      fallback_prompt: 好的，帮您准备学术会议材料。请问是什么会议？您的研究主题是什么？发言时长多少？需要发言稿还是PPT提纲？
  brand: AI老汤+AI云朵
  version: 1.0.1
  grade: S
  priority: P2
  tags:
  - 学术会议
  - 发言稿
  - 会议PPT
  - 学术报告
  - 科研处
  author: 🔬 云端学校 · AI老汤（汤幸初）
  source: AI老汤 · 自研
  preconditions:
  - raw_request
  - has_knowledge_base
  - analysis_complete
  postconditions:
  - output_proposal
  - output_article
  security_level: low
---

# 学术会议 Skill · v1.0
---

*AI老汤（汤幸初）出品 · 深圳市云端学校*



---

## 关联技能

**前置技能**（可接在本技能之前运行）：

- `darwin-skill` → 输出 "has_knowledge_base" 后调用本技能
- `edu-knowledge-cards` → 输出 "has_knowledge_base" 后调用本技能
- `find-skills` → 输出 "has_knowledge_base" 后调用本技能
- `github-deep-research` → 输出 "has_knowledge_base" 后调用本技能
- `skill` → 输出 "has_knowledge_base" 后调用本技能

> 关联关系由技能图谱的 pre/postconditions 自动生成。



## 可编辑文件输出（可选能力）

先完成方法要求的内容与人工核对，再按教师需要交付文件。
默认给可复制的完整正文或CSV表格，不以安装软件作为任务前提。
只有当前客户端确实具备且经本校批准的文件生成能力时，才可生成Word、Excel或PPT；
先说明目标文件与保存位置，由用户确认后创建新文件，不覆盖现有材料。
未具备能力时明确说明，给可编辑文本，不能声称文件已生成、已保存或已发送。
不提供或执行联网下载后直接运行的安装命令；维护人员另行核对依赖与授权。

## AI 公约
本技能遵循 agent-constitution 12 条规则。
## 🧬 技能进化档案（EmbodiSkill）

本技能维护 body 和 appendix 两部分，区分「技能该不该改」和「AI 有没有照做」。

### 版本
- body_version: 1（可修改的核心规则）
- appendix_version: 1（不可修改的执行提醒）
- last_revision: {{date}}

### 反思日志
| 轮次 | 归因类型 | 来源轨迹 | 操作 | 影响范围 |
|------|---------|---------|------|---------|
| — | — | 初始版本 | — | — |

### 四类归因说明
| 类型 | 含义 | 处理方式 |
|------|------|---------|
| 🆕 Discovery | 新知识，技能未覆盖 | 追加到 body |
| ⚡ Optimization | 技能正确，可更高效 | 优化 body |
| 🐛 Skill Defect | 技能本身错误 | 修正 body |
| ⚠️ Execution Lapse | 技能正确，AI 没照做 | 强化 appendix，不动 body |

### 稳定状态
- 安全稳定：连续 3 轮无 Skill Defect

## 输出规范

四条同时满足才算交付完成。

- 交付物是结构化提纲或简报（问题 / 现状 / 证据 / 结论 / 待补），段落用二级标题分开。
- 每条结论后用方括号标证据编号，文末统一列「证据清单」：来源、年份、页码或链接。
- 没有出处的判断标「待核」，不写成结论；数据标年份与统计口径。
- 结尾给 3 个可继续深入的方向，每个方向写一句「需要什么材料才能推进」。

## 失败与异常处理

1. **起点不清**：如果用户没给研究选题、已有文献/数据和时间节点，先问清「研究什么问题、手上有什么材料、什么时候要交」，问清再动手；实在拿不到，就按最保守的假设出一版，并在开头标注「假设：…」，不编造未提供的信息。
2. **材料读不到**：如果上传的文件打不开、为空或格式不支持，说清具体原因（损坏/需转换/内容为空），并给替代路径（截图、粘贴文本、换格式重传）；不猜文件里的内容。
3. **条件冲突**：如果用户的要求与已给材料或学校规定冲突，不直接照做也不直接拒绝，先列出冲突点，给 2 个可选处置方案，等用户选。
4. **超出范围**：如果请求属于代写论文正文、伪造数据或参考文献，说明这部分不在本技能范围，按「转写作润色类技能」处理，不硬答。

