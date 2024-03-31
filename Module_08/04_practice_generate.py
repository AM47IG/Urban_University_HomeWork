from random import randint, choice


def some_random(what_need):
    list_for_operation = ['+', '-', '*', '/', '//', '%', ]
    if what_need == 'int':
        return str(randint(1, 999))
    elif what_need == 'op':
        return choice(list_for_operation)
    else:
        return ''


def generate_str_for_calc(number_of_row=10_000, error_rate=10):  # Колличество строк и частота ошибок
    for _ in range(number_of_row):
        cur_str = ''
        dice = randint(a=0, b=100)
        if error_rate <= dice <= 100:  # Правильные строки
            cur_str += some_random('int') + ' '
            cur_str += some_random('op') + ' '
            cur_str += some_random('int')
        else:  # Ошибочные строки, но иногда случайно создаются правильные :)
            what_need = ['int', 'op', 'emp']
            cur_str += some_random(choice(what_need)) + ' '
            cur_str += some_random(choice(what_need)) + ' '
            cur_str += some_random(choice(what_need))
        yield cur_str + '\n'


with open('calc.txt', mode='w') as file:
    for gen_str in generate_str_for_calc():
        file.write(gen_str)

print('calc.txt создан')
