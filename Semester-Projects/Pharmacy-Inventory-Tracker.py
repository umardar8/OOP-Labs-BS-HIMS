# Use this boilerplate code and work on the logic for this project

class Medicine:
    def __init__(self, med_name, batch_number, price, quantity):
        """
        Initialize the medicine attributes.
        """
        self.med_name = med_name
        self.batch_number = batch_number
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        """
        Initialize an empty list to hold Medicine objects.
        """
        self.medicines = []

    def add_medicine(self, medicine):
        """
        Add a Medicine object to the inventory.
        """
        pass

    def dispense_medicine(self, med_name, amount):
        """
        Find the medicine by name. If found, check if the requested amount 
        is less than or equal to the current quantity. 
        If yes, subtract the amount from the quantity. 
        If no, print an "Insufficient stock" message.
        """
        pass

    def check_low_stock(self, threshold_quantity=10):
        """
        Loop through all medicines and print the names of any 
        that have a quantity below the threshold_quantity.
        """
        pass

# --- Testing Area (For Students) ---
# 1. Create an Inventory object
# 2. Add some medicines (e.g., Paracetamol, Amoxicillin)
# 3. Dispense a valid amount of medicine
# 4. Try to dispense more medicine than is in stock
# 5. Check for low stock