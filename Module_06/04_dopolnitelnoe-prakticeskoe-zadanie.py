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
        self.__height = self.get_sides()

    def get_square(self):
        pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_sides(self, *sides):
        super().set_sides(*sides * 12)

    def get_volume(self):
        return self.get_sides()[0]**3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
