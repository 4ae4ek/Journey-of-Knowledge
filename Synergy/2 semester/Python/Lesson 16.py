# Урок №16. Классы и объекты
# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у
# него есть методы:
# ● top_up(X) - пополнить на X
# ● count_1000() - выводит сколько целых тысяч осталось в кассе
# ● take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не
# достаточно денег
# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также
# s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# ● go_up() - увеличивает y на s
# ● go_down() - уменьшает y на s
# ● go_left() - уменьшает x на s
# ● go_right() - увеличивает y на s
# ● evolve() - увеличивает s на 1
# ● degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может
# стать ≤ 0
# ● count_moves(x2, y2) - возвращает минимальное количество действий, за
# которое черепашка сможет добраться до x2 y2 от текущей позиции
# Вместе с файлом, отправляемом на проверку домашнего задания,
# комментарием укажите ссылку на репозиторий GitHub, где хранится ваша
# программа.
# Критерии оценки:
# 1 балла - Выполнено 1 задание
# 3 балла - Выполнено 2 задания

def task_1():
    class CashRegister:
        __money = 0

        def __init__(self, money):
            self.__money = money

        def top_up(self, money):
            self.__money += money

        def count_1000(self):
            print(f'{self.__money // 1000} тысяч в кассе')

        def take_away(self, x):
            if not self.__money - x < 0:
                self.__money -= x
            else:
                print('Недостаточно денег в кассе')

    cash = CashRegister(1000)
    cash.count_1000()
    cash.top_up(1000)
    cash.count_1000()
    cash.take_away(1000)
    cash.count_1000()
    cash.take_away(2000)


def task_2():
    class Turtle:
        def __init__(self, x=0, y=0, s=1):
            self.x = x
            self.y = y
            self.s = s

        def go_up(self):
            self.y += self.s

        def go_down(self):
            self.y -= self.s

        def go_left(self):
            self.x -= self.s

        def go_right(self):
            self.x += self.s

        def evolve(self):
            self.s += 1

        def degrade(self):
            if not self.s - 1 <= 0:
                self.s -= 1
            else:
                print('Нельзя уменьшить скорость меньше 1')

        def count_moves(self, x2, y2):
            dx = abs(x2 - self.x)
            dy = abs(y2 - self.y)
            if dx % self.s == 0 and dy % self.s == 0:
                print(f'Минимальное количество шагов {dx // self.s + dy // self.s}')
            else:
                print(f'Невозможно достичь заданной позиции с текущим шагом из текущих координат')

    turtle = Turtle()
    turtle.evolve()
    turtle.count_moves(5, 5)


task_1()
task_2()
