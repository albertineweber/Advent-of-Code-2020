arq = open('input15.txt', 'r')

dict_numbers = {}
i = 1

for line in arq:
    temp = line.split(',')
    for elem in temp:
        dict_numbers[int(elem)] = [0, i]
        last_num = int(elem)
        i = i + 1

while i <= 30000000:
#while i <= 2020:
    if i%100000 == 0:
        print(i)

    if dict_numbers[last_num][0] == 0:
        new_last_num = 0

    else:
        new_last_num = dict_numbers[last_num][1] - dict_numbers[last_num][0]

    if new_last_num in dict_numbers:
        dict_numbers[new_last_num] = [dict_numbers[new_last_num][1], i]
    else:
        dict_numbers[new_last_num] = [0, i]

    last_num = new_last_num
    
    i = i + 1

print(new_last_num)