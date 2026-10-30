---
name: collaborative-data-analysis
description: '"1+N"共同体运行数据与成效分析报告生成工具。涵盖各入驻校参与数据、 四维课堂实施统计、同备同研同教活跃度、学生学业对比等。 触发词：「1+N数据」「共同体数据」「运行分析」「成效分析」「共同体报告」

  '
metadata:
  short-description: 1+N数据分析 · 用数据看共同体的成效
  routing:
    scenarios:
    - name: 数据分析
      keywords:
      - 1+N数据
      - 共同体数据
      - 运行分析
      - 成效分析
      - 共同体报告
    - name: 成效评估
      keywords:
      - 成效评估
      - 数据报告
      - 运行报告
      - 共同体评估
    typical_users:
    - 科研主任
    - 校长
    - 项目负责人
    subjects: []
    trigger_intents:
    - intent: 数据分析
      weight: 1.0
      keywords:
      - 1+N
      - 共同体
      - 运行数据
      - 成效分析
      - 数据报告
      - 共同体报告
    disambiguation:
    - similar_skill: 学校数据分析-SKILL
      differentiator: 1+N数据分析 专注共同体运行和四维课堂数据；学校数据分析 综合全校多维度数据
    skill_chain:
      upstream:
      - 共同体管理-SKILL
      downstream: []
      parallel:
      - 学校数据分析-SKILL
    confidence_rules:
      high: 用户提到时间段+具体分析维度
      medium: 用户说'做运行报告'+ 有数据范围
      low: 用户只说'数据报告'
      fallback_prompt: 好的，帮您生成1+N共同体数据分析报告。请问是哪个时间段？关注哪些维度（参与数据/课堂数据/教研活跃度/学生成效）？
  brand: AI老汤+AI云朵
  version: 1.0.1
  grade: S
  priority: P2
  tags:
  - 1+N数据
  - 共同体数据
  - 运行分析
  - 科研处
  author: ☁️ 深圳市云端学校 · AI老汤（汤幸初）
  source: AI老汤 · 自研
  preconditions:
  - has_exam_results
  - has_student_data
  - has_data
  postconditions:
  - analysis_complete
  - output_report
  - output_spreadsheet
  security_level: high
---

# 1+N数据分析 Skill · v1.0

**常见分析维度：**
- 各入驻校参与课时统计
- 四维课堂实施次数与覆盖面
- 同备同研同教活动频次
- 入驻校学生学业对比分析
- 共同体运行问题汇总
---

*AI老汤（汤幸初）出品 · 深圳市云端学校*



---

## 关联技能

**后置技能**（本技能输出后可继续执行）：

- `academic-research-hub` — 需要输入 "analysis_complete"
- `academic-writing-chinese` — 需要输入 "analysis_complete"
- `ai-compass` — 需要输入 "analysis_complete"
- `ai-laotang-identity` — 需要输入 "analysis_complete"
- `artifact-router` — 需要输入 "analysis_complete"

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

交付前对照这四条自检一遍。

- 交付物是结论页 + 数据表 + 图表；有图就配一句「这张图看什么」。
- 先给 3 条结论（每条一句话、带具体数字），再给支撑表；结论不重复表格内容。
- 每个数字标口径：时间范围、样本量、分母是什么；口径不明的数字不写进结论。
- 结尾给「异常值清单」与「下一步要补的数据」，异常值写清偏离方向和幅度。

## 失败与异常处理

1. **信息不全**：如果用户没给成绩表/学情数据、对比参照（上次考试或平行班），先问清「哪次考试、哪个年级班级学科、跟什么比」，问清再动手；实在拿不到，就按最保守的假设出一版，并在开头标注「假设：…」，不编造未提供的信息。
2. **材料读不到**：如果上传的文件打不开、为空或格式不支持，说清具体原因（损坏/需转换/内容为空），并给替代路径（截图、粘贴文本、换格式重传）；不猜文件里的内容。
3. **条件冲突**：如果用户的要求与已给材料或学校规定冲突，不直接照做也不直接拒绝，先列出冲突点，给 2 个可选处置方案，等用户选。
4. **超出范围**：如果请求属于预测学生升学结果、给个别学生下结论性判断，说明这部分不在本技能范围，按「转教学改进类技能」处理，不硬答。

