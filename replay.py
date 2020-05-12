import plane as pl
import time
import csv
timesleep = 0
filepath = input("Input file path")
with open(filepath, newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))
    data = data[0]
    print(data)
    a = pl.plane()
    move = 0
    gamestate = 0
    turning = "p1"
    while gamestate == 0:

        y = int(data[move * 2])
        x = int(data[move * 2 + 1])
        move += 1

        if turning == "p1":
            a.checkemptydig(a.p1919, 1)
            a.print(data=a.p1919)
            gamestate = a.MachineInput(y,x,1)
            turning = 'p2'
            time.sleep(timesleep)

        elif turning == "p2":
            a.checkemptydig(a.p1919, -1)
            a.print(data=a.p1919)
            gamestate = a.MachineInput(y,x,-1)
            turning = 'p1'
            time.sleep(timesleep)
    a.print(data=a.p1919)
    if gamestate == 1:
        print("p1 win________")
    if gamestate == -1:
        print("p2 win________")
    if gamestate == -2:
        print("ERROR")
    if gamestate == 2:
        print("Draw")