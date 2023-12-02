#srcPath = "2018/py 1/1-test.txt"
srcPath = "2018/py 1/1-input.txt"
f = open(srcPath,"r")
payload = f.readlines()
f.close()

found = False
result = 0

while found == False:

    for frequency in payload:
        result += int(frequency)
        


print("The result is: ", result)



