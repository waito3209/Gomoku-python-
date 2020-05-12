import plane as pl
import RandomMachine
print("game start")
a=pl.plane()
p2=RandomMachine.test()

a.startrecord('D:\data'+'/')
gamestate=0
turning="p1"
while gamestate==0:
    a.print(data=a.p1919)
    if turning=="p1":
        a.checkemptydig(a.p1919,1)
        gamestate=a.Humaninput(1)
        turning='p2'

    elif turning=="p2":
        p2.InputData__Available(a.checkemptydig(a.p1919, -1))

        gamestate=a.MachineInput(p2.resulty, p2.resultx, -1)
        turning = 'p1'

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