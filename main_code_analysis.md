# main.py 代码详细解析

## 1. 文件概述

`main.py` 是闲鱼自动智能体桌面端的主入口，负责：
- WebSocket 长连接与闲鱼服务器通信
- 消息收发、心跳维护
- 消息解密、上下文管理
- 调用智能体（XianyuReplyBot）自动回复

---

## 2. 主要依赖
- `asyncio`、`websockets`：异步通信
- `loguru`：日志
- `dotenv`：环境变量加载（如COOKIES_STR）
- 项目自定义模块：`XianyuApis`、`XianyuAgent`、`context_manager`、`utils.xianyu_utils`

---

## 3. 主要类与结构

### 3.1 XianyuLive
**核心类，负责与闲鱼服务器通信和消息处理。**

#### 构造方法 `__init__(self, cookies_str, bot)`
- 初始化API、WebSocket地址、cookie、device_id、上下文管理器。
- `self.bot` 保存智能体实例。

#### 主要成员变量
- `self.xianyu`：API操作对象
- `self.cookies_str`/`self.cookies`：cookie字符串与字典
- `self.myid`：当前用户id
- `self.device_id`：设备id
- `self.context_manager`：上下文管理器
- `self.bot`：智能体
- 心跳相关变量

#### 主要方法

##### 1. `async def send_msg(self, ws, cid, toid, text)`
- 发送消息到指定会话。

##### 2. `async def init(self, ws)`
- WebSocket注册与初始化。
- 获取token，发送注册包。

##### 3. `def is_chat_message(self, message)`
- 判断消息是否为用户聊天消息。

##### 4. `def is_sync_package(self, message_data)`
- 判断是否为同步包消息。

##### 5. `def is_typing_status(self, message)`
- 判断是否为用户正在输入状态。

##### 6. `async def handle_message(self, message_data, websocket)`
- **消息处理核心**：
    - 解密消息，判断类型。
    - 订单消息、聊天消息分流。
    - 聊天消息：
        - 获取商品信息、上下文。
        - 调用 `self.bot.generate_reply(...)` 生成回复。
        - 记录对话、议价次数。
        - 通过 `send_msg` 发送回复。

##### 7. `async def send_heartbeat(self, ws)`
- 发送心跳包。

##### 8. `async def heartbeat_loop(self, ws)`
- 心跳维护循环，自动重连。

##### 9. `async def handle_heartbeat_response(self, message_data)`
- 处理心跳响应。

##### 10. `async def main(self)`
- **主循环**：
    - 建立WebSocket连接。
    - 注册、启动心跳。
    - 异步监听消息，分发处理。
    - 自动重连。

---

### 3.2 智能体 XianyuReplyBot
- 在 `if __name__ == '__main__'` 处实例化。
- 通过 `self.bot.generate_reply(...)` 被调用，负责自动回复生成。

---

## 4. 执行流程

1. **加载环境变量**（如COOKIES_STR）
2. **实例化智能体** `bot = XianyuReplyBot()`
3. **实例化主类** `xianyuLive = XianyuLive(cookies_str, bot)`
4. **启动主循环** `asyncio.run(xianyuLive.main())`
5. **WebSocket连接建立**，注册、心跳维护
6. **消息监听与处理**
    - 解密、分流、上下文管理
    - 智能体生成回复
    - 发送消息
7. **异常与重连机制**

---

## 5. 关键点说明
- **全异步架构**，高并发消息处理
- **cookie、device_id、token** 需有效，保证登录态
- **上下文管理** 支持多轮对话、议价统计
- **智能体可灵活替换**，只需实现 generate_reply 接口
- **自动重连与心跳**，保证长连接稳定

---

## 6. 适合人群
- 希望理解闲鱼自动智能体消息处理、自动回复、WebSocket通信的开发者
- 需要二次开发、定制化对接的工程师

---

如需更细致的某一部分解析，可随时补充！ 