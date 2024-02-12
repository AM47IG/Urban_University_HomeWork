def number_is_s_out():  # Функция для определения из какого столбца берем блок
    n = ''
    while not (n == '1' or n == '2' or n == '3'):
        n = input('Откуда берем блок? ')
    if n == '1':
        n = s1
    elif n == '2':
        n = s2
    elif n == '3':
        n = s3
    return n


def number_is_s_in():  # Функция для определения на какой столбец кладем блок
    n = ''
    while not (n == '1' or n == '2' or n == '3'):
        n = input('Куда кладём? ')
    if n == '1':
        n = s1
    elif n == '2':
        n = s2
    elif n == '3':
        n = s3
    return n


def move(s_out, s_in):  # Функция для переписывания блока из списка в список (перемещение блока)
    if not s_out:
        print('Нечего перемещать')
    elif not s_in:
        print('Блок перемещён')
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
    elif s_in[-1] > s_out[-1]:
        print('Блок перемещён')
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
    else:
        print('Больший блок нельзя класть на меньший!')


def visual(s1, s2, s3):  # Функция для отрисовки игры в консоли
    sd1 = list(s1)  # Временные переменные для столбцов
    sd2 = list(s2)
    sd3 = list(s3)
    while len(sd1) < lvl:  # Дорисовка пустых столбцов
        sd1.append(s0)
    while len(sd2) < lvl:
        sd2.append(s0)
    while len(sd3) < lvl:
        sd3.append(s0)
    if lvl >= 7:  # Отрисовка согласно уровня сложности
        sp7 = (sd1[6], sd2[6], sd3[6])
        print(*sp7)
    if lvl >= 6:
        sp6 = (sd1[5], sd2[5], sd3[5])
        print(*sp6)
    if lvl >= 5:
        sp5 = (sd1[4], sd2[4], sd3[4])
        print(*sp5)
    if lvl >= 4:
        sp4 = (sd1[3], sd2[3], sd3[3])
        print(*sp4)
    sp3 = (sd1[2], sd2[2], sd3[2])
    sp2 = (sd1[1], sd2[1], sd3[1])
    sp1 = (sd1[0], sd2[0], sd3[0])
    print(*sp3)
    print(*sp2)
    print(*sp1)


lvl = 0
while True:  # Выбор сложности игры (уровень башни, количество блоков)
    try:
        lvl = int(input('Введите сложность от 3 до 7: '))
        if 3 <= lvl <= 7:
            break
        else:
            continue
    except ValueError:
        print('Неправильный ввод. Попробуйте еще раз.')
s0 = (' ' * (lvl - 1)) + '|' * 1 + (' ' * (lvl - 1))  # обозначение пустого столбца
b1 = (' ' * (lvl - 1)) + '_' * 1 + (' ' * (lvl - 1))  # обозначение блока (далее блоки по возрастанию)
b2 = (' ' * (lvl - 2)) + '_' * 3 + (' ' * (lvl - 2))
b3 = (' ' * (lvl - 3)) + '_' * 5 + (' ' * (lvl - 3))
b4 = (' ' * (lvl - 4)) + '_' * 7 + (' ' * (lvl - 4))
b5 = (' ' * (lvl - 5)) + '_' * 9 + (' ' * (lvl - 5))
b6 = (' ' * (lvl - 6)) + '_' * 11 + (' ' * (lvl - 6))
b7 = (' ' * (lvl - 7)) + '_' * 13 + (' ' * (lvl - 7))

lvl_b = [b7, b6, b5, b4, b3, b2, b1]  # Заготовка списка
win = []  # Список для определения победы
s1 = []  # Стартовый столбец (левый)
s2 = []
s3 = []
s1 += lvl_b[-lvl:]  # Присваивание стартовому списку уровня
win += lvl_b[-lvl:]  # Присваивание финальному заданию уровня
count_of_step = 0  # Переменная счетчик ходов
print('Переместите башню с левого столба в правый. \n'
      'За один ход можно переместить только один блок. \n'
      'На меньший блок нельзя класть больший блок.\n')
visual(s1, s2, s3)

while not s3 == win:  # Игровой цикл
    s_out = number_is_s_out()
    s_in = number_is_s_in()
    move(s_out, s_in)
    print()
    visual(s1, s2, s3)
    count_of_step += 1

print('У ВАС ПОЛУЧИЛОСЬ!\nКоличество ходов:', count_of_step)
