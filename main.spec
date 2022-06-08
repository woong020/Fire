# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [ ("./.data/*", './.data'),
                ("./.ico/*", './.ico'),
                ("./FireUI.ui", '.'),
                ("./ui.py", '.'),
                ("./graph.py", '.')]
a = Analysis(
    ['main.py', 'graph.py', 'ui.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=["os.path", "PyQt5.QtWidgets", "PyQt5.QtGui", "PyQt5.QtCore", "PyQt5", "matplotlib.pyplot", "seaborn", "pandas", "matplotlib.backends.backend_qt5agg"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='Lonely Death',
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
    icon='./.ico/icon.png'
)
