class Vehicle:

    def __init__(self, vehicle_type='none', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vehicle_type = vehicle_type

    def __str__(self):
        return 'Тип транспорта: {}.'.format(self.vehicle_type)


class Car:

    def __init__(self, price=1_000_000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = price
        self.horse_powers = 125
        self.cnt_turbo = 0

    def turbo(self):
        self.cnt_turbo += 1
        if self.cnt_turbo < 4:
            self.price += 1_000_000
            self.horse_powers += 125
            print('Тачка на прокачку!!!')
        else:
            print('Ваш автомобиль уже очень крут! Остановись!')

    def __str__(self):
        return 'Цена автомобиля {} {} - {} руб., количество лошадиных сил {}\n'.format(
            self.__class__.__name__, self.name, self.price, self.horse_powers)


class Nissan(Vehicle, Car):

    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return super().__str__() + ' ' + Car.__str__(self)

    def __del__(self):
        print('{} {} {} разбился и больше не существует :(\n'.format(
            self.vehicle_type, self.__class__.__name__, self.name))


almera = Nissan(name='Almera', price=1_250_000, vehicle_type='Автомобиль')
print(almera.vehicle_type, almera.price)

print(almera)
almera.turbo()
print(almera)
almera.turbo()
print(almera)
almera.turbo()
print(almera)
almera.turbo()
print(almera)
almera.turbo()
print(almera)
almera.turbo()
print(almera)

del almera

fugo = Nissan(name='Fugo', vehicle_type='Автомобиль бизнес класса', price=5_000_000)
fugo.horse_powers = 350
print(fugo)
fugo.turbo()
print(fugo)
