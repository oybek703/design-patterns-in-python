class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value == self.age:
            return
        old_can_vote = self.can_vote
        self._age = value
        self.property_changed('age', value)
        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)


class TrafficAuthority:
    def __init__(self, person: 'Person'):
        self.person = person
        self.person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == 'age':
            if value < 16:
                print('Sorry you still can not drive.')
            else:
                print('Okay, you can drive now.')
                self.person.property_changed.remove(self.person_changed)


def person_changed(name, value):
    if name == 'can_vote':
        print(f'Voting status changed to {value}')


person = Person()
person.property_changed.append(person_changed)
for age in range(16, 21):
    print(f'Changing age to {age}')
    person.age = age
