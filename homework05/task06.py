# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open('task06_1.txt', 'r', encoding='utf-8') as my_file:
    dic_profit = {}
    dic_average_profit = {}
    dic_loss_profit = {}
    list_dic = []
    profit_list = []
    for line in my_file:
        line = line.rstrip('\n')
        strings = line.split()  # Делим строку на подстроки по пробелам (список подстрок: [фирма, форма, выручка, издержки])
        profit = int(strings[2]) - int(strings[3])  # Значение прибыли = выручка - издержки
        profit_list.append(profit)  # Наполняем список прибылей
        if profit > 0:
            dic_profit[strings[0]] = profit  # Добавление пары key:value к словарю прибылей
        elif profit < 0:
            dic_loss_profit[strings[0]] = profit  # Добавление пары key:value к словарю убытков
if bool(dic_profit) == True:
    list_dic.append(dic_profit)
    dic_average_profit["average_profit"] = sum(dic_profit.values()) / len(dic_profit) # Среднее только для прибыльных фирм
if bool(dic_average_profit) == True:
    list_dic.append(dic_average_profit)
if bool(dic_loss_profit) == True:
    list_dic.append(dic_loss_profit)

print(f"Фирмы в прибыли: {dic_profit}")
print(f"Средняя прибыль: {dic_average_profit}")
print(f"Фирмы в убытке: {dic_loss_profit}")

with open('task06_02_W.json', "w") as my_file_write:
    json.dump(list_dic, my_file_write)

my_file_res = open("task06_02_W.json", "r", encoding='utf-8')
print()
print(my_file_res.read())  # Вывод файла на печать для контроля
my_file_res.close()
