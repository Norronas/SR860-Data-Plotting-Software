import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "includes": ["tkinter", "matplotlib", "pyvisa", "PIL", "cmath", "sympy", "scipy", "numpy"],
    "zip_include_packages": ["encodings", "PySide6", "numpy"],
}

sys.setrecursionlimit(sys.getrecursionlimit() * 5)

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="3Ꞷ Helping Software",
    version="1.0",
    description="Software of MITEC to help with 3Ꞷ method ",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="icon.ico")],
)