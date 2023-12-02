filePath = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-test.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-prod.txt"

file = open(filePath, "r").read()
src = file.split('\n')

calibration_sum = 0

for line in src: 
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)

    calibration_value = str(digits[0]) + str(digits[-1])
    calibration_sum += int(calibration_value)
     
print(calibration_sum)