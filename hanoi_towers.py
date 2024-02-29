def number_is_s(text):  # Функция для определения из какого столбца берем блок
    n = 0
    while not 1 <= n <= 3:
        n = input(text)
        if not n.isdigit():
            n = 0
            continue
        n = int(n)
    return stolbs[n-1]


def move(a, b):  # Функция для переписывания блока из списка в список (перемещение блока)
    if not a:
        print('Нечего перемещать')
    elif not b:
        print('Блок перемещён')
        b.append(a[-1])
        del a[-1]
    elif b[-1] > a[-1]:
        print('Блок перемещён')
        b.append(a[-1])
        del a[-1]
    else:
        print('Больший блок нельзя класть на меньший!')


def visual(a, b, c):  # Функция для отрисовки игры в консоли
    cur_s = list(a), list(b), list(c)  # Временные переменные для столбцов
    s0 = (' ' * (lvl - 1)) + '|' * 1 + (' ' * (lvl - 1))  # Обозначение пустого столбца
    for el in cur_s:
        while len(el) < lvl:  # Дорисовка пустых столбцов
            el.append(s0)
    i = lvl
    while i != 0:  # Отрисовка согласно уровня сложности
        i -= 1
        print(*(cur_s[0][i], cur_s[1][i], cur_s[2][i]))


def level():  # Генератор списка согласно сложности
    global lvl  # Необходимо для функции visual
    while not 1 <= lvl <= 999:  # Выбор сложности игры (уровень башни, количество блоков)
        lvl = input('Введите сложность от 1 до 999: ')
        if not lvl.isdigit():
            lvl = 0
            continue
        lvl = int(lvl)
    lvl_n = []
    for i in range(1, lvl + 1):
        lvl_n.insert(0, (' ' * (lvl - i)) + '_' * (i * 2 - 1) + (' ' * (lvl - i)))
    return list(lvl_n)


lvl = 0
s1 = level()  # Стартовый столбец (левый)
s2 = []
s3 = []
stolbs = (s1, s2, s3)
win = list(s1)  # Список для определения победы
print('Переместите башню с левого столба в правый. \n'
      'За один ход можно переместить только один блок. \n'
      'На меньший блок нельзя класть больший блок.\n')
visual(*stolbs)
count_of_step = 0  # Переменная счетчик ходов

while not s3 == win:  # Игровой цикл
    count_of_step += 1
    move(number_is_s('Откуда берем блок? '), number_is_s('Куда кладём? '))
    print(f'\nХод {count_of_step}')
    visual(*stolbs)

print('У ВАС ПОЛУЧИЛОСЬ!\nКоличество ходов:', count_of_step)
