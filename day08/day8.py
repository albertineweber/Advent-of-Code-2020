arq = open('input8.txt', 'r')

def decide_action(instructions):
    flag = 0
    flag_stop = 0
    i = 0
    accumulator = 0
    visited = []

    while flag != 1:
        action = instructions[i][0]
        counter = int(instructions[i][1])
        if action == "nop":
            i = i + 1
        elif action == "acc":
            accumulator = accumulator + counter
            i = i + 1
        elif action == "jmp":
            i = i + counter
        if i in visited:
            flag = 1
        else:
            visited.append(i)

        if i == (len(instructions) - 1):
            flag_stop = 1
            flag = 1

    return(accumulator, flag_stop)

def change_field(field):
    if field == "nop":
        return("jmp")
    
    elif field == "jmp":
        return("nop")
    
    else:
        return("acc")


def check_condition(flag_stop, instructions, accumulator):
    if flag_stop == 1:
        if instructions[-1] == "acc":
            print(accumulator + instructions[-1][1])
        else:
            print(accumulator)


#main

instructions = []

for line in arq:
    temp = line.split()
    instructions.append(temp)


stop_condition = instructions[-1]


for j in range(0, len(instructions)):
    instructions[j][0] = change_field(instructions[j][0])
    accumulator, flag_stop = decide_action(instructions)
    check_condition(flag_stop, instructions, accumulator)
    instructions[j][0] = change_field(instructions[j][0])

print(accumulator)