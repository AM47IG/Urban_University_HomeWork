from pprint import pp

file_name = 'my_soul_is_dark.txt'
file = open(file_name, mode='r', encoding='utf8')
file_content = file.read()
pp(file_content)
file.close()  # Порядок действий как в задании :)
