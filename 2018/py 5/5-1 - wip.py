val = "dabAcCaCBAcCcaDA"

newList = list(val)

indexList = []
tmpList = []
for i in range(len(newList) - 1):
    el1 = newList[i]
    el2 = newList[i+1]

    print(f"Looking at {el1} and {el2}")

    if el1.lower() == el2.lower() and el1 != el2:
        print('SAME!!!')
    else:
        tmpList.append(el1)

tmpList.append(el2)
newList = tmpList.copy()

print(newList)

    

