arq = open('input9.txt', 'r')

previous = {}
full_list = []
i = 0
flag = 0
flag2 = 0

for line in arq:
    num = int(line.split()[0])
    if i < 25:
        previous[num] = i
        full_list.append(num)
    else:
        for elem in previous:
            complement = num - elem
            if complement in previous:
                flag = 1

        if flag == 0 and flag2 == 0:
            invalid = num
            flag2 = 1

        remove = list(previous.keys())[0]
        previous.pop(remove)
        previous[num] = i
        full_list.append(num)
        flag = 0
    
    i = i + 1

print(invalid)

i = 0
j = i + 1
soma = 0

for i in range(0, len(full_list)):
    contiguous = []
    soma = 0
    j = i + 1
    contiguous.append(full_list[i])
    for j in range(i+1, len(full_list)):
        contiguous.append(full_list[j])
        if sum(contiguous) == invalid:
            print(min(contiguous)+max(contiguous))
        elif soma > invalid:
            break
        j = j + 1
    
