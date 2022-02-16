from abc import abstractmethod
from enum import Enum


class RelationShip(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


class Person:
    def __init__(self, name):
        self.name = name


class RelationShipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class RelationsShips(RelationShipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, RelationShip.PARENT, child)
        )
        self.relations.append(
            (child, RelationShip.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == RelationShip.PARENT:
                yield r[2].name


class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == RelationShip.PARENT:
    #             print(f'John has child called: {r[2].name}')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has children called: {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Anna')

relations_ships = RelationsShips()
relations_ships.add_parent_and_child(parent, child1)
relations_ships.add_parent_and_child(parent, child2)
Research(relations_ships)
