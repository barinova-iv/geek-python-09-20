# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b=0):
        self.a = int(a)
        self.b = int(b)


    def __str__(self):
        if self.b < 0:
            if self.b == -1:
                return f"{self.a}-i"  # self + other
            else:
                return "%g%gi" % (self.a, self.b)  # self + other
        elif self.b > 0:
            if self.b == 1:
                return f"{self.a}+i"  # self + other
            else:
                return "%g+%gi" % (self.a, self.b)  # self + other
        elif self.b == 0:
            return f"{self.a}+0i={self.a}"  # self + other

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a))


c1 = Complex(2, -9)
c2 = Complex(-3, 5)
print(c1 + c2)
print(c1 * c2)
