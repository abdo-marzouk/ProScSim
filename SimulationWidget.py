# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\College and Courses\College\Operating systems\Practical\SimulationWidgetWithTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimulationWidget(object):
    def setupUi(self, SimulationWidget):
        SimulationWidget.setObjectName("SimulationWidget")
        SimulationWidget.resize(430, 320)
        self.GrantChartWidget = QtWidgets.QWidget(SimulationWidget)
        self.GrantChartWidget.setGeometry(QtCore.QRect(10, 10, 410, 140))
        self.GrantChartWidget.setObjectName("GrantChartWidget")
        self.GrantScrollArea = QtWidgets.QScrollArea(self.GrantChartWidget)
        self.GrantScrollArea.setGeometry(QtCore.QRect(0, 0, 410, 140))
        self.GrantScrollArea.setWidgetResizable(False)
        self.GrantScrollArea.setObjectName("GrantScrollArea")
        self.GrantScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.GrantScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.processTable = QtWidgets.QTableWidget(SimulationWidget)
        self.processTable.setGeometry(QtCore.QRect(10, 160, 410, 150))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.processTable.setFont(font)
        self.processTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.processTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.processTable.setAlternatingRowColors(True)
        self.processTable.setRowCount(0)
        self.processTable.setColumnCount(5)
        self.processTable.setObjectName("processTable")
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.processTable.setHorizontalHeaderItem(4, item)
        self.processTable.setColumnWidth(0,80)
        self.processTable.setColumnWidth(1,80)
        self.processTable.setColumnWidth(2,80)
        self.processTable.setColumnWidth(3,80)
        self.processTable.setColumnWidth(4,70)
        self.processTable.verticalHeader().setVisible(False)

        self.retranslateUi(SimulationWidget)
        QtCore.QMetaObject.connectSlotsByName(SimulationWidget)

    def retranslateUi(self, SimulationWidget):
        _translate = QtCore.QCoreApplication.translate
        SimulationWidget.setWindowTitle(_translate("SimulationWidget", "Form"))
        self.processTable.setSortingEnabled(True)
        item = self.processTable.horizontalHeaderItem(0)
        item.setText(_translate("SimulationWidget", "PID"))
        item = self.processTable.horizontalHeaderItem(1)
        item.setText(_translate("SimulationWidget", "Arrival time"))
        item = self.processTable.horizontalHeaderItem(2)
        item.setText(_translate("SimulationWidget", "Burst time"))
        item = self.processTable.horizontalHeaderItem(3)
        item.setText(_translate("SimulationWidget", "Waiting time"))
        item = self.processTable.horizontalHeaderItem(4)
        item.setText(_translate("SimulationWidget", "Priority"))
