count = 0
with open('input.txt', 'r') as f:
    for l in f:
        mass1 = [i for i in
                 range(int(l.strip().split(',')[0].split('-')[0]), int(l.strip().split(',')[0].split('-')[1]) + 1)]
        mass2 = [i for i in
                 range(int(l.strip().split(',')[1].split('-')[0]), int(l.strip().split(',')[1].split('-')[1]) + 1)]
        if mass1[0] in mass2 and mass1[-1] in mass2:
            count += 1
        elif mass2[0] in mass1 and mass2[-1] in mass1:
            count += 1
print(count)