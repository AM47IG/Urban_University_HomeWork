import warnings


def to_divide(a, b):
    try:
        if b < 0.01:
            warnings.warn('ОСТОРОЖНО!!! Делитель близок к нулю!')
    except UserWarning as err:
        print(f'Предупреждение было перехвачено как ошибка "{err}"')
    else:
        return a / b


my_list = ['error', 'ignore', 'default', ]
for el in my_list:
    warnings.simplefilter(el, UserWarning)
    print(to_divide(2, 0.004))
    print()
