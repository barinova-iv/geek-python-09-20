# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:

    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def extract_number(cls, date_str):
        return [int(item) for item in date_str.split("-")]

    @staticmethod
    def date_validation(date_str):
        dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        date_list = Data.extract_number(date_str)
        if not 1 <= date_list[1] <= 12:
            return False
        elif not 1 <= date_list[0] <= dict[date_list[1]]:
            return False
        elif not 0 < date_list[2] <= 9999:
            return False
        else:
            return True

    def __str__(self):
        if Data.date_validation(self.date_str) == True:
            date_list = self.date_str.split("-")
            if int(date_list[0]) < 10:
                date_list[0] = '0' + date_list[0]
            if int(date_list[1]) < 10:
                date_list[1] = '0' + date_list[1]
            return '.'.join(date_list)
        else:
            return f"Некорректная дата"


# Корректная дата 1
s1 = '23-2-2020'
print(f"Исходная дата: {s1}")
print(f"Преобразованная дата: {Data(s1)}")  # Использование статического метода в методе __str__
if Data.date_validation(s1) == True:
    print(f"Список чисел (если дата - корректная): {Data.extract_number(s1)}")

# НЕкорректная дата 2
print()
s2 = '31-2-2020'
print(f"Исходная дата: {s2}")
print(f"Преобразованная дата: {Data(s2)}")  # Использование статического метода в методе __str__
if Data.date_validation(s2) == True:
    print(f"Список чисел (если дата - корректная): {Data.extract_number(s2)}")

# НЕкорректная дата 3
print()
s3 = '11-13-2020'
print(f"Исходная дата: {s3}")
print(f"Преобразованная дата: {Data(s3)}")  # Использование статического метода в методе __str__
if Data.date_validation(s3) == True:
    print(f"Список чисел (если дата - корректная): {Data.extract_number(s3)}")

# НЕкорректная дата 4
print()
s3 = '01-1-20201'
print(f"Исходная дата: {s3}")
print(f"Преобразованная дата: {Data(s3)}")  # Использование статического метода в методе __str__
if Data.date_validation(s3) == True:
    print(f"Список чисел (если дата - корректная): {Data.extract_number(s3)}")
