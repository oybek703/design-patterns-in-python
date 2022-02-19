import copy


class Address:
    def __init__(self, street_code, city, postal_code):
        self.street_code = street_code
        self.city = city
        self.postal_code = postal_code

    def __str__(self):
        return f'{self.street_code}, {self.city}, {self.postal_code}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}.'


john = Person('John', Address('123', 'London', '242187'))
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_code = '124'
print(jane)
print(john)