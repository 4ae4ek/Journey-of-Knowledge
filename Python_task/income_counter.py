def income(num: int, d: int):
    st = num
    for i in range(1, d):
        pr = num / 100
        num += pr * 1.9
    return num - st

print(income(1000, 30))