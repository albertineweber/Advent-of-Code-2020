arq = open('input13.txt', 'r')

flag = 0

frequency = []
time_difference = []

for line in arq:
    temp = line.split()
    if flag == 0:
        earliest = int(temp[0])
        flag = 1
    else:
        i = 0
        for elem in (temp[0].split(",")):
            if elem != "x":
                frequency.append(int(elem))
                time_difference.append(i)
            i = i + 1
        
min_waiting_time = earliest*1000

for i in range(0, len(frequency)):
    last_departure = ((earliest//frequency[i]) * frequency[i])
    if last_departure != earliest:
        last_departure = last_departure + frequency[i]

    waiting_time = last_departure - earliest

    if waiting_time < min_waiting_time:
        min_waiting_time = waiting_time
        index_min = i


earliest_bus = frequency[index_min]

print(earliest_bus*min_waiting_time)

base_time = frequency[0]


flagdo = 0

x = 1
num = 0

for i in range(0, len(frequency)):
    while True:
        num = num + x
        if (num + time_difference[i])%frequency[i] == 0:
            x = x * frequency[i]
            break
print(num)