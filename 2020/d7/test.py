

    #parent_bag_name = line.split(' bags contain ')[0]
    #children = line.split(' bags contain ')[1].replace(' bag', '').replace(' bags', '')
    #children = children.replace('.','').split(', ')




line = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
parent, children = process_line(line)

print(children[0]["name"])
