class Clock:
    def __init__(self, name, firma, year, price, type):
        self._name = name
        self._firma = firma
        self._year = year
        self._price = price
        self._type = type

    def __str__(self):
        return f"Name: {self._name}\nFirma: {self._firma}\nYear: {self._year}\nPrice: {self._price}\nType: {self._type}"


c = Clock("Amand", "Rolex", 2008, 120, "hand")

print(c)