import datetime

class PatientRecord:
    def __init__(self, patient_id, name, ssn, temperature_celsius):
        # Public attributes (Accessible anywhere)
        self.patient_id = patient_id
        self.name = name
        self.temperature = temperature_celsius
        
        # Protected attributes (single underscore - meant for internal/subclass use)
        self._admit_date = datetime.date.today()
        
        # Private attributes (double underscore - cannot be accessed directly without setter or getter)
        self.__ssn = ssn
        

    # 1. Data Masking with Encapsulation
    @property
    def ssn_masked(self):
        # Only the class itself can easily access self.__ssn
        return f"***-**-{self.__ssn[-3:]}"

    # 2. Data Validation with Encapsulation
    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value >= 30.0 and value <= 45.0:
            self.__temperature = value
        else:
            print(f"Alert: {value}C is invalid. Input rejected.")

    # 3. Assigning Dynamic Properties with Encapsulation (Read-Only State)
    @property
    def clinical_status(self):
        if self.temperature > 37.5:
            return "Febrile (Fever)"
        elif self.temperature < 35.0:
            return "Hypothermic"
        else:
            return "Normal"

# Execution of Program
patient_1 = PatientRecord(patient_id="HIMS-9921", name="Umar", ssn="the patient has come", temperature_celsius=36.8)

# 1. Accessing Public Data
print(f"Patient: {patient_1.name} (ID: {patient_1.patient_id})")

# 2. Accessing Masked Private Data
# print(patient_1.__ssn)
print(f"Masked SSN: {patient_1.ssn_masked}")

# 3. Utilizing Computed Properties
print(f"Initial Vitals Status: {patient_1.clinical_status}")

# 4. Triggering the Validation Logic
print("Attempting to update temperature to 39.2C...")
patient_1.temperature = 39.2
print(f"Success. New Status: {patient_1.clinical_status}")
print("\nAttempting to input a typo (e.g., 400C)...")
patient_1.temperature = 400.0  # This will trigger our ValueError