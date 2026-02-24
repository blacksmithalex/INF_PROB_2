from math import sqrt
def dividers(n):
    div = set()
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return sorted(div)

def even_count(div):
    count = 0
    for d in div:
        if d % 2 == 0:
            count += 1
    return count

k = 1
count = 0
while count != 5:
    Nk = 750_000 + k
    num_even = even_count(dividers(Nk))
    if num_even % 2 != 0:
        print(k, num_even)
        count += 1
    k += 1