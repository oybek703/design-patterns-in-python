class Foo:
    def __new__(cls, *args, **kwargs):
        print('Creating instance: ')
        instance = super(Foo, cls).__new__(cls)
        return instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}, {self.b}'

    def bar(self):
        pass


foo = Foo(1, 2)
