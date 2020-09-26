# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, *lists_of_lists):
        self.lists_of_lists = [*lists_of_lists[0]]

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.lists_of_lists)

    def __add__(self, ex2):
        result = [[ex2.lists_of_lists[i][j] + self.lists_of_lists[i][j] for j in range(len(self.lists_of_lists[0]))]
                  for i in range(len(self.lists_of_lists))]

        return result


matrix1 = Matrix([[2, 2, 2], [2, 2, 3], [1, 2, 3]])
matrix2 = Matrix([[2, 2, 2], [2, 2, 3], [1, 2, 3]])

# # Ввод данных пользователем:
# matrix1 = Matrix([list(map(int, input("Введите строку из 3-х значений через пробел для 1-ой матрицы 3х3: ").split())) for i in range(3)])
# matrix2 = Matrix([list(map(int, input("Введите строку из 3-х значений через пробел для 2-ой матрицы 3х3: ").split())) for i in range(3)])

print(matrix1)
print('----------')
print(matrix2)
print('----------')
print(Matrix(matrix1 + matrix2))
