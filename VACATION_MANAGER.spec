# -*- mode: python -*-

block_cipher = None


a = Analysis(['VACATION_MANAGER.py'],
             pathex=['C:\\Windows\\WinSxS\\x86_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.17134.1_none_50c6cb8431e7428f', 'C:\\Users\\Maciek\\Documents\\BELSAN\\VACATION_MANAGER\\VACATION_MANAGER'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='VACATION_MANAGER',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='logo_ikona.ico')
