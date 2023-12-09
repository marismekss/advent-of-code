"""AoC day 4 part 1"""
#FILEPATH = "./2023/d4/source-test.txt"
FILEPATH = "./2023/d4/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

result = []

for card in content:
    card = card.split('|')
    card_id = card[0].split(': ')[0].split()[1]
    card_win_num = list(map(int,card[0].split(': ')[1].split()))
    card_my_num = list(map(int,card[1].split()))

    matching_numbers = set(card_win_num) & set(card_my_num)

    if len(matching_numbers) > 1:
        res = 1
        for _ in range(len(matching_numbers)-1):
            res = res * 2
        result.append(res)
    elif len(matching_numbers) == 1:
        result.append(1)
    else:
        result.append(0)


print(sum(result))
