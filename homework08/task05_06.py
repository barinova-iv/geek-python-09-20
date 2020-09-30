# Задание 5
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Задание 6
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте
# «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from homework08 import task04


class TypeNotNum(Exception):
    def __init__(self, text):
        self.text = text


class Dep(task04.Warehouse):

    def __init__(self, name):
        self.count_in = {}
        self.name = name

    def __str__(self):
        return f'в подразделении "{self.name}": {self.count_in}'

    def move_to_dep(self, warehouse: task04.Warehouse, name, count):
        count_to_dep_new = {}
        try:
            if not type(count) == int:
                raise TypeNotNum(
                    f'Ошибка! Количество оргтехники "{name}", отправляемой в подразделение "{self.name}", не число')
            else:
                count_to_dep_new[name] = count
                if name in self.count_in:
                    self.count_in[name] += count
                    warehouse.count_in[name] -= count
                else:
                    self.count_in.update(count_to_dep_new)
                    warehouse.count_in[name] = warehouse.count_in[name] - count
        except TypeNotNum as exception:
            print(exception)


w1 = task04.Warehouse()
w1.accept_to_warehouse(task04.p1.type, task04.p1.quantity)  # Передача на склад экземпляра p1
w1.accept_to_warehouse(task04.p2.type, task04.p2.quantity)  # Передача на склад экземпляра p2
w1.accept_to_warehouse(task04.s1.type, task04.s1.quantity)  # Передача на склад экземпляра s1
w1.accept_to_warehouse(task04.c1.type, task04.c1.quantity)  # Передача на склад экземпляра c1
print('----------')
print(w1)
print('----------')
d1 = Dep('Отдел маркетинга')
d2 = Dep('Бухгалтерия')
d1.move_to_dep(w1, 'принтер', 4)  # Передача 4-х принтеров в подразделение d1 = Отдел маркетинга
d1.move_to_dep(w1, 'ксерокс', 2)  # Передача 2-х ксероксов в подразделение d1 = Отдел маркетинга
d2.move_to_dep(w1, 'принтер', 3)  # Передача 3-х принтеров в подразделение d2 = Бухгалтерия
d2.move_to_dep(w1, 'сканер', 1)  # Передача 1-го сканера в подразделение d2 = Бухгалтерия
print(d1)
print(d2)
print(f"осталось {w1}")  # Вывод остатка на складе
print('----------')
d2.move_to_dep(w1, 'ксерокс', 'один')  # Валидация кол-ва передаваемой оргтехники в подразделение d2 = Бухгалтерия
