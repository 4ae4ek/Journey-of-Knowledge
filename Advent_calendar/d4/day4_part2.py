count = 0
with open('input.txt', 'r') as f:
    for l in f:
        a, b, c, d = int(l.strip().split(',')[0].split('-')[0]), int(l.strip().split(',')[0].split('-')[1]), int(
            l.strip().split(',')[1].split('-')[0]), int(l.strip().split(',')[1].split('-')[1])
        if a <= c <= b or a <= d <= b:
            count += 1
        elif c <= a <= d or c <= b <= d:
            count += 1
print(count)