from abc import ABC, abstractmethod

class DiagnosticTool(ABC):
    @abstractmethod
    def perform_scan(self, patient_id):
        pass

class XRayMachine(DiagnosticTool):
    def perform_scan(self, patient_id):
        print(f"Generating 2D Radiographic Image for Patient {patient_id}...")

class MRIScanner(DiagnosticTool):
    def perform_scan(self, patient_id):
        print(f"Generating 3D Magnetic Resonance Workspace for Patient {patient_id}...")

# Student Challenge: 
# "The hospital just bought a new 'ECG_Machine'. Write the class 
# for it using the DiagnosticTool blueprint so it fits into our system."