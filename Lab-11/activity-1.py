# Activity 1: Method Overriding

class HospitalStaff:
    def __init__(self, name):
        self.name = name

    def perform_duty(self):
        # Base method to be overridden
        return f"{self.name} is performing a general hospital duty."

class Doctor(HospitalStaff):
    def perform_duty(self):
        # Overriding the parent method
        return f"Dr. {self.name} is diagnosing patients and prescribing medication."

class Nurse(HospitalStaff):
    def perform_duty(self):
        # Overriding the parent method
        return f"Nurse {self.name} is checking patient vitals and administering IVs."

# --- Demonstration ---
print("--- Activity 1: Method Overriding ---")
staff1 = HospitalStaff("Mohsin")
staff2 = Doctor("Aqsa")
staff3 = Nurse("Sadiq")

# Polymorphism in action: The same method name yields different behaviors
print(staff1.perform_duty())
print(staff2.perform_duty())
print(staff3.perform_duty())