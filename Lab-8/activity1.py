from abc import ABC, abstractmethod

# The Abstract Base Class (The Standard Protocol)
class PatientRecord(ABC):
    def __init__(self, name, patient_id):
        self.name = name
        self.patient_id = patient_id

    @abstractmethod
    def get_billing_summary(self):
        """Must calculate costs based on patient type."""
        pass

    @abstractmethod
    def record_vitals(self):
        """Must log temperature, BP, etc."""
        pass

class Inpatient(PatientRecord):
    def get_billing_summary(self):
        return "Billing includes Room Charges + Surgery + Pharmacy."

    def record_vitals(self):
        return "Logging vitals every 4 hours (Intensive Monitoring)."

class Outpatient(PatientRecord):
    def get_billing_summary(self):
        return "Billing includes Consultation Fee + Lab Tests."

    def record_vitals(self):
        return "Logging vitals once during the visit."

# Task: try to create a 'PatientRecord()' object. 
# Expected Result: Python prevents it, enforcing the use of specific types.