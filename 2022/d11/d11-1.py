import math


#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d11/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d11/prod-input.txt"


class Monkey:
    def __init__ (self, name):
        self.name = name
        self.items = []
        self.worry_1 = None
        self.worry_2 = None
        self.worry_3 = None
        self.testDivision = None
        self.testTrue = None
        self.testFalse = None
        self.activity = 0
    
    def __name__ (self):
        return self.name

    def checkWorryLevel (self, item):
        
        if self.worry_1 == 'old':
            a = int(item)
        else:
            a = int(self.worry_1)
        
        if self.worry_3 == 'old':
            b = int(item)
        else:
            b = int(self.worry_3)

        if self.worry_2 == '*':
            newLevel = a * b
        elif self.worry_2 == '+':
            newLevel = a + b

        return newLevel



###############################################

monkeys = []

## Prepare initial data of monkeys
src = open(filePath, 'r').read().split('\n\n')
for each in src:
    each = each.split('\n')

    name = each[0][-2:-1]
    items = each[1].split(':')[1].strip().replace(' ','').split(',')
    items = list(map(int,items)) #[54, 65, 75, 74]
    newWorryLevel = each[2].split('=')[1].strip().split(' ') #['old', '*', '19']
    testDivision = int(each[3].strip().split(' ')[3])
    testTrue = int(each[4].strip().split(' ')[5])
    testFalse = int(each[5].strip().split(' ')[5])
    

    monkey = Monkey(name)
    monkey.items.extend(items)
    monkey.worry_1 = newWorryLevel[0]
    monkey.worry_2 = newWorryLevel[1]
    monkey.worry_3 = newWorryLevel[2]
    monkey.testDivision = testDivision
    monkey.testTrue = testTrue
    monkey.testFalse = testFalse

    monkeys.append(monkey)



##

rounds = 20

for round in range(rounds):

    for monkey in monkeys:
        if len(monkey.items) > 0:

            tmpList = monkey.items.copy()
            for item in tmpList:
                monkey.activity += 1
                index = monkey.items.index(item)
                worryLevel = monkey.checkWorryLevel(item)
                worryLevel = math.floor(worryLevel / 3)


                division = worryLevel / monkey.testDivision
                if division.is_integer() == True:
                    monkey.items.pop(index)
                    monkeys[monkey.testTrue].items.append(worryLevel)
                else:
                    monkey.items.pop(index)
                    monkeys[monkey.testFalse].items.append(worryLevel)

result = []

print('==============================')
for monkey in monkeys:
    result.append(monkey.activity)

print('==============================')
resultSorted = sorted(result)
print(resultSorted[-1] * resultSorted[-2])
