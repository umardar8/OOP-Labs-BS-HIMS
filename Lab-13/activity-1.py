class Patient:
    def __init__(self, name, age, gender, mrn):
        self.name = name
        self.age = age
        self.gender = gender
        self.__mrn = mrn  
        self.__diagnoses = [] 

    # Getter for MRN
    def get_mrn(self):
        return self.__mrn

    # Method to safely add a diagnosis
    def add_diagnosis(self, diagnosis):
        self.__diagnoses.append(diagnosis)
        print(f"Diagnosis '{diagnosis}' securely added for {self.name}.")

    # Method to view patient summary
    def display_info(self):
        print(f"\n--- Patient Info ---")
        print(f"Name: {self.name} | Age: {self.age} | Gender: {self.gender}")
        print(f"MRN: {self.__mrn}")
        print(f"Diagnoses: {', '.join(self.__diagnoses) if self.__diagnoses else 'None recorded'}")
        print("--------------------\n")

# Execution for Activity 1
if __name__ == "__main__":
    print("Executing Activity 1: Encapsulation & Objects")
    patient1 = Patient("Hamza Khan", 45, "Male", "001")
    patient1.add_diagnosis("Type 2 Diabetes")
    patient1.add_diagnosis("Hypertension")
    
    patient1.display_info()