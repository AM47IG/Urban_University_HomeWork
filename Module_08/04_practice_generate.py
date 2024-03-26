from random import randint, choice


def some_random(what_need):
    list_for_operation = ['+', '-', '*', '/', '//', '%', ]
    if what_need == 'int':
        return str(randint(1, 999))
    elif what_need == 'op':
        return choice(list_for_operation)
    else:
        return ' '


def generate_str_for_calc(x):  # x = Количество строк
    for _ in range(x):
        list_for_str = []
        dice = randint(1, 25)  # От этой переменной зависит частота ошибок
        if dice > 1:  # Правильные строки
            list_for_str.append(some_random('int'))
            list_for_str.append(some_random('op'))
            list_for_str.append(some_random('int'))
        else:  # Ошибочные строки
            what_need = ['int', 'op', 'emp']
            list_for_str.append(some_random(choice(what_need)))
            list_for_str.append(some_random(choice(what_need)))
            list_for_str.append(some_random(choice(what_need)))
        yield ' '.join(list_for_str) + '\n'


with open('calc.txt', mode='w') as file:
    for i in generate_str_for_calc(10_000):
        file.write(i)

print('calc.txt создан')
