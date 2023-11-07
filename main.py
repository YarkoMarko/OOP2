class Human:
    def __init__(self, name, age, ID, address):
        self._name = name
        self._age = age
        self._ID = ID
        self._address = address

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nID: {self._ID}\nAddress: {self._address}"

    def get_age(self):
        return self._age

    def __lt__(self, other):
        return self.get_age() < other.get_age()

    def __le__(self, other):
        return self.get_age() <= other.get_age()

    def __gt__(self, other):
        return self.get_age() > other.get_age()

    def __ge__(self, other):
        return self.get_age() >= other.get_age()

    def __eq__(self, other):
        return self.get_age() == other.get_age()

    def __ne__(self, other):
        return self.get_age() != other.get_age()


h = Human("Olexiy", 25, "34DFaQ1", "Grushevskogo 13")

print(h)