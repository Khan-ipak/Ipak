# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Horse(Animal):
#     pass
#
# pony = Horse()
# pony.make_sound('Igogo')


# class Family:
#     def heritage(self, x):
#         print(x)
#
# class People(Family):
#     pass
#
# khan = People()
# khan.heritage('xa')


# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor


# class Calculate:
#     @classmethod
#     def summary(cls, a, b):
#         return a + b
#
# print(Calculate.summary(2, 4))





class Player:
    def __init__(self, strike, defender, midfielder, goalkeeper):
        self.strike = strike
        self.defender = defender
        self.midfielder = midfielder
        self.goalkeeper = goalkeeper

class SuperStrike(Player):
    def __init__(self, strike, defender, midfielder, goalkeeper, tough):
        super().__init__(strike, defender, midfielder, goalkeeper)
        self.tough = tough


