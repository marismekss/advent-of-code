import re

filePath = "/Users/marismekss/Documents/Advent of Code/2022/d13/tst-input.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d13/prod-input.txt"

class Pair:

    def __init__(self, rawline):
        self.rawline = rawline
        self.left = None
        self.right = None
        self.right_order = False
        self.processed = False

        self.initialize_pairs()


    def check_depth(self):
        pass

    def initialize_pairs(self):
        split = self.rawline.split('\n')
        self.left = split[0]
        self.right = split[1]
    
    


def convert_to_list(packet):
    packet_as_list = list(re.search('\[(.*?)\]',packet)[1].split(','))
    return packet_as_list

def is_list(side):
    if side[0] == '[':
        return True

# Test pair
#packets = '[1,1,3,1,1]\n[1,1,5,1,1]'
packets = '[[1],[2,3,4]]\n[[1],4]'


def process (pair_l, pair_r):

    if is_list(pair_l) == True and is_list(pair_r) == True:
        pair_l = convert_to_list(pair_l)
        pair_r = convert_to_list(pair_r)
    



pair = Pair(packets)

#while pair.processed == False:
    #pass
process(pair.left, pair.right)
    




"""
pair.left = convert_to_list(pair.left)
pair.right = convert_to_list(pair.right)



# go through the indeces
print('Comparing ',pair.left, ' vs ',pair.right)
for i in range(0,len(pair.left)):

    print(' - Comparing ',pair.left[i], ' vs ',pair.right[i])

#!!! Check if integers


#!!! Check if other types
    if int(pair.left[i]) < int(pair.right[i]):
        pair.right_order = True
        print(' - Right order')
        break


"""






#src = open(filePath, "r").read().split('\n\n')




