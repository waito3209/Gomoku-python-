import plane as pl

while True:
    print("game start")
    a=pl.plane(0)

    gamestate=0
    turning="p1"
    while gamestate==0:
        a.print(pygameoo=True)
        if turning=="p1":
            print("p1 enter corrdinate")
            gamestate=a.change(input("y"),input('x'),1)
            turning='p2'
            continue
        if turning=="p2":
            print("p2 enter corrdinate")
            gamestate=a.change(input("y"),input('x'),-1)
            turning = 'p1'
            continue
    if gamestate==1:
        print("p1 win________")
    if gamestate==-1:
        print("p2 win________")
    a.print(pygameoo=True)
