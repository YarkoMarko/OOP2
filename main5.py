class WebSite:
    def __init__(self, name, address, description):
        self._name = name
        self._address = address
        self._description = description

    def __str__(self):
        return f"Name: {self._name}\nAddress: {self._address}\nDescription: {self._description}"


w = WebSite("Mystat", "https://mystat.itstep.org/ru/main/dashboard/page/index", "Your cabinet, where you get H/w and can observe your progress")

print(w)