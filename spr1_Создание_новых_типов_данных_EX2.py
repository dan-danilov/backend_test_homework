from cmath import pi


class Planet:
    def __init__(self, name, radius, temp_celsius):
        self.name = name
        self.surface_area = 4 * pi * radius**2
        self.average_temp_celcius = temp_celsius
        self.average_temp_fahrenheit = temp_celsius * 9 / 5 + 32

    def show_info(self):
        print(
            f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км."
        )
        print(
            f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту."
        )


venus = Planet("Venus", 10, 0)

venus.show_info(z)
