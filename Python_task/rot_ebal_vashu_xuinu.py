# n, k = int(input()), int(input())
# mass = [int(i) for i in input().split()]

n, k = 5, 1
mass = [int(i) for i in '-1 2 4 3 0'.split()]
print(mass)

count = 0
count1 = []

for i in mass:
    if i % 2 == 0:
        count += 1
    else:
        count = 0
    if count != 0:
        count1.append(count)


print(count1)
