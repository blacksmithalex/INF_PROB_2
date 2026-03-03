def F(n):
    if n > 70:
        return n - 50
    return F(n + 2) + 2 * F(3 * n)

print(F(40))