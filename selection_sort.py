import random

a = [random.randint(0, 5000) for _ in range(10000)]
random.shuffle(a)
n = len(a)

for i in range(n):
    mini = i
    for j in range(i + 1, n):
        if a[mini] > a[j]:
            mini = j
    a[i], a[mini] = a[mini], a[i]
print(a)
