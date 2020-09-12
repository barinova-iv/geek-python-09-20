# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    sum_max = sum([arg_1, arg_2, arg_3]) - min([arg_1, arg_2, arg_3])
    return sum_max


try:
    arg_1 = int(input("Введите значение 1-го аргумента: "))
    arg_2 = int(input("Введите значение 2-го аргумента: "))
    arg_3 = int(input("Введите значение 3-го аргумента: "))
except ValueError:
    print("Ошибка. Введено не число")
    exit()

print(f"Сумма 2-х максимальных аргументов = {my_func(arg_1, arg_2, arg_3)}")
