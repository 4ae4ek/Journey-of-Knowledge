def task_1():
    print('Пожалуйста введите вид питомца')
    species = input()
    print('Пожалуйста введите возраст питомца')
    age = int(input())
    print('Пожалуйста введите кличку питомца')
    name = input()
    print(f'Это {species} по кличке "{name}". Возраст: {age}')


def task_2():
    mass = []
    print("Пожалуйста введите по очереди основные этапы развития человек", '*подсказка*', 'всего 5 основных этапов', sep='\n')
    for _ in range(5):
        stage = input()
        mass.append(stage)
    print(*mass, sep='=>')


task_1()
task_2()
