def f(x, p):
    if x >= 81 and p == 3:
        return True
    elif x < 81 and p == 3:
        return False
    elif x >= 81:
        return False
    else:
        return f(x + 1, p + 1) or f(x * 4, p + 1)

for S in range(1, 80 + 1):
    if f(S, 1):
        print(S)