from cx_Freeze import setup, Executable
import sys




setup(
    name = "Lolik",
    version = "0.1.0",
    #options = {"build_exe": {"include_files": ["backspace-icon.png", "copy-icon.png", "information-icon.png", "RomanToInteger-icon.png", "qt-icon.png"]}},
    #options = {"build_exe": {"include_files": ["backspace-icon.png", "copy-icon.png", "information-icon.png", "RomanToInteger-icon.png", "qt-icon.png"]}},
    executables = [Executable("Lolik.py", base = "Win32GUI", icon = "Lolik-MainIcon.ico")]
) 


