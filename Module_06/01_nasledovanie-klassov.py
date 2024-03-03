class Car:

    def __init__(self, price=1_000_000):
        self.price = price

    def horse_powers(self):
        return 250

    def __str__(self):
        return 'Стоимость {} - {} и количество лошадиных сил {}'.format(
            self.__class__.__name__, self.price, self.horse_powers()
        )


class Nissan(Car):

    def horse_powers(self):
        return 120


class Kia(Car):

    def horse_powers(self):
        return 115


car = Car()
note = Nissan(1_100_000)
rio = Kia(2_000_000)

print(car)
print(note)
print(rio)
