class MedicalTest:
    def display_result(self):
        print("General medical test result.")

class BloodTest(MedicalTest):
    def display_result(self):
        # Specific implementation for Blood Tests
        print("Blood Test Result: Hemoglobin level is 14.5 g/dL.")

class XRay(MedicalTest):
    def display_result(self):
        # Specific implementation for Imaging
        print("X-Ray Result: No fractures detected in the distal radius.")

# Polymorphism in action
tests = [BloodTest(), XRay()]

for test in tests:
    test.display_result()