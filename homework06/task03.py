# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname,position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._init_income(wage, bonus)

    def _init_income(self, wage, bonus):
        self._income = {'оклад': wage, 'премия': bonus}


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income['оклад'] + self._income['премия']

    def info(self):
        print(f"Атрибуты экземпляра класса Position: {self.name}, {self.surname}, {self.position}, {self._income}")
        print(f"Полное имя: {self.get_full_name()}")
        print(f"Доход: {str(self.get_total_income())}\n")


a = Position("Иван", "Иванов", "менеджер", 25000, 9000)
b = Position("Сергей", "Петров", "руководитель отдела", 45000, 12000)
a.info()
b.info()
