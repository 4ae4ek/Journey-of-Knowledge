def task_1():
    n = int(input())
    mass = [int(input()) for _ in range(n)]
    mass.reverse()
    return mass


def task_2():
    n = int(input())
    mass = list(map(int, input().split()))
    mass = [mass[-1]] + mass[:-1]
    return mass[:n]


def task_3():
    m, n = int(input()), int(input())
    mass = [int(input()) for _ in range(n)]
    boat_mass = [[]]
    for i in mass:
        boat = None
        for j in boat_mass:
            if sum(j) + i <= m and len(j) < 2:
                boat = j
                break
        if boat is None:
            boat_mass.append([])
            boat = boat_mass[-1]
        boat.append(i)
    return len(boat_mass)


print(task_1())
print(task_2())
print(task_3())
