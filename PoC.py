import random
class BasicJob:
    def __init__(self, ArrivalTime:int, RemainingTime:int):
        self.ArrivalTime = ArrivalTime
        self.RemainingTime = RemainingTime
        self.StartingTime = 0
        self.EndTime = 0
        self.WaitingTime = 0
NoOfJobs = int(input("Please enter number of desired jobs: "))
# Jobs = [BasicJob(0,random.randint(1,10))]
# Jobs.extend([BasicJob(random.randint(2,25),random.randint(1,10)) for x in range(NoOfJobs - 1)])
# for i in range(NoOfJobs):
#     Jobs[i].ID = i
Jobs = [BasicJob(0,2),BasicJob(0,3),BasicJob(0,1),BasicJob(9,4),BasicJob(12,3)]
for i in range(NoOfJobs):
    Jobs[i].ID = i
CurrTime = 0
WorkingOnJob = False
def FCFS(CurrTime : int, WorkingOnJob : bool):
    JobQueue = []
    JobsDone = []
    while len(JobsDone) != NoOfJobs:
        for i in Jobs:
            if i.ArrivalTime <= CurrTime and i not in JobQueue and i not in JobsDone:
                JobQueue.append(i)
        try:
            JobQueue.sort(key=lambda x: x.ArrivalTime)
        except:
            pass
        if len(JobQueue) == 0:
            print(f"Current time is {CurrTime} seconds and current job queue is empty")
        else:
            print(f"Current time is {CurrTime} seconds and current job queue is {[i.ID for i in JobQueue]}")
            if WorkingOnJob == False:
                JobQueue[0].StartingTime = CurrTime
                print(f"Starting job {JobQueue[0].ID} at time {CurrTime} that arrived at time {JobQueue[0].ArrivalTime}")
                WorkingOnJob = True
            if WorkingOnJob:
                if JobQueue[0].RemainingTime > 0:
                    JobQueue[0].RemainingTime -= 1
                else:
                    JobQueue[0].EndTime = CurrTime
                    JobQueue[0].WaitingTime = JobQueue[0].StartingTime - JobQueue[0].ArrivalTime
                    print(f"This job ended at {JobQueue[0].EndTime} seconds and waited for {JobQueue[0].WaitingTime}")
                    JobsDone.append(JobQueue.pop(0))
                    WorkingOnJob = False
                    CurrTime -= 1
        CurrTime += 1

if __name__ == '__main__':
   FCFS(CurrTime,WorkingOnJob) 