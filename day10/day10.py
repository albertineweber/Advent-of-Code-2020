arq = open('input10.txt', 'r')

adapters = []

for line in arq:
    temp = int(line.split()[0])
    adapters.append(temp)


adapters.append(0)
adapters = sorted(adapters)
adapters.append(adapters[-1]+3)

def check_dif(dif, c1, c3):
    if dif == 1:
        c1 = c1 + 1
    
    elif dif == 3:
        c3 = c3 + 1

    return(c1, c3)


c1 = 0
c3 = 0

i = 0


#part1
while i < (len(adapters)-1):
    dif = adapters[i+1] - adapters[i]
    c1, c3 = check_dif(dif, c1, c3)
    i = i + 1
    
print(c1*c3)


#part2
dict_adapters = {}

def search_pairs(adapter, adapters):
    if adapter in dict_adapters:
        return(dict_adapters[adapter])
    if adapter == adapters[-1]:
        return(1)

    counter = 0

    for j in range(1, 3+1):
        if adapter + j in adapters:
            counter = counter + search_pairs(adapter + j, adapters)
    
    dict_adapters[adapter] = counter
    return(counter)



counter = search_pairs(0, adapters)
print(counter)