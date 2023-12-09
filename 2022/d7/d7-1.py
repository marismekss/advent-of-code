filePath = "./2022/d7/tst-input.txt"
#filePath = "./2022/d7/prod-input.txt"


class Node:
    def __init__ (self, name, type):
        self.name = name
        self.type = type
        self.size = 0
        self.parent = None
        self.child = []

def changeLocation(value,currentDir):
    if value == '/':
        return root
    elif value == '..':
        return currentDir.parent
    else:
        for item in currentDir.child:
            if item.name == value:
                newDir = item
                return newDir
        

def listLocation(output):
    for item in output:
        item = item.split()
        
        if item[0] == 'dir':
            # FOLDER
            node = Node(item[1], 'folder')
            node.parent = pwd
            pwd.child.append(node)
            tree.append(node)
        else:
            # FILE
            node = Node(item[1], 'file')
            node.parent = pwd
            node.size = int(item[0])
            pwd.child.append(node)
            tree.append(node)
        
#########################################################


# Initialize root node and tree
tree = []
root = Node('/','folder')
root.type = 'folder'
root.parent = 'root'
tree.append(root)
pwd = root



src = open(filePath, 'r').read().split('$')



for line in src[1:]:
    
    line = line.strip().split('\n')

    if line[0][0:2] == 'cd':
        #print('CD--')
        pwd = changeLocation(line[0][2:].strip(),pwd)
        #print('Current working dir: ', pwd.name)
  
    if line[0][0:2] == 'ls':
        #print('LS--')
        screen = line[1:]
        listLocation(screen)



## Find all children
children = []
for node in tree:
    if len(node.child) == 0:
        children.append(node)


## Traverse the tree and put sizes
for child in children:
    size = child.size
    while child.parent != 'root':
        child.parent.size += size
        child = child.parent


## Find resulting folders
sum = 0
for node in tree:
    if node.type == 'folder' and node.size < 100000:
        sum += node.size

print('Result is: ', sum)