class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer: 'list'):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


exp = AdditionExpression(
    DoubleExpression(1),
    AdditionExpression(
        DoubleExpression(2),
        DoubleExpression(3)
    )
)

buffer = []
exp.print(buffer)
print(''.join(buffer), '=', exp.eval())
