class City:
    def __init__(self, name, age, country, population):
        self._name = name
        self._age = age
        self._country = country
        self._population = population

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nCountry: {self._country}\nPopulation: {self._population}"

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


c = City("Lviv", 800, "Ukraine", 1000000)

print(c)