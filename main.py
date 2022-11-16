# import random
#
# random.seed(15)
# a = [random.randint(1, 101) for _ in range(random.randint(1, 101))]
# b = [random.randint(1, 101) for _ in range(random.randint(1, 101))]
# c = [random.randint(1, 101) for _ in range(random.randint(1, 101))]
#
# a.extend(b)
# a.extend(c)
#
#
# def counter(fu):
#     def inner(*args, **kw):
#         inner.count += 1
#         return fu(*args, **kw)
#
#     inner.count = 0
#     return inner
#
#
# @counter
# def quicksort(nums, r):
#     if len(nums) <= 1:
#         return nums
#     else:
#         q = nums[len(nums) // 2]
#     if r:
#         l_nums = [n for n in nums if n > q]
#         e_nums = [q] * nums.count(q)
#         b_nums = [n for n in nums if n < q]
#     else:
#         l_nums = [n for n in nums if n < q]
#         e_nums = [q] * nums.count(q)
#         b_nums = [n for n in nums if n > q]
#     return quicksort(l_nums, r) + e_nums + quicksort(b_nums, r)
#
#
# sor_a = quicksort(a, False)
# l_sor_a = quicksort.count
# print(l_sor_a)
# sor_b = quicksort(a, True)
# l_sor_b = quicksort.count - l_sor_a
# print(l_sor_b)
# print(sor_a)
# print(sor_b)
from copy import deepcopy


def repl(mass):
    mass1 = deepcopy(mass)
    for i in range(len(mass)):
        if mass[i] in mass[i + 1:]:
            mass1.pop(i)
    return mass1


# 1 2 3
# 2 3 1



def merge(a, b):
    for i in range(len(a)):
        print(a[i:len(a)])
        if a[i:len(a)] in b:
            print(a[i:len(a)])

    # else:
    #     for i in range(len(a)):
    #         if a[i] in b:
    #             b = list(filter(lambda s: s != a[i], b))
    #     a.extend(b)
    return [i for i, j in zip(a, b) if i == j]


a = '5 1 2 3 4 5'.split()
b = '4 9 10 11 12'.split()
c = '2 3 1'.split()
a = repl(a)
b = repl(b)
c = repl(c)
a = merge(a, b)
# a = merge(b, c)
print(a, b, c)
