from math import gcd
"""AoC day 8 part 2"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d8/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d8/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n\n')

INSTRUCTIONS = list(content[0])
NETWORK = content[1].split('\n')



##############################################

mapping = {}
root_nodes = []
steps_to_z = []


# Create mapping
for line in NETWORK:
    line = line.split(' = ')
    root = line[0]
    root_l = line[1].split(', ')[0][1:]
    root_r = line[1].split(', ')[1][:-1]

    mapping[root] = {'L': root_l, 'R': root_r}


# Get all root nodes
for each in mapping.items():
    if each[0][-1:] == 'A':
        #root_nodes[each[0]] = each[0]
        root_nodes.append(each[0])


# Process instructions and get steps needed to get to Z
for each in root_nodes:
    root = each
    i = 0
    steps = 0
    while each[-1:] != 'Z':
        each = mapping[each][INSTRUCTIONS[i]]
        i += 1
        if i == len(INSTRUCTIONS):
            i = 0
        steps += 1

    steps_to_z.append(steps)


# Find least common multiple
lcm = 1
for i in steps_to_z:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)
