# -*- mode: python ; coding: utf-8 -*-
"""光伏收益分析系统 v11.0 - PyInstaller spec文件"""

import os
import sys

block_cipher = None

# 应用根目录
app_root = os.path.dirname(os.path.abspath(SPEC))

a = Analysis(
    [os.path.join(app_root, 'main.py')],
    pathex=[app_root],
    binaries=[],
    datas=[
        (os.path.join(app_root, 'app', 'index.html'), 'app'),
        (os.path.join(app_root, 'app', 'lib', 'chart.umd.min.js'), 'app/lib'),
    ],
    hiddenimports=['webview', 'webview.platforms.winforms'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'pytest', 'django', 'flask'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='光伏收益分析系统',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
