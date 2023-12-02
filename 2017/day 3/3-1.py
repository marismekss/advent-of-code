tileCount = 14
tileCounter = 0
x = 0
y = 0


xFlag = True
incr = 1
increment = 1
incrCounter = 0



for tile in range(tileCount):
    tile += 2
    print("Tile ",tile)

    if incrCounter  == incr * 2:
        incr += 1
        incrCounter = 0
        if (incr % 2) == 0: increment = incr * -1
    

    # Incr positive or negative
    

    print(increment)

        #if xFlag == True:
    #    x += incr
    #else:
    #    y += incr


    incrCounter += 1

    

    xFlag = False
    #print("--",x,",",y,". Tile: ",tile," Incremental: ",incr)


#incr 1
    #x += incr
    #y += incr
#tileCounter += incr * 2
    #plusFlag = False

#incr 2
    #incr = incr neg
    #x += incr
    #y += incr
#tileCounter += incr(+) * 2
    #plusFlag = False





