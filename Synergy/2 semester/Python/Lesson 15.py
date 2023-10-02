# Урок №15. ООП
# Задание №1
# Есть родительский класс:
# class Transport:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
# Создайте объект Autobus, который унаследует все переменные и методы
# родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12
# Задание №2
# Создайте класс Autobus, который наследуется от класса Transport.
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного
# средства:
# class Transport:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#     def seating_capacity(self, capacity):
#         return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров
# Вместе с файлом, отправляемом на проверку домашнего задания,
# комментарием укажите ссылку на репозиторий GitHub, где хранится ваша
# программа.


def task_1():
    class Transport:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

    class Autobus_task(Transport):
        def __init__(self, name, max_speed, mileage):
            super().__init__(name, max_speed, mileage)

        def prints(self):
            print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

    Autobus = Autobus_task('Renaul Logan', 180, 12)
    Autobus.prints()


def task_2():
    class Transport:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def seating_capacity(self, capacity):
            return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

    class Autobus(Transport):
        def __init__(self, name, max_speed, mileage):
            super().__init__(name, max_speed, mileage)

        def seating_capacity(self, capacity=50):
            return super().seating_capacity(capacity)

    car = Autobus('Renaul Logan', 180, 12)
    print(car.seating_capacity())


task_1()
task_2()
