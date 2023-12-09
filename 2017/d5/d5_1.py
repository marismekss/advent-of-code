"""AoC 2017 day 5 part 1"""
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2017/d5/source-test.txt"
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2017/d5/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


track = content.copy()
track = list(map(int,track))
idx = 0

#for idx in range(4):
while idx < len(track)+1:
    print("Current i:", idx)
    print("Current val:", track[idx])
    
    print("Value changed to:", track[idx])
    idx = idx + track[idx]
    print("Jump to i:", idx)
    track[idx] += 1
    print('-----')
    

