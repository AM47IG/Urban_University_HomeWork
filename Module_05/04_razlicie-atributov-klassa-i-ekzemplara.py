from random import choice, randint


class Building:
    total, name = 0, ['tolbukhina_', 'lenina_', 'kosmonavtov_', 'rosy_luxembourg_', ]
    name_count = len(name)

    def __init__(self):
        Building.total += 1
        self.name = choice(Building.name) + str(randint(1, 100))

    def __str__(self):
        return 'Building:' + ' ' + self.name + '\n'


addresses = []
for _ in range(40):
    new_building = Building()
    addresses.append(new_building)

print('Number of buildings:', Building.total)
print(*addresses)
