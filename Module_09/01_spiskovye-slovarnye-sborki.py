def square(n):
    return n ** 2


def is_odd(n):
    return n % 2 == 1


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
result = list(filter(is_odd, map(square, numbers)))
print(result)

