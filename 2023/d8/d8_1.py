"""AoC day 8 part 1"""
#FILEPATH = "./2023/d8/source-test.txt"
FILEPATH = "./2023/d8/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n\n')

INSTRUCTIONS = list(content[0])
NETWORK = content[1].split('\n')



##############################################

mapping = {}

# Create mapping
for line in NETWORK:
    line = line.split(' = ')
    root = line[0]
    root_l = line[1].split(', ')[0][1:]
    root_r = line[1].split(', ')[1][:-1]

    mapping[root] = {'L': root_l, 'R': root_r}

# Process instructions
next = 'AAA'
i = 0
steps = 0
while next != 'ZZZ':
    next = mapping[next][INSTRUCTIONS[i]]
    i += 1
    if i == len(INSTRUCTIONS):
        i = 0
    steps += 1

print(steps)
