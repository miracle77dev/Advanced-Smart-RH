from cx_Freeze import setup, Executable
import os, sys

song = os.path.abspath("song.mp3")
db = os.path.abspath("srh.db")
Files = ['./ASRH_logo.ico', db, song, './know/MIRACULEUX - 7777777777777777.PNG', 'sanflan.png']

Target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="ASRH_logo.ico"
)

setup(
    name="Advanced Smart RH",
    version="0.1",
    description="Test de convertion py to exe",
    options={"build_exe": {"include_files": Files}},
    executables=[Target]
)


