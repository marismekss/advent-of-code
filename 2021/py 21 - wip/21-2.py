

p1_score = 0
p2_score = 0

p1_pos = 10
p2_pos = 1

diceNum = 0
i = 0

def rollDice ():
    global diceNum, i
    if diceNum == 100:
        diceNum = 1
    else: 
        diceNum += 1

    i += 1

    return diceNum

def movePawn (prevPos, dice):
    newPos = prevPos + dice
    while newPos > 10:
        newPos -= 10

    return newPos


while p1_score < 1000 and p2_score < 1000:

    roll = rollDice() + rollDice() + rollDice()
    p1_prev = p1_score
    p1_pos = movePawn(p1_pos, roll)
    p1_score += p1_pos
    #print("P1 - position: ", p1_pos, ", score: ", p1_score)


    roll = rollDice() + rollDice() + rollDice()
    p2_prev = p2_score
    p2_pos = movePawn(p2_pos, roll)
    p2_score += p2_pos
    #print("P2 - position: ", p2_pos, ", score: ", p2_score)


if p1_score >= 1000:
    result = p2_prev * (i - 3)
    print("Result is: ", result)

if p2_score >= 1000:
    result = p1_prev * (i - 3)
    print("Result is: ", result)