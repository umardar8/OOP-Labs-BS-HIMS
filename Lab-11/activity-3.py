# Activity 3: Using both of Overriding and Overloading in same system

class MedicalTest:
    def __init__(self, patient_name):
        self.patient_name = patient_name

    # Overloaded Method
    def schedule_test(self, date, is_urgent=False):
        
        if is_urgent is True:
            return f"[Urgent] Test scheduled for {self.patient_name} on {date}."
        else:
            return f"[Standard] Test scheduled for {self.patient_name} on {date}."
        

    # Method to be overridden
    def conduct_test(self):
        return "Conducting a generic medical test."

class BloodPanel(MedicalTest):
    # Overriding
    def conduct_test(self):
        return f"Drawing blood samples for {self.patient_name}'s lipid and glucose panel."

class MRIScan(MedicalTest):
    # Overriding
    def conduct_test(self):
        return f"Preparing {self.patient_name} for MRI. Ensuring no metal objects are present."

# --- Demonstration ---
print("\n--- Activity 3: Mixed Polymorphism ---")
test1 = BloodPanel("Anisha")
test2 = MRIScan("Bakhtawar")

# Using the inherited overloaded method
print(test1.schedule_test("Oct 12"))                     # Standard
print(test2.schedule_test("Oct 10", is_urgent=True))     # Urgent

# Using the overridden methods
print(test1.conduct_test())
print(test2.conduct_test())