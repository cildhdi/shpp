import sys
from PyQt5 import Qt, QtGui, QtCore, QtWidgets, uic

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
        self.axWidget.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.axWidget.setProperty("DisplayAlerts", False)
        self.axWidget.setProperty("DisplayScrollBars", False)
        self.axWidget.dynamicCall("Navigate(const QString&)", constents.dftUrl)
        self.axWidget.setFixedWidth(900)
        self.axWidget.setFixedHeight(700)

        self.btnLogin.clicked.connect(self.login)

    def login(self):
        print("login")

        point = QtCore.QPoint(760, 500)
        mousePress = QtGui.QMouseEvent(QtCore.QEvent.Type.MouseButtonPress, point, QtCore.Qt.MouseButton.LeftButton,
                                       QtCore.Qt.MouseButton.LeftButton, QtCore.Qt.KeyboardModifier.NoModifier)
        mouseRelease = QtGui.QMouseEvent(QtCore.QEvent.Type.MouseButtonRelease, point, QtCore.Qt.MouseButton.LeftButton,
                                         QtCore.Qt.MouseButton.LeftButton, QtCore.Qt.KeyboardModifier.NoModifier)
        QtWidgets.QWidget.setFocus(self.axWidget)
        print(QtWidgets.QApplication.sendEvent(
            self.axWidget, mousePress))
        print(QtWidgets.QApplication.sendEvent(
            self.axWidget, mouseRelease))
