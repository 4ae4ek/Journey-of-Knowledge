eng_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
with open('input.txt', 'r') as f:
    mass_temp = []
    counter = 0
    for i in f.readlines():
        counter += 1
        mass_temp.append(i.strip())
        if counter == 3:
            counter = 0
            for j in mass_temp[0]:
                if j in mass_temp[1] and j in mass_temp[2]:
                    total += eng_letters.index(j) + 1
                    break
            mass_temp = []
    print(total)