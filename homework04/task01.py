# Реализовать скрипт, в котором должна быть предусмотрена функция расчета
# заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
from homework04 import task01_script

try:
    script, arg_hours, arg_rate, arg_bonus = argv
except ValueError:
    print("Ошибка. Аргументы не заданы")

print(f"Параметры argv: {argv}")
print(f"Зарплата сотрудника: {task01_script.salary(int(arg_hours), int(arg_rate), int(arg_bonus))} руб.")
