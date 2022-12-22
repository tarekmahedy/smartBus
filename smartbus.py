seatsGroup = []
occuipiedSeats = 0
totalTax = 0
seatTax = 7
busSeats = 15


def setData():
    occuipiedSeats = 0
    x = len(seatsGroup)
    looper = 0
    while x > looper:
          okseat = seatsGroup[looper]
          occuipiedSeats = occuipiedSeats + okseat[0]
          looper += 1

    totalTax = occuipiedSeats * seatTax
    return occuipiedSeats


def recievSign(occSeats,needsSeats=1):

    avaiableSeats = busSeats - occSeats
    if(avaiableSeats>=needsSeats):
        seatsGroup.append([needsSeats, False])
        return 1
    else:
        return checkGroupsSeats((avaiableSeats-needsSeats), needsSeats)


def checkGroupsSeats(needsSeats, commingseats):

    x = len(seatsGroup)
    looper = 0
    while x > looper:
        okseat = seatsGroup[looper]
        if okseat[0] >= needsSeats and okseat[1] == True:
            okseat[0] = commingseats
            return 3
        looper += 1
    return 2


def closeDoorletsGo(commingSeats, outSeats, state):

    if state == 1:
        msg = "welcome {} "
    elif state == 2:
        msg = "Sorry no available seats For {} "
    elif state == 3:
        msg = "Thanks you for help : Welcome {} "
    return msg


while occuipiedSeats < busSeats:
     commingSeats = int(input("write coming seats ?"))
     occuipiedSeats = setData()
     state = recievSign(occuipiedSeats, commingSeats)
     Msg = closeDoorletsGo(commingSeats, 0, state)
     occuipiedSeats = setData()
     print(Msg.format(occuipiedSeats))



print(seatsGroup)
