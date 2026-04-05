# Activity 1: Base Patient Class
class Patient:
    def __init__(self, pid, name, age, condition):
        self.pid = pid  # Patient ID
        self.name = name
        self.age = age
        self.condition = condition

    def get_details(self):
        return f"ID: {self.pid} | {self.name} ({self.age}) | Condition: {self.condition}"
    
# Activity 2: Registration System
class RegistrationSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient_obj):
        self.patients.append(patient_obj)
        print(f"Success: {patient_obj.name} registered.")

    def show_all(self):
        print("\n--- Registered Patients ---")
        for p in self.patients:
            print(p.get_details())

# Testing Area
hms = RegistrationSystem()
hms.add_patient(Patient("Ahmed Ali", 45, "Male", "Fever"))
hms.show_all()