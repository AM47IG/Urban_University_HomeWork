#  Фабрика функций:
def create_operation(operation):
    if operation == 'add':
        def add(x, y):
            return x + y

        return add
    elif operation == 'subtract':
        def subtract(x, y):
            return x - y

        return subtract
    elif operation == 'multiplication':
        def multiplication(x, y):
            return x * y

        return multiplication
    elif operation == 'division':
        def division(x, y):
            return x / y

        return division


my_number_x = [1, 4, 7, 67, 101, 489, 1000, 0, -45, 24.31]
my_number_y = [2, 3, 4, 5, 1, 0, 2.05, 100, 50, 25]
my_func_mult = create_operation('multiplication')
my_func_div = create_operation('division')
result_mult = map(my_func_mult, my_number_x, my_number_y)
result_div = map(my_func_div, my_number_x, filter(lambda y: y != 0, my_number_y))
print('Умножение:', list(result_mult))
print('Деление:', list(result_div))


#  Лямбда функции с аналогом через def
result_sq = map(lambda x: x ** 2, my_number_x)
print('Квадратная степень (лямбда):', list(result_sq))


def square_def(x):
    return x ** 2


print('Квадратная степень (деф):', list(map(square_def, my_number_y)))


#  Вызываемый объект
class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


calculate_square = Rect(25, 4)
result_sq2 = calculate_square()
print('Посчитали площадь:', result_sq2)
