from random import randint
from colorama import Fore, Back, Style


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}.'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print(Fore.YELLOW + '{} поел'.format(self.name), Style.RESET_ALL)
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print(Fore.RED + '{} сходил на работу'.format(self.name), Style.RESET_ALL)
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        print(Fore.GREEN + '{} смотрел MTV целый день'.format(self.name), Style.RESET_ALL)
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print(Fore.MAGENTA + '{} сходил в магазин за едой'.format(self.name), Style.RESET_ALL)
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги закончились'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def go_into_house(self, house):
        self.house = house
        print(Fore.GREEN + '{} заехал в дом'.format(self.name), Style.RESET_ALL)
        self.fullness -= 10


class House:

    def __init__(self, name):
        self.food = 10
        self.money = 50
        self.name = name

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}.'.format(self.food, self.money)


citizens = [
    Man('Бивис'),
    Man('Батхэд'),
    Man('Кенни')
]

my_sweet_home = House('Мой милый дом')
for citizen in citizens:
    citizen.go_into_house(my_sweet_home)

for day in range(1, 366):
    print('\n', Back.LIGHTBLACK_EX + Fore.BLUE + '============ День {} ============'.format(day), Style.RESET_ALL)
    for citizen in citizens:
        citizen.act()
    print(Fore.BLUE + '-------- в конце дня ------------', Style.RESET_ALL)
    for citizen in citizens:
        print(citizen)
    print(my_sweet_home)
