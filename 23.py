def f(a, b): # кол-во путей из a в b
    if a < b or a == 12 or a == 15:
        return 0
    elif a == b:
        return 1
    else:
        if a % 2 == 0 and a % 3 == 0:
            return f(a - 1, b) + f(a // 2, b) + f(a // 3, b)
        elif a % 2 == 0:
            return f(a - 1, b) + f(a // 2, b)
        elif a % 3 == 0:
            return f(a - 1, b) + f(a // 3, b)
        else:
            return f(a - 1, b)

print(f(19, 1))
