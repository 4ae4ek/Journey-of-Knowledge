def start_mass(mass):
    mass_of_mass = [[], [], [], [], [], [], [], [], []]
    for i in reversed(mass):
        if i[1].isalpha():
            mass_of_mass[0].append(i[1])
        if i[5].isalpha():
            mass_of_mass[1].append(i[5])
        if i[9].isalpha():
            mass_of_mass[2].append(i[9])
        if i[13].isalpha():
            mass_of_mass[3].append(i[13])
        if i[17].isalpha():
            mass_of_mass[4].append(i[17])
        if i[21].isalpha():
            mass_of_mass[5].append(i[21])
        if i[25].isalpha():
            mass_of_mass[6].append(i[25])
        if i[29].isalpha():
            mass_of_mass[7].append(i[29])
        if i[33].isalpha():
            mass_of_mass[8].append(i[33])
    return mass_of_mass


with open('input.txt', 'r') as f:
    counter = 0
    mass = []
    instructor_mass = []
    for i in f.readlines():
        counter += 1
        if counter <= 8:
            mass.append(i.replace('\n', ''))
        if counter == 9:
            mass = start_mass(mass)
        if counter >= 11:
            instructor_mass.append(i.replace('\n', ''))

for i in instructor_mass:
    itr = int(i.split()[1])
    frm = int(i.split()[3]) - 1
    to = int(i.split()[5]) - 1
    old_to = mass[to]
    new_from = mass[frm][-itr:]
    new_fr = mass[frm][:-itr]
    mass[to] = old_to + new_from
    mass[frm] = new_fr

answer = []
for i in mass:
    answer.append(i[-1])
print(*answer, sep='')
