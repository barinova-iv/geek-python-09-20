# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора ** ;
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Способ 1
def my_func1(x, y):
    try:
        res = x ** y
        print(f"Возведение в степень с помощью оператора **: {res}")
    except ZeroDivisionError:
        print("С помощью оператора **: Ошибка. Ноль нельзя возвести в отрицательную степень")


# Способ 2
def my_func2(x, y):
    try:
        res = 1
        for i in range(abs(y)):
            res *= x
        if y < 0:
            res = 1 / res
        print(f"Возведение в степень с помощью цикла: {res}")
    except ZeroDivisionError:
        print("С помощью цикла: Ошибка. Ноль нельзя возвести в отрицательную степень")


try:
    x = int(input("Введите положительное целое число: "))
    y = int(input("Введите отрицательное целое число: "))
except ValueError:
    print("Ошибка. Введено не число")
    exit()

my_func1(x, y)
my_func2(x, y)
