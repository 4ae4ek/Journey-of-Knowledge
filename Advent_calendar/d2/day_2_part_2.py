with open('input.txt', 'r') as f:
    opponent_dict = {
        'AX': 3,
        'AY': 1,
        'AZ': 2,
        'BX': 1,
        'BY': 2,
        'BZ': 3,
        'CX': 2,
        'CY': 3,
        'CZ': 1,
    }
    my_dict = {'X': 0, 'Y': 3, 'Z': 6}
    total = 0
    for l in f:
        total += my_dict[l.split()[1]]
        total += opponent_dict[''.join(l.split())]
    print(total)
