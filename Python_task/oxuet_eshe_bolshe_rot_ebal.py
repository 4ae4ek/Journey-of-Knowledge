s_num = int(input())

table = []

for i in range(s_num):
    s = input()
    types_s = int(s[0])
    table.append(s[2:])

flag = True

while flag:
    f2 = True
    for i in range(len(table)):
        f1 = False
        if table[i].isdigit():
            continue
        else:
            f = table[i]
            f = f.split('C')
            f = ''.join(f)
            fn = ''
            s = 0
            k = len(f)
            for j in range(len(f)):
                if f[j] == '+' or f[j] == '-' or f[j] == '*':
                    k = j
                    ind = int(f[s:k])
                    try:
                        if ind - 1 < 0:
                            table = [-1]
                            break
                        if ind == i:
                            table = [-1]
                            break
                        if not table[ind - 1].isdigit():
                            f1 = True
                            f2 = False
                            break
                        fn += table[ind - 1] + f[j]
                        s = k + 1
                    except IndexError:
                        table = [-1]
                        break
                if j == len(f) - 1:
                    k = len(f)
                    ind = int(f[s:k])
                    try:
                        if ind - 1 < 0:
                            table = [-1]
                            break
                        if ind == i:
                            table = [-1]
                            break
                        if not table[ind - 1].isdigit():
                            f1 = True
                            f2 = False
                            break
                        fn += table[ind - 1]
                        s = k
                    except IndexError:
                        table = [-1]
                        break
            if f1:
                continue
            if table == [-1]:
                flag = False
                break
            else:
                fn = eval(fn)
                table[i] = fn
    if f2:
        flag = False


print(*table, sep='\n')