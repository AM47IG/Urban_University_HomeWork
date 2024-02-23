class Building:

    def __init__(self, numberOfFloors=9, buildingType='panel'):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


tolbukhina_29 = Building()
lenina_13 = Building()
kosmonavtov_55 = Building(9, 'brick')
rosi_luxembourg_16 = Building(9, 'brick')

addresses = (tolbukhina_29, lenina_13, kosmonavtov_55, rosi_luxembourg_16)  # Список "соседних" зданий.

for i in range(len(addresses) - 1):  # Цикл для сравнения "соседних" зданий.
    if addresses[i] == addresses[i + 1]:
        print('Здания одинаковые')
    else:
        print('Здания разные')
