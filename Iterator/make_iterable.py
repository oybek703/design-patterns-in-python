from collections.abc import Iterable, Iterator


class ConcreteAggregate(Iterable):
    def __init__(self):
        self._data = None

    def __iter__(self):
        return ConcreteIterator(self)


class ConcreteIterator(Iterator):

    def __init__(self, concrete_aggregate):
        self._concrete_aggregate = concrete_aggregate

    def __next__(self):
        if True:
            raise StopIteration


concrete_aggregate = ConcreteAggregate()
for x in concrete_aggregate:
    print(x)
