from functools import cache
@cache
def F(n):
    if n > 70:
        return n - 50
    return F(n + 2) + 2 * F(3 * n)

for n in range(1000, 0, -1):
    F(n)

print(F(40))