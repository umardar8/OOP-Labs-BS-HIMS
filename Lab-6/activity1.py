class Person:
    """The Base Class (Parent)"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Testing the base class
p1 = Person("Generic User", 30)
p1.display_info()