class Car:
    price = 1000000

    def horse_powers(self):
        return 250

    def __str__(self):
        return 'Стоимость {} - {} и количество лошадинных сил {}'.format(
            self.__class__.__name__, self.price, self.horse_powers()
        )


class Nissan(Car):
    price = 500000

    def horse_powers(self):
        return 120


class Kia(Car):
    price = 850000

    def horse_powers(self):
        return 115


car = Car()
note = Nissan()
rio = Kia()

print(car)
print(note)
print(rio)
