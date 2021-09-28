import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def ConditionMin(array, ignoreIndex=[]):
    Min    = 1e10
    argmin = 0
    for i in range(len(array)):
        if (array[i] < Min) and (i not in ignoreIndex):
            Min    = array[i]
            argmin = i
    return Min, argmin
            

def GreedyTSP(dist):
    Route   = [0]
    Alldist = []
    going   = Route[-1]
    while len(dist) > len(Route):
        going = ConditionMin(dist[Route[-1]], Route)
        Alldist.append(going[0])
        Route  .append(going[1])
    Alldist.append(dist[Route[-1]][0])
    Route  .append(0)
    return Route, Alldist


def PlotTSP(data, Route):
    plt.scatter(data[1:,0], data[1:,1], color="b")
    plt.scatter(data[0,0] , data[0,1] , color="r")
    data2 = []
    for i in Route:
        data2.append(data[i])
    data2 = np.array(data2)
    plt.plot(data2[:,0], data2[:,1])

data = np.array([[ 10,  50],
                 [ 80,  70],   
                 [ 20,  60],
                 [ 90,  50],   
                 [ 30,  80],
                 [100,  90],
                 [  0, -15], 
                 [-20,  30], 
                 [-30, -15],
                 [-20, -50],
                 [-30,   0]])

dist = sp.spatial.distance_matrix(data, data)
Route, Alldist = GreedyTSP(dist)
PlotTSP(data, Route)
print("The route is {}".format(Route))
print("Total distance = {}".format(sum(Alldist)))