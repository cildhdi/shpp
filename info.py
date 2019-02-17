import sys
from PyQt5 import QtCore, QtWidgets, uic

import constents

Ui_MainWindow, QtBaseClass = uic.loadUiType(constents.uiInfo)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.editTender.setText(constents.dftTender)
        self.editPswd.setText(constents.dftPswd)
        self.editId.setText(constents.dftId)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec()
