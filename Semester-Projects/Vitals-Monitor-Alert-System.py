# Use this boilerplate code and work on the logic for this project

class VitalsRecord:
    def __init__(self, patient_name, heart_rate, bp_systolic, temperature):
        """
        Initialize the patient's vitals.
        """
        self.patient_name = patient_name
        self.heart_rate = heart_rate
        self.bp_systolic = bp_systolic
        self.temperature = temperature

    def check_heart_rate(self):
        """
        Check the heart rate. 
        Normal is between 60 and 100.
        Print an alert if it is too high (Tachycardia) or too low (Bradycardia).
        """
        pass

    def check_blood_pressure(self):
        """
        Check the systolic blood pressure.
        Normal is under 120. Over 140 is high.
        Print appropriate warnings.
        """
        pass

    def check_temperature(self):
        """
        Check the body temperature (in Celsius).
        Normal is around 37.0. Above 38.0 is a fever.
        Print an alert if there is a fever.
        """
        pass

    def generate_full_report(self):
        """
        Print the patient's name and run all three check methods above.
        """
        pass

# --- Testing Area (For Students) ---
# 1. Create a VitalsRecord for a patient with normal vitals
# 2. Generate a full report for them
# 3. Create a VitalsRecord for a patient with a high heart rate and fever
# 4. Generate a full report for them