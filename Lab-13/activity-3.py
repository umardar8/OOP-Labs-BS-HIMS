class Person:
    def __init__(self, name): self.name = name

class Doctor(Person):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

class Patient(Person):
    def __init__(self, name, mrn):
        super().__init__(name)
        self.mrn = mrn

class Consultation:
    def __init__(self, doctor, patient):
        self.doctor = doctor
        self.patient = patient

    def calculate_fee(self):
        pass # Abstract method

class InPersonConsultation(Consultation):
    def calculate_fee(self):
        return 2500 # Standard physical visit fee

class TelehealthConsultation(Consultation):
    def calculate_fee(self):
        return 1500 # Discounted online visit fee

# System Manager Class
class ClinicSystem:
    def __init__(self, clinic_name):
        self.clinic_name = clinic_name
        self.doctors = []
        self.patients = []
        self.consultations = []

    def register_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Registered Dr. {doctor.name}.")

    def register_patient(self, patient):
        self.patients.append(patient)
        print(f"Registered Patient {patient.name}.")

    def book_consultation(self, doctor_index, patient_index, is_telehealth=False):
        if is_telehealth:
            cons = TelehealthConsultation(self.doctors[doctor_index], self.patients[patient_index])
            cons_type = "Telehealth"
        else:
            cons = InPersonConsultation(self.doctors[doctor_index], self.patients[patient_index])
            cons_type = "In-Person"
            
        self.consultations.append(cons)
        print(f"Booked {cons_type} consultation for {self.patients[patient_index].name} with Dr. {self.doctors[doctor_index].name}.")
        print(f"Fee due: Rs. {cons.calculate_fee()}")

# --- Final System Demonstration ---
if __name__ == "__main__":
    print("\n=== Initializing Clinic System ===")
    my_clinic = ClinicSystem("LUMHS Health Center")
    
    # 1. Setup Data
    doc = Doctor("Ahmed Raza", "Neurology")
    pat = Patient("Sana Ali", "MRN-001")
    
    my_clinic.register_doctor(doc)
    my_clinic.register_patient(pat)
    
    print("\n=== Booking Appointments ===")
    # 2. Polymorphism in action
    my_clinic.book_consultation(0, 0, is_telehealth=False) # In person
    my_clinic.book_consultation(0, 0, is_telehealth=True)  # Telehealth follow-up