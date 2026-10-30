---
name: safety-drill
description: '学校安全演练方案制定工具。涵盖消防疏散、地震避险、防暴恐、防踩踏 等各类演练方案，含演练脚本、人员分工、疏散路线、评估反馈。 触发词：「安全演练」「消防演练」「疏散演练」「地震演练」「演练方案」

  '
metadata:
  short-description: 安全演练 · 练在平时，用在急时
  routing:
    scenarios:
    - name: 演练方案
      keywords:
      - 安全演练
      - 消防演练
      - 疏散演练
      - 地震演练
      - 演练方案
      - 避险演练
    - name: 演练总结
      keywords:
      - 演练总结
      - 演练评估
      - 演练反馈
      - 演练记录
    typical_users:
    - 安全主任
    - 安全管理员
    - 德育主任
    subjects: []
    trigger_intents:
    - intent: 演练管理
      weight: 1.0
      keywords:
      - 演练
      - 消防演练
      - 疏散
      - 地震演练
      - 应急演练
      - 安全演练
    disambiguation:
    - similar_skill: 应急预案-SKILL
      differentiator: 安全演练 管演练方案和脚本设计；应急预案 管应急处置流程和制度
    skill_chain:
      upstream:
      - 应急预案-SKILL
      downstream:
      - 安全台账-SKILL
      parallel: []
    confidence_rules:
      high: 用户提到演练类型（消防/地震/防暴）+参与范围
      medium: 用户说'做演练方案'+ 有基本信息
      low: 用户只说'搞个演练'
      fallback_prompt: 好的，帮您制定安全演练方案。请问是什么类型（消防/地震/防暴恐/防踩踏）？全校还是年级/班级范围？
  brand: AI老汤+AI云朵
  version: 1.0.1
  grade: S
  priority: P1
  tags:
  - 安全演练
  - 消防演练
  - 疏散演练
  - 安全处
  author: 🛡️ 云端学校 · AI老汤（汤幸初）
  source: AI老汤 · 自研
  preconditions:
  - raw_request
  - has_student_data
  postconditions:
  - output_report
  - plan_ready
  security_level: high
---

# 安全演练方案 Skill · v1.0

## 一句话启动

打开就说「**排安全演练**」，不用先描述格式。

---

*AI老汤（汤幸初）出品 · 深圳市云端学校*



---

## 关联技能

**后置技能**（本技能输出后可继续执行）：

- `classroom-flow-designer` — 需要输入 "plan_ready"
- `edu-html-presentation` — 需要输入 "plan_ready"
- `edu-ppt-master` — 需要输入 "plan_ready"
- `html-ppt` — 需要输入 "plan_ready"
- `kami` — 需要输入 "plan_ready"

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

- 交付物是可执行的流程单或台账表（事项 / 责任人 / 时限 / 交付物 / 状态），便于直接派工。
- 每行必须有人和时间；暂缺的写【待定】并在表下单列，不默认由发起人承担。
- 涉及审批的写清前置条件与流转顺序（谁先签、谁后签、卡在哪一步）。
- 结尾给「本周要推进的 3 件事」，按截止时间排序。

## 失败与异常处理

1. **信息不全**：如果用户没给申请单/表单、审批人和台账记录，先问清「谁申请、什么事、什么时间、谁审批」，问清再动手；实在拿不到，就按最保守的假设出一版，并在开头标注「假设：…」，不编造未提供的信息。
2. **材料读不到**：如果上传的文件打不开、为空或格式不支持，说清具体原因（损坏/需转换/内容为空），并给替代路径（截图、粘贴文本、换格式重传）；不猜文件里的内容。
3. **条件冲突**：如果用户的要求与已给材料或学校规定冲突，不直接照做也不直接拒绝，先列出冲突点，给 2 个可选处置方案，等用户选。
4. **超出范围**：如果请求属于代替学校作出审批结论、绕过规定流程先办后补，说明这部分不在本技能范围，按「转对应处室负责人」处理，不硬答。

