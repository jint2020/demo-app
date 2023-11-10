import tkinter as tk
from tkinter import messagebox
import subprocess
from main_app import SimpleApp


def show_message(message):
    messagebox.showinfo("更新提示", message)

def main_app():
    # 模拟检查更新的逻辑
    has_update = True  # 根据实际情况设置是否有更新

    if has_update:
        # 模拟下载新程序的过程
        # 此处可以使用实际的下载逻辑，例如使用 requests 库下载新程序
        # ...

        # 下载完成后显示提示信息
        show_message("更新完成，正在重启主程序。")
    else:
        show_message("当前是最新版本，无需更新。")

if __name__ == "__main__":

    # 获取主程序的进程ID
    main_app_process_id = SimpleApp.kill_current_pid()
    # 启动主程序
    subprocess.run(["python", "main_app.py"])

    # 关闭当前的更新程序
    subprocess.run(["taskkill", "/F", "/PID", str(tk.Tk().pid)])
