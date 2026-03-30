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
        """Returns a masked version of the SSN for display purposes."""
        # Only the class itself can easily access self.__ssn
        return f"***-**###-{self.__ssn[-4:]}"

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

    # 3. Assigning Dynamic Properties with Encapsulation
    @property
    def clinical_status(self):
        if self.temperature > 37.5:
            return "Febrile (Fever)"
        elif self.temperature < 35.0:
            return "Hypothermic"
        else:
            return "Normal"