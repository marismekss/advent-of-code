#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d6/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d6/prod-input.txt"

src = open(filePath, "r").read().split('\n')


ind = 14


for datastream in src:
    print(datastream)

    for i in range(0,len(datastream)-ind+1):
        count = len(set(datastream[i:i+ind]))
        if count == ind:
            print(i+ind)
            break




