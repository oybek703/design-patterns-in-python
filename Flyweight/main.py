import random
import string


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for ch in range(8)])


class User:
    def __init__(self, name):
        self.name = name


class User2:
    strings = []

    def __init__(self, full_name: 'str'):
        def get_or_add(s):
            if s in self.strings:
                self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(s) for s in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[s] for s in self.names])


users = []
first_names = [random_string() for _ in range(100)]
last_names = [random_string() for _ in range(100)]
for first_name in first_names:
    for last_name in last_names:
        users.append(User2(f'{first_name.capitalize()} {last_name.capitalize()}'))
print(users[0])
