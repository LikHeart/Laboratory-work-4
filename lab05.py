class Label:
    def __init__(self, name):
        if name.isspace():
            raise TypeError()
        if not isinstance(name, str):
            raise TypeError()
        self.name = name.strip(" ")

try:
    Label("   ")
except ValueError:
    print("ValueError")
else:
    print("Исключение не возникло")