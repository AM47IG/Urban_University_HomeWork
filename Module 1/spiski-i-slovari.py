my_list = ['Hello', 'Goodbye', 'Fanks', 'Please', 'Good Night', 'Welcome', ]  # Создал список
print('List: ', my_list)  # Вывел список
print('First element: ', my_list[0])  # Вывел первый элемент списка
print('Last element: ', my_list[-1])  # Вывел последний элемент списка
print('Sublist', my_list[2:4])  # Вывел элементы списка с 3 по 5
my_list[2] = 'Thanks'  # Изменил элемент списка
print('Modified list: ', my_list)  # Вывел список с измененным элементом
print('')  # Просто пустая строка для разделения
my_dict = {'Hello': 'Привет', 'Goodbye': 'Досвидания', 'Thanks': 'Спасибо', 'Please': 'Пожалуйста',
           'Good Night': 'Спокойной ночи', 'Welcome': 'Добро Пожаловать', }  # Создал словарь
print('Dictionary: ', my_dict)  # Вывел словарь
print('Translation: ', my_dict['Thanks'])  # Вывел элемент словаря
my_dict['Goodbye'] = 'До свидания'  # Изменил элемент словаря
print('Modified dictionary: ', my_dict)  # Вывел словарь с измененным элементом
