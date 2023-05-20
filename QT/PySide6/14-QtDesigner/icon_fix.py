###########################################################################################
# Purpose: File created to fix the issue with the icon not showing up in the taskbar on Windows 10
# Reference: https://stackoverflow.com/questions/33768634/pyqt5-application-icon-not-showing-in-taskbar
# Creator: Paul Sherwood
# Date: May 20 2023
###########################################################################################

import ctypes, platform

# Setup to test for operating system version
os_name = platform.system()

def set_taskbar_icon():
    # Taskbar Icon fix for Windows 10
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
