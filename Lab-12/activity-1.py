import datetime

class PatientRecord:
    def __init__(self, patient_id, name, temperature_celsius, ssn):
        # Public attributes (Accessible anywhere)
        self.patient_id = patient_id
        self.name = name
        self.temperature = temperature_celsius
        
        # Protected attributes (single underscore - meant for internal/subclass use)
        self._admit_date = datetime.date.today()
        
        # Private attributes (double underscore - cannot be accessed directly without setter or getter)
        self.__ssn = ssn