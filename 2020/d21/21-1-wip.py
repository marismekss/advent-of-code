import json

srcPath = "2020/py 21/1-prod.txt"

f = open(srcPath,"r")
payload = f.readlines()

encList = []
decList = []
uniqueList = []
dict = {}
mapping = {}

def mappingDone (obj):
    counter = 0
    for keys in obj:
        if obj[keys] == "":
            counter +=1

    return counter


for line in payload:
    encIngrLine = (line.strip().split(" (")[0]).split()
    decIngrLine = (line.strip().split(" (")[1]).replace("contains ","").replace(")","").split(", ")

    encList.extend(encIngrLine)


    ## Prepare dictionaries of all ingredients
    for item in decIngrLine:
        if item in dict:
            # if ingredient is found
            for coded in encIngrLine:
                if coded in dict[item]["list"]:
                    # if ingredient AND code found
                    dict[item]["list"][coded] += 1
                else:
                    # if ingredient found but code NOT found
                    dict[item]["list"].update({coded : 1})
            dict[item]["count"] += 1 
        else:
            ## ingredient hasn't yet been found, add to dictionary
            dict.update({item : {"count" : 1}})
            mapping.update({item : ""})
            dict[item].update({"found" : 0})
            dict[item].update({"list" : {}})
            
            for coded in encIngrLine:
                dict[item]["list"].update({coded : 1})
            

json_object = json.dumps(dict, indent = 4) 
#print(json_object)

wrFile = open("2020/py 21/output-test.json", "a")
wrFile.write(json_object)
wrFile.close()

## ===============================================================================
## Get rid of all ingredients that have alergens


countOfKeys = mappingDone(mapping) # count how many keys are yet not found 

while countOfKeys > 0:
    for ingredient in dict:
        i = 0
        

        for coded in dict[ingredient]["list"]:
            if dict[ingredient]["list"][coded] == dict[ingredient]["count"]:
                foundCode = coded
                i += 1
        

        if i == 1:
            mapping.update({ingredient : foundCode })
            print("Found ingredient: ",foundCode, " for alergen: ",ingredient)
            dict[ingredient].update({"found" : 1})
            codeToDelete = foundCode


    ## Delete ingredient and coded ingredient from dictionary
    for ingredient in dict:
        dict[ingredient]["list"].pop(codeToDelete, None)       


    ## Measure how many keys are in dictionary
    countOfKeys = mappingDone(mapping)




## === Find all ingredients without alergens
remainingIngredients = []
for alergen in dict:
    for ingredient in dict[alergen]["list"]:
        remainingIngredients.append(ingredient)
remainingIngredients = set(remainingIngredients)

#print(remainingIngredients)



## --- Count how many times ingredients are without alergens
counter = 0
for ingredient in remainingIngredients: 
    counter += encList.count(ingredient)



print(counter)



#json_object = json.dumps(dict, indent = 4) 
#print(json_object)
#print ("-----------------------------------------------")
#json_object = json.dumps(mapping, indent = 4) 
#print(json_object)


f.close
