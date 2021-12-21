# icon fix for pyinstaller, suggested by joylin1984 at https://github.com/PySimpleGUI/PySimpleGUI/issues/445
import os

root = os.path.dirname(__file__)
icon_crop_ico = os.path.join(root, 'images/crop.ico')
icon_crop_gif = os.path.join(root, 'images/crop.gif')