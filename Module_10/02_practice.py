import random
from collections import defaultdict
from threading import Thread

FISH = (None, 'плотва', 'окунь', 'лещ')


class Fisher(Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.worms = worms
        self.catch = defaultdict(int)

    def run(self):
        name = self.name
        for worm in range(self.worms):
            print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10 ** 4)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{name}: Тьфу, сожрали червяка...', flush=True)
            else:
                print(f'{name}: Ага, у меня {fish}', flush=True)
                self.catch[fish] += 1


vasya = Fisher(name='Вася', worms=10)
kolya = Fisher(name='Коля', worms=10)
print(f'{'Они пошли на рыбалку':-^50}')

vasya.start()
kolya.start()
print(f'{'Ждем пока они вернуться...':-^50}')

vasya.join()
kolya.join()
print(f'{'Итак, они вернулись':-^50}')

for fisher in (kolya, vasya):
    print(f'Итого рыбак {fisher.name} поймал:')
    for fish, count in fisher.catch.items():
        print(f'    {fish} - {count}')