def password(n=None):
    if not n:
        n = int(input('Введите число от 3 до 20: '))
    result = ''
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n):
            cur = n % (i + j)
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


print('Пароль:', password())


def test_():
    str_ = """
    3 - 12
    4 - 13
    5 - 1423
    6 - 121524
    7 - 162534
    8 - 13172635
    9 - 1218273645
    10 - 141923283746
    11 - 11029384756
    12 - 12131511124210394857
    13 - 112211310495867
    14 - 1611325212343114105968
    15 - 1214114232133124115106978
    16 - 1317115262143531341251161079
    17 - 11621531441351261171089
    18 - 12151811724272163631545414513612711810
    19 - 118217316415514613712811910
    20 - 13141911923282183731746416515614713812911
    """

    list_ = [el for el in str_.split() if el not in '-']
    dict_ = {int(k): v for k, v in zip(list_[0::2], list_[1::2])}
    for k in dict_:
        assert password(k) == dict_[k], f'{password(k)} != {dict_[k]}'


test_()
