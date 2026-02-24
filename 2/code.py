def F(x, y, z, w):
    l1 = (not w) <= (not y)
    l2 = l1 <= (not z)
    l3 = l2 <= x
    l = not l3
    return int(l)

print('x y z w | F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                print(x, y, z, w, '|', F(x, y, z, w))