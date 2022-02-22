from enum import Enum, auto


class Token:
    class Type(Enum):
        PLUS = auto()
        MINUS = auto()
        LPARENT = auto()
        RPARENT = auto()
        INTEGER = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input):
    result = []
    i = 0
    while i < len(input):
        if input[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input[i] == '(':
            result.append(Token(Token.Type.LPARENT, '('))
        elif input[i] == ')':
            result.append(Token(Token.Type.RPARENT, ')'))
        else:
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1
    return result


# ↑↑↑ lexing ↑↑↑

# ↓↓↓ parsing ↓↓↓

class Integer:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    class Type:
        ADDITION = auto()
        SUBSTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBSTRACTION:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryOperation()
    have_hls = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_hls:
                result.left = integer
                have_hls = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryOperation.Type.SUBSTRACTION
        elif token.type == Token.Type.LPARENT:  # note no if for RPARENT
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPARENT:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_hls:
                result.left = element
                have_hls = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))
    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


calc('(13+4)-(12+1)')
