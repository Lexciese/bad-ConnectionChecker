# [[source]]
# name = "pypi"
# url = "https://pypi.org/simple"
# verify_ssl = true

# [dev-packages]

# [packages]
# requests = "*"
# py-getch = "*"
# pyinstaller = "*"
# pywinauto = "*"

# [requires]
# python_version = "3.8"

from requests import get
from time import sleep
import winsound
from getch import pause
from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow


class Connect:

    req = "https://www.google.com"

    def check(self):
        try:
            res = get(self.req, timeout=4)
            print("Connection is normal with status code : " + str(res.status_code))
        except Exception as e:
            winsound.MessageBeep(winsound.SND_ASYNC)
            SetForegroundWindow(find_window(title='Connection Checker.exe'))
            print("error occured")
            sleep(1)

    # def ping():
    #     subprocess = subprocess.Popen(
    #         "ping 192.168.0.1 -t -l 32", shell=True, stdout=subprocess.PIPE)
    #     subprocess_return = subprocess.stdout.read()
    #     print(subprocess_return)



# CLA Main menu
print("=== Just press 'CTRL + C' to Exit/ close ===")
pause("Press any key to start...")


# var = True

try:
    while True:
        Connect().check()
        sleep(2)
except:
    print('Closing the program')
    sleep(3)
