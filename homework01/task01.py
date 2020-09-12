# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.
region_number = 78
region_name = "Санкт-Петербург"
print(region_number)
print(region_name)
name = str(input("Введите Ваше имя: "))
age = int(input("Введите Ваш возраст: "))
work = str(input("Кем Вы работаете? "))
experience = int(input("Стаж работы: "))
print(f"Привет, {name}! Тебе {age} лет.")
print(f"В должности '{work}' ты работаешь {experience} лет.")
