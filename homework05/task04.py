# Создать(программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами.Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

my_file = open("task04_1_W.txt", "w", encoding='utf-8')
numbers = input("Введите числа через пробел: ")
my_file.writelines(numbers)
numbers = numbers.split()
print(f"Сумма чисел в файле = {sum(map(int, numbers))}")
my_file.close()
