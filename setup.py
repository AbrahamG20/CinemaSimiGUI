import sys
import os
from cx_Freeze import setup, Executable

files = ['upc_logo.ico']

target = Executable(
    script= "mainGUI.py",
    base = "Win32GUI",
    icon = 'upc_logo.ico'
)

setup(
    name = "CinemaSimi",
    version = "1.0",
    description = "CinemaSimi: Subtitulado de cine al quechua utilizando deep learning",
    author = "Abraham G. Alvarez Crespo, Diego L. Miranda Salazar",
    options = {'build.exe' : {'include_files' : files}},
    executables = [target]
)
