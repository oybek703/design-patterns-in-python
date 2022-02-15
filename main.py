class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistentManager:
    @staticmethod
    def save_to_file(filename, journal):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


journal = Journal()
journal.add_entry('Play football.')
journal.add_entry('Ate apple pie.')

PersistentManager.save_to_file('./test.txt', journal)
with open('./test.txt') as fh:
    print(fh.read())
