# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

# class DivZero(Exception):
#     def __init__(self, divider):
#         self.divider = divider
#
#     def __str__(self):
#         return f"Нельзя делить на {self.divider}"
#
#
# divisible = int(input("Введите делимое: "))
# divider = int(input("Введите делитель: "))
# try:
#     if divider == 0:
#         raise DivZero(divider)
# except DivZero as exception:
#     print(exception)
# else:
#     result = divisible / divider
#     print("Результат деления:", "%.1f" % result)
#
class DivZero(Exception):
    def __init__(self, text):
        self.text = text


divisible = int(input("Введите делимое: "))
divider = int(input("Введите делитель: "))
try:
    if divider == 0:
        raise DivZero(f"Нельзя делить на {divider}")
except DivZero as exception:
    print(exception)
else:
    result = divisible / divider
    print("Результат деления:", "%.1f" % result)
