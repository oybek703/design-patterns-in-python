class CEO:
    __shared_state = {
        'name': 'Steve',
        'age': 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


ceo1 = CEO()
ceo2 = CEO()
ceo2.age = 60
print(ceo1)
print(ceo2)
