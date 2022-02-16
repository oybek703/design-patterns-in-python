from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotADirectoryError

    def fax(self, document):
        raise NotADirectoryError

    def scan(self, document):
        raise NotADirectoryError


class OldMachine(Machine):
    def print(self, document):
        print(document)

    def fax(self, document):
        """Not supported!"""
        print(f'Fax - {document}')


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice): # noqa
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    # def print(self, document):
    #     self.printer.print(document)
    #
    # def scan(self, document):
    #     self.scanner.scan(document)
