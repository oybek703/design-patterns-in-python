def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database from file: ')


d1 = Database()
d2 = Database()
print(d1 == d2)
