arq = open('input7.txt', 'r')

counter = 0

rules = []

for line in arq:
    temp = line.split()
    father = temp[0] + temp[1]
    if temp[4] == "no" and temp[5] == "other":
        rules.append([father, "", 0])

    else:
        n = len(temp)
        for i in range(1, 1+(n-4)//4):
            numson = int(temp[4*i])
            son = temp[4*i + 1] + temp[4*i + 2]
            rules.append([father, son, numson])


#part1
bags = []

for rule in rules:
    if rule[1] == "shinygold":
        bags.append(rule[0])

stack = list(bags)

while stack != []:
    p0 = stack.pop(-1)
    for rule in rules:
        if rule[1] == p0 and rule[0] not in bags:
            bags.append(rule[0])
            stack.append(rule[0])

print(len(bags))


#part2
filter_rules = []
stack = []

for rule in rules:
    if rule[0] == "shinygold":
        stack.append(rule[1])
        filter_rules.append(rule)

while stack != []:
    p0 = stack.pop(-1)
    for rule in rules:
        if rule[0] == p0 and rule not in filter_rules:
            filter_rules.append(rule)
            stack.append(rule[1])


#thanks @pwschneider for the help
def search_bag(bag, rules):
    if rules[0] == bag and rules[2] == 0:
        return(1)
        
    prod = 1
    for rule in rules:
        if rule[0] == bag:
            prod = prod + rule[2] * search_bag(rule[1], rules) 

    return(prod)


prod = search_bag("shinygold", filter_rules)
for elem in filter_rules:
    print(elem)
print(prod - 1)
