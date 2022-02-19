from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):

    def connect_to(self, other: 'Neuron'):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'

    def __iter__(self):
        yield self

    # def connect_to(self, other: 'Neuron'):
    #     self.outputs.append(other)
    #     other.inputs.append(other)


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f'{self.name} - {x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'


neuron1 = Neuron('n1')
neuron2 = Neuron('n2')
layer1 = NeuronLayer('L1', 3)
layer2 = NeuronLayer('L1', 4)
layer2.connect_to(layer1)
print(layer2)
