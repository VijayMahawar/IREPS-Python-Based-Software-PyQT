import cx_Freeze
import sys
import os

dir_to_look_in = [r'C:\Bib\Prod\Miniconda3-64\envs\weap-dev\Lib\site-packages',
r'C:\Bib\Prod\Miniconda3-64\envs\statmath\Lib\site-packages',
r'C:\Bib\Prod\Miniconda3-64\Lib\site-packages',
r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App',
r'C:\Bib\Prod\Miniconda3-64\pkgs\qt-5.6.2-vc14h6f8c307_12']
[sys.path.append(x) for x in dir_to_look_in]

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

os.__file__ = r'C:\\Miniconda3\\envs\\statmath\\lib\\os.py'	
#os.environ['TCL_LIBRARY'] = r'C:\Miniconda3\envs\statmath\tcl\tcl8.5'
#os.environ['TK_LIBRARY'] = r'C:\Miniconda3\envs\statmath\tcl\tk8.5'
#os.environ['TCL_LIBRARY'] = r'C:\Bib\Prod\Miniconda3-64\tcl\tcl8.6'
#os.environ['TK_LIBRARY'] = r'C:\Bib\Prod\Miniconda3-64\tcl\tk8.6'
os.environ['TCL_LIBRARY'] = r'C:\Miniconda3\envs\statmath\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Miniconda3\envs\statmath\tcl\tk8.6'
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
    
executables = [cx_Freeze.Executable(r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App\IREPS\launch_app.py',
                                    base = base, icon = r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\AppIcon.ico')]

cx_Freeze.setup(name = 'IREPS Tender DataBase Manager',
               options = {'build_exe':{'packages':['asyncio', 'appdirs', 'packaging', 'pkg_resources', 'idna', r'C:\Miniconda3\envs\statmath\Lib\site-packages\numpy',
			                                       r'C:\Miniconda3\envs\statmath\Lib\site-packages\pandas',
			                                       r'C:\Miniconda3\envs\statmath\Lib\site-packages\bs4',
												   'ssl', r'C:\Miniconda3\envs\statmath\Lib\site-packages\urllib3',
												   r'C:\Miniconda3\envs\statmath\Lib\site-packages\certifi',
												   r'C:\Miniconda3\envs\statmath\Lib\site-packages\requests', 'webbrowser', 'tika',
												   'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets',
												  r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App\IREPS'],
                                       'include_files':[os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                                                        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
														#r'C:\Bib\Prod\Miniconda3-64\DLLs\tk86t.dll',
														#r'C:\Bib\Prod\Miniconda3-64\DLLs\tcl86t.dll',
														r'C:\Bib\Prod\Miniconda3-64\pkgs\qt-5.6.2-vc14h6f8c307_12\Library\plugins\platforms\qwindows.dll',
														r'C:\Bib\Prod\Miniconda3-64\Library\plugins\PyQt5\pyqt5qmlplugin.dll',
														r'C:\Bib\Prod\Miniconda3-64\Lib\site-packages\PyQt5\uic\port_v2\invoke.py',
                                       			        r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App\IREPS',
														r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\AppIcon.png',
														r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\AppIcon.ico']}},
               version = '1.0',
               description = 'IREPS Tender DataBase Manager',
               executables = executables)
			   
			   
#options = {"build_exe": {"packages":["tkinter","PyQt5.QtCore","PyQt5.QtGui", "PyQt5.QtWidgets","ctypes","timeit",
#"matplotlib","numpy","cv2"],
# "include_files":[r"C:\Users\danial khan\AppData\Local\Programs\Python\Python35\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll",
# r"C:\Users\danial khan\AppData\Local\Programs\Python\Python35\DLLs\tcl86t.dll",
# r"C:\Users\danial khan\AppData\Local\Programs\Python\Python35\DLLs\tk86t.dll","tdic1.ico"]}},
#version = "0.01",
#r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\AppIcon.png',
#['numpy', 'pandas',"PyQt5.QtCore","PyQt5.QtGui", "PyQt5.QtWidgets", r'C:\Users\g200673\Desktop\India\Python\GUI_Tutorial\PyQT\IREPS_App\IREPS']






