"""AoC 2020 day 7 part 2"""
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2020/d7/source-test.txt"
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2020/d7/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


class Bag:
    """"Class to describe bags"""
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.bags_inside = 0

    def __repr__(self):
        return self.name


def process_line(l):
    """Process line from source input and prepare structured info"""
    l = l.split(' bags contain ')
    p_text = {"name": l[0]}
    c_text = l[1]
    new_children_list = []

    c_text = c_text.replace('.', '').replace('bags', 'bag').replace(' bag', '').split(',')

    if c_text[0] == 'no other':
        new_children_list = []
    else:
        for c in c_text:
            split = c.split()
            c = {"amount": int(split[0]), "name": split[1] + ' ' + split[2]}
            new_children_list.append(c)

    return p_text, new_children_list


def find_bag(b_name):
    """Searches if there is already existing bag"""
    found = next(
        (bag for bag in BAGS if bag.name == b_name),
        None
    )

    return found


#########################################################


BAGS = []

for line in content:
    # process line
    parent, children = process_line(line)

    # process parent
    parent_bag = find_bag(parent["name"])
    if not parent_bag:
        parent_bag = Bag(parent["name"])
        BAGS.append(parent_bag)

    # process children
    for child in children:
        # check if bag already exists
        child_bag = find_bag(child["name"])
        if not child_bag:
            child_bag = Bag(child["name"])
            BAGS.append(child_bag)

        # prepare children object
        child_bag.parents.append(parent_bag)
        parent_bag.children.append([child["amount"], child_bag])


######################################################


ROOT_BAG_NAME = "shiny gold"
CHILDREN = []
ROOT_BAG = find_bag(ROOT_BAG_NAME)
CHILDREN.extend(ROOT_BAG.children)

print(CHILDREN)

# Find leaf nodes
while len(CHILDREN) > 0:
    next_children = []
    for each in CHILDREN:
        next_children.extend(each[1].children)

        print(next_children)
        if len(next_children) == 0:
            break
        else:
            CHILDREN = next_children.copy()
        #print(CHILDREN)


# start counting bags
for child in CHILDREN:
    pass
    #print(child)
