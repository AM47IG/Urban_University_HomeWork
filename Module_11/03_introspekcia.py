import inspect
from pprint import pprint
from decimal import Decimal
from Module_05.practice import Man  # Класс из практики Модуля 5.


def introspection_info(obj):
    type_ = type(obj)
    attributes = dir(obj)
    methods = [el[0] for el in inspect.getmembers(obj, inspect.ismethod)]
    module = obj.__module__
    return {'type': type_, 'attributes': attributes, 'methods': methods, 'module': module}


citizen = Man('Alex')
citizen_info = introspection_info(citizen)
num = Decimal(42)
decimal_info = introspection_info(num)
print(f'{'Инфо об объекте citizen':-^100}')
pprint(citizen_info, compact=True, width=100, sort_dicts=False)
print('\n', f'{'Инфо об объекте decimal':-^100}', sep='')
pprint(decimal_info, compact=True, width=100, sort_dicts=False)