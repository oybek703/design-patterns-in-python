import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        with open('capitals.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                self.population[lines[i].strip()] = lines[i + 1].strip()


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for city in cities:
            result += int(Database().population[city])
        return result


class ConfigurableRecordFinder:

    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += int(self.db.population[city])
        return result


class DummyDatabase:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        """This tests on a live database :("""
        rf = SingletonRecordFinder()
        names = ['Tokyo', 'Delhi']
        tp = rf.total_population(names)
        self.assertEqual(37435191 + 29399141, tp)

    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        crf = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(4, crf.total_population(['alpha', 'gamma']))


unittest.main()
