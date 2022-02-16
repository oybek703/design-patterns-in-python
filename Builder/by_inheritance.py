class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born in {self.date_of_birth} ' \
               f'and works at position {self.position}.'

    @staticmethod
    def new():
        return PersonJobBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()

person = pb\
        .called('John Doe')\
        .born('01.10.2000')\
        .works_as_a('Engineer')\
    .build()

print(person)
