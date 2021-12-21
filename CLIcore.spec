# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['CLIcore.py'],
             pathex=[],
             binaries=[],
             datas=[('iconfix.py', '.'),('images/crop.ico', 'images'), ('images/crop.gif', 'images')],
             hiddenimports=['PIL.Image'],
             hookspath=[],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='PictureCropperCLI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None, 
          icon='images/crop.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PictureCropperCLI', 
               icon='images/crop.ico')
