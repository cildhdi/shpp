# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Miles\Desktop\shpp\uis\Simulate.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 804)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.axWidget = QAxContainer.QAxWidget(self.centralwidget)
        self.axWidget.setProperty("geometry", QtCore.QRect(0, 0, 900, 700))
        self.axWidget.setObjectName("axWidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 730, 301, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLogin = QtWidgets.QPushButton(self.widget)
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout.addWidget(self.btnLogin)
        self.btnVerifi = QtWidgets.QPushButton(self.widget)
        self.btnVerifi.setObjectName("btnVerifi")
        self.horizontalLayout.addWidget(self.btnVerifi)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "模拟"))
        self.btnLogin.setText(_translate("MainWindow", "登录"))
        self.btnVerifi.setText(_translate("MainWindow", "验证"))

from PyQt5 import QAxContainer
