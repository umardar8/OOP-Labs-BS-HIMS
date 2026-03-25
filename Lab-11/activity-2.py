# Activity 2: Method Overloading (Pythonic Way)

class AdmissionSystem:
    
    def admit_patient(self, patient_name, condition, ward=None):
        
        base_record = f"Patient {patient_name} admitted for {condition}."
        
        if ward is not None:
            return f"{base_record} Assigned to: {ward} Ward."
        else:
            return f"{base_record} Ward assignment pending. Placed in triage."

# --- Demonstration ---
print("\n--- Activity 2: Method Overloading ---")
admin = AdmissionSystem()

# Calling the method with 2 arguments
print(admin.admit_patient("Kashif", "High Fever"))

# Calling the SAME method with 3 arguments
print(admin.admit_patient("Najaf", "Fractured Arm", "Orthopedics"))