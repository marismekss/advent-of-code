from myClasses import *

##################################

filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/tst-input.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/tst-input-2.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/prod-input.txt"
src = open(filePath, "r").read().split('\n')




for instruction in src:
    
    inst = instruction.split()

    for i in range(1,int(inst[1])+1):
        instruct = str(inst[0]) + ' 1'
            
        print(instruct)






#trees = Grid(5,5,'#')
#trees.draw()
#print('  ')
#print(trees.cell[0][0])
#trees.setInitalValues(src, 'integer')
#trees.draw()


#print(trees.cell[0][1])
