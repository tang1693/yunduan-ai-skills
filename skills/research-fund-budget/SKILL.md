---
name: research-fund-budget
description: '教育科研课题经费预算编制辅助工具。按课题经费管理办法生成预算表， 涵盖设备费、材料费、差旅费、会议费、劳务费等科目。 触发词：「经费预算」「课题经费」「预算表」「项目预算」「科研经费」

  '
metadata:
  short-description: 课题经费 · 每一分钱都有去向
  routing:
    scenarios:
    - name: 经费预算
      keywords:
      - 经费预算
      - 课题经费
      - 预算表
      - 科研经费
      - 项目预算
      - 经费申请
    - name: 经费决算
      keywords:
      - 经费决算
      - 经费使用
      - 经费报销
      - 财务报账
    typical_users:
    - 课题负责人
    - 科研主任
    subjects: []
    trigger_intents:
    - intent: 编制预算
      weight: 1.0
      keywords:
      - 经费预算
      - 课题经费
      - 预算
      - 经费
      - 经费申请
    disambiguation:
    - similar_skill: 财务报销-SKILL
      differentiator: 课题经费 管课题预算编制和决算；财务报销 管日常报销单审核
    skill_chain:
      upstream:
      - 课题申请书-SKILL
      downstream: []
      parallel: []
    confidence_rules:
      high: 用户提到具体课题+课题级别+总经费
      medium: 用户说'做预算表'+ 有课题信息
      low: 用户只说'做个经费预算'
      fallback_prompt: 好的，帮您编制课题经费预算。请问是哪个级别的课题（市级/省级/国家级）？总经费多少？课题涉及哪些研究活动？
  brand: AI老汤+AI云朵
  version: 1.0.1
  grade: S
  priority: P3
  tags:
  - 课题经费
  - 预算
  - 经费
  - 财务
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

# 课题经费预算 Skill · v1.0
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

