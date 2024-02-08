# '''представим что у нас есть три столба и три блока (в будущем это количество соответственно должно иметь
# возможность масштабироваться). Столбы - массивы, блоки - для начала кортеж из названия и площади. Задача
# переместить блоки между массивами с проверками, можно ли положить данный кортеж в данный массив на основе
# площади объекта. Если площадь последнего элемента массива меньше, чем площадь перемещаемого объекта - класть
# блок в данный массив нельзя'''
def dorisovka_s0(lvl):
    while len(lvl) < 3:
        lvl.append(s0)


def move(s_out, s_in):
    if not s_in:
        print('Переклали')
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
    elif s_in[-1] > s_out[-1]:
        print('Переклали')
        b = s_out[-1]
        s_out.remove(b)
        s_in.append(b)
    else:
        print('Так не пойдет!')


def number_is_s_out():
    n = ''
    while not (n == '1' or n == '2' or n == '3'):
        n = input('Откуда берем блок? ')  # Здесь остановился

    if n == '1':
        n = s1
    elif n == '2':
        n = s2
    elif n == '3':
        n = s3

    return n


def number_is_s_in():
    n = input('Куда кладем? ')
    if n == '1':
        n = s1
    elif n == '2':
        n = s2
    elif n == '3':
        n = s3
    else:
        print('Только от одного до трех!!!')
        number_is_s_in()
    return n


s0 = '  |  '
b1 = '  _  '
b2 = ' ___ '
b3 = '_____'

s1 = [b3, b2, b1]
s2 = []
s3 = []

while not s3 == [b3, b2, b1]:
    s_out = number_is_s_out()
    s_in = number_is_s_in()
    move(s_out, s_in)
    print(s1, s2, s3, sep='\n')

dorisovka_s0(s1)
dorisovka_s0(s2)
dorisovka_s0(s3)
print('ВЫ ВЫИГРАЛИ', s1, s2, s3, sep='\n')
