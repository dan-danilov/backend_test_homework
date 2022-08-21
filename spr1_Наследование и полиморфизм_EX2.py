# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos


class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км

    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(
            other.latitude
        ) * cos(self.longitude - other.longitude)
        dist = 6371 * acos(cos_d)
        print(dist)


class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        # допишите код: сохраните свойства родителя
        # и добавьте свойства name и population
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")


class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    # допишите код: напишите конструктор, в нём сохраните свойства родителя
    # и добавьте свойства name и height
    def show(self):
        print(f"Высота горы {self.name}, высота {self.height} м.")

    # Переопределите метод show(self):
    # информацию о горе нужно вывести в формате:
    # "Высота горы <название> - <высота> м."


Moscow = City(
    latitude=55.773010, longitude=37.617617, name="Москва", population="3 млн"
)
Everest = Mountain(
    latitude=27.988488, longitude=86.925822, name="Эверест", height="8000"
)
Moscow.show()
Everest.show()

Moscow.distance(Everest)
