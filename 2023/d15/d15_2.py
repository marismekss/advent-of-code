"""AoC day 15 part 2"""
FILEPATH = "./2023/d15/source-test.txt"
#FILEPATH = "./2023/d15/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split(',')


def get_hash(input_val):
    current_val = 0
    for char_val in input_val:
        current_val += ord(char_val)
        current_val *= 17
        current_val = current_val % 256

    return current_val


##################################################

boxes = [[]] * 256

for each in content:

    if '=' in each:
        each = each.split('=')
        lens_label = each[0]
        lens_focal = each[1]
        operator = '='
    else:
        lens_label = each[:-1]
        operator = '-'

        hash_val = get_hash(lens_label)

        

    
    print(lens_label)
    

    #result.append(get_hash(each))


#print(boxes)
