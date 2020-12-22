arq = open('input1.txt', 'r')

nums = {}

for line in arq:
    elem = int(line.split()[0])
    nums[elem] = elem
    complement = 2020 - elem
    if complement in nums:
        print(elem, complement, complement*elem)

    rest = complement
    for x in nums:
        y = complement - x
        if y in nums:
            print(elem, x, y, elem*x*y)