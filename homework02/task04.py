# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

list_ex = input("Введите строку из нескольких слов, разделенных пробелами: ")
list_ex = list(map(str, list_ex.split()))
for ind, el in enumerate(list_ex):
    print(ind + 1, el[0:10])

# for ind, el in enumerate(list_ex):
#     if len(el) <= 10:
#         print(ind + 1, el)
#     else:
#         print(ind + 1, el[0:10])
