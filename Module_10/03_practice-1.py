import random
import time
from collections import defaultdict
from threading import Thread, Lock

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        for worm in range(self.worms):
            time.sleep(0.01)
            fish = random.choice(FISH)
            if fish is not None:
                self.catch[fish] += 1


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 6)
        print(f'Функция {func.__name__} работала {elapsed} секунд(ы)', )
        return result

    return surrogate


@time_track
def run_in_one_thread(fishers):
    for fisher in fishers:
        fisher.run()


@time_track
def run_in_threads(fishers):
    for fisher in fishers:
        fisher.start()
    for fisher in fishers:
        fisher.join()


humans = ['Васек', 'Колян', 'Петрович', 'Хмурый', 'Клава', ]
fishers = [Fisher(name=name, worms=100) for name in humans]

run_in_one_thread(fishers=fishers)
run_in_threads(fishers=fishers)
