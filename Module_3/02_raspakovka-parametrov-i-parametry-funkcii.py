def print_params(a=9, b='девять', c=False):
    print(a)
    print(b)
    print(c)
    print()  # Для читабельности в консоли


def new_item_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


print_params(15, 'Hello, World!', True)
print_params(c=True, a=37, b='Привет, Мир!')
print_params(a=74, c=True)
print_params()
print_params(b=25)  # Параметры работают, но есть предупреждения о несовпадении типов данных
print_params(c=[1, 2, 3])  # Параметры работают, но есть предупреждения о несовпадении типов данных

for_print_params = [456, 'Pineapple']
new_item_to_list(item=True, my_list=for_print_params)
print(for_print_params)
print_params(*for_print_params)

my_dict = {'b': 'Lion', 'c': True, 'a': 246}
print(my_dict)
print_params(**my_dict)

values_list_2 = new_item_to_list(item=753)
new_item_to_list(item='BMW', my_list=values_list_2)
print(values_list_2)
print_params(*values_list_2, 42)
