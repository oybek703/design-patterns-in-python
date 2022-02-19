class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(self.driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver is too young.')


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


car = CarProxy(Driver('John', 20))
car.drive()
