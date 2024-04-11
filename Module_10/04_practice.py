import time
from collections import defaultdict

import queue
import random
import threading

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(threading.Thread):

    def __init__(self, name, worms, cather, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.cather = cather

    def run(self):
        for worm in range(self.worms):
            print(f'{self.name}, {worm}: забросили ждем...', flush=True)
            time.sleep(random.randint(10, 20) / 10)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}, {worm}: сожрали червяка!', flush=True)
            else:
                print(f'{self.name}, {worm}: поймал {fish} и хочет положить его в садок', flush=True)
                if self.cather.full():
                    print(f'{self.name}, {worm}: у приемщика заняты руки!!!', flush=True)
                self.cather.put(fish)
                print(f'{self.name}, {worm}: наконец-то отдал {fish} приёмщику', flush=True)


class Boat(threading.Thread):

    def __init__(self, worms_per_fisher=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fishers = []
        self.worms_per_fisher = worms_per_fisher
        self.cather = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self, name):
        fisher = Fisher(name=name, worms=self.worms_per_fisher, cather=self.cather)
        self.fishers.append(fisher)

    def run(self):
        print('Лодка вышла в море...', flush=True)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                fish = self.cather.get(timeout=1)
                print(f'Приемщик принял {fish} и положил в садок', flush=True)
                self.fish_tank[fish] += 1
            except queue.Empty:
                print('Приемщик свободен в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)


boat = Boat(worms_per_fisher=10)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
for name in humans:
    boat.add_fisher(name=name)

boat.start()
boat.join()
