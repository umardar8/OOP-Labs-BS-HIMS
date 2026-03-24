# base classes
class Staff:
    def show_org(self): print("City Hospital")

class Person:
    def bio(self): print("Name: Ali")

class License:
    def verify(self): print("License Active")

# Single inheritance
class Doctor(Staff):
    def role(self): print("Treating Patients")

# Multiple inheritance
class Nurse(Person, License):
    pass

# Multilevel inheritance
class Doctor(Staff):
    def work(self): print("General Medicine")

class Surgeon(Doctor):
    def surgery(self): print("Specialized Surgery")

# Hierarchical inheritance
class Patient:
    def register(self): print("Patient Registered")

class InPatient(Patient):
    def stay(self): print("Assigned to Ward 5")

class OutPatient(Patient):
    def visit(self): print("Consultation only")

# Hybrid inheritance
class Hospital:
    def location(self): print("Main Campus")

class ClinicalStaff(Hospital):
    pass

class AdminStaff(Hospital):
    pass

class MedicalDirector(ClinicalStaff, AdminStaff): # Multiple
    def manage(self): 
        print("Overseeing Clinical & Admin")

# Execution of single inheritance 
doc = Doctor()
doc.show_org()

# Execution of multiple inheritance
n = Nurse()
n.bio()
n.verify()

# Execution of multilevel inheritance
s = Surgeon()
s.show_org()
s.surgery()

# Execution of hierarchical inheritance
p1 = InPatient()
p2 = OutPatient()
p1.register()
p2.register()

# Execution of hierarchical inheritance
md = MedicalDirector()
md.location()
md.manage()