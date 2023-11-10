import logging
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简单程序")
        
        # 创建标签
        self.label = tk.Label(root, text="欢迎使用简单程序", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # 创建消息提示按钮
        self.message_button = tk.Button(root, text="消息提示", command=self.show_message)
        self.message_button.pack(pady=10)

        # 创建更新检查按钮
        self.update_button = tk.Button(root, text="检查更新", command=self.check_for_updates)
        self.update_button.pack(pady=10)
    def kill_current_pid():
        pid = os.getpid()
        return pid

    def show_message(self):
        messagebox.showinfo("消息提示", "这是一个简单的消息提示。")

    def check_for_updates(self):
        try:
            # 启动更新程序
            subprocess.run(["python", "update_app.py"])
        except Exception as e:
            messagebox.showerror("错误", f"检查更新时出错：{str(e)}")

if __name__ == "__main__":
    # 创建 Tkinter 窗口
    root = tk.Tk()

    # 实例化应用程序类
    app = SimpleApp(root)

    # 运行主循环
    root.mainloop()
