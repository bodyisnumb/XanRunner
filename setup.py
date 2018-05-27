import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("XanRunner.py")]

cx_Freeze.setup(
    name="Xan Runner",
    options={"build_exe": {"packages":["pygame", "random", "time"],
                           "include_files":["Images/", "Music/"]}},
    executables = executables

    )