arq = open('input6.txt', 'r')

questions = ""
counter = 0
counter2 = 0
group_size = 0

for line in arq:
    temp = line.split()
    if temp == []:
        counter = counter + len(set(questions))
        for question in set(questions):
            if questions.count(question) == group_size:
                counter2 = counter2 + 1
        questions = ""
        group_size = 0

    else:
        questions = questions + temp[0]
        group_size = group_size + 1

if questions != "":
    counter = counter + len(set(questions))
    for question in set(questions):
        if questions.count(question) == group_size:
            counter2 = counter2 + 1
    questions = ""
    group_size = 0

print(counter)
print(counter2)