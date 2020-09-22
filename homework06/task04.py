# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction)
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Автомобиль {self.name} ({self.color}) поехал"

    def stop(self):
        return f"Автомобиль {self.name} ({self.color}) остановился"

    def turn(self, direction):
        return f"{direction}"

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"превышение скорости"
        else:
            return f"скорость {self.speed} км/ч"


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"превышение скорости"
        else:
            return f"cкорость {self.speed} км/ч"


class PoliceCar(Car):
    pass


ex_TownCar = TownCar(78, "бел.", "Ford", False)
ex_SportCar = SportCar(130, "красн.", "Audi", False)
ex_WorkCar = WorkCar(0, "желт.", "Газель", False)
ex_PoliceCar = PoliceCar(120, "бел.", "Лада", True)
print(f"{ex_WorkCar.stop()}, {ex_WorkCar.show_speed()}")
print(f"{ex_TownCar.go()} {ex_TownCar.turn('налево')}, {ex_TownCar.show_speed()}")
print(f"{ex_SportCar.go()} {ex_SportCar.turn('прямо')}, скорость {ex_SportCar.show_speed()} км/ч")
if ex_PoliceCar.is_police == True:
    print(f"Полицейский {ex_PoliceCar.go()} {ex_PoliceCar.turn('прямо')}, скорость {ex_PoliceCar.show_speed()} км/ч")
