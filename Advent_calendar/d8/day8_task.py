mass_of_row = []
mass_of_column = []
counter = 0
mass_of_beauty = []


def func_of_really_dich(number, i, j):
    left = mass_of_row[i][:j]
    right = mass_of_row[i][j + 1:]
    up = mass_of_column[j][:i]
    down = mass_of_column[j][i + 1:]
    try:
        if not max(left) >= number:
            return 1
        if not max(right) >= number:
            return 1
        if not max(up) >= number:
            return 1
        if not max(down) >= number:
            return 1
    except:
        return 1
    return 0


def func_of_really_dich_part_two(number, i, j):
    left = mass_of_row[i][:j]
    right = mass_of_row[i][j + 1:]
    up = mass_of_column[j][:i]
    down = mass_of_column[j][i + 1:]
    ct = 0
    ct1 = 0
    ct2 = 0
    ct3 = 0
    for i in left[::-1]:
        if i < number:
            ct += 1
        else:
            break
    for i in right:
        if i < number:
            ct1 += 1
        else:
            break
    for i in up[::-1]:
        if i < number:
            ct2 += 1
        else:
            break
    for i in down:
        if i < number:
            ct3 += 1
        else:
            break
    if ct == 0:
        ct = 1
    if ct1 == 0:
        ct1 = 1
    if ct2 == 0:
        ct2 = 1
    if ct3 == 0:
        ct3 = 1
    return ct * ct1 * ct2 * ct3


with open('input.txt', 'r') as f:
    flag = True
    for l in f:
        mass = [int(i) for i in l.strip()]
        if flag:
            mass_of_column = [[] for _ in range(len(mass))]
            flag = False
        for i in range(len(mass)):
            mass_of_column[i].append(mass[i])
        mass_of_row.append(mass)

for k in range(len(mass_of_row)):
    for r in range(len(mass_of_row[k])):
        counter += func_of_really_dich(mass_of_row[k][r], k, r)
        mass_of_beauty.append(func_of_really_dich_part_two(mass_of_row[k][r], k, r))

print(mass_of_beauty)
print(counter)
print(max(mass_of_beauty))
