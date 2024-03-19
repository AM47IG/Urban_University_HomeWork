class InvalidDataException(Exception):

    def __init__(self, input_data=None):
        self.message = 'Не хочу делить на 45'
        self.input_data = input_data

    def __str__(self):
        return f'{self.message}, вот что Вы ввели {self.input_data}...'


class ProcessingException(Exception):

    def __init__(self, input_data=None):
        self.message = 'Тот кого нельзя называть'
        self.input_data = input_data

    def __str__(self):
        return f'{self.message} есть в тексте "{self.input_data}"...'


def to_divide(a, b):
    if b == 45:
        raise InvalidDataException(input_data=dict(a=a, b=b))
    return a / b


def check_volan(text):
    if 'волан' in text.lower():
        raise ProcessingException(input_data=text)


# to_divide(5, 45)  # Прекращает код с ошибкой
list1 = [[90, 45], [90, 15], [15, 45]]
for ls in list1:
    try:
        res = to_divide(*ls)
    except InvalidDataException as exc:
        print(f'Внимание: {exc}')
    else:
        print('Поделили! Ответ:', res)
    finally:
        print('И чему мы научились?')


try:
    harry_speak = 'Это Волан-де-Морт!'
    print(check_volan(harry_speak))
except ProcessingException:
    print('Он испытывает судьбу, дальше без нас!')
    raise
finally:
    print('Это конец!')

print('Проверка выполняется ли код дальше')
