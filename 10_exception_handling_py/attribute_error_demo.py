class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alice", 25)

try:
    print(person.address)
except AttributeError as e:
    print(f"Attribute Error: {e}")
