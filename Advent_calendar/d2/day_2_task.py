with open('input.txt', 'r') as f:
    opponent_dict = {
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }
    my_dict = {'X': 1, 'Y': 2, 'Z': 3}
    total = 0
    for l in f:
        total += my_dict[l.split()[1]]
        total += opponent_dict[''.join(l.split())]
    print(total)

