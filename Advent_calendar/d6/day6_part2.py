from collections import defaultdict


def is_unique(s):
    dicts = defaultdict(bool)
    for j in s:
        if dicts[j]:
            return False
        dicts[j] = True
    return True


counter = 0
with open('input.txt', 'r') as f:
    mass = f.readlines()[0].strip()
    list_ch = mass[:14]
    if is_unique(list_ch):
        counter = 14
        print(counter)
    mass = mass[14:]
    for i, ch in enumerate(mass):
        list_ch = list_ch[1:] + ch
        if is_unique(list_ch):
            counter = 15 + i
            print(counter)
            break
