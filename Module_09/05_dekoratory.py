def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 1:
            flag = 'Ненатуральное'
        elif result == 1:
            flag = 'Интересное'
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    flag = 'Составное'
                    break
            else:
                flag = 'Простое'
        print(flag)
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
