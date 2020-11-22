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
from win10toast import ToastNotifier
# from pywinauto import *

req = "https://www.google.com"


class Connect:

    # app = application.Application()

    def notif(self):
        n = ToastNotifier()

        n.show_toast("Bad Connection",
                     "Wait until your connection is stable", duration=3)
        # while n.notification_active():
        #     sleep(0.1)

    def check(self):
        try:
            res = get(req, timeout=4)
            print("Connection is normal with status code : " + str(res.status_code))
        except Exception as e:
            print("error occured")
            # winsound.MessageBeep(winsound.SND_ASYNC)
            self.notif()
            # SetForegroundWindow(find_window(title='Connection Checker.exe'))
            # appp = self.app.connect(
            #     path="C:\\Users\\ZAKI\\Desktop\\Connection Checker.exe")
            # appp.minimize()
            # appp.restore()
            sleep(1)


# CLA Main menu
print("=== Just press 'CTRL + C' to Exit/ close ===")
pause("Press any key to start...")


# var = True

try:
    while True:
        Connect().check()
        sleep(2)
except Exception as e:
    print('Closing the program', e)
    sleep(3)
