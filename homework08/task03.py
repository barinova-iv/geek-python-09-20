# Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class TypeNotNum(Exception):
    def __init__(self, text):
        self.text = text


list_num = []

while True:
    try:
        val_str = input('Введите значения и нажимайте Enter (для выхода введите stop) - ')
        if not val_str.isdigit():
            if not val_str == 'stop':
                raise TypeNotNum(f"Введено не число")
        else:
            list_num.append(int(val_str))
    except TypeNotNum as exception:
        print(exception)
    if val_str == 'stop':
        print(f'Текущий список - {list_num} \n ')
        break
