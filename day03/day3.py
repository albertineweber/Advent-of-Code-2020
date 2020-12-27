arq = open('input3.txt', 'r')

k = 0

slopes = [1, 3, 5, 7, 1]
counter = [0, 0, 0, 0, 0]
position = [0, 0, 0, 0, 0]
flag = 0

for line in arq:
    pattern = line.split()[0]
    for i in range(0, len(slopes)):
        if i == 4 and flag == 1:
            flag = 0
        else:
            if i == 4:
                flag = 1
            k = position[i]
            if pattern[k] == "#":
                counter[i] = counter[i] + 1
            
            position[i] = k + slopes[i]
            if position[i] > 30:
                position[i] = position[i] - 31
            
print(counter)
mult = 1
for i in range(0, len(counter)):
    mult = mult*counter[i]

print(mult)