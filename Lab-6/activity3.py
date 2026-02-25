class Person:
    """The Base Class (Parent)"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Doctor(Person):
    """Another Derived Class (Child)"""
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def write_prescription(self, medicine):
        print(f"Dr. {self.name} ({self.specialty}) prescribed: {medicine}")

# Create a Doctor object
doc1 = Doctor("Sara", 45, "Cardiologist")
doc1.write_prescription("Aspirin")