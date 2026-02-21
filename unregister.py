"""Remove TinyURLCatcher registry entries from HKCU."""

import winreg

PROG_ID = "TinyURLCatcherURL"


def delete_tree(hive, path):
    """Recursively delete a registry key and all its subkeys."""
    try:
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_ALL_ACCESS)
    except FileNotFoundError:
        return False

    # Enumerate and delete subkeys first
    while True:
        try:
            subkey = winreg.EnumKey(key, 0)
            delete_tree(hive, rf"{path}\{subkey}")
        except OSError:
            break

    winreg.CloseKey(key)
    winreg.DeleteKey(hive, path)
    return True


def delete_value(hive, path, name):
    """Delete a single value from a registry key."""
    try:
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, name)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False


def main():
    hkcu = winreg.HKEY_CURRENT_USER

    # 1. ProgID
    path = rf"Software\Classes\{PROG_ID}"
    if delete_tree(hkcu, path):
        print(f"  Removed HKCU\\{path}")
    else:
        print(f"  Not found: HKCU\\{path}")

    # 2. App capabilities
    path = r"Software\TinyURLCatcher"
    if delete_tree(hkcu, path):
        print(f"  Removed HKCU\\{path}")
    else:
        print(f"  Not found: HKCU\\{path}")

    # 3. RegisteredApplications entry
    if delete_value(hkcu, r"Software\RegisteredApplications", "TinyURLCatcher"):
        print(f"  Removed RegisteredApplications\\TinyURLCatcher")
    else:
        print(f"  Not found: RegisteredApplications\\TinyURLCatcher")

    print("\nDone. You may want to reset your default browser in Windows Settings > Default Apps.")


if __name__ == "__main__":
    print("Unregistering TinyURLCatcher...\n")
    main()
