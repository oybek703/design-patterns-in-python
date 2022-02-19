from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is delicious.')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious.')


# class HotDrinkFactory(ABC):
#     def prepare(self, amount):
#         pass


class TeaFactory():
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory():
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrinks:
                name = f'{d.name[0]}{d.name[1:].lower()}'
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((factory_name, factory_instance))

    def make_drink(self):
        print('Available drinks: ')
        for f in self.factories:
            print(f[0])
        type_ = input(f'Select pick drink (0-{len(self.factories) - 1}): \n')
        index = int(type_)
        amount = int(input('Specify amount: \n'))
        print(amount)
        return self.factories[index][1].prepare(amount)


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(300)
    elif type == 'coffee':
        return CoffeeFactory().prepare(200)
    else:
        return None


hdm = HotDrinkMachine()
hdm.make_drink()
