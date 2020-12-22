arq = open('input2.txt', 'r')

counter = 0
counter2 = 0

for line in arq:
    count, letter, password = line.split()
    min, max = count.split('-')
    min = int(min)
    max = int(max)
    letter = letter.replace(':','')
    if password.count(letter) >= min and password.count(letter) <= max:
        counter = counter + 1

    if bool(password[min-1] == letter) ^ bool(password[max-1] == letter):
        counter2 = counter2+1
            
print(counter)
print(counter2)