from itertools import product

arq = open('input14.txt', 'r')

def decimal_to_binary(value):
    binary = []
    for i in range(0, 36):
        binary.append(0)
        
    i = 35
    while value >= 1:
        if value%2 == 0:
            value = value/2
        else:
            binary[i] = 1
            value = (value -1)/2
        i = i - 1

    return(binary)


def apply_mask(binary, mask):
    for i in range(0, len(mask)):
        if mask[i] != "X":
            binary[i] = int(mask[i])

    return(binary)


def apply_mask2(binary, mask):
    count = 0
    list_pos = []

    for i in range(0, len(mask)):
        if mask[i] != "X":
            if int(mask[i]) == 1:
                binary[i] = int(mask[i])
        else:
            binary[i] = mask[i]
            list_pos.append(i)
            count = count + 1

    combinations = list(product((0, 1), repeat=count))
    binary_possibilities = []

    for i in range(0, 2**count):
        new_binary = list(binary)
        combination = combinations[i]
        for j in range(0, len(list_pos)):
            new_binary[list_pos[j]] = combination[j]
        binary_possibilities.append(new_binary)
    
    return(binary_possibilities)


def binary_to_decimal(binary):
    value = 0
    for i in range(0, len(binary)):
        value = value + binary[i]*(2**(35-i))

    return(value)
        
dict_memory = {}

for line in arq:
    temp = line.split()
    if temp[0] == "mask":
        mask = []
        for i in range(0, len(temp[2])):
            mask.append(temp[2][i])
    else:
        mem = temp[0].split("[")[1].split("]")[0]
        value = int(temp[2])
        

        #part1
        #binary = decimal_to_binary(value)
        #binary = apply_mask(binary, mask)
        #value = binary_to_decimal(binary)
        #dict_memory[mem] = value

        #part2
        binary = decimal_to_binary(int(mem))
        binary_possibilities = apply_mask2(binary, mask)
        for binary in binary_possibilities:
            dict_memory[binary_to_decimal(binary)] = value


print(sum(list(dict_memory.values())))