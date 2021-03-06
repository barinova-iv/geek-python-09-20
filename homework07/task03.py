# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell():
    cell_of_cell: int

    def __init__(self, cells: int):
        self.cell_of_cell = cells

    def __str__(self):
        return str(self.cell_of_cell)

    def __add__(self, other):
        return self.cell_of_cell + other.cell_of_cell

    def __sub__(self, other):
        res = self.cell_of_cell - other.cell_of_cell
        if res >= 0:
            return res
        else:
            return f"ячеек не может быть меньше нуля"

    def __mul__(self, other):
        return self.cell_of_cell * other.cell_of_cell

    def __truediv__(self, other):
        try:
            res = round(self.cell_of_cell / other.cell_of_cell)
        except ZeroDivisionError:
            res = f"ошибка, деление на 0"
        return res

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.cell_of_cell / cells_in_row)):
            row += f'{"*" * cells_in_row}\n'
        row += f'{"*" * (self.cell_of_cell % cells_in_row)}'
        return row


cells1 = Cell(int(input("Введите кол-во ячеек 1-ой орг.клетки: ")))
cells2 = Cell(int(input("Введите кол-во ячеек 2-ой орг.клетки: ")))
print(f"Результат сложения: {Cell(cells1 + cells2)}")
print(f"Результат вычитания: {Cell(cells1 - cells2)}")
print(f"Результат умножения: {Cell(cells1 * cells2)}")
print(f"Результат деления (целочисленного): {Cell(cells1 / cells2)}")

print(cells1.make_order(int(input("\nВведите кол-во ячеек в ряду (для 1-ой орг.клетки): "))))
