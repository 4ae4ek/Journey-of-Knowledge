# объявление функции
import random


def merge(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1


# считываем данные
numbers1 = [random.randint(0, 5000) for _ in range(random.randint(2, 100000))]  # создание рандомного списка чисел
numbers2 = [random.randint(0, 5000) for _ in range(random.randint(2, 100000))]

# вызываем функцию
print(merge(numbers1, numbers2))
