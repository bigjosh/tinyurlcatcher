"""Register TinyURLCatcher as a URL handler in the Windows Registry (HKCU)."""

import os
import sys
import winreg

PYTHON_EXE = sys.executable
SCRIPT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tinyurlcatcher.py")
PROG_ID = "TinyURLCatcherURL"
APP_KEY = r"Software\TinyURLCatcher"
CAPABILITIES_PATH = APP_KEY + r"\Capabilities"


def set_value(key, name, value):
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)


def main():
    command = f'"{PYTHON_EXE}" "{SCRIPT_PATH}" "%1"'

    # 1. ProgID: HKCU\Software\Classes\TinyURLCatcherURL
    prog_id_path = rf"Software\Classes\{PROG_ID}"
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, prog_id_path) as key:
        set_value(key, "", "TinyURLCatcher URL")
        set_value(key, "URL Protocol", "")

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, rf"{prog_id_path}\shell\open\command") as key:
        set_value(key, "", command)

    print(f"  ProgID: HKCU\\{prog_id_path}")

    # 2. Capabilities: HKCU\Software\TinyURLCatcher\Capabilities
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, CAPABILITIES_PATH) as key:
        set_value(key, "ApplicationName", "TinyURLCatcher")
        set_value(key, "ApplicationDescription", "Catches and displays URLs")

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, CAPABILITIES_PATH + r"\URLAssociations") as key:
        set_value(key, "https", PROG_ID)
        set_value(key, "http", PROG_ID)

    print(f"  Capabilities: HKCU\\{CAPABILITIES_PATH}")

    # 3. RegisteredApplications
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\RegisteredApplications") as key:
        set_value(key, "TinyURLCatcher", CAPABILITIES_PATH)

    print(f"  RegisteredApplications: TinyURLCatcher")

    print()
    print(f"Python: {PYTHON_EXE}")
    print(f"Script: {SCRIPT_PATH}")
    print(f"Command: {command}")
    print()
    print("Done. Go to Windows Settings > Default Apps and select TinyURLCatcher as your web browser.")


if __name__ == "__main__":
    print("Registering TinyURLCatcher...\n")
    main()
