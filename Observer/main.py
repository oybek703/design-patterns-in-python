class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f'{name} needs help at {address}')


def call_doctor_1(name, address):
    print(f'{name} needs help at {address}')


person = Person('John', 'London Street 121')
person.falls_ill.append(lambda name, address: print(f'{name} is ill.'))
person.falls_ill.append(call_doctor)

person.falls_ill.remove(call_doctor)


person.catch_a_cold()
