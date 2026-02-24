file = open('24.txt')
a = file.readline()
file.close()

count, countm = 1, 1
for i in range(len(a) - 1):
    if not(a[i] in 'ABC' and a[i + 1] in 'ABC'):
        count += 1
        countm = max(count, countm)
    else:
        count = 1
print(countm)
