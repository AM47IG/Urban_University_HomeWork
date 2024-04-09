import random
from collections import defaultdict
from threading import Thread, Lock

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):

    def __init__(self, name, worms, fish_tank, lock, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catched = 0
        self.fish_tank = fish_tank
        self.fish_tank_lock = lock

    def run(self):
        for worm in range(self.worms):
            fish = random.choice(FISH)
            if fish is not None:
                with self.fish_tank_lock:
                    self.fish_tank[fish] += 1
                self.catched += 1


global_fish_tank = defaultdict(int)

humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
lock = Lock()
fishers = [Fisher(name=name, worms=100000, fish_tank=global_fish_tank, lock=lock) for name in humans]

for fisher in fishers:
    fisher.start()
for fisher in fishers:
    fisher.join()

total_fish_from_fishers = sum(fisher.catched for fisher in fishers)
total_fish_in_tank = sum(global_fish_tank.values())

print(f'Итого рыбаки поймали {total_fish_from_fishers} шт., а с берега увидели {total_fish_in_tank} шт.')
