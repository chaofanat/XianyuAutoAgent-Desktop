import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from dotenv import load_dotenv

class ConfigGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("闲鱼智能客服配置工具")
        self.root.geometry("800x600")
        
        # 加载现有配置
        self.load_config()
        
        # 创建选项卡
        self.create_tabs()
        
    def load_config(self):
        """加载现有配置"""
        load_dotenv()
        self.config = {
            'COOKIES_STR': os.getenv('COOKIES_STR', ''),
            'API_KEY': os.getenv('API_KEY', 'ollama'),
            'MODEL_BASE_URL': os.getenv('MODEL_BASE_URL', 'http://localhost:11434/v1'),
            'MODEL_NAME': os.getenv('MODEL_NAME', 'qwen3:30b-a3b')
        }
        
    def create_tabs(self):
        """创建选项卡"""
        tab_control = ttk.Notebook(self.root)
        
        # Cookies配置页
        cookies_tab = ttk.Frame(tab_control)
        tab_control.add(cookies_tab, text='Cookies配置')
        self.create_cookies_tab(cookies_tab)
        
        # 模型配置页
        model_tab = ttk.Frame(tab_control)
        tab_control.add(model_tab, text='模型配置')
        self.create_model_tab(model_tab)
        
        tab_control.pack(expand=1, fill="both")
        
    def create_cookies_tab(self, parent):
        """创建Cookies配置页"""
        # 说明文本
        instructions = """
1. 点击"打开闲鱼网站"按钮
2. 在打开的浏览器中登录闲鱼
3. 登录成功后，按F12打开开发者工具
4. 切换到"网络/Network"标签
5. 刷新页面
6. 在请求列表中找到任意请求
7. 在请求头中找到"Cookie"字段
8. 复制整个Cookie值
9. 粘贴到下方输入框

注意：请确保Cookie中包含 'unb' 字段，这是系统必需的。
        """
        label = tk.Label(parent, text=instructions, justify=tk.LEFT)
        label.pack(pady=10)
        
        # 按钮框架
        button_frame = tk.Frame(parent)
        button_frame.pack(pady=10)
        
        # 打开网站按钮
        open_site_btn = tk.Button(button_frame, text="打开闲鱼网站", command=self.open_website)
        open_site_btn.pack(side=tk.LEFT, padx=5)
        
        # 自动获取按钮
        auto_get_btn = tk.Button(button_frame, text="自动获取Cookies", command=self.auto_get_cookies)
        auto_get_btn.pack(side=tk.LEFT, padx=5)
        
        # 保存按钮
        save_btn = tk.Button(button_frame, text="保存配置", command=self.save_all_config)
        save_btn.pack(side=tk.LEFT, padx=5)
        
        # Cookies输入框
        cookies_frame = tk.LabelFrame(parent, text="Cookies")
        cookies_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.cookies_text = tk.Text(cookies_frame, height=10)
        self.cookies_text.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        if self.config['COOKIES_STR']:
            self.cookies_text.insert(tk.END, self.config['COOKIES_STR'])
            
    def create_model_tab(self, parent):
        """创建模型配置页"""
        # 创建配置框架
        config_frame = tk.Frame(parent)
        config_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        # API Key配置
        tk.Label(config_frame, text="API Key:").grid(row=0, column=0, sticky='w', pady=5)
        self.api_key_entry = tk.Entry(config_frame, width=50)
        self.api_key_entry.grid(row=0, column=1, pady=5)
        self.api_key_entry.insert(0, self.config['API_KEY'])
        
        # 模型基础URL配置
        tk.Label(config_frame, text="模型基础URL:").grid(row=1, column=0, sticky='w', pady=5)
        self.model_url_entry = tk.Entry(config_frame, width=50)
        self.model_url_entry.grid(row=1, column=1, pady=5)
        self.model_url_entry.insert(0, self.config['MODEL_BASE_URL'])
        
        # 模型名称配置
        tk.Label(config_frame, text="模型名称:").grid(row=2, column=0, sticky='w', pady=5)
        self.model_name_entry = tk.Entry(config_frame, width=50)
        self.model_name_entry.grid(row=2, column=1, pady=5)
        self.model_name_entry.insert(0, self.config['MODEL_NAME'])
        
        # 保存按钮
        save_btn = tk.Button(config_frame, text="保存配置", command=self.save_all_config)
        save_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
    def open_website(self):
        webbrowser.open("https://www.goofish.com")
        
    def auto_get_cookies(self):
        try:
            # 设置Chrome选项
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            # 添加SSL相关选项
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--allow-running-insecure-content')
            # 禁用GPU加速
            chrome_options.add_argument('--disable-gpu')
            # 禁用沙箱模式
            chrome_options.add_argument('--no-sandbox')
            # 禁用开发者工具
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            # 创建Chrome浏览器实例
            driver = webdriver.Chrome(options=chrome_options)
            
            # 打开闲鱼网站
            driver.get("https://www.goofish.com")
            
            # 等待用户手动登录
            messagebox.showinfo("提示", "请在打开的浏览器中登录闲鱼\n登录成功后点击确定")
            
            # 获取所有cookies
            cookies = driver.get_cookies()
            cookies_str = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            
            # 验证是否包含unb字段
            if 'unb=' not in cookies_str:
                messagebox.showwarning("警告", "Cookie中未找到'unb'字段，请确保已正确登录闲鱼")
                driver.quit()
                return
            
            # 设置到文本框
            self.cookies_text.delete(1.0, tk.END)
            self.cookies_text.insert(tk.END, cookies_str)
            
            # 关闭浏览器
            driver.quit()
            
        except Exception as e:
            messagebox.showerror("错误", f"自动获取cookies失败: {str(e)}\n请尝试手动获取")
            
    def save_all_config(self):
        """保存所有配置"""
        try:
            config = {
                'COOKIES_STR': self.cookies_text.get(1.0, tk.END).strip(),
                'API_KEY': self.api_key_entry.get().strip(),
                'MODEL_BASE_URL': self.model_url_entry.get().strip(),
                'MODEL_NAME': self.model_name_entry.get().strip()
            }
            
            # 验证必填项
            if not config['COOKIES_STR']:
                messagebox.showerror("错误", "请先配置Cookies")
                return
                
            # 验证cookies是否包含unb字段
            if 'unb=' not in config['COOKIES_STR']:
                messagebox.showerror("错误", "Cookie中未找到'unb'字段，请确保已正确登录闲鱼")
                return
                
            # 保存到.env文件
            with open('.env', 'w', encoding='utf-8') as f:
                for key, value in config.items():
                    f.write(f'{key}={value}\n')
                    
            messagebox.showinfo("成功", "配置已保存到.env文件")
            
        except Exception as e:
            messagebox.showerror("错误", f"保存配置失败: {str(e)}")
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ConfigGUI()
    app.run() 