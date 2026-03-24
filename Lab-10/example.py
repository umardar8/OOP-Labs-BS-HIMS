# base classes
class Person:
    def bio(self):
        print("Name: Anaya")

class Staff:
    def org(self):
        print("LUMHS Hospital")

class Hospital:
    def location(self):
        print("Main Campus")

class License:
    def verify(self):
        print("Active License")

# Types of Inheritance

# 1. Single Inheritance
class Doctor(Staff):
    def role(self):
        print("Checking Patients")

# 2. Multilevel Inheritance
class Surgeon(Doctor):
    def role(self):
        print("Performing Operations and Surgery")

# 3. Multiple Inheritance
class Nurse(Person, License):
    pass

# 4. Hierarchical inheritance
class Patient(Person):
    pass

class InPatient(Patient):
    pass

class OutPatient(Patient):
    pass

# 5. Hybrid Inheritance
class Hospital_branch(Hospital, Staff): # multiple inheritance
    pass

class Admin_Staff(Hospital_branch): # single inheritance
    pass

class Director(Staff, Admin_Staff): # hierarchical inheritance
    pass



