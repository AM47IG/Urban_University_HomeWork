def calculate_structure_sum(*args):
    result = 0
    for el in args:
        if isinstance(el, int):
            result += el
        elif isinstance(el, str):
            result += len(el)
        elif isinstance(el, (tuple, list, set)):
            result += calculate_structure_sum(*el)
        elif isinstance(el, dict):
            result += calculate_structure_sum(*el.items())
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
result2 = calculate_structure_sum(*data_structure, data_structure, 10000, 'И даже так работает', None, True, False)
print(result2)
