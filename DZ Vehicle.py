class Vehicle:
    def __init__(self, brand, year, model, price):
        self.brand = brand
        self.year = year
        self.model = model
        self.price = price

    def display_info(self):
        print(f'Марка: {self.brand}'
        f'Год выпуска: {self.year}'
        f'Модель: {self.model}' 
        f'Цена: {self.price}')

class Car(Vehicle):
    def __init__(self, brand, year, model, price):
        super().__init__(brand, year, model, price)
        self.model = model
        self.price = price

class Motorcycle(Vehicle):
    def __init__(self, brand, year, price, model):
        super().__init__(brand, year, price, model)
        self.price = price

car = Car('Toyota', 2019, 'Corola', '7000$')
moto = Motorcycle('Ford', 2013, '2000$', 'Mers')

car.display_info()
moto.display_info()
