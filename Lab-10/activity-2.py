# base classes
class Person:
    def bio(self): 
        print("Name: Ali")

class Staff:
    def show_org(self): 
        print("LUMHS Hospital")

class License:
    def verify(self): 
        print("License Active")

class Hospital:
    def location(self): 
        print("Main Campus")

# Single inheritance
class Doctor(Staff):
    def role(self): 
        print("Treating Patients")

# Multiple inheritance
class Nurse(Person, License):
    pass

# Multilevel inheritance
class Surgeon(Doctor):
    def surgery(self): 
        print("Specialized Surgery")

# Hierarchical inheritance
class Patient:
    def register(self): 
        print("Patient Registered")

class InPatient(Patient):
    def stay(self): 
        print("Assigned to Ward 5")

class OutPatient(Patient):
    def visit(self): 
        print("Consultation only")

# Hybrid inheritance
class ClinicalStaff(Hospital):
    pass

class AdminStaff(Hospital):
    pass

class MedicalDirector(ClinicalStaff, AdminStaff): # Multiple & Multilevel
    def manage(self): 
        print("Overseeing Clinical & Admin")