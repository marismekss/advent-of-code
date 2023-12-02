#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d3/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d3/prod-input.txt"


file = open(filePath, "r")
src = open(filePath, "r").read().split('\n')

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
counter = 0

while counter != len(src):
    counter += 3

    l1 = list(file.readline().strip())
    l2 = list(file.readline().strip())
    l3 = list(file.readline().strip())

    matchingLetter = list(set(l1).intersection(l2,l3))[0]
    index = abc.find(matchingLetter) + 1
    result += index

print(result)
 


