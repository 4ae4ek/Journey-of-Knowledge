def task_1(a, b, c, d):
    area = a * c
    perimeter = a + b + c + d
    return [area, perimeter]


def task_2(num: float):
    num = float(num)
    ed = num % 10
    des = num % 100 // 10
    sot = num % 1000 // 100
    tis = num % 10000 // 1000
    destis = num % 100000 // 10000
    answer = (des ** ed * sot) / (destis - tis)
    return answer


print(*task_1(2, 4, 2, 4))
print(task_2(46275))
