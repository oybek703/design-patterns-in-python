import copy


class Address:
    def __init__(self, street_code, suite, city):
        self.street_code = street_code
        self.city = city
        self.suite = suite

    def __str__(self):
        return f'{self.street_code}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee('', Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new__employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new__employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new__employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )


john = EmployeeFactory.new_main_office_employee('John', 200)
jane = EmployeeFactory.new_aux_office_employee('Jane', 500)
print(john)
print(jane)
