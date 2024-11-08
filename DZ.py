class Animal:
    def make_sound(self):
        print('Generic animal sound')

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав - Гав!"

class Cat(Animal):
    def make_sound(self):
        return 'Мяу - Мяу!'

class Cow(Animal):
    def make_sound(self):
        return 'Му - Му'

pet_first = Dog()
pet_second = Cat()
pet_third = Cow()
animals = [pet_first, pet_second, pet_third]
for animal in animals:
    print(animal.make_sound())
