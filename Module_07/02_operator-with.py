file_name = 'my_soul_is_dark.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')

print(file.closed)
