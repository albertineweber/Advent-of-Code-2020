import pandas as pd
arq = open('input4.txt', 'r')

passport = []
dict_passaport = {}
counter = 0
counter2 = 0
flag = 0

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
keys_cid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

df = pd.DataFrame(columns = keys_cid)


valid_keys = set(keys)
i = 0

for line in arq:
    temp = line.split()
    if temp == []:
        passport = []
        dict_passaport = {}
        flag = 0
        i = i + 1

    else:
        for elem in temp:
            key = elem.split(':')[0]
            val = elem.split(':')[1]
            df.loc[i, key] = val
            passport.append(key)
            dict_passaport[key] = val

df = df.dropna(subset = keys, how = 'any')
result1 = len(df)
print(result1)

df['byr'] = df['byr'].astype(int)
df['iyr'] = df['iyr'].astype(int)
df['eyr'] = df['eyr'].astype(int)

df = df[df['byr'] >= 1920]
df = df[df['byr'] <= 2002]

df = df[df['iyr'] >= 2010]
df = df[df['iyr'] <= 2020]

df = df[df['eyr'] >= 2020]
df = df[df['eyr'] <= 2030]

df = df[(df['hgt'].str.contains("\d+cm") | df['hgt'].str.contains("\d+in"))]
df['tipo'] = df['hgt'].str.extract("(\d+)(cm|in)")[1]
df['#'] = df['hgt'].str.extract("(\d+)(cm|in)")[0]
df['#'] = df['#'].astype(int)

mask = []
for i in range(0, len(df)):
    if list(df['tipo'])[i] == "cm":
        if list(df['#'])[i] >= 150 and list(df["#"])[i] <= 193:
            mask.append(1)
        else:
            mask.append(0)

    if list(df['tipo'])[i] == "in":
        if list(df['#'])[i] >= 59 and list(df["#"])[i] <=76:
            mask.append(1)
        else:
            mask.append(0)

df['mask'] = mask
df = df[df['mask'] == 1]

df = df[(df['hcl'].str.contains("#(\d+[a-f]+)") | df['hcl'].str.contains("#([a-f]+\d+)") | df['hcl'].str.contains("#([a-f]+)") | df['hcl'].str.contains("#\d+"))]

df = df[df['ecl'].isin(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])]

mask2 = []

for i in range(0, len(df)):
    if len(list(df['pid'])[i]) != 9:
        mask2.append(0)
    else:
        mask2.append(1)

df['mask2'] = mask2
df = df[df['mask2'] == 1]

result2 = len(df)
print(result2)