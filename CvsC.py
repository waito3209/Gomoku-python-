import plane as pl
import RandomMachine as M1
import numpy as np
from numpy import asarray

traindata = []
trainlabel = []
traindatastep = []
ranger=int(input("range"))
name=input(" name")
for dfajfij in range(ranger):
    p1history = []
    p1label = []
    p2label = []
    p2history = []
    p1info = np.full((19, 19), 1)
    p2info = np.full((19, 19), -1)

    VisibleInConsole = False
    WaitTime = 0
    p1 = M1.test()
    p2 = M1.test()
    a = pl.plane()
    a.startrecord('D:\data' + '/')

    import time

    counter = 0
    print("game start")

    gamestate = 0
    turning = "p1"
    while gamestate == 0:
        temp = []
        counter += 1
        temp.append(a.p1919)
        if VisibleInConsole:
            a.print(data=a.p1919)
            time.sleep(WaitTime)
        if turning == "p1":
            p1history.append([p1info, a.p1919.copy()])

            p1.InputData__Available(a.checkemptydig(a.p1919, 1))
            gamestate = a.MachineInput(p1.resulty, p1.resultx, 1)
            p1label.append([p1.resulty, p1.resultx])
            turning = 'p2'
        elif turning == "p2":
            p2history.append([p2info, a.p1919.copy()])
            p2.InputData__Available(a.checkemptydig(a.p1919, -1))

            gamestate = a.MachineInput(p2.resulty, p2.resultx, -1)
            p2label.append([p2.resulty, p2.resultx])
            turning = 'p1'
    a.print(a.p1919)
    p1history = asarray(p1history)
    p2history = asarray(p2history)
    p1label = asarray(p1label)
    p2label = asarray(p2label)
    print("p1label : ")
    print(p1label.shape)
    print("p1hist  : ")
    print(p1history.shape)
    print("p2label : ")
    print(p2label.shape)
    print("p2hist  : ")
    print(p2history.shape)

    if gamestate == 1:
        print("p1 win________")
        trainlabel.append(p1label[:20])
        traindata.append(p1history[:20])
        traindatastep.append(p1label.shape[0]+p2label.shape[0])
    if gamestate == -1:
        print("p2 win________")
        trainlabel.append(p2label[:20])
        traindata.append(p2history[:20])
        traindatastep.append(p1label.shape[0] + p2label.shape[0])
    if gamestate == -2:
        print("ERROR")
    if gamestate == 2:
        print("Draw")
    a.closerecord()

    print("traindata   : ")
    print(asarray(trainlabel).shape)
    print("trainlable  : ")
    print(asarray(traindata).shape)
    # data = asarray(traindata)

    a.__del__()
    print(counter)
traindata = asarray(traindata)
trainlabel = asarray(trainlabel)
traindatastep = asarray(traindatastep)
np.save('D:\RR' +"/"+ name +  "/"+'trainlabel.npy', trainlabel)
np.save('D:\RR' +"/"+ name +  "/"+'traindata.npy', traindata)
np.save('D:\RR' +"/"+ name +  "/"+'traindatastep.npy', traindatastep)
