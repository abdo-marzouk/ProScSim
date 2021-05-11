import sys
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QFont, QPainter,QColor,QPen, QTextOption
from MainMenu import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from BackEnd import *
from SimulationWidget import *

class SimWindow(QtWidgets.QWidget,Ui_SimulationWidget):
    def __init__(self,*args,**kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_SimulationWidget.__init__(self)
        self.setupUi(self)
    def paintEvent(self, e):
        Painter = QPainter()
        Painter.begin(self)
        Painter.setFont(QFont("times",12))
        Pen = QPen(Qt.black,3,Qt.SolidLine)
        CurrX = 30
        CurrY = 50
        CurrTime = 0
        Painter.setPen(Pen)
        for i in range(len(self.EventList)):
            if CurrX+(15*self.EventList[i][1]) > self.size().width():
                self.resize(self.size().width() + 100,self.size().height())
            Painter.drawLine(CurrX,CurrY-30,CurrX,CurrY)
            Painter.drawLine(CurrX,CurrY,CurrX+(15*self.EventList[i][1]),CurrY)
            TextPoint = QPoint()
            TextPoint.setX(CurrX + (abs(CurrX - CurrX+10*self.EventList[i][1])//2))
            TextPoint.setY(CurrY - 20)
            Painter.drawText(TextPoint,self.EventList[i][0])
            AnotherTextPoint = QPoint()
            AnotherTextPoint.setX(CurrX)
            AnotherTextPoint.setY(CurrY + 20)
            Painter.drawText(AnotherTextPoint,str(CurrTime))
            CurrTime += self.EventList[i][1]
            CurrX += 15*self.EventList[i][1]
            if i == len(self.EventList) - 1:
                Painter.drawLine(CurrX,CurrY-30,CurrX,CurrY)
                AnotherTextPoint.setX(CurrX)
                AnotherTextPoint.setY(CurrY + 20)
                Painter.drawText(AnotherTextPoint,str(CurrTime))
        CurrX = 30
        CurrY = 100
        self.KeyList = list(self.WaitingTimes.keys())
        self.KeyList.sort()
        for i in range(len(self.KeyList)):
            S = f"{self.KeyList[i]}'s Waiting time is {self.WaitingTimes[self.KeyList[i]]}"
            TextPoint = QPoint(CurrX,CurrY+(i*20))
            Painter.drawText(TextPoint,S)
    def TakeEventsAndTimes(self,EventList,WaitingTimes):
        self.EventList = EventList
        self.WaitingTimes = WaitingTimes

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.SimulateButton.clicked.connect(self.DrawChart)
    def DrawChart(self):
        if self.spinBox.value() <= 0:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid input")
            msg.setText("Invalid input. Must be positive integer.")
            msg.exec()
        NoOfJobs = self.spinBox.value()
        if self.FCFSRadio.isChecked():
            EventList,WaitingTimes = ProScSim(NoOfJobs,1)
        elif self.SJFNonRadio.isChecked():
            EventList,WaitingTimes = ProScSim(NoOfJobs,2)
        elif self.SJFPreRadio.isChecked():
            EventList,WaitingTimes = ProScSim(NoOfJobs,3)
        elif self.PrioRadio.isChecked():
            EventList,WaitingTimes = ProScSim(NoOfJobs,4)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Mode not selected")
            msg.setText("You forgot to select the mode.")
            msg.exec()
        try:
            SimWin.TakeEventsAndTimes(EventList,WaitingTimes)
            SimWin.show()
        except:
            pass
App = QtWidgets.QApplication(sys.argv)
Main = MainWindow()
SimWin = SimWindow()


if __name__ == "__main__":
    
    Main.show()
    sys.exit(App.exec())