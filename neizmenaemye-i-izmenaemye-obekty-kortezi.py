immutable_var = (True, 'Cat', 156, 2)
print('Immutable tuple: ', immutable_var)
# immutable_var[1] = 'Dog'  Данная операция вызовет ошибку,так как кортеж является неизменяемым объектом
mutable_list = [True, 'Bird', 852, -56]
print('Mutable list: ', mutable_list)
mutable_list[0] = False
mutable_list[1] = 'Airbus'
mutable_list[3] = 37
mutable_list.append('Car')
mutable_list.remove(852)
print('Modified mutable list: ', mutable_list)
