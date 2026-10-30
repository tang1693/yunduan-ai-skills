---
name: thesis-report-writing
description: '教育科研课题三件套——开题报告/中期报告/结题报告智能撰写工具。 每个阶段按规范格式生成，适配各级课题管理要求。 触发词：「开题报告」「中期报告」「结题报告」「课题报告」「结题材料」

  '
metadata:
  short-description: 课题三件套 · 从开题到结题步步规范
  routing:
    scenarios:
    - name: 开题报告
      keywords:
      - 开题报告
      - 开题
      - 课题开题
      - 开题论证
    - name: 中期报告
      keywords:
      - 中期报告
      - 中期汇报
      - 阶段总结
      - 研究进展
    - name: 结题报告
      keywords:
      - 结题报告
      - 结题
      - 课题结题
      - 结项报告
      - 研究总结
    typical_users:
    - 课题负责人
    - 教师
    - 科研主任
    subjects: []
    trigger_intents:
    - intent: 开题报告
      weight: 1.0
      keywords:
      - 开题报告
      - 开题
      - 开题论证
    - intent: 中期报告
      weight: 0.9
      keywords:
      - 中期报告
      - 中期
      - 阶段汇报
    - intent: 结题报告
      weight: 0.9
      keywords:
      - 结题报告
      - 结题
      - 结项
      - 课题总结
    disambiguation:
    - similar_skill: 课题申报书-SKILL
      differentiator: 课题三件套 是立项后的过程管理报告；课题申报书 是立项前的申请材料
    skill_chain:
      upstream:
      - 课题申报书-SKILL
      downstream: []
      parallel: []
    confidence_rules:
      high: 用户明确报告类型（开题/中期/结题）+有课题信息
      medium: 用户说'写课题报告'+ 有课题基本信息
      low: 用户只说'写报告'，未说明阶段
      fallback_prompt: 好的，帮您写课题报告。请问是哪个阶段（开题/中期/结题）？课题名称是什么？目前有什么素材？
  brand: AI老汤+AI云朵
  version: 1.0.1
  grade: S
  priority: P1
  tags:
  - 开题报告
  - 中期报告
  - 结题报告
  - 课题
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

# 课题三件套 Skill · v1.0

**开题报告核心结构：** 研究背景→文献综述→研究目标→研究内容→研究方法→进度安排→预期成果→可行性分析
**中期报告核心结构：** 研究进展→阶段成果→存在问题→改进措施→下一步计划
**结题报告核心结构：** 研究概述→研究过程→研究成果→创新点→问题与展望→附录

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

按下面的形态交付，不要只给一段散文。

- 交付物是结构化提纲或简报（问题 / 现状 / 证据 / 结论 / 待补），段落用二级标题分开。
- 每条结论后用方括号标证据编号，文末统一列「证据清单」：来源、年份、页码或链接。
- 没有出处的判断标「待核」，不写成结论；数据标年份与统计口径。
- 结尾给 3 个可继续深入的方向，每个方向写一句「需要什么材料才能推进」。

## 失败与异常处理

1. **输入不全**：如果用户没给研究选题、已有文献/数据和时间节点，先问清「研究什么问题、手上有什么材料、什么时候要交」，问清再动手；实在拿不到，就按最保守的假设出一版，并在开头标注「假设：…」，不编造未提供的信息。
2. **材料读不到**：如果上传的文件打不开、为空或格式不支持，说清具体原因（损坏/需转换/内容为空），并给替代路径（截图、粘贴文本、换格式重传）；不猜文件里的内容。
3. **条件冲突**：如果用户的要求与已给材料或学校规定冲突，不直接照做也不直接拒绝，先列出冲突点，给 2 个可选处置方案，等用户选。
4. **超出范围**：如果请求属于代写论文正文、伪造数据或参考文献，说明这部分不在本技能范围，按「转写作润色类技能」处理，不硬答。

