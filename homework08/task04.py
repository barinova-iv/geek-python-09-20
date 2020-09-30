# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы
# оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    count_in: dict

    def __init__(self):
        self.count_in = {}

    def __str__(self):
        return f'на складе: {self.count_in}'

    def accept_to_warehouse(self, name, count):
        count_in_new = {}
        count_in_new[name] = count
        if name in self.count_in:
            self.count_in[name] = self.count_in[name] + count
        else:
            self.count_in.update(count_in_new)


class OfficeEquipment:

    def __init__(self, model: str, price: int, type: str, quantity: int):
        self.model = model
        self.price = price
        self.type = type
        self.quantity = quantity

    def __str__(self):
        return f'Тип: {self.type:8}; Наименование: {self.model:18}; Цена: {self.price:>5} руб; Кол-во: {self.quantity:>2} шт'


class Printer(OfficeEquipment):

    def __init__(self, model, price, type, paper_size: str, print_color: str, quantity: int):
        super().__init__(model, price, type, quantity)
        self.paper_size = paper_size
        self.print_color = print_color


class Scanner(OfficeEquipment):

    def __init__(self, model, price, type, two_way_scan: bool, scan_to_email: bool, quantity: int):
        super().__init__(model, price, type, quantity)
        self.two_way_scan = two_way_scan
        self.scan_to_email = scan_to_email


class Copier(OfficeEquipment):

    def __init__(self, model, price, type, speed_copy: int, tray_capacity: int, quantity: int):
        super().__init__(model, price, type, quantity)
        self.speed_copy = speed_copy
        self.tray_capacity = tray_capacity


p1 = Printer('Pantum P3010DW', 8460, 'принтер', 'A4', 'цветной', 3)
p2 = Printer('HP LaserJet', 16500, 'принтер', 'A4', 'чб', 12)
s1 = Scanner('HP ScanJet', 12700, 'сканер', False, True, 7)
c1 = Copier('Canon imageRUNNER', 49450, 'ксерокс', 22, 250, 6)
print("Оргтехника")
print('----------')
print(p1)
print(p2)
print(s1)
print(c1)
