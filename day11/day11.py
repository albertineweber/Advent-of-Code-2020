import copy

arq = open('input11.txt', 'r')

automata = []

for line in arq:
    temp = line.split()[0]
    auto = []
    for elem in temp:
        auto.append(elem)
    automata.append(auto)


def check_adjacents(automata):
    new_automata = []
    for i in range(0, len(automata)):
        line = []
        for j in range(0, len(automata[i])):
            count_ocup = 0
            for m in range(-1,1+1):
                for n in range(-1, 1+1):
                    if m != 0 or n != 0:
                        if i+m >= 0 and n+j >= 0 and i + m < len(automata) and n+j < len(automata[i]):
                            if automata[i+m][n+j] == "#":
                                count_ocup = count_ocup + 1
            
            if automata[i][j] == "L" and count_ocup == 0:
                line.append("#")
            elif automata[i][j] == "#" and count_ocup >= 4:
                line.append("L")
            else:
                line.append(str(automata[i][j]))
        new_automata.append(line)
    
    return(new_automata)

def check_seats(automata):
    new_automata = []
    for i in range(0, len(automata)):
        line = []
        for j in range(0, len(automata[i])):
            count_ocup = 0
            for m in range(-1,1+1):
                for n in range(-1, 1+1):
                    if m != 0 or n != 0:
                        if i+m >= 0 and n+j >= 0 and i + m < len(automata) and n+j < len(automata[i]):
                            flag = 0

                            nm = m
                            nn = n
                            while automata[i+m][n+j] == ".":
                                m = m + nm
                                n = n + nn
                                if i+m < 0 or n+j < 0 or i + m >= len(automata) or n+j >= len(automata[i]):
                                    flag = 1
                                    break
                            
                            if flag == 0:
                                if automata[i+m][n+j] == "#":
                                    count_ocup = count_ocup + 1
                            m = nm
                            n = nn
            
            if automata[i][j] == "L" and count_ocup == 0:
                line.append("#")
            elif automata[i][j] == "#" and count_ocup >= 5:
                line.append("L")
            else:
                line.append(str(automata[i][j]))
        new_automata.append(line)
    
    return(new_automata)


flag = 0
c = 0

while flag == 0:
    c = c + 1

    #part1
    new_automata = check_adjacents(automata)

    #part2
    #new_automata = check_seats(automata)  

    if automata == new_automata:
        flag = 1

    for i in range(0, len(automata)):
        for j in range(0, len(automata[i])):
            automata[i][j] = str(new_automata[i][j])

count_ocup = 0

for i in range(0, len(automata)):
    for j in range(0, len(automata[i])):
        if automata[i][j] == "#":
            count_ocup = count_ocup + 1

print(count_ocup)
