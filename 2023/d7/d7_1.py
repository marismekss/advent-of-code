from collections import Counter
"""AoC day 7 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d7/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d7/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

DECK_STRENGTH = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}

HAND_TYPES = {
    'high-card': [],
    'one-pair': [],
    'two-pair': [],
    'three-of-a-kind': [],
    'full-house': [],
    'four-of-a-kind': [],
    'five-of-a-kind': []
}


class Hand:
    def __init__(self, card_hand, hand_bid):
        self.hand = card_hand
        self.type = None
        self.bid = hand_bid

    def __repr__(self):
        return self.hand


    def get_hand_type (self):
        hand = list(self.hand)
        counts = Counter(hand)
        encounters = []
        for each in counts.items():
            encounters.append(each[1])
        encounters = Counter(encounters)


        if encounters[5] == 1:
            hand_type = 'five-of-a-kind'

        if encounters[4] == 1:
            hand_type = 'four-of-a-kind'

        if encounters[3] == 1 and encounters [2] == 1:
            hand_type = 'full-house'

        if encounters[3] == 1 and encounters [1] == 2:
            hand_type = 'three-of-a-kind'

        if encounters[2] == 2:
            hand_type = 'two-pair'

        if encounters[2] == 1 and encounters [1] == 3:
            hand_type = 'one-pair'

        if encounters[1] == 5:
            hand_type = 'high-card'

        HAND_TYPES[hand_type].append(self)
        return hand_type



def first_hand_stronger (hand1, hand2):
    hand1 = list(hand1.hand)
    hand2 = list(hand2.hand)

    i = 0
    while i < 5:
        strength1 = DECK_STRENGTH[hand1[i]]
        strength2 = DECK_STRENGTH[hand2[i]]

        if strength1 == strength2:
            i += 1
        elif strength1 > strength2:
            return True
        else:
            return False


def bubble_sort(arr):
    swapped = False

    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if first_hand_stronger (arr[j], arr[j+1]):
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return

##########################################

all_hands = []
ranking = []
results = []


# Create objects for each hand and get type of each
for line in content:
    line = line.split()

    obj = Hand(line[0], line[1])
    obj.type = obj.get_hand_type()
    all_hands.append(obj)

# Set hands according to rankings
for hand_type in HAND_TYPES.items():
    local_list = HAND_TYPES[hand_type[0]]
    bubble_sort(local_list)
    ranking.extend(local_list)

# Calculate bids
for idx, each in enumerate(ranking):
    score = int(each.bid) * (idx+1)
    results.append(score)

print(sum(results))
