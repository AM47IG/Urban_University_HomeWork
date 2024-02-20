class House:
	
	
	def __init__(self, floors=10):
		self.floors = floors
		self.current_floor = 1
	
	
	def elevator_on_floor(self, need_a_floor):
	    print ('Ожидание лифта на этаже:', self.current_floor)
	    print ('Лифт прибыл')
	    while self.current_floor != need_a_floor:
	        print ('Этаж:', self.current_floor)
	        if self.current_floor > need_a_floor:
	            self.current_floor -= 1
	        if self.current_floor < need_a_floor:
	            self.current_floor += 1
	    print('Вы на этаже:', self.current_floor)
            print()

house_1 = House(int(input('Количество этажей:')))
while True:
    need_a_floor = int(input('Выберете этаж:'))
    if not 1 <= need_a_floor <= house_1.floors:
        break
    house_1.elevator_on_floor(need_a_floor)
