from threading import Thread
import time
from random import randint


class Knight(Thread):

    def __init__(self, name, skill):
        super().__init__()
        self.name = name
        self.skill = skill
        self.enemy = randint(50, 400)
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напало {self.enemy} воинов!', flush=True)
        while self.enemy > 0:
            time.sleep(1)
            self.day += 1
            if self.enemy >= self.skill:
                self.enemy -= self.skill
            else:
                self.enemy -= self.enemy
            print(f'{self.name}, сражается {self.day} день(дня)..., осталось {self.enemy} воинов.', flush=True)
        else:
            print(f'{self.name} одержал победу спустя {self.day} дней!', flush=True)


knight1 = Knight(name="Sir Lancelot", skill=10)
knight2 = Knight(name="Sir Galahad", skill=40)

knight1.start()
time.sleep(0.001)
knight2.start()

knight1.join()
knight2.join()
