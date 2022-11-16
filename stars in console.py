def draw_box(h, w):
    print('*' * w)
    for i in range(h - 2):
        print('*' + ' ' * (w - 2) + '*')
    print('*' * w, end='')


def draw_triangle(size):
    [print('*' * i) for i in range(size + 1)]


def draw_triangle_ravnobed(w):
    for j in range(1, w + 1, 2):
        ws = int((w - j) / 2)
        print(' ' * ws + '*' * j)


draw_triangle(10)
print()
draw_box(14, 10)
print()
draw_triangle_ravnobed(15)
