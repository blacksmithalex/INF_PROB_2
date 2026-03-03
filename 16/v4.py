F = [0] * 500
for n in range(71, 500):
    F[n] = n - 50

for n in range(70, 0, -1):
    F[n] = F[n + 2] + 2 * F[3 * n]

print(F[40])