# Use this boilerplate code and work on the logic for this project

class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        """
        Initialize the patient with an ID, name, age, and diagnosis.
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def get_details(self):
        """
        Return a formatted string of the patient's details.
        """
        pass

class RecordSystem:
    def __init__(self):
        """
        Initialize an empty list to store Patient objects.
        """
        self.patients = []

    def add_patient(self, patient):
        """
        Add a Patient object to the patients list.
        """
        pass

    def display_all_patients(self):
        """
        Loop through the patients list and print each patient's details.
        """
        pass

    def find_patient(self, patient_id):
        """
        Search for a patient by their ID. 
        Print their details if found, or an error message if not.
        """
        pass

# --- Testing Area (For Students) ---
# 1. Create a RecordSystem object
# 2. Create a few Patient objects
# 3. Add the patients to the system
# 4. Display all patients
# 5. Search for a specific patient ID