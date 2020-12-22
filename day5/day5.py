arq = open('input5.txt', 'r')

def find_row(passport, min, max):
    for i in range(0, len(passport)):
        if passport[i] == 'F':
            max = (max + min)//2
        else:
            min = (max + min)//2 + 1
    return(min)

def find_col(passport, min, max):
    for i in range(0, len(passport)):
        if passport[i] == 'L':
            max = (max + min)//2
        else:
            min = (max + min)//2 + 1
    return(min)

def find_seat(passport):
    row = find_row(passport[:-3], min_row, max_row)
    col = find_col(passport[-3:], min_col, max_col)
    id = row*8 + col
    return(id)


def find_missing(id_list, missing_ids):
    for i in range(min_row, max_row):
        for j in range(min_col, max_col):
            id = i*8 + j
            if id not in id_list:
                missing_ids.append(id)

    for elem in missing_ids:
        before = elem - 1
        after = elem + 1
        if before in id_list and after in id_list:
            return(elem)


#global ctes
min_row = 0
max_row = 127
min_col = 0
max_col = 7

max_id = 0
min_id = max_row*8 + max_col

#lists
id_list = []
missing_ids = []

for line in arq:
    passport = line.split()[0]
    id = find_seat(passport)
    id_list.append(id)
    if id > max_id:
        max_id = id

my_seat = find_missing(id_list, missing_ids)

#results
print(max_id)
print(my_seat)
    