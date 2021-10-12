import pandas as pd
import numpy  as np

def ClockToSec(Clock):
    return 3600 * int(Clock[:2]) + 60 * int(Clock[3:5]) + int(Clock[6:])

def SecToClock(Sec):
    Hr = int(Sec / (60*60))
    Mn = int((Sec - Hr * 60 * 60) / 60)
    Sc = int(Sec - Hr * 60 * 60 - Mn * 60)
    return str(Hr).zfill(2) + ":" + str(Mn).zfill(2) + ":" + str(Sc).zfill(2)

class QueuingSystem:
    def __init__(self, Arrival, ServTime):
        self.Arrival = Arrival
        self.ServTime = ServTime
    
    def InterArrival(self):
        return [self.Arrival[0]] + [self.Arrival[i] - self.Arrival[i-1] for i in range(1,len(self.Arrival))]
    
    def Simulation(self, ServerN, PhaseN, SystemSize=1e10000):
        if PhaseN == 1:
            if ServerN == 1:
                self.WaitingTime  = [0]
                self.Departure = [self.Arrival[0] + self.ServTime[0]]
                for i in range(1,len(self.Arrival)):
                    self.WaitingTime.append ( max(self.Arrival[i], self.Departure[i-1]) - self.Arrival [i] )
                    self.Departure.append( max(self.Arrival[i], self.Departure[i-1]) + self.ServTime[i] )
            else:
                self.WaitingDeparture = np.zeros([ServerN, len(Arrival)])
                self.WaitingTime      = np.zeros([ServerN, len(Arrival)])
                self.Server           = np.zeros([ServerN-1, len(Arrival)])
                self.Server[0][0]     = 1
                self.Departure        = [min(self.WaitingTime[:,0]) + self.Arrival[0] + self.ServTime[0]]
                for i in range(1,len(self.Arrival)):
                    for j in range(ServerN):
                        WaitDepLogical = self.Server[j][i-1] == 1 if j<ServerN-1 else sum(self.Server[:,i-1]) == 0
                        self.WaitingDeparture[j][i] = self.Departure[i-1] if WaitDepLogical else self.WaitingDeparture[j][i-1]
                        self.WaitingTime[j][i]      = max(0, self.WaitingDeparture[j][i] - self.Arrival[i])
                    
                    for j in range(ServerN-1):
                        ServerLogical1 = True if j==0 else sum(self.Server[:j+1,i]) == 0
                        ServerLogical2 = min(self.WaitingTime[:,i]) == self.WaitingTime[j,i]
                        ServerLogical  = ServerLogical1 and ServerLogical2
                        self.Server[j][i] = 1 if ServerLogical else 0
                    
                    self.Departure.append( min(self.WaitingTime[:,i]) + self.Arrival[i] + self.ServTime[i] )
                        
df1 = pd.read_excel("Queuing Data.xlsx", sheet_name="Ex.1")
df2 = pd.read_excel("Queuing Data.xlsx", sheet_name="Ex.2")
df3 = pd.read_excel("Queuing Data.xlsx", sheet_name="Ex.3")
df4 = pd.read_excel("Queuing Data.xlsx", sheet_name="Ex.4")

ShopStart    = "07:00:00"
ShopStartSec = ClockToSec(ShopStart)
Columns      = df1.columns
Arrival      = df1[Columns[1]]
ArrivalClean = [ClockToSec(i) - ShopStartSec for i in Arrival]
ServiceTime1 = df1[Columns[2]]
ServiceTime2 = df2[Columns[2]]
ServiceTime3 = df3[Columns[2]]
ServiceTime4 = df4[Columns[2]]

if __name__ == "__main__":

    A = QueuingSystem(ArrivalClean, ServiceTime2)
    I = A.InterArrival()
    A.Simulation(ServerN=3,PhaseN=1)
    W, D = A.WaitingTime, A.Departure
    DClock = [SecToClock(i + ShopStartSec) for i in D]
    
    Data = pd.DataFrame()
    Data["Arrival"] = ArrivalClean
    Data["InterArrival"] = I
    Data["ServiceTime"] = ServiceTime2
    Data["WaitingDeparture1"] = A.WaitingDeparture[0]
    Data["WaitingDeparture2"] = A.WaitingDeparture[1]
    Data["WaitingDeparture3"] = A.WaitingDeparture[2]
    Data["WaitingTime1"] = W[0]
    Data["WaitingTime2"] = W[1]
    Data["WaitingTime3"] = W[2]
    Data["Server1 ?"] = A.Server[0]
    Data["Server2 ?"] = A.Server[1]
    Data["Departure"] = D
    Data.to_excel("GG3 Ex.2 Result.xlsx", index=False)
    
    
    