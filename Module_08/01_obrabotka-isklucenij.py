def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f'"{s}" невозможно преобразовать в целое число!'


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    file = None
    try:
        file = open(filename, 'r')
        s = file.readline()
        return s
    except FileNotFoundError as exc:
        return f'Файл {filename} не найден! {exc.args}'
    except IOError as exс:
        return f'Ошибка {exс}. Невозможно открыть файл {filename}'
    except Exception as exc:
        return f'Произошла непредвиденная ошибка! {exc}'
    finally:
        if file is not None:
            file.close()


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return f'На ноль делить нельзя!'
    except TypeError:
        return f'Не числа делить нельзя!'


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'Нет элемента под индексом {index} в списке {lst}'
    except TypeError:
        return f'Индекс должен быть целыми числом!'


def assign_number(a):
    try:
        global numm
        return numm
    except NameError:
        print('Переменной "numm" не существует!')


print(string_to_int('r'))
print(string_to_int('9'))

print(read_file('probe.txt'))
print(read_file(34))
print(read_file(54.00))

print(divide_numbers(10, 0))
print(divide_numbers('10', 2))
print(divide_numbers(10, 2))

my_list = [5, 6]
print(access_list_element(my_list, 2))
print(access_list_element(my_list, '1'))
print(access_list_element(my_list, 1))

new_numm = assign_number(3)
print(new_numm)

# Исключения SyntaxError не ловятся
# try:
#     print('Это не распечатать!' 12 'раз')
# except SyntaxError:
#     print('Здесь мы пишем что не так. Ошибка - {exc} - {exc.args}')
