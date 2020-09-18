# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# path = 'C:/Users/Irina/PycharmProjects/geek-python-09-20/homework05/task02_1.txt'
path = 'task02_1.txt'
my_file = open(path, "rt", encoding='utf-8')
num_words = 0
num_lines = 0
for line in my_file:
    num_words += len(line.split())
    num_lines += 1
my_file.seek(0)
print(my_file.read()) # Вывод файла на печать для контроля
print(f"\nКоличество строк: {num_lines}")
print(f"Количество слов: {num_words}")
my_file.close()
