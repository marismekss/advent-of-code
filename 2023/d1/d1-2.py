#filePath = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-test.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-prod.txt"

file = open(filePath, "r").read()
src = file.split('\n')

digits_as_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
calibration_sum = 0


def matchDigitFirst(line_l, i):
    # if index is digit, there is no point further to search
    if line_l[i].isdigit():
        return line_l, True
    
    for word in digits_as_words:
        if word == line_l[i:i+len(word)]:
            line_l = line_l[:i] + str(digits_as_words.index(word)) + line_l[i+len(word):]
            return line_l, True
    return line_l, False    
         

def matchDigitLast(line_l, i):
    # if index is digit, there is no point further to search
    if line_l[i].isdigit():
        return line_l, True
    
    for word in digits_as_words:
        if word == line_l[i-len(word)+1:i+1]:
            line_l = line_l[:i-len(word)+1] + str(digits_as_words.index(word)) + line_l[i+1:]
            return line_l, True
    return line_l, False  




for line in src: 
    digits = []

    # Search for first digit
    for idx in range(0,len(line)):
        res, found = matchDigitFirst(line, idx)
        if found:
            line = res
            #print(line)
            break

    # Search for last digit
    for idx in range(len(line)-1,0, -1):
        res, found = matchDigitLast(line, idx)
        if found:
            line = res
            break
   
    # goes through string and puts all digits in list
    for char in line:
        if char.isdigit():
            digits.append(char)

    calibration_value = str(digits[0]) + str(digits[-1])
    calibration_sum += int(calibration_value)

print('Result: ', calibration_sum)