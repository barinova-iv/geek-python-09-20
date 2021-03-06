# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods_dict = []
goods_list = []
list_goods_name = []
list_goods_price = []
list_goods_quantity = []
list_goods_unit = []
goods_tuple = ()
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед.': []}
num_goods = int(input("Введите количество товаров: "))
n = 1
while n <= num_goods:
    print(f"Данные товара {n}")
    goods_dict = dict({'Название': input("Введите название: "),
                       'Цена': int(input("Введите цену: ")),
                       'Количество': int(input('Введите количество: ')),
                       'Ед.': input("Введите единицу измерения: ")})
    goods_list.append((n, goods_dict))
    n += 1
    list_goods_name.append(goods_dict.get('Название'))
    list_goods_price.append(goods_dict.get('Цена'))
    list_goods_quantity.append(goods_dict.get('Количество'))
    list_goods_unit.append(goods_dict.get('Ед.'))
print()
goods_tuple = tuple(goods_list)
print("Структура данных 'Товары':")
for ind, el in enumerate(goods_tuple):
    print(el)
print()
print("Аналитика о товарах:")
analytics['Название'] = list(set(list_goods_name))
analytics['Цена'] = list(set(list_goods_price))
analytics['Количество'] = list(set(list_goods_quantity))
analytics['Ед.'] = list(set(list_goods_unit))
print(analytics)
