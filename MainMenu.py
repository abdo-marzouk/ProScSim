# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\College and Courses\College\Operating systems\MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SimulateButton = QtWidgets.QPushButton(self.centralwidget)
        self.SimulateButton.setGeometry(QtCore.QRect(270, 240, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.SimulateButton.setFont(font)
        self.SimulateButton.setObjectName("SimulateButton")
        self.SJFNonRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.SJFNonRadio.setGeometry(QtCore.QRect(330, 150, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.SJFNonRadio.setFont(font)
        self.SJFNonRadio.setObjectName("SJFNonRadio")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 100, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.FCFSRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.FCFSRadio.setGeometry(QtCore.QRect(110, 150, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.FCFSRadio.setFont(font)
        self.FCFSRadio.setObjectName("FCFSRadio")
        self.SJFPreRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.SJFPreRadio.setGeometry(QtCore.QRect(110, 190, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.SJFPreRadio.setFont(font)
        self.SJFPreRadio.setObjectName("SJFPreRadio")
        self.PrioRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.PrioRadio.setGeometry(QtCore.QRect(330, 190, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.PrioRadio.setFont(font)
        self.PrioRadio.setObjectName("PrioRadio")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(380, 100, 51, 21))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SimulateButton.setText(_translate("MainWindow", "Simulate"))
        self.SJFNonRadio.setText(_translate("MainWindow", "Shortest Job First (Non-Preemptive)"))
        self.label.setText(_translate("MainWindow", "Number of processes"))
        self.label_2.setText(_translate("MainWindow", "Process Scheduling Simulator"))
        self.FCFSRadio.setText(_translate("MainWindow", "First Come First Served"))
        self.SJFPreRadio.setText(_translate("MainWindow", "Shortest Job First (Preemptive)"))
        self.PrioRadio.setText(_translate("MainWindow", "Priority"))
        self.label_3.setText(_translate("MainWindow", "ProScSim"))
