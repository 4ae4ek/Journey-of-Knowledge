def task_1(num: int):
    if num > 0:
        otr = 'положительное'
    elif num == 0:
        otr = 'нулевое'
    else:
        otr = 'отрицательное'
    if num % 2:
        odd = 'нечетное'
    else:
        odd = 'четное'
    print("число не является четным" if num % 2 else '')
    print(f'{otr} {odd} число' if not num == 0 else f'{otr} число')


def task_2():
    word = input()
    result = {'a': False, 'e': False, 'i': False, 'o': False, 'u': False}
    for i in word:
        if i in result:
            result[i] += 1
    for k, v in result.items():
        print(f'{k}: {v}')


def task_3(min_invest, maik, ivan):
    if maik >= min_invest and ivan >= min_invest:
        result = 2
    elif maik >= min_invest:
        result = 'Mike'
    elif ivan >= min_invest:
        result = 'Ivan'
    elif maik + ivan >= min_invest:
        result = 1
    else:
        result = 0
    return result


task_1(0)
task_2()
print(task_3(100, 50, 50))