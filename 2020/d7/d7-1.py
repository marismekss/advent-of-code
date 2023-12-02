#filePath = "/Users/marismekss/Documents/Advent of Code/2020/d7/tst-input.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2020/d7/prod-input.txt"

src = open(filePath, "r").read().split('\n')


class Bag:
  def __init__(self, name):
    self.name = name
    self.parent = None
    self.children = []

  def __str__(self):
    return self.name

#light red bags contain 1 bright white bag, 2 muted yellow bags.
#dark orange bags contain 3 bright white bags, 4 muted yellow bags.

bags = []


for line in src:

  # parse the line
  parent_bag_name = line.split(' bags contain ')[0]
  children = line.split(' bags contain ')[1].replace(' bag', '').replace(' bags', '').replace('.','').split(', ')
  
  # prepare parent object
  parent_bag = Bag(parent_bag_name)
  bags.append(parent_bag)
  
  # get multipliers
  for child in children:
    child = child.split()
    multiplier = int(child[0])

    # remove plural from the bag name  
    if multiplier > 1: 
      child[2] = child[2][:-1]

    # prepare children object
    child_bag = Bag(child[1] + child[2])
    parent_bag.append([1, child_bag])


  
  
  



#['1 bright white', '2 muted yellows']
#['3 bright whites', '4 muted yellows']






#print(b1)
