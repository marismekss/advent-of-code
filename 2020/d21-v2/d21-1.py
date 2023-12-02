srcPath = "2020/d21-v2/tst-input.txt"

src = open(srcPath,"r").read().split('\n')

encIngrList = []
decIngrList = []
dict = {}

for line in src:
    encIngrLine = (line.strip().split(" (")[0]).split()
    decIngrLine = (line.strip().split(" (")[1]).replace("contains ","").replace(")","").split(", ")
    encIngrList.extend(encIngrLine)
    
    decIngrList.extend(decIngrLine)

uniqueEncIngredients = set(encIngrList)
uniqueDecIngredients = set(decIngrList) 

## Gets unique ingredients and prepares dictionary objects for each
for ingredient in uniqueDecIngredients:
    dict.update({ingredient : {"count" : 0}})
    dict[ingredient].update({"list" : []})



## Adds all encrypted ingredients with matching 
for line in src:
    encIngrLine = (line.strip().split(" (")[0]).split()
    decIngrLine = (line.strip().split(" (")[1]).replace("contains ","").replace(")","").split(", ")

    for ingredient in decIngrLine:
        dict[ingredient]["list"].extend(encIngrLine)
        dict[ingredient]["count"] += 1


foundIngredients = []
for ingredient in uniqueDecIngredients:
    ingrList = dict[ingredient]["list"]

    for i in ingrList:
        count = ingrList.count(i)
        if count == dict[ingredient]["count"]:
            foundIngredients.append(i)
            break
            

tmp = set(uniqueEncIngredients).difference(foundIngredients) 

print(tmp)