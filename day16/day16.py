arq = open('input16.txt', 'r')

flag = 0

ranges = []

ticket_errors = []
valid_tickets = []
fields = {}
fields_ranges = []
my_ticket = []

i = 0

for line in arq:
    temp = line.split()
    
    if temp == []:
        flag = flag + 1
    
    if flag == 0:
        if temp[3] =='or':
            fields[i] = temp[0]+""+temp[1]
            fields_ranges.append([temp[0]+""+temp[1], [int(temp[2].split('-')[0]), int(temp[2].split('-')[1])], [int(temp[4].split('-')[0]), int(temp[4].split('-')[1])]])
            temp_ranges = [[int(temp[2].split('-')[0]), int(temp[2].split('-')[1])], [int(temp[4].split('-')[0]), int(temp[4].split('-')[1])]]
        else:
            fields[i] = temp[0]
            fields_ranges.append([temp[0], [int(temp[1].split('-')[0]), int(temp[1].split('-')[1])], [int(temp[3].split('-')[0]), int(temp[3].split('-')[1])]])
            temp_ranges = [[int(temp[1].split('-')[0]), int(temp[1].split('-')[1])], [int(temp[3].split('-')[0]), int(temp[3].split('-')[1])]]
        
        for elem in temp_ranges:
            ranges.append(elem)

        i = i + 1
    
    if flag == 1:
        if temp != [] and temp != ['your', 'ticket:']:
            temp = temp[0].split(",")
            for elem in temp:
                my_ticket.append(elem)

    if flag == 2:
        if temp != [] and temp != ['nearby', 'tickets:']:
            temp = temp[0].split(",")
            flag_ticket = 0
            for elem in temp:
                flag_range = 0
                for rng in ranges:
                    if int(elem) >= rng[0] and int(elem) <= rng[1]:
                        flag_ticket = flag_ticket + 1
                        break
                    else:
                        flag_range = flag_range + 1
            
                if flag_range == len(ranges):
                    ticket_errors.append(int(elem))

            if flag_ticket == len(temp):
                valid_tickets.append(temp)

print(sum(ticket_errors))

#part2
for elem in fields_ranges:
    elem.append(list(fields.keys()))


for ticket in valid_tickets:
    for i in range(0, len(ticket)):
        for field in fields_ranges:
            if i in field[3]:
                if (int(ticket[i]) >= field[1][0] and int(ticket[i]) <= field[1][1]) or (int(ticket[i]) >= field[2][0] and int(ticket[i]) <= field[2][1]):
                    pass
                else:
                    field[3].remove(i)

decided = []
total_len = 0


while total_len != len(fields):
    total_len = 0
    for elem in fields_ranges:
        if len(elem[3]) == 1:
            if elem not in decided:
                decided.append(elem[3][0])

        if len(elem[3]) > 1:
            for item in elem[3]:
                if item in decided:
                    elem[3].remove(item)

        total_len = total_len + len(elem[3])  

soma_departure = 1

for elem in fields_ranges:
    if "departure" in elem[0]:
        soma_departure = soma_departure*int(my_ticket[elem[3][0]])

print(soma_departure)