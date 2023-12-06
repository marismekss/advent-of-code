"""AoC day 4 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d4/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d4/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


def won_card_amount(i, win_cards, max_len):
    """Checks how many cards can be assigned considering list bounds"""
    if i + win_cards > max_len:
        win_cards = max_len - i

    return win_cards


#########################################################

LIST_SIZE = len(content)
score_cards = [0 for _ in range(1, LIST_SIZE+1)]
idx = 0


for card in content:
    idx += 1
    card = card.split('|')
    card_id = card[0].split(': ')[0].split()[1]
    card_win_num = list(map(int,card[0].split(': ')[1].split()))
    card_my_num = list(map(int,card[1].split()))

    cards_won = len(set(card_win_num) & set(card_my_num))
    card_multiplier = score_cards[idx-1]

    cards_to_assign = won_card_amount(idx, cards_won, LIST_SIZE)
    
    #print('Idx:', idx, ' Won cards:', cards_to_assign, ' Multiply:', card_multiplier)

    score_cards[idx-1] += 1
    for card in range(1,cards_to_assign+1):
        score_cards[idx+card-1] += 1
        
        if card_multiplier >= 1:
            for _ in range(card_multiplier):
                score_cards[idx+card-1] += 1

            
    
    #print(score_cards)

    
print(sum(score_cards))


#print(sum(result))
