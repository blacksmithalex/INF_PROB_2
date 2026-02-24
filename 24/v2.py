file = open('24.txt')
a = file.readline()
file.close()

for symb1 in 'ABC':
    for symb2 in 'ABC':
        pair = symb1 + symb2
        a = a.replace(pair, '* *')
parts = a.split()

countm = 0
for part in parts:
    countm = max(countm, len(part))
print(countm)
