#f = open("/Users/marismekss/Documents/Advent of Code/2016/day3/3-test.txt", "r")
f = open("/Users/marismekss/Documents/Advent of Code/2016/day3/3-prod.txt", "r")

counter = 0

def process_triangle (line):
    splitLine = line.split()

    a = int(splitLine[0])
    b = int(splitLine[1])
    c = int(splitLine[2])

    if a < b + c and b < a + c and c < a + b :
        return True



fileList = list(f)
for i in range(len(fileList) - 2):
    line1 = fileList[i].split()
    line2 = fileList[i+1].split()
    line3 = fileList[i+2].split()

    triangle1 = f"{line1[0]} {line2[0]} {line3[0]}"
    triangle2 = f"{line1[1]} {line2[1]} {line3[1]}"
    triangle3 = f"{line1[2]} {line2[2]} {line3[2]}"
    
    if process_triangle(triangle1) == True:
        counter += 1
    if process_triangle(triangle2) == True:
        counter += 1
    if process_triangle(triangle3) == True:
        counter += 1

    

print("Result: ", counter)