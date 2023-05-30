import random
import string

st = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(2, 100000)))

def count_max(st):
    dct = {}
    for now in st:
        if now not in dct:
            dct[now] = 0
        dct[now] += 1
    result = max(dct, key=dct.get)
    return dct[result], result

print(st)
print(count_max(st))