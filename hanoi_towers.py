def dorisovka_s0(s1, s2, s3):
    sd1 = list(s1)
    sd2 = list(s2)
    sd3 = list(s3)
    while len(sd1) < 3:
        sd1.append(s0)
    while len(sd2) < 3:
        sd2.append(s0)
    while len(sd3) < 3:
        sd3.append(s0)
    sp3 = (sd1[0], sd2[0], sd3[0])
    sp2 = (sd1[1], sd2[1], sd3[1])
    sp1 = (sd1[2], sd2[2], sd3[2])
    print(sp1, sp2, sp3, sep='\n')
    


def move(s_out, s_in):
    if not s_out:
    	print('Нечего перекладывать!')
    elif not s_in:
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
        n = input('Откуда берем блок? ')
    if n == '1':
        n = s1
    elif n == '2':
        n = s2
    elif n == '3':
        n = s3
    return n


def number_is_s_in():
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


s0 = '  |  '
b1 = '  _  '
b2 = ' ___ '
b3 = '_____'

s1 = [b3, b2, b1]
s2 = []
s3 = []
dorisovka_s0(s1, s2, s3)
while not s3 == [b3, b2, b1]:
    s_out = number_is_s_out()
    s_in = number_is_s_in()
    move(s_out, s_in)
    dorisovka_s0(s1, s2, s3)

print('ВЫ ВЫИГРАЛИ')
