my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['Masha'])
print('Not existing value:', my_dict.get('Nikita'))
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print('Deleted value:', my_dict.pop('Egor'))
print('Modified dictionary:', my_dict)
print()

my_set = {1, 'Яблоко', 42.314, 42.314, 1, 'Яблоко'}
print('Set:', my_set)
my_set.update((13, (5, 6, 1.6)))
my_set.remove(1)
print('Modified set:', my_set)

'''
Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
Existing value: 2002
Not existing value: None
Deleted value: 1999
Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}

Set: {1, 'Яблоко', 42.314}
Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}
'''