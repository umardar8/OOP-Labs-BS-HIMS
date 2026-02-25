class PharmacyRecord:
    def get_summary(self):
        return "Medication: Metformin 500mg, Quantity: 30"

class LabRecord:
    def get_summary(self):
        return "Lab: Fasting Blood Sugar, Result: 110mg/dL"

def process_record(record):
    print(f"Processing... {record.get_summary()}")

# Both objects work despite having no inheritance relationship
pharmacy_item = PharmacyRecord()
lab_item = LabRecord()

process_record(pharmacy_item)
process_record(lab_item)