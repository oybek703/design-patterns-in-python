class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postal_code = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.street_address}, {self.postal_code}, {self.city}. \n' \
               f'Employment: at {self.company_name} as {self.position} with income {self.annual_income}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def with_earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postal_code(self, postal_code):
        self.person.postal_code = postal_code
        return self

    def in_city(self, city):
        self.person.city = city
        return self


pb = PersonBuilder()

person = pb\
    .lives\
        .at('London Road 123')\
        .in_city('London')\
        .with_postal_code('123813')\
    .works\
        .at('Hi Tech')\
        .as_a('Programmer')\
        .with_earning(120000)\
    .build()

print(person)