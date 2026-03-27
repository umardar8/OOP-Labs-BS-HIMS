# Activity 1: Polymorphism with Method Overriding

class HospitalStaff:
    def __init__(self, name):
        self.name = name

    def perform_duty(self):
        return f"{self.name} is performing a general task"
    
class Doctor(HospitalStaff):
    def perform_duty(self):
        return f"{self.name} is diagnosing patients and writing prescriptions"
    
class Nurse(HospitalStaff):
    def perform_duty(self):
        return f"{self.name} is checking patient vitals and administering injections"
    
# Execution of Method Overring
print("---- Activity 1 -----")
staff1 = HospitalStaff("Mohsin")
staff2 = Doctor("Aqsa")
staff3 = Nurse("Sadiq")

print(staff1.perform_duty())
print(staff2.perform_duty())
print(staff3.perform_duty())

# Activity 2: Polymorphism with Method Overloading (Pythonic Way)

class PatientAdmissionSystem:

    def admit_patient(self, patient_name, condition, ward = None):

        if ward is None:
            return f"{patient_name} is admitted for {condition} but waiting to be assigned a ward"
        else:
            return f"{patient_name} is admitted for {condition} and assigned ward: {ward}"
        
# Execution of Method Overloading
print("--- Activity 2 ---")
admin = PatientAdmissionSystem()

print(admin.admit_patient("Kashif", "High Fever"))
print(admin.admit_patient("Najaf", "Bone Fracture", ward="Orthopedic"))

# Activity 3: Use Method Overriding and Overloading in Same program

# base Class -> Class 1
# base Class -> Class 2