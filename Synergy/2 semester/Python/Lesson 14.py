# Урок №14. Рекурсия
# Задание №1
# Есть последовательность
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Напишите рекурсивную функцию, которая выведет все элементы от первого
# до последнего и в конце отобразит сообщение Конец списка, если выводить
# больше нечего. Циклы использовать запрещено
# Вместе с файлом, отправляемом на проверку домашнего задания,
# комментарием укажите ссылку на репозиторий GitHub, где хранится ваша
# программа.

print('Введите список')
my_list = list(map(int, input().split()))


def recursion(mass):
    if len(mass) == 0:
        print('Конец списка')
        return
    print(mass[0])
    recursion(mass[1:])


recursion(my_list)
