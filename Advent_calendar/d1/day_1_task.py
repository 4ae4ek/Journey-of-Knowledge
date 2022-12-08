# input file with number of callories separated by empty line find the max invenotry
try:
    f = open('input.txt', 'r')
    mass = []
    summ = 0
    for l in f:
        if len(l) == 1:
            mass.append(summ)
            summ = 0
            continue
        else:
            summ += int(l.strip())
finally:
    f.close()

print(max(mass))