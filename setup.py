from cx_Freeze import setup, Executable

files = ['upc_logo.ico']
#, 'D:\\Documentos\\Abraham Docs\\UPC\\2022-1\\Taller de Proyecto 1\\CinemaSimi_APP\\GUI v3.0\\model'
#Win32GUI

target = Executable(
    script= "mainGUI.py",
    base = "Console",
    icon = 'upc_logo.ico'
)

setup(
    name = "CinemaSimi",
    version = "1.0",
    description = "CinemaSimi: Subtitulado de cine al quechua utilizando deep learning",
    author = "Abraham G. Alvarez Crespo, Diego L. Miranda Salazar",
    options = {'build.exe' :
              {'include_files' : files,
               "packages":["moviepy", "tinytag", "os", "time", "torch", "sentencepiece", "transformers"]}},
    executables = [target]
)
