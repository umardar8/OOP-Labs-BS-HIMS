# Use this boilerplate code and work on the logic for this project

class Bed:
    def __init__(self, bed_number):
        """
        Initialize the bed. By default, is_occupied should be False 
        and assigned_patient_name should be None.
        """
        self.bed_number = bed_number
        self.is_occupied = False
        self.assigned_patient_name = None

class Ward:
    def __init__(self, total_beds):
        """
        Initialize the ward with a list of Bed objects.
        Use a loop to create the specified number of beds.
        """
        self.beds = []
        # Hint: use a for loop and range(1, total_beds + 1) to create Bed objects
        pass

    def assign_bed(self, patient_name):
        """
        Find the first bed where is_occupied is False.
        Set it to True and assign the patient_name.
        Print a success message. If no beds are available, print an error.
        """
        pass

    def discharge_patient(self, bed_number):
        """
        Find the bed by its number.
        Set is_occupied to False and assigned_patient_name to None.
        """
        pass

    def show_available_beds(self):
        """
        Loop through all beds and print the bed numbers of those 
        that are NOT occupied.
        """
        pass

# --- Testing Area (For Students) ---
# 1. Create a Ward with 5 beds
# 2. Show available beds
# 3. Assign 3 beds to different patients
# 4. Show available beds again
# 5. Discharge one patient
# 6. Show available beds one last time