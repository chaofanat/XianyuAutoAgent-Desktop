# 🚀 Xianyu AutoAgent-Desktop - 智能闲鱼客服机器人系统-桌面强化版

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![Python Version](https://img.shields.io/badge/nodejs-18%2B-blue)](https://nodejs.org/zh-cn/) [![LLM Powered](https://img.shields.io/badge/LLM-powered-FF6F61)](https://platform.openai.com/)

专为闲鱼平台打造的AI值守解决方案，实现闲鱼平台7×24小时自动化值守，支持多专家协同决策、智能议价和上下文感知对话。 


## 🌟 核心特性

### 智能对话引擎
| 功能模块   | 技术实现            | 关键特性                                                     |
| ---------- | ------------------- | ------------------------------------------------------------ |
| 上下文感知 | 会话历史存储        | 轻量级对话记忆管理，完整对话历史作为LLM上下文输入            |
| 专家路由   | LLM prompt+规则路由 | 基于提示工程的意图识别 → 专家Agent动态分发，支持议价/技术/客服多场景切换 |

### 业务功能矩阵
| 模块     | 已实现                        | 规划中                       |
| -------- | ----------------------------- | ---------------------------- |
| 核心引擎 | ✅ LLM自动回复<br>✅ 上下文管理 | 🔄 情感分析增强               |
| 议价系统 | ✅ 阶梯降价策略                | 🔄 市场比价功能               |
| 技术支持 | ✅ 网络搜索整合                | 🔄 RAG知识库增强              |
| 运维监控 | ✅ 基础日志                    | 🔄 钉钉集成<br>🔄  Web管理界面 |
| 桌面应用 | 🔄 一键启停服务<br>🔄 会话管理界面<br>🔄 数据统计面板<br>🔄 配置可视化 | 待定 |

## 🎨效果图
<div align="center">
  <img src="./images/demo1.png" width="600" alt="客服">
  <br>
  <em>图1: 客服随叫随到</em>
</div>


<div align="center">
  <img src="./images/demo2.png" width="600" alt="议价专家">
  <br>
  <em>图2: 阶梯式议价</em>
</div>

<div align="center">
  <img src="./images/demo3.png" width="600" alt="技术专家"> 
  <br>
  <em>图3: 技术专家上场</em>
</div>

<div align="center">
  <img src="./images/log.png" width="600" alt="后台log"> 
  <br>
  <em>图4: 后台log</em>
</div>


## 🚴 快速开始

### 环境要求
- Python 3.8+
- NodeJS 18+

### 安装步骤
```bash
1. 克隆仓库
git clone https://github.com/shaxiu/XianyuAutoAgent.git
cd xianyu-autoagent

2. 安装依赖
pip install -r requirements.txt

3. 配置环境变量
创建一个 `.env` 文件，包含以下内容，也可直接重命名 `.env.example` ：

API_KEY=apikey通过模型平台获取
COOKIES_STR=填写网页端获取的cookie
MODEL_BASE_URL=模型地址
MODEL_NAME=模型名称


注意：默认使用的模型是通义千问，如需使用其他API，请自行修改.env文件中的模型地址和模型名称；
COOKIES_STR自行在闲鱼网页端获取cookies(网页端F12打开控制台，选择Network，点击Fetch/XHR,点击一个请求，查看cookies)
或者通过运行setup_assistant.py进行更详细的环境变量指引
python setup_assistant.py

4. 创建提示词文件prompts/*_prompt.txt（也可以直接将模板名称中的_example去掉）
默认提供四个模板，可自行修改
```

### 使用方法

运行主程序：
```bash
python main.py
```

### 自定义提示词

可以通过编辑 `prompts` 目录下的文件来自定义各个专家的提示词：

- `classify_prompt.txt`: 意图分类提示词
- `price_prompt.txt`: 价格专家提示词
- `tech_prompt.txt`: 技术专家提示词
- `default_prompt.txt`: 默认回复提示词

## 🤝 参与贡献

欢迎通过 Issue 提交建议或 PR 贡献代码。



## 🛡 注意事项

⚠️ 注意：**本项目仅供学习与交流，如有侵权联系作者删除。**

鉴于项目的特殊性，开发团队可能在任何时间**停止更新**或**删除项目**。

如需学习交流，请联系：[coderxiu@qq.com](https://mailto:coderxiu@qq.com/)

## 🧸特别鸣谢
本项目参考了以下开源项目：
https://github.com/cv-cat/XianYuApis

感谢<a href="https://github.com/cv-cat">@CVcat</a>的技术支持

本项目分支于[Xianyu AutoAgent](https://github.com/shaxiu/XianyuAutoAgent).






## 📈 Star 趋势
<a href="https://www.star-history.com/#chaofanat/XianyuAutoAgent-Desktop&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=chaofanat/XianyuAutoAgent-Desktop&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=chaofanat/XianyuAutoAgent-Desktop&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=chaofanat/XianyuAutoAgent-Desktop&type=Date" />
 </picture>
</a>

## 🖥️ 桌面应用设计（规划中）

### 核心功能
- **服务控制**
  - 一键启动/停止智能体服务
  - 服务状态实时监控
  - 系统资源占用展示

- **会话管理**
  - 实时会话列表展示
  - 手动接入/转接会话
  - 会话历史记录查看
  - 会话状态标记（待处理/处理中/已完成）

- **配置中心**
  - 模型参数配置
  - 专家系统配置
  - 价格策略设置
  - 系统参数调整

### 界面布局
```
+------------------------+
|     顶部工具栏         |
+------------------------+
|        |              |
| 会话   |   主内容区    |
| 列表   |              |
|        |              |
+--------+--------------+
|     底部状态栏        |
+------------------------+
```

### 技术实现
- 使用 Electron + React 构建跨平台桌面应用
- 采用 IPC 通信实现主进程与渲染进程交互
- WebSocket 实现实时会话数据同步
- SQLite 本地存储会话历史


