def task_1(num):
    counter = 0
    for i in range(num):
        b = int(input())
        if b == 0:
            counter += 1
    return counter


def task_2(num):
    counter = 1
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            counter += 1
    return counter


def task_3(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)


n = int(input())
print(task_1(n))
n = int(input())
print(task_2(n))
a, b = int(input()), int(input())
task_3(a, b)
