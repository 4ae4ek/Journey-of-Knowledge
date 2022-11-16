import random

a = [random.randint(0, 5000) for _ in range(10000)]
n = len(a)

for i in range(n - 1):
    flag = True
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            flag = False
    if flag:
        break

print(*a, sep='\n')