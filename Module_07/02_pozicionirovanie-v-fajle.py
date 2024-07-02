def custom_write(file_name, strings):
    strings_positions = {}
    with (open(file_name, 'w', encoding='utf-8') as output):
        for i, el in zip(range(1, len(strings) + 1), strings):
            strings_positions[(i, output.tell())] = el
            output.write(el + '\n')
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
