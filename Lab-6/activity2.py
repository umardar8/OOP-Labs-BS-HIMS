class Person:
    """The Base Class (Parent)"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Patient(Person):
    """The Derived Class (Child)"""
    def __init__(self, name, age, patient_id, ailment):
        # super() calls the __init__ of the Person class
        super().__init__(name, age) 
        self.patient_id = patient_id
        self.ailment = ailment

    def display_patient_record(self):
        # Accessing self.name which was inherited from Person
        print(f"Record [{self.patient_id}]: {self.name} is treated for {self.ailment}")

# Create a Patient object
pat1 = Patient("Ali Hassan", 22, "P-101", "Seasonal Flu")
pat1.display_info()           # Inherited method
pat1.display_patient_record() # Child-specific method