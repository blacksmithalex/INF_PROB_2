file = open('9.txt')
for line in file:
    line = sorted([int(x) for x in line.split()])
    freq1, freq2 = [], [] # уникальные, повторяются по два раза
    for x in line:
        if line.count(x) == 1:
            freq1.append(x)
        if line.count(x) == 2:
            freq2.append(x)
    if len(freq1) == 2 and len(freq2) == 4:
        rule1 = line[-1] not in freq2
        rule2 = line[5] * line[0] > line[1] + line[2] + line[3] + line[4]
        if rule1 and rule2:
            print(line, sum(line))
            break

