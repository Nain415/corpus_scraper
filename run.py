import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'convokit'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])
import gui.controllerview, main.scrapermodel

def main():
    gui.controllerview.main()

if __name__ == '__main__':
    main()
