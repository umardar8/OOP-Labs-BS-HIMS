class Patient:
    """
    The Class is the 'Blueprint'. 
    It defines what every patient has (Name, Age) 
    and what they can do (Actions).
    """
    
    def __init__(self, name, age, condition):
        # The Constructor: Sets up the data for a new patient
        self.name = name
        self.age = age
        self.condition = condition

    def display_info(self):
        """Action: Print the patient's details."""
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Status: {self.condition}")
        print("-------------------------")

    def update_condition(self, new_condition):
        """Action: Update the patient's medical status."""
        print(f" > Updating status for {self.name}...")
        self.condition = new_condition


# --- Main Application ---

# 1. Create an object (p1) from the blueprint
p1 = Patient("John Doe", 45, "Flu")

# 2. Use the object's method to see data
p1.display_info()

# 3. Change the data using a method
p1.update_condition("Recovering")

# 4. Check if the change happened
p1.display_info()

# 5. Create a second, independent patient
p2 = Patient("Jane Smith", 30, "Hypertension")
p2.display_info()