from abc import ABC, abstractmethod

class DataExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class FHIR_Exporter(DataExporter):
    def export(self, data):
        print("Converting patient data to JSON-based FHIR standard for cloud sharing.")

class CSV_Exporter(DataExporter):
    def export(self, data):
        print("Saving patient data to a local Excel-compatible CSV file.")

# Practical Application:
def process_hospital_export(exporter: DataExporter, data):
    # The system doesn't care IF it's FHIR or CSV, it just calls .export()
    exporter.export(data)

patient_data = {"id": 101, "diagnosis": "Flu"}
process_hospital_export(FHIR_Exporter(), patient_data)