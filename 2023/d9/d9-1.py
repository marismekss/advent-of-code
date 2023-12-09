from collections import Counter
"""AoC day 9 part 1"""
#FILEPATH = "./2023/d9/source-test.txt"
FILEPATH = "./2023/d9/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

main_list = []

def prepare_lists (inp_list):
    outp_list = []

    outp_list.append(inp_list)
    while len(inp_list) != Counter(inp_list)[0]:
        tmp_list = []

        for j in range(0,len(inp_list)-1):
            d = inp_list[j+1] - inp_list[j]
            tmp_list.append(d)
        outp_list.append(tmp_list)

        inp_list = tmp_list.copy()

    return outp_list


def add_last_nodes (ind):
    to_add = 0

    for i in range(len(main_list[ind])-1,-1,-1):
        main_list[ind][i].append(main_list[ind][i][-1] + to_add)
        to_add = main_list[ind][i][-1]


#########################################§

result = []


for idx, history in enumerate(content):
    history = list(map(int,history.split()))

    main_list.append(prepare_lists(history))
    add_last_nodes(idx)
    result.append(main_list[idx][0][-1])


print(sum(result))
