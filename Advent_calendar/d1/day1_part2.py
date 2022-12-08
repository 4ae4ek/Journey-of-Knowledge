# input file with number of callories separated by empty line find the max invenotry
with open('input.txt', 'r') as f:
    mass = []
    summ = 0
    for l in f:
        if len(l) == 1:
            mass.append(summ)
            summ = 0
            continue
        else:
            summ += int(l.strip())
mass.sort()
print(sum(mass[-3:]))
