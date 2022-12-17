from collections import defaultdict

counter = 0


def is_unique(s):
    dicts = defaultdict(bool)
    for j in s:
        if dicts[j]:
            return False
        dicts[j] = True
    return True


with open('input.txt', 'r') as f:
    mass = f.readlines()[0].strip()
    list_ch = mass[:4]
    if is_unique(list_ch):
        counter = 4
        print(counter)
    mass = mass[4:]
    for i, ch in enumerate(mass):
        list_ch = list_ch[1:] + ch
        if is_unique(list_ch):
            counter = 5 + i
            print(counter)
            break