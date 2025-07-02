import sys

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QFont, QPainter, QPen
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from BackEnd import *
from MainMenu import *
from ManualEntry import *
from SimulationWidget import *


class DrawingWidget(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        super(DrawingWidget, self).__init__(*args, **kwargs)
        
    def TakeLists(self,EventList:list,JobsDone:list,IsPrio:bool):
        self.EventList = EventList
        self.JobsDone = JobsDone
        self.IsPrio = IsPrio
        self.resize(400,140)

    def paintEvent(self,e):
        Painter = QPainter()
        Painter.begin(self)
        Painter.setFont(QFont("times",12))
        self.Pen = QPen(Qt.black,3,Qt.SolidLine)
        CurrX = 30
        CurrY = 70
        CurrTime = 0
        Painter.setPen(self.Pen)
        for i in range(len(self.EventList)):
            if CurrX+(15*self.EventList[i][1]) > self.size().width():
                self.resize((CurrX+(15*self.EventList[i][1])) + 20,self.size().height())
            Painter.drawLine(CurrX,CurrY-30,CurrX,CurrY)
            if self.EventList[i][0] == "Idle":
                Painter.drawLine(CurrX,CurrY,CurrX+40,CurrY)
            else:
                if self.EventList[i][1] < 2:
                    Painter.drawLine(CurrX,CurrY,CurrX+30,CurrY)    
                else:
                    Painter.drawLine(CurrX,CurrY,CurrX+(15*self.EventList[i][1]),CurrY)
            TextPoint = QPoint()
            if self.EventList[i][0] == "Idle":
                TextPoint.setX(CurrX + ((abs(CurrX - CurrX+self.EventList[i][1]))+10//2))    
            else:
                TextPoint.setX(CurrX + (abs(CurrX - CurrX+10*self.EventList[i][1])//2))
            TextPoint.setY(CurrY - 20)
            Painter.drawText(TextPoint,self.EventList[i][0])
            AnotherTextPoint = QPoint()
            AnotherTextPoint.setX(CurrX)
            AnotherTextPoint.setY(CurrY + 20)
            Painter.drawText(AnotherTextPoint,str(CurrTime))
            CurrTime += self.EventList[i][1]
            if self.EventList[i][0] == "Idle":
                CurrX += 40
            else:
                if self.EventList[i][1] < 2:
                    CurrX += 30
                else:
                    CurrX += 15*self.EventList[i][1]
            if i == len(self.EventList) - 1:
                Painter.drawLine(CurrX,CurrY-30,CurrX,CurrY)
                AnotherTextPoint.setX(CurrX)
                AnotherTextPoint.setY(CurrY + 20)
                Painter.drawText(AnotherTextPoint,str(CurrTime))

class SimWindow(QtWidgets.QWidget,Ui_SimulationWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        Ui_SimulationWidget.__init__(self)
        self.setupUi(self)
        self.setFixedHeight(self.size().height())
        self.GrantChartContent = DrawingWidget()
        self.GrantChartContent.setGeometry(QtCore.QRect(0, 0, 408, 138))
        self.GrantChartContent.setObjectName("GrantChartContent")
        self.GrantScrollArea.setWidget(self.GrantChartContent)
    
    def drawProcessInfo(self):
        self.JobsDone.sort(key=lambda x: x.ID)
        self.processTable.setRowCount(0)
        for i in range(len(self.JobsDone)):
            self.processTable.insertRow(i)
            self.processTable.setItem(i,0,QTableWidgetItem(str(self.JobsDone[i].ID)))
            self.processTable.setItem(i,1,QTableWidgetItem(str(self.JobsDone[i].ArrivalTime)))
            self.processTable.setItem(i,2,QTableWidgetItem(str(self.JobsDone[i].BurstTime)))
            self.processTable.setItem(i,3,QTableWidgetItem(str(self.JobsDone[i].WaitingTime)))
            self.processTable.setItem(i,4,QTableWidgetItem(str(self.JobsDone[i].Priority)))
        self.processTable.insertRow(len(self.JobsDone))
        self.processTable.setItem(len(self.JobsDone),0,QTableWidgetItem("Avg"))
        self.processTable.setItem(len(self.JobsDone),1,QTableWidgetItem("Turnaround"))
        self.processTable.setItem(len(self.JobsDone),2,QTableWidgetItem(str(sum(x.EndTime - x.StartingTime for x in self.JobsDone) / len(self.JobsDone))))
        self.processTable.setItem(len(self.JobsDone),3,QTableWidgetItem("Wait"))
        self.processTable.setItem(len(self.JobsDone),4,QTableWidgetItem(str(sum(x.WaitingTime for x in self.JobsDone) / len(self.JobsDone))))
    
    def paintEvent(self,e):        
        self.GrantChartContent.TakeLists(self.EventList,self.JobsDone,self.IsPrio)
        self.drawProcessInfo()

    def TakeLists(self,EventList:list,JobsDone:list,IsPrio:bool):
        self.EventList = EventList
        self.JobsDone = JobsDone
        self.IsPrio = IsPrio

class MnaualEntryWindow(QtWidgets.QWidget,Ui_ManualEntryWidnow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QWidget.__init__(self)
        Ui_SimulationWidget.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.NextButton.clicked.connect(self.NextJob)
        self.PrevButton.clicked.connect(self.PrevJob)
        
    def TakeData(self, NoOfJobs:int, SchedMode : int, QuantumValue : int, IsPrio : bool):
        self.NoOfJobs = NoOfJobs
        self.JobList = [BasicJob(0,0,"P0",0) for i in range(NoOfJobs)]
        self.CurrJobIndex = 0
        self.CurrentProcessLabel.setText(f"P{self.CurrJobIndex}")
        self.SchedMode = SchedMode
        self.QuantumValue = QuantumValue
        self.IsPrio = IsPrio
        if self.IsPrio:
            self.PrioSpin.setEnabled(True)
            self.PrioSpin.setReadOnly(False)
        else:
            self.PrioSpin.setEnabled(False)
            self.PrioSpin.setReadOnly(True)

    def EditJobAtIndex(self,ArrivalTime:int,BurstTime:int,Prio:int,CurrJobIndex:int):
        self.JobList[CurrJobIndex] = BasicJob(ArrivalTime,BurstTime,f"P{CurrJobIndex}",Prio)
    
    def NextJob(self):
        self.EditJobAtIndex(self.ArrivalTimeSpin.value(),self.BurstTimeSpin.value(),self.PrioSpin.value(),self.CurrJobIndex)
        self.ArrivalTimeSpin.setValue(0)
        self.BurstTimeSpin.setValue(0)
        self.PrioSpin.setValue(0)
        if self.CurrJobIndex == self.NoOfJobs - 1:
            msg = QMessageBox()
            msg.setWindowTitle("Done")
            msg.setText("Input recieved.")
            self.CurrJobIndex = 0
            self.CurrentProcessLabel.setText(f"P{self.CurrJobIndex}")
            EventList,JobsDone = MainHelperFunc(self.NoOfJobs,self.JobList,self.SchedMode,True,self.QuantumValue)
            if self.SchedMode == 4:
                SimWin.TakeLists(EventList,JobsDone,True)
            else:
                SimWin.TakeLists(EventList,JobsDone,False)
            SimWin.show()
            self.close()
        else:
            self.CurrJobIndex += 1
            self.CurrentProcessLabel.setText(f"P{self.CurrJobIndex}")

    def PrevJob(self):
        if self.CurrJobIndex <= 0:
            msg = QMessageBox()
            msg.setWindowTitle("Invalid input")
            msg.setText("Can't go back more.")
            msg.exec()
        else:
            self.CurrJobIndex -= 1
            self.JobToEdit = self.JobList[self.CurrJobIndex]
            self.ArrivalTimeSpin.setValue(self.JobToEdit.ArrivalTime)
            self.BurstTimeSpin.setValue(self.JobToEdit.BurstTime)
            self.PrioSpin.setValue(self.JobToEdit.Priority)
            self.CurrentProcessLabel.setText(f"P{self.CurrJobIndex}")

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.SimulateButton.clicked.connect(self.DrawRandom)
        self.ManualEntriesButton.clicked.connect(self.SummonManualWindow)

    def areInputsValid(self) -> bool:
        msg = QMessageBox()
        if self.spinBox.value() <= 0:
            msg.setWindowTitle("Invalid input")
            msg.setText("Invalid input. Number of processes must be a positive integer.")
            msg.exec()
            return False
        if self.QuantumSpin.value() == 0 and self.RoundRobinRadio.isChecked():
            msg.setWindowTitle("Invalid Quantum")
            msg.setText("Invalid input. Time quantum must be a positive integer.")
            msg.exec()
            return False
        return True

    def DrawRandom(self):
        if self.areInputsValid():
            NoOfJobs = self.spinBox.value()
            if self.FCFSRadio.isChecked():
                EventList,JobsDone = MainHelperFunc(NoOfJobs,[],1,False,0)
            elif self.SJFNonRadio.isChecked():
                EventList,JobsDone = MainHelperFunc(NoOfJobs,[],2,False,0)
            elif self.SJFPreRadio.isChecked():
                EventList,JobsDone = MainHelperFunc(NoOfJobs,[],3,False,0)
            elif self.PrioRadio.isChecked():
                EventList,JobsDone = MainHelperFunc(NoOfJobs,[],4,False,0)
            elif self.RoundRobinRadio.isChecked():
                QuantumNumber= self.QuantumSpin.value()
                EventList,JobsDone = MainHelperFunc(NoOfJobs,[],5,False,QuantumNumber)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Mode not selected")
                msg.setText("You forgot to select the mode.")
                msg.exec()
            try:
                if self.PrioRadio.isChecked():
                    SimWin.TakeLists(EventList,JobsDone,True)
                    SimWin.show()
                else:
                    SimWin.TakeLists(EventList,JobsDone,False)
                    SimWin.show()
            except:
                pass

    def SummonManualWindow(self):
        if self.areInputsValid():
            self.NoOfJobs = self.spinBox.value()
            self.QuantumNumber = self.QuantumSpin.value()
            if self.FCFSRadio.isChecked():
                ManualEntryWindow.TakeData(self.NoOfJobs, 1, self.QuantumNumber, False)
                ManualEntryWindow.show()
            elif self.SJFNonRadio.isChecked():
                ManualEntryWindow.TakeData(self.NoOfJobs, 2, self.QuantumNumber, False)
                ManualEntryWindow.show()
            elif self.SJFPreRadio.isChecked():
                ManualEntryWindow.TakeData(self.NoOfJobs, 3, self.QuantumNumber, False)
                ManualEntryWindow.show()
            elif self.PrioRadio.isChecked():
                ManualEntryWindow.TakeData(self.NoOfJobs, 4, self.QuantumNumber, True)
                ManualEntryWindow.show()
            elif self.RoundRobinRadio.isChecked():
                ManualEntryWindow.TakeData(self.NoOfJobs, 5, self.QuantumNumber, False)
                ManualEntryWindow.show()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Mode not selected")
                msg.setText("You forgot to select the mode.")
                msg.exec()

App = QtWidgets.QApplication(sys.argv)
Main = MainWindow()
SimWin = SimWindow()
ManualEntryWindow = MnaualEntryWindow()
if __name__ == "__main__":
    Main.show()
    sys.exit(App.exec())