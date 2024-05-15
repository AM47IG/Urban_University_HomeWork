immutable_var = (True, 'Cat', 156, 2)  # Создал кортеж
print('Immutable tuple: ', immutable_var)  # Вывел кортеж
# immutable_var[1] = 'Dog'  #  Данная операция вызовет ошибку, так как кортеж является неизменяемым объектом
mutable_list = [True, 'Bird', 852, -56]  # Создал список
print('Mutable list: ', mutable_list)  # Вывел список
mutable_list[0] = False  # Изменил элемент в списке
mutable_list[1] = 'Airbus'  # Изменил элемент в списке
mutable_list[3] = 37  # Изменил элемент в списке
mutable_list.append('Car')  # Добавил элемент в список
mutable_list.remove(852)  # Удалил элемент из списка
print('Modified mutable list: ', mutable_list)  # Вывел измененный список
