class Insurance:
    def calculate_bill(self, amount):
        pass

class Medicare(Insurance):
    def calculate_bill(self, amount):
        return amount * 0.20  # Patient pays 20%

class PrivateInsurance(Insurance):
    def calculate_bill(self, amount):
        return (amount * 0.10) + 50  # 10% co-insurance + $50 deductible

def generate_invoice(provider, total_cost):
    patient_share = provider.calculate_bill(total_cost)
    print(f"Total Bill: ${total_cost} | Patient Owes: ${patient_share}")

# Execution
generate_invoice(Medicare(), 1000)
generate_invoice(PrivateInsurance(), 1000)