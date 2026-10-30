---
name: school-branding
description: '学校品牌建设方案策划工具。涵盖品牌定位、学校特色提炼、品牌传播策略、 校园文化建设方案等。 触发词：「品牌建设」「学校品牌」「品牌定位」「校园文化」「特色学校」

  '
metadata:
  short-description: 品牌建设 · 让学校被看见被记住
  routing:
    scenarios:
    - name: 品牌建设
      keywords:
      - 品牌建设
      - 学校品牌
      - 品牌定位
      - 校园文化
      - 特色学校
      - 学校特色
    - name: 品牌传播
      keywords:
      - 品牌传播
      - 宣传策略
      - 形象塑造
      - 学校形象
      - 文化提炼
    typical_users:
    - 校长
    - 副校长
    - 办公室主任
    subjects: []
    trigger_intents:
    - intent: 品牌策划
      weight: 1.0
      keywords:
      - 品牌
      - 校园文化
      - 学校特色
      - 品牌定位
      - 特色学校
      - 品牌建设
    disambiguation:
    - similar_skill: 品牌规范-SKILL
      differentiator: 品牌建设 策划学校品牌定位和传播策略；品牌规范 检查对外宣传材料的合规性
    skill_chain:
      upstream: []
      downstream:
      - 品牌规范-SKILL
      - 新闻稿-SKILL
      parallel: []
    confidence_rules:
      high: 用户提到学校现状+品牌建设方向
      medium: 用户说'做品牌方案'+ 有学校基本信息
      low: 用户只说'品牌'
      fallback_prompt: 好的，帮您策划品牌建设方案。请问学校目前有什么特色或优势？希望打造什么形象？目标受众（家长/社会/上级）？
  brand: AI老汤+AI云朵
  version: 1.0.1
  grade: S
  priority: P3
  tags:
  - 品牌建设
  - 学校品牌
  - 校园文化
  - 校长驾驶舱
  author: 🏛️ 云端学校 · AI老汤（汤幸初）
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

# 学校品牌建设 Skill · v1.0

## 一句话启动

打开就说「**做学校品牌**」，不用先描述格式。


**品牌建设框架：**
1. 学校现状分析（优势/特色/短板）
2. 品牌定位（核心价值/目标受众/差异化）
3. 视觉形象体系（校徽/校训/VI建议）
4. 传播策略（渠道/内容/节奏）
5. 校园文化建设（环境/活动/制度）
6. 品牌评估机制

**参考维度：**
- 办学理念凝练
- 特色课程/项目打造
- 家校社协同品牌传播
- 教育类媒体关系
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

- 交付物是成稿正文 + 3 个可选标题或开头；通知类另附一条 120 字以内的群发短版。
- 先结论后背景，一段不超过 3 行；面向家长的版本不用专业术语和内部缩写。
- 人名、时间、地点、金额等空缺处用【待填】标出，不自行补写。
- 结尾附「发出前需核对的 3 项」，逐项写成可勾选的动作。

## 失败与异常处理

1. **信息不全**：如果用户没给沟通对象、事情经过和期望达成的结果，先问清「跟谁说、发生了什么、希望对方最后做什么」，问清再动手；实在拿不到，就按最保守的假设出一版，并在开头标注「假设：…」，不编造未提供的信息。
2. **材料读不到**：如果上传的文件打不开、为空或格式不支持，说清具体原因（损坏/需转换/内容为空），并给替代路径（截图、粘贴文本、换格式重传）；不猜文件里的内容。
3. **条件冲突**：如果用户的要求与已给材料或学校规定冲突，不直接照做也不直接拒绝，先列出冲突点，给 2 个可选处置方案，等用户选。
4. **超出范围**：如果请求属于代替学校对外发布正式声明、承诺政策之外的条件，说明这部分不在本技能范围，按「转学校办公室」处理，不硬答。

