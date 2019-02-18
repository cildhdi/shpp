import sys
from PyQt5 import QtCore, QtWidgets, uic

import constents
from simulate import SimulateWnd
from uis.Ui_Info import Ui_MainWindow


class InfoWnd(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.editTender.setText(constents.dftTender)
        self.editPswd.setText(constents.dftPswd)
        self.pushButton.clicked.connect(self.confirm)

    def confirm(self):
        self.simulate = SimulateWnd(
            self.editTender.text(), self.editPswd.text())
        self.simulate.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    info = InfoWnd()
    info.show()
    app.exec()
