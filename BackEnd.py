from random import randint
from itertools import groupby

class BasicJob:
    def __init__(self, ArrivalTime : int, RemainingTime : int, ID : str, Priority:int = 0):
        self.ID = ID
        self.ArrivalTime = ArrivalTime
        self.BurstTime = RemainingTime
        self.RemainingTime = RemainingTime
        self.StartingTime = 0
        self.EndTime = 0
        self.WaitingTime = 0
        self.Priority = Priority
        self.ChangedStartingTime = False

def FillJobsRandomly(NoOfJobs:int,IsPriority:bool):
    Jobs = [BasicJob(0,randint(1,15),"P1")]
    Jobs.extend([BasicJob(randint(0,15),randint(1,15),f"P{x+2}") for x in range(NoOfJobs - 1)])
    if IsPriority:
        for i in range(NoOfJobs):
            Jobs[i].Priority = randint(1,NoOfJobs)
    return Jobs

def SortQueue(JobQueue:list,SchedMode:int) -> list:
    if SchedMode == 1:
        JobQueue.sort(key=lambda x: (x.ArrivalTime, x.ID))
    elif SchedMode == 2:
        JobQueue.sort(key=lambda x: (x.BurstTime, x.ID))
    elif SchedMode == 3:
        JobQueue.sort(key=lambda x: (x.RemainingTime,x.ID))
    elif SchedMode == 4:
        JobQueue.sort(key=lambda x: (x.Priority,x.RemainingTime))
    return JobQueue

def ProScSim(Jobs : list, SchedMode : int, Quantum : int = 0):
    CurrTime = 0
    NoOfJobs = len(Jobs)
    EventList = []
    JobQueue = []
    JobsDone = []
    WorkingOnJob = False
    while len(JobsDone) != NoOfJobs:
        for i in Jobs:
            if i.ArrivalTime <= CurrTime and i not in JobQueue and i not in JobsDone:
                JobQueue.append(i)
        if SchedMode == 1 or SchedMode == 2:
            if not WorkingOnJob:
                JobQueue = SortQueue(JobQueue,SchedMode)
        elif SchedMode == 3 or SchedMode == 4:
            JobQueue = SortQueue(JobQueue,SchedMode)
        if len(JobQueue) == 0:
            EventList.append("Idle")
        else:
            if SchedMode == 1 or SchedMode == 2:
                if WorkingOnJob == False:
                    if JobQueue[0].ChangedStartingTime == False:
                        JobQueue[0].StartingTime = CurrTime
                        JobQueue[0].ChangedStartingTime = True
                    WorkingOnJob = True
                if WorkingOnJob:
                    if JobQueue[0].RemainingTime > 0:
                        EventList.append(JobQueue[0].ID)
                        JobQueue[0].RemainingTime -= 1
                    else:
                        JobQueue[0].EndTime = CurrTime
                        JobQueue[0].WaitingTime = JobQueue[0].StartingTime - JobQueue[0].ArrivalTime
                        JobsDone.append(JobQueue.pop(0))
                        WorkingOnJob = False
                        CurrTime -= 1

            elif SchedMode == 3 or SchedMode == 4:
                if JobQueue[0].ChangedStartingTime == False:
                    JobQueue[0].StartingTime = CurrTime
                    JobQueue[0].ChangedStartingTime = True
                if JobQueue[0].RemainingTime > 0:
                    EventList.append(JobQueue[0].ID)
                    JobQueue[0].RemainingTime -= 1
                else:
                    JobQueue[0].EndTime = CurrTime
                    JobQueue[0].WaitingTime = JobQueue[0].EndTime - JobQueue[0].ArrivalTime - JobQueue[0].BurstTime
                    JobsDone.append(JobQueue.pop(0))
                    CurrTime -= 1
            else:
                if CurrTime != 0:
                    if CurrTime % Quantum == 0:
                        JobQueue.append(JobQueue.pop(0))
                        WorkingOnJob = False
                if WorkingOnJob == False:
                    if JobQueue[0].ChangedStartingTime == False:
                        JobQueue[0].StartingTime = CurrTime
                        JobQueue[0].ChangedStartingTime = True
                    WorkingOnJob = True
                if WorkingOnJob:
                    if JobQueue[0].RemainingTime > 0:
                        EventList.append(JobQueue[0].ID)
                        JobQueue[0].RemainingTime -= 1
                    else:
                        JobQueue[0].EndTime = CurrTime
                        JobQueue[0].WaitingTime = JobQueue[0].EndTime - JobQueue[0].ArrivalTime - JobQueue[0].BurstTime 
                        JobsDone.append(JobQueue.pop(0))
                        WorkingOnJob = False
                        CurrTime -= 1
        CurrTime += 1
    FinalEventList = []
    for i in groupby(EventList):
        FinalEventList.append([i[0],len(list(i[1]))])
    return FinalEventList,JobsDone

def MainHelperFunc(NoOfJobs : int, Jobs : list, SchedMode : int, IsManual : bool, Quantum : int = 0):
    if not IsManual:
        if SchedMode == 4:
            Jobs = FillJobsRandomly(NoOfJobs,True)
        else:
            Jobs = FillJobsRandomly(NoOfJobs,False)
    FinalEventList, JobsDone = ProScSim(Jobs,SchedMode,Quantum)
    return FinalEventList, JobsDone