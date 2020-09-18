# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные.
# При этом английские числительные должны
# заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('task03_1.txt', 'r', encoding='utf-8') as my_file:
    dic = {}
    for lines in my_file:
        strings = lines.split(' ')  # Разбить lines на 2 подстроки
        key = strings[0]
        value = float(strings[1])
        dic[key] = value  # Добавить пару key:value к словарю dic
    # print("dic =", dic)  # Вывод словаря для контроля
# my_file.close()
surnames = {key: value for key, value in dic.items() if value < 20000.0}
print("Средний оклад всех сотрудников, руб.: %.2f" % (sum(dic.values()) / len(dic)))
print(f"Сотрудники с доходом < 20 тыс. руб.: {', '.join(surnames)}")
print("Средний оклад этих сотрудников, руб.: %.2f" % (sum(surnames.values()) / len(surnames)))

with open("task03_2.txt", "r") as my_file2:
    dic_eng_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    strings_rus = []
    for line in my_file2:
        line = line.rstrip('\n')
        strings = line.split(' - ')
        strings_rus.append(str(dic_eng_rus.get(str(strings[0]))) + " - " + strings[1])

with open("task03_3_W.txt", "w", encoding='utf-8') as my_file3:
    for i in strings_rus:
        my_file3.write("%s\n" % i)

my_file_res = open("task03_3_W.txt", "r", encoding='utf-8')
print()
print(my_file_res.read()) # Вывод файла на печать для контроля
my_file_res.close()
