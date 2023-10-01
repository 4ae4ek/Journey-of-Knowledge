import random

matrix_1 = []
matrix_2 = []
matrix_3 = []


def fill_matrix(matrix):
    for i in range(10):
        mass = []
        for i in range(10):
            number = random.randint(-1000, 1000)
            mass.append(number)
        matrix.append(mass)
    return matrix


def matrix_add(matrix_1, matrix_2):
    matrix_3 = []
    for i, v in enumerate(matrix_1):
        mass = []
        for j, val in enumerate(v):
            num = matrix_1[i][j] + matrix_2[i][j]
            mass.append(num)
        matrix_3.append(mass)
    return matrix_3


matrix_1 = fill_matrix(matrix_1)
matrix_2 = fill_matrix(matrix_2)
print('Первая матрица')
print(*matrix_1, sep='\n')
print('*' * 100)
print('Вторая матрица')
print(*matrix_2, sep='\n')
print('*' * 100)
print('Результат сложения 2 матрица')
print(*matrix_add(matrix_1, matrix_2), sep='\n')
