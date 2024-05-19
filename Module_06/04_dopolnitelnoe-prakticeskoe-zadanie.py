# При создании объектов использую те же методы, что и необходимы для изменения свойств фигур. Считаю, что так меньше
# проверок создавать нужно, ведь мне не надо проверять разными способами одни и те же параметры при создании,
# а потом при использовании методов.

import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filed=False):
        self.__color = [0, 0, 0]
        self.__sides = [1] * self.sides_count
        self.set_color(*color)
        self.set_sides(*sides)
        self.filed = filed

    @staticmethod
    def __is_valid_color(r, g, b):
        for c in (r, g, b):
            if not 0 <= c <= 255:
                return False
        return True

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            if all([isinstance(i, int) for i in sides]):
                if all([i > 0 for i in sides]):
                    return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        sides = list(sides)
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__radius = self.get_sides()[0]*2/(4*math.pi)

    def get_square(self):
        return math.pi * self.__radius * 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        self.square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        self.__height = a * b / c

    def get_square(self, round_=3):
        return round(self.square, round_)


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_sides(self, *sides):  # Переопределяю set_sides, вместо __sides, что бы не повторять проверки из Figure.
        super().set_sides(*sides * 12)

    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((154, 167, 489), 4, 6, 8)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print('Цвет круга:', circle1.get_color())
print('Цвет куба:', cube1.get_color())
print('Цвет треугольника:', triangle1.get_color())  # [0, 0, 0], потому что при создании некорректные параметры

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
triangle1.set_sides(2, 2, 2, 2)  # Не изменится
print('Стороны куба:', cube1.get_sides())
print('Стороны круга:', circle1.get_sides())
print('Стороны треугольника:', triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print('Периметр круга:', len(circle1))
print('Периметр треугольника:', len(triangle1))

# Проверка объёма (куба):
print('Объем куба:', cube1.get_volume())

# Проверка площади (треугольника):
print('Площадь треугольника:', triangle1.get_square())
