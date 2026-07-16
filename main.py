#!/usr/bin/env python3
"""光伏收益分析系统 v11.0 - pywebview桌面应用"""

import os
import sys
import webview

def get_html_path():
    """获取HTML文件的绝对路径"""
    if getattr(sys, 'frozen', False):
        # PyInstaller打包后的路径
        base = sys._MEIPASS
    else:
        # 开发模式下的路径
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'app', 'index.html')

def main():
    html_path = get_html_path()

    # 创建窗口
    window = webview.create_window(
        title='光伏收益分析系统 v11.0',
        url=html_path,
        width=1440,
        height=900,
        min_size=(1024, 700),
        resizable=True,
        text_select=True,
    )

    # 启动应用
    webview.start(debug=False)

if __name__ == '__main__':
    main()
