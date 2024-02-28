def number_is_s(text):  # Функция для определения из какого столбца берем блок
    n = 0
    while not 1 <= n <= 3:
        n = input(text)
        if not n.isdigit():
            n = 0
            continue
        n = int(n)
    if n == 1:
        return s1
    elif n == 2:
        return s2
    else:
        return s3


def move(a, b):  # Функция для переписывания блока из списка в список (перемещение блока)
    if not a:
        print('Нечего перемещать')
    elif not b:
        print('Блок перемещён')
        block = a[-1]
        a.remove(block)
        b.append(block)
    elif b[-1] > a[-1]:
        print('Блок перемещён')
        block = a[-1]
        a.remove(block)
        b.append(block)
    else:
        print('Больший блок нельзя класть на меньший!')


def visual(a, b, c):  # Функция для отрисовки игры в консоли
    sd1, sd2, sd3 = list(a), list(b), list(c)  # Временные переменные для столбцов
    s0 = (' ' * (lvl - 1)) + '|' * 1 + (' ' * (lvl - 1))  # обозначение пустого столбца
    while len(sd1) < lvl:  # Дорисовка пустых столбцов
        sd1.append(s0)
    while len(sd2) < lvl:
        sd2.append(s0)
    while len(sd3) < lvl:
        sd3.append(s0)
    i = lvl
    while i != 0:
        i -= 1
        print(*(sd1[i], sd2[i], sd3[i]))  # Отрисовка согласно уровня сложности


def level(lv):
    lvl_n = []
    for i in range(1, lv + 1):
        lvl_n.insert(0, (' ' * (lv - i)) + '_' * (i * 2 - 1) + (' ' * (lv - i)))
    return lvl_n


lvl = 0
while not 1 <= lvl <= 999:  # Выбор сложности игры (уровень башни, количество блоков)
    lvl = input('Введите сложность от 1 до 999: ')
    if not lvl.isdigit():
        lvl = 0
        continue
    lvl = int(lvl)


s1 = list(level(lvl))  # Стартовый столбец (левый)
s2 = []
s3 = []
win = list(s1)  # Список для определения победы
print('Переместите башню с левого столба в правый. \n'
      'За один ход можно переместить только один блок. \n'
      'На меньший блок нельзя класть больший блок.\n')
visual(s1, s2, s3)
count_of_step = 0  # Переменная счетчик ходов

while not s3 == win:  # Игровой цикл
    s_out, s_in = number_is_s('Откуда берем блок? '), number_is_s('Куда кладём? ')
    move(s_out, s_in)
    print()
    visual(s1, s2, s3)
    count_of_step += 1

print('У ВАС ПОЛУЧИЛОСЬ!\nКоличество ходов:', count_of_step)
