# QDQ Logo Generator

一个专业的 SVG Logo 生成器 Skill，为 OpenClaw 提供高质量的 Logo 设计能力。

## 功能特性

- 🎨 **多种设计风格**: 几何形状、点阵系统、线条系统、混合构图
- 🖼️ **交互式展示**: 生成美观的 HTML 展示页面
- 📱 **移动端友好**: 响应式设计，支持各种设备
- 🎯 **现代设计原则**: 极简、负空间、精准比例
- 📦 **一键导出**: SVG 源码 + PNG 展示图

## 安装使用

### 安装到 OpenClaw

```bash
# 克隆到 skills 目录
cd ~/.openclaw/workspace/skills
git clone https://github.com/Leon-Drq/qdq_logo.git

# 或者直接下载 skill 文件
```

### 使用示例

在 OpenClaw 中直接调用：

```
@666Claw 设计一个 "MyBrand" 的 logo
```

## 设计流程

1. **信息收集**: 品牌名称、行业、核心理念
2. **生成方案**: 至少 6 种不同风格的设计变体
3. **交互展示**: 生成 HTML 展示页面
4. **导出交付**: PNG 预览图 + SVG 源码

## 设计风格

| 风格 | 描述 | 适用场景 |
|------|------|----------|
| 几何形状 | 简洁的几何图形组合 | 科技、金融 |
| 点阵系统 | 点阵构成的图案 | AI、数据 |
| 线条系统 | 线条构成的流动感 | 通信、音频 |
| 混合构图 | 多种元素组合 | 综合类品牌 |

## 文件结构

```
qdq_logo/
├── SKILL.md              # Skill 主文档
├── README.md             # 本文件
├── references/
│   └── design_patterns.md # 设计模式参考
├── assets/
│   └── showcase_template.html # 展示页面模板
└── scripts/
    └── screenshot_showcase.py # 截图脚本
```

## 设计原则

- **极简主义**: 1-2 个核心元素
- **负空间**: 40-50% 留白
- **精准比例**: 线条粗细 2.5-4px
- **视觉张力**: 有意的不对称
- **单一焦点**: 清晰的视觉层次

## 示例

### AI Pioneer Logo 设计

为 "AI Pioneer" 生成的 6 个设计方案：

1. **Pioneer Compass** - 指南针象征探索方向
2. **Neural Constellation** - 神经网络点阵
3. **Horizon Lines** - 地平线线条
4. **Pioneer Path** - 开拓者之路
5. **Converge** - 汇聚融合
6. **Pulse Rings** - 脉冲波纹

## 技术栈

- SVG (可缩放矢量图形)
- React + Tailwind CSS (展示页面)
- Playwright (截图生成)

## 贡献

欢迎提交 Issue 和 PR！

## 许可证

MIT License

## 作者

Created by [Leon-Drq](https://github.com/Leon-Drq)
