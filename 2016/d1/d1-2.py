filePath = "/Users/marismekss/Documents/Advent of Code/2016/d1/source-test.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2016/d1/source-prod.txt"


file = open(filePath, "r")
src = open(filePath, "r").read().split(', ')


pov = 0
x = 0
y = 0

hit = []


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
    print('Step: ', pov, loc_x, loc_y)
    if pov == 0:
        for i in range(loc_y+1, distance+1):
            status = one_step(str(loc_x)+'|'+str(i))
            #print(str(loc_x)+'|'+str(i))
            if status:
                break
        loc_y += distance
    elif pov == 90:
        print(loc_x, distance)
        for i in range(loc_x+1, distance+1):
            status = one_step(str(i)+'|'+str(loc_y))
           # print(str(i)+'|'+str(loc_y))
            if status:
                break
        loc_x += distance
    elif pov == 180:
        for i in range(loc_y+1, distance+1, -1):
            status = one_step(str(loc_x)+'|'+str(i))
            #print(str(loc_x)+'|'+str(i))
            if status:
                break
        loc_y -= distance
    else:
        for i in range(loc_x+1, distance+1, -1):
            status = one_step(str(i)+'|'+str(loc_y))
            #print(str(i)+'|'+str(loc_y))
            if status:
                break
        loc_x -= distance


    return loc_x, loc_y
    

def one_step(visit):
    print('One step: ', visit)
    if visit in visited_places:
        print('Double hit!', visit)
        xy = visit.split('|')
        hit.append(abs(int(xy[0])))
        hit.append(abs(int(xy[1])))
        return True
    else:
        visited_places.append(visit)
        return False







visited_places = []


for step in src:

    turn_direction = step[0]
    blocks = int(step[1:])

    pov = turn(pov, turn_direction)
    x, y = move(pov, blocks, x, y)

    if len(hit) > 0:
        print(sum(hit))
        break