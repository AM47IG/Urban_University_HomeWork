from random import randint
from colorama import Fore, Back, Style

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'Я - {}, сытость {}, еды осталось {}, денег осталось {}.\n'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            print(Fore.YELLOW + '{} поел'.format(self.name), Style.RESET_ALL)
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print(Fore.RED + '{} сходил на работу'.format(self.name), Style.RESET_ALL)
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        print(Fore.GREEN + '{} играл в доту целый день'.format(self.name), Style.RESET_ALL)
        self.fullness -= 10

    def shopping(self):
        if self.money >= 50:
            print(Fore.MAGENTA + '{} сходил в магазин за едой'.format(self.name), Style.RESET_ALL)
            self.money -= 50
            self.food += 50
        else:
            print('{} деньги закончились'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.food <= 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()


man = Man(name='Гоша')
for day in range(1, 21):
    print(Back.LIGHTBLACK_EX + Fore.BLUE + '============ День {} ============'.format(day), Style.RESET_ALL)
    man.act()
    print(man)
