# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# Способ 1:
# my_file = open("task01_1_W.txt", "w", encoding='utf-8')
# data_row = input("Введите данные строки:")
# for line in data_row:
#     # my_file.writelines(data_row + '\n')
#     my_file.write(data_row + '\n')
#     data_row = input('Введите строку и нажмите Enter (для выхода ничего не вводите и нажмите Enter):\n')
#     if not data_row:
#         break

# Способ 2:
with open('task01_1_W.txt', 'w+', encoding='utf-8') as my_file:
    while True:
        data_row = input('Введите строку и нажмите Enter (для выхода ничего не вводите и нажмите Enter):\n')
        if data_row:
            my_file.write(data_row + '\n')
        else:
            break
my_file.close()

my_file = open("task01_1_W.txt", "r", encoding='utf-8')
print(my_file.read()) # Вывод файла на печать для контроля
my_file.close()
