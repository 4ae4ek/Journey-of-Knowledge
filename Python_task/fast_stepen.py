import timeit


def pow(a, n):
    if n % 2 == 0:
        return (a ** 2) ** (n / 2)
    if n % 2 != 0:
        return a * pow(a, n - 1)
    return a


def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 != 0:
        return a * power(a, n - 1)
    elif n % 2 == 0:
        return power(a * a, n / 2)

def start_fast():
    a = float(99999999.9999)
    n = int(33)
    print("Total time : %.3f ms" % (1000 * timeit.timeit(f'print({pow(a, n)}, end=" ")', globals=globals(), number=1)))
    print("Total time : %.3f ms" % (1000 * timeit.timeit(f'print({a**n}, end=" ")', globals=globals(), number=1)))

start_fast()