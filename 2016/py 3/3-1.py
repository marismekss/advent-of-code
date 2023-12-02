#f = open("/Users/marismekss/Documents/Advent of Code/2016/day3/3-test.txt", "r")
f = open("/Users/marismekss/Documents/Advent of Code/2016/day3/3-prod.txt", "r")


counter = 0

for line in f:
    splitLine = line.split()
    
    a = int(splitLine[0])
    b = int(splitLine[1])
    c = int(splitLine[2])


    if a < b + c and b < a + c and c < a + b :
        print("Good")
        counter += 1
    else:
        print("Bad")

print("Result: ", counter)