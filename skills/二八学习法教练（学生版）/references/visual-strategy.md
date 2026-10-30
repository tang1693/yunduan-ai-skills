# 四层图文策略 · 完整规范

> 核心原则：用对的工具画对的图。AI生图擅长概念场景，但画坐标系时数字错位；数学教学图需要精确。因此采用四层策略 + 环境检测。
> 
> 当 SKILL.md 要求你输出图示时，按此文件中的规则执行。

---

## 1. 环境检测

```
检测运行环境：
  if (有write工具可用 且 运行在本地/桌面端) → 本地模式
     → 用write工具生成HTML文件（含内联SVG），返回file://链接
  else → Web模式
     → 输出<svg-diagram>标签，平台内联渲染SVG
  endif
```

| 模式 | 图文输出方式 | 适用环境 |
|------|-------------|----------|
| **本地模式** | `write`工具生成HTML文件 → 返回 `[图名](file:///路径)` 可点击链接 | CodeBuddy/WorkBuddy桌面端 |
| **Web模式** | `<svg-diagram>`标签内联SVG → 平台直接渲染 | Web浏览器/小程序 |

两种模式共用同一套SVG代码，只是输出载体不同。

---

## 2. 第一层：SVG精确图示

适用于：坐标系、函数图像、几何图形、数轴、流程图等需要精确数值的场景。

### 2.1 Web模式输出

```text
<svg-diagram name="图示标题">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="-30 -30 260 260" width="300" height="300">
  <!-- 坐标轴 -->
  <line x1="0" y1="200" x2="200" y2="200" stroke="#2563eb" stroke-width="2"/>
  <line x1="30" y1="0" x2="30" y2="200" stroke="#2563eb" stroke-width="2"/>
  <!-- 关键线 -->
  <line x1="30" y1="180" x2="180" y2="30" stroke="#ef4444" stroke-width="2.5"/>
  <!-- 标记点 -->
  <circle cx="30" cy="180" r="5" fill="#ef4444"/>
  <text x="35" y="195" font-size="12">(0,1)</text>
  <circle cx="105" cy="105" r="5" fill="#ef4444"/>
  <text x="110" y="120" font-size="12">(2,5)</text>
  <!-- 标签 -->
  <text x="140" y="50" font-size="13" fill="#ef4444">y=2x+1</text>
  <text x="190" y="215" font-size="12" fill="#2563eb">x</text>
  <text x="10" y="15" font-size="12" fill="#2563eb">y</text>
</svg>
</svg-diagram>
```

### 2.2 本地模式输出

用 `write` 工具生成HTML文件：

```
1. 用write工具生成HTML文件（白底卡片 + 内联SVG + 已知条件 + 解题思路）
2. 给出可点击链接：[图名](file:///绝对路径)
3. 文字指向图中关键元素
```

**HTML模板**：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>图示标题</title>
<style>
  body { display:flex; justify-content:center; align-items:center;
         min-height:100vh; background:#f0f4f8; font-family:"Microsoft YaHei",sans-serif; margin:0; }
  .container { background:white; border-radius:16px; padding:32px;
               box-shadow:0 4px 20px rgba(0,0,0,0.1); }
  h2 { text-align:center; color:#2c3e50; margin-bottom:24px; }
  svg text { font-family:"Microsoft YaHei", sans-serif; }
</style>
</head>
<body>
<div class="container">
  <h2>📌 标题</h2>
  <svg width="500" height="400" viewBox="0 0 500 400">
    <!-- SVG图形内容 -->
  </svg>
  <div style="margin-top:24px; padding:16px; background:#eaf2f8; border-radius:8px;">
    <h3 style="margin:0 0 12px; color:#2c3e50;">📐 已知条件</h3>
    <!-- 条件列表 -->
  </div>
  <div style="margin-top:16px; padding:16px; background:#fef9e7; border-radius:8px;">
    <h3 style="margin:0 0 12px; color:#f39c12;">💡 解题思路</h3>
    <!-- 思路提示 -->
  </div>
</div>
</body>
</html>
```

### 2.3 SVG输出规范（两种模式通用）

- viewBox统一使用合理坐标范围，宽高 ≤ 400px
- 坐标轴用蓝色（#2563eb），关键线用红色（#ef4444），辅助线用灰色（#d1d5db）
- 标记点用实心圆（r=4~6），旁边标注坐标文字
- 字号：标签 ≥ 12px，标题 ≥ 14px
- 风格简洁，不加装饰

### 2.4 本地模式颜色语义

| 颜色 | 色值 | 含义 |
|------|------|------|
| 绿色 | #2ecc71 | 力向上、正向运动 |
| 红色 | #e74c3c | 重力/向下、关键线 |
| 蓝色 | #3498db | 水/液体、坐标轴 |
| 橙色 | #f39c12 | 标注、重点提示 |
| 紫色 | #9b59b6 | 尺寸、测量 |

### 2.5 SVG绘图要点

- `<rect>` 画容器、物体
- `<line>` 画力臂、连线、箭头杆
- `<polygon>` 画三角形、支架
- `<path>` 画波浪线（水面）、曲线
- `<defs>` + `<marker>` 定义箭头
- `<text>` 添加标签

---

## 3. 第二层：AI生图（概念场景、生活类比、卡通插图）

适用于：概念可视化、生活场景、抽象比喻的具象化等不需要精确数值的场景。

### 3.1 输出格式

```text
<image name="描述文字" prompt="卡通风格，[具体场景]，颜色鲜艳，适合X年级学生" />
```

### 3.2 prompt要素

| 要素 | 说明 |
|------|------|
| **风格** | 小学→"卡通风格"，初中→"教学风格"，高中→"简洁学术风格" |
| **主体** | 需要呈现的核心场景或对象 |
| **配色** | 颜色要求，鲜明、区分度高 |
| **安全** | "不出现真实人物、商标" |

### 3.3 配额控制

- 每轮 ≤ 3张
- 单张 ≤ 400KB
- 超额则返回文字占位

---

## 4. 第三层：LaTeX公式

数学公式直接使用 `$$y = 2x + 1$$` 语法。前端使用MathJax或KaTeX渲染。
若平台不支持，改为SVG手写或纯文字公式。

---

## 5. 第四层：文字兜底

当以上三层都不可用时，使用ASCII文字描述：

```text
  y
  ↑    /
  5 +-·----
  4 |/
  3 /
  2/|
  1·------→ x
  0 1 2 3
```

---

## 6. 图文确认闭环

**每张图/图示后必须追加确认句**，指向图中关键元素：
- SVG图示："看到坐标图了吗？红线经过哪两个点？"
- AI生图："看到图了吗？砂锅里的香料是什么颜色？"
- 公式："看到公式了吗？x前面的数字是多少？"

**用户说"看不到"时的降级路径**：
- SVG看不到 → 尝试ASCII文字描述
- AI生图看不到 → 简化prompt重新生成，或提供文字描述
- LaTeX看不到 → 改为纯文字公式（如 "y = 2x + 1"）

---

## 7. 图文适配年级

| 年级 | SVG风格 | AI生图风格 | 公式展示 |
|------|---------|-----------|----------|
| 小学4-6年级 | 大标签、粗线条、鲜艳颜色 | 卡通化、颜色鲜艳 | 简单算式，避免复杂符号 |
| 初中 | 标准教学图、标注清晰 | 教学风格 | 基础LaTeX公式 |
| 高中 | 简洁精确、可含辅助线 | 简洁学术风格 | 完整推导过程 |
