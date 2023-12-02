filePath = "/Users/marismekss/Documents/Advent of Code/2016/d1/source-test.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2016/d1/source-prod.txt"


file = open(filePath, "r")
src = open(filePath, "r").read().split(', ')


pov = 0
x = 0
y = 0


def turn(pov, turn_dir):
    if turn_dir == 'R':
        pov += 90
        if pov == 360:
            pov = 0
    else:
        pov -= 90
        if pov == -90:
            pov = 270

    return pov


def move(pov, distance, loc_x, loc_y):
    if pov == 0:
        loc_y += distance
    elif pov == 90:
        loc_x += distance
    elif pov == 180:
        loc_y -= distance
    else:
        loc_x -= distance

    return loc_x, loc_y
    



for step in src:
    turn_direction = step[0]
    blocks = int(step[1:])

    pov = turn(pov, turn_direction)
    x, y = move(pov, blocks, x, y)



x = abs(x)
y = abs(y)

print(x+y)
