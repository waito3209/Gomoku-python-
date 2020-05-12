import plane as pl
print("game start")
a=pl.plane()
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
        a.checkemptydig(a.p1919,-1)
        gamestate=a.Humaninput(-1)
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
