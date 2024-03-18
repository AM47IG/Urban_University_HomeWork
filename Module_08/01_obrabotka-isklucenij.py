def string_to_int(s):  # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f'"{s}" невозможно преобразовать в целое число!'


def read_file(filename):  # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'Файл {filename} не найден!'
    except IOError as exp:
        return f'Ошибка {exp}. Невозможно открыть файл {filename}'


def divide_numbers(a, b):  # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError:
        return f'На ноль делить нельзя!'
    except TypeError:
        return f'Не числа делить нельзя!'


def access_list_element(lst, index):  # добавить обработку IndexError, TypeError
    try:
        return 10 / lst[index]
    except IndexError:
        return f'Нет элемента под индексом {index} в списке {lst}'
    except TypeError:
        return f'10 невозможно поделить на "{lst[index]}"!'


with open('probe.txt', 'w') as file:
    file.write(input('Введи что-нибудь: '))

n = read_file('probe.txt')
print(n)

n = string_to_int(n)
print(n)

list_for_divide = [5, n]
divide = divide_numbers(*list_for_divide)
print(divide)


print(access_list_element(list_for_divide, 1))
