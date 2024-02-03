def test(*args, **kwargs):
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus1 = factorial(n=n-1)
    return n * factorial_n_minus1


test(1, 594, 56.41, 'Hello world', True, name='Alexander', city='Irkutsk')

print(factorial(19))
