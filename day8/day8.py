arq = open('input8.txt', 'r')

instructions = []

for line in arq:
    temp = line.split()
    instructions.append(temp)


stop_condition = instructions[-1]

for j in range(0, len(instructions)):
    flag = 0
    flag_stop = 0
    i = 0
    accumulator = 0
    visited = []

    if instructions[j][0] == "nop":
        instructions[j][0] = "jmp"


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

        if flag_stop == 1:
            if instructions[-1] == "acc":
                print(accumulator + instructions[-1][1])
            else:
                print(accumulator)

        instructions[j][0] = "nop"
    
    elif instructions[j][0] == "jmp":
        instructions[j][0] = "nop"

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

        if flag_stop == 1:
            if instructions[-1] == "acc":
                print(accumulator + instructions[-1][1])
            else:
                print(accumulator)

        instructions[j][0] = "jmp"

    

print(accumulator)