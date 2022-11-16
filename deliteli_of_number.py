# объявление функции
def get_factors(num):
    return [i for i in range(1, num//2 + 1) if num % i == 0] + [num]


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
