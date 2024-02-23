class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('numberOfFloors:', self.numberOfFloors)


house_1 = House()
house_1.setNewNumberOfFloors(25)
