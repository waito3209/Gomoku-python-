


import plane as pl
import RandomMachine as M1
VisibleInConsole = True
WaitTime=0
p1 = M1.test()
p2 = M1.test()
a=pl.plane()
a.startrecord('D:\data'+'/')

import time
counter=0
print("game start")



gamestate=0
turning="p1"
while gamestate==0:
    counter+=1
    if VisibleInConsole:
        a.print(data=a.p1919)
        time.sleep(WaitTime)
    if turning=="p1":

        p1.InputData__Available(a.checkemptydig(a.p1919,1))
     
        gamestate=a.MachineInput(p1.resulty,p1.resultx,1)
       
        turning='p2'
    elif turning=="p2":

        p2.InputData__Available(a.checkemptydig(a.p1919,-1))
     
        gamestate=a.MachineInput(p2.resulty,p2.resultx,-1)
       
        turning = 'p1'
a.print(a.p1919)
if gamestate==1:
    print("p1 win________")
if gamestate==-1:
    print("p2 win________")
if gamestate==-2:
    print("ERROR")
if gamestate==2:
    print("Draw")
a.closerecord()
a.__del__()
print(counter)

