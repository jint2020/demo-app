import tkinter as tk
from tkinter import messagebox

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简单程序")
        
        # 创建标签
        self.label = tk.Label(root, text="欢迎使用简单程序", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # 创建按钮
        self.button = tk.Button(root, text="点击我", command=self.show_message)
        self.button.pack(pady=20)

    def show_message(self):
        messagebox.showinfo("提示", "你点击了按钮！")

if __name__ == "__main__":
    # 创建 Tkinter 窗口
    root = tk.Tk()

    # 实例化应用程序类
    app = SimpleApp(root)

    # 运行主循环
    root.mainloop()
