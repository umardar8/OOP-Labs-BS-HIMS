class Person:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number

    def display_basic_info(self):
        print(f"Name: {self.name} | Contact: {self.contact_number}")

class Doctor(Person):
    def __init__(self, name, contact_number, specialty, license_num):
        super().__init__(name, contact_number) # Call parent constructor
        self.specialty = specialty
        self.license_num = license_num

    def display_profile(self):
        print(f"Dr. {self.name} - Specialty: {self.specialty}")

class Patient(Person):
    def __init__(self, name, contact_number, mrn):
        super().__init__(name, contact_number)
        self.__mrn = mrn

    def get_mrn(self):
        return self.__mrn

class Appointment:
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor     # Expects a Doctor object
        self.patient = patient   # Expects a Patient object
        self.date = date
        self.time = time

    def print_ticket(self):
        print("\n--- Appointment Ticket ---")
        print(f"Patient: {self.patient.name} (MRN: {self.patient.get_mrn()})")
        print(f"Consulting: Dr. {self.doctor.name} ({self.doctor.specialty})")
        print(f"When: {self.date} at {self.time}")
        print("--------------------------\n")

# Execution for Activity 2
if __name__ == "__main__":
    print("Executing Activity 2: Inheritance & Relationships")
    doc1 = Doctor("Ahmed Raza", "0300-1234567", "Cardiology", "LIC-998")
    pat1 = Patient("Sana Ali", "0333-7654321", "MRN-50012")
    
    # Passing objects into another object
    appt = Appointment(doc1, pat1, "2026-04-10", "10:30 AM")
    appt.print_ticket()