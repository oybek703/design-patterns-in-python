from abc import ABC
from enum import Enum, auto


class ListStrategy(ABC):
    def start(self, buffer: 'list'): pass

    def end(self, buffer: 'list'): pass

    def add_list_item(self, buffer: 'list', item): pass


class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer: 'list', item):
        buffer.append(f' <li>{item}</li>\n')


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:
    def __init__(self, list_strategy: 'ListStrategy' = HtmlListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format: 'OutputFormat'):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return ''.join(self.buffer)


items = ['foo', 'bar', 'baz']

tp = TextProcessor()
tp.set_output_format(OutputFormat.MARKDOWN)
tp.append_list(items)
tp.clear()
tp.set_output_format(OutputFormat.HTML)
tp.append_list(items)
print(tp)
