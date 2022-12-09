eng_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
mass_lett = []
with open('input.txt', 'r') as f:
    for l in f:
        p1 = l[:len(l.strip()) // 2]
        p2 = l[len(l.strip()) // 2:]
        for i in p1:
            if i in p2:
                total += eng_letters.index(i) + 1
                mass_lett.append(i)
                break
print(total)
