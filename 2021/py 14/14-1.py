polimerStr = 'NNCB'
#polimerStr = 'KKOSPHCNOCHHHSPOBKVF'

f = open("2021/py 14/14-test.txt", "r").readlines()


## Process mapping
mapping = {}
for line in f:
    line = line.strip().split(" -> ")
    mapping.update({ line[0] : line[1] })


polimer = list(polimerStr)
print(polimer)

newPolimer = []
newPolimer = polimer.copy()


for step in range(20):

    for i in range(len(polimer)-1):
        pair = polimer[i] + polimer[i+1]
        
        mappedElem = mapping[pair]
        newPolimer.insert(i*2+1, mappedElem)
        
    polimer = newPolimer.copy()
    #print(''.join(polimer))

unique = set(polimer)
#print(unique)

max = 0
min = 100000000000000

for elem in unique:
  #  count = polimer.count(elem)
  #  print("Element: ", elem, ", Count: ", count)
  #  if count > max: max = count
  #  if count < min: min = count

#print("Max: ", max, " Min: ", min)


#result = max - min
#print("Result: ", result)