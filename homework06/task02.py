# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_asphalt(self, weight=25, thickness=5):
        return (self._length * self._width * weight * thickness) / 1000


a = Road(20, 5000)
print(f"Вызов метода с параметрами по умолчанию:\nМасса асфальта = {round(a.weight_asphalt())} т")
print(f"Вызов метода с передачей параметров (масса на 1 кв.м = 25, толщина = 15):\nМасса асфальта = {round(a.weight_asphalt(30,6))} т")
