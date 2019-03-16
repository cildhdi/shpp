import sys
from PyQt5 import Qt, QtGui, QtCore, QtWidgets, uic
import win32api
import win32gui
import win32con
import win32clipboard
import time
import threading
import sip
import constents
from uis.Ui_Simulate import Ui_MainWindow


class SimulateWnd(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, tender, pswd):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.tender = tender
        self.pswd = pswd
        self.setupUi(self)
        self.setFixedSize(900, 800)
        self.setWindowFlags(self.windowFlags() |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)

        self.axWidget.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.axWidget.setProperty("DisplayAlerts", False)
        self.axWidget.setProperty("DisplayScrollBars", False)
        self.axWidget.dynamicCall("Navigate(const QString&)", constents.dftUrl)
        self.axWidget.setFixedWidth(900)
        self.axWidget.setFixedHeight(700)

        self.btnLogin.clicked.connect(self.login)

    def click(self, x, y):
        win32api.SetCursorPos([self.x() + x, self.y() + y])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN |
                             win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def sendText(self, text, x, y):
        win32clipboard.OpenClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
        win32clipboard.CloseClipboard()
        self.click(x, y)
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        win32api.keybd_event(86, 0, 0, 0)
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(win32con.VK_CONTROL, 0,
                             win32con.KEYEVENTF_KEYUP, 0)

    def login(self):
        win32gui.SetFocus(int(self.winId()))
        t = threading.Thread(target=self.loginThread, name="loginThread")
        t.start()

    def loginThread(self):
        self.click(760, 540)
        self.click(760, 540)
        self.sendText(self.tender, 600, 250)
        time.sleep(0.5)
        self.sendText(self.pswd, 600, 300)
