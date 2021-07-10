from  random import randint
from time import sleep

class BasicJob:
    def __init__(self, ArrivalTime : int, RemainingTime : int, ID : str):
        self.ID = ID
        self.ArrivalTime = ArrivalTime
        self.BurstTime = RemainingTime
        self.RemainingTime = RemainingTime
        self.StartingTime = 0
        self.EndTime = 0
        self.WaitingTime = 0
        self.Priority : int

def FillJobs(NoOfJobs:int,IsPriority:bool): 
    Jobs = [BasicJob(0,randint(1,20),"P1")] ## Starts the jobs list with one element with arrival time of 0
    Jobs.extend([BasicJob(randint(0,10),randint(1,15),f"P{x+2}") for x in range(NoOfJobs - 1)]) ## extends the job list with jobs with random arrival times and random initial remaining times (Burst times). 
    if IsPriority:
        for i in range(NoOfJobs):
            Jobs[i].Priority = randint(1,NoOfJobs)
    return Jobs

def SortQueue(JobQueue:list,SchedMode:int) -> list:
    if SchedMode == 1:
        JobQueue.sort(key=lambda x: x.ArrivalTime) ## Attempts to sort the queue based on arrival time.
    elif SchedMode == 2 or SchedMode == 3:
        JobQueue.sort(key=lambda x: x.RemainingTime) ## Attempts to sort the queue based on Remaining time.
    elif SchedMode == 4:
        JobQueue.sort(key=lambda x: (x.Priority,x.RemainingTime))
    return JobQueue

def ProScSim(NoOfJobs:int,SchedMode:int): ## Takes the number of proccsses and the scheduling mode
    CurrTime = 0
    WorkingOnJob = False
    if SchedMode == 4:
        Jobs = FillJobs(NoOfJobs,True)
    else:
        Jobs = FillJobs(NoOfJobs,False)
    JobQueue = []
    JobsDone = []
    while len(JobsDone) != NoOfJobs: ## Loops until all jobs are done
        for i in Jobs:
            if i.ArrivalTime <= CurrTime and i not in JobQueue and i not in JobsDone:  ## Adds the job into the job queue if it isn't there already and if it isn't done
                JobQueue.append(i)
        JobQueue = SortQueue(JobQueue,SchedMode) ## Calls the Function that sorts the queue based on the mode and updates the queue value
        if len(JobQueue) == 0:  ## Job Queue is empty
            sleep(1)
            print(f"Current time is {CurrTime} seconds and current job queue is empty")
        else:  ## job queue is not empty
            sleep(1)
            print(f"Current time is {CurrTime} seconds and current job queue is {[i.ID for i in JobQueue]}")
            if SchedMode == 4:
                print(f"Priorities are currently {[i.Priority for i in JobQueue]}")
            
            
            if SchedMode == 1 or SchedMode == 2: ## If the scheduling mode is non-preemptive it will keep working on the same proccess until it finishes it no matter what happens.
                if WorkingOnJob == False:  ## If currently not working on a job then start working on the first one
                    JobQueue[0].StartingTime = CurrTime ## Set the starting time for the first job in the job queue as the current time
                    print(f"Starting job {JobQueue[0].ID} at time {CurrTime} that arrived at time {JobQueue[0].ArrivalTime}")
                    WorkingOnJob = True ## Sets the WorkingOnJob flag to True
                if WorkingOnJob: ## Didn't write "else" because if WorkingOnJob was false then made it true it would ignore this block of code
                    if JobQueue[0].RemainingTime > 0: ## the job is still not done
                        JobQueue[0].RemainingTime -= 1  ## decrease the remaining time by 1
                    else:  ## The job is done
                        JobQueue[0].EndTime = CurrTime ## marks the ending time
                        JobQueue[0].WaitingTime = JobQueue[0].StartingTime - JobQueue[0].ArrivalTime ## Calculates the waiting time
                        print(f"Job {JobQueue[0].ID} ended at {JobQueue[0].EndTime} seconds and waited for {JobQueue[0].WaitingTime}")
                        JobsDone.append(JobQueue.pop(0)) ## Removes the completed job from the job queue and adds it to the completed jobs list
                        WorkingOnJob = False ## No longer working on job
                        CurrTime -= 1
            
            
            else:  ## The Scheduling mode is preemptive
                if JobQueue[0].StartingTime != 0:
                    JobQueue[0].StartingTime = CurrTime ## Set the starting time for the first job in the job queue as the current time
                    print(f"Starting job {JobQueue[0].ID} at time {CurrTime} that arrived at time {JobQueue[0].ArrivalTime}")
                if JobQueue[0].RemainingTime > 0: ## the job is still not done
                    JobQueue[0].RemainingTime -= 1  ## decrease the remaining time by 1
                else:
                    JobQueue[0].EndTime = CurrTime
                    JobQueue[0].WaitingTime = JobQueue[0].EndTime - JobQueue[0].ArrivalTime - JobQueue[0].BurstTime
                    print(f"Job {JobQueue[0].ID} ended at {JobQueue[0].EndTime} seconds and waited for {JobQueue[0].WaitingTime}")
                    JobsDone.append(JobQueue.pop(0))
                    CurrTime -= 1
        CurrTime += 1

if __name__ == '__main__':
    NoOfJobs = int(input("Please enter number of desired jobs: "))
    if NoOfJobs <=0:
        print("Positive integers only")
    print("Please enter the number in front of the desired scheduling mode")
    print("Available modes are: 1 - First Come First Served, 2 - Shortest job first: Non-Preemptive")
    print("3 - Shortest job first: Preemptive, 4 - Priority: Preemptive")
    SchedMode = int(input("Enter Number: "))
    if SchedMode not in range(1,5):
        print("Invalid Input")
    else:
        ProScSim(NoOfJobs,SchedMode)